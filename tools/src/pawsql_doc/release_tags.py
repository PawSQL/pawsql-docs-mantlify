"""Backfill release tags into a source repository from a verified boundary table.

Tags must exist before the changelog can slice a repository into versions, and
neither source repo has usable ones. This module turns
``metadata/documentation/changelog-release-boundaries.yaml`` into ``git tag -a``
commands, refusing to touch anything until every row is human-verified.

Two rules make backfilled tags honest:

* the tag carries the **real ship date** (``GIT_COMMITTER_DATE``), because the
  changelog reads ``%(creatordate)`` — an annotated tag's own date, not the
  commit's — so without it every backfilled release would look like today;
* an existing tag is never rewritten: same name on the same commit is a skip,
  same name on another commit is an error.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Callable, Mapping, Sequence

import yaml

from pawsql_doc.changelog import load_sources, merged_tag_names, version_key
from pawsql_doc.models.changelog import ReleaseBoundaries, ReleaseBoundary

BOUNDARIES_DIR = Path("metadata/documentation/changelog-release-boundaries")
TAG_TIMEZONE = timezone(timedelta(hours=8))
TAG_HOUR = 12  # noon local: a ship date cannot drift across a day boundary

Runner = Callable[..., subprocess.CompletedProcess]


class TagError(RuntimeError):
    """The boundary table or the repository state blocks tagging."""


@dataclass(frozen=True)
class PlannedTag:
    name: str
    version: str
    commit: str
    date: str
    action: str  # create | skip | conflict
    detail: str = ""
    label: str = ""

    @property
    def message(self) -> str:
        subject = f"PawSQL {self.label} {self.version}" if self.label else f"PawSQL {self.version}"
        return f"{subject} ({self.date})"


def render_command(repo: Path, tag: PlannedTag) -> str:
    """The exact shell command this tag would be created with, for review."""
    return (
        f'GIT_COMMITTER_DATE="{tag_timestamp(tag.date)}" git -C "{repo}" tag -a '
        f"{tag.name} {tag.commit} -m {json.dumps(tag.message, ensure_ascii=False)}"
    )


@dataclass
class TagPlan:
    component: str
    repo: Path
    trunk: str
    tags: list[PlannedTag] = field(default_factory=list)
    problems: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def to_create(self) -> list[PlannedTag]:
        return [tag for tag in self.tags if tag.action == "create"]

    @property
    def ok(self) -> bool:
        return not self.problems


def tag_timestamp(date: str) -> str:
    """ISO timestamp for a ship date, at a fixed local noon."""
    day = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=TAG_TIMEZONE)
    return day.replace(hour=TAG_HOUR).isoformat()


def compute_versions(boundaries: ReleaseBoundaries) -> list[tuple[ReleaseBoundary, str]]:
    """Number the deliveries: patch per delivery, minor (patch reset) on a major one."""
    major, minor, patch = (int(part) for part in boundaries.start.split("."))
    numbered: list[tuple[ReleaseBoundary, str]] = []
    for index, delivery in enumerate(boundaries.deliveries):
        if index:
            if delivery.major:
                minor, patch = minor + 1, 0
            else:
                patch += 1
        numbered.append((delivery, f"{major}.{minor}.{patch}"))
    return numbered


def boundaries_path(root: Path, component: str) -> Path:
    """One boundary table per component: <dir>/<component>.yaml."""
    return root / BOUNDARIES_DIR / f"{component}.yaml"


def available_components(root: Path) -> list[str]:
    directory = root / BOUNDARIES_DIR
    if not directory.is_dir():
        return []
    return sorted(path.stem for path in directory.glob("*.yaml"))


def load_boundaries(root: Path, component: str) -> ReleaseBoundaries | None:
    path = boundaries_path(root, component)
    if not path.is_file():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8-sig")) or {}
    return ReleaseBoundaries.model_validate(data)


def _git(repo: Path, args: Sequence[str], runner: Runner, env: Mapping[str, str] | None = None) -> subprocess.CompletedProcess:
    return runner(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        env=None if env is None else {**os.environ, **env},
    )


def resolve_commit(repo: Path, commit: str, runner: Runner) -> str | None:
    """Full sha for a (possibly abbreviated) commit, or None when it is unknown."""
    done = _git(repo, ["rev-parse", "--verify", "--quiet", f"{commit}^{{commit}}"], runner)
    if done.returncode != 0:
        return None
    return done.stdout.strip() or None


def is_on_trunk(repo: Path, commit: str, trunk: str, runner: Runner) -> bool:
    done = _git(repo, ["merge-base", "--is-ancestor", commit, trunk], runner)
    return done.returncode == 0


def is_ancestor(repo: Path, old: str, new: str, runner: Runner) -> bool:
    done = _git(repo, ["merge-base", "--is-ancestor", old, new], runner)
    return done.returncode == 0


def existing_tags(repo: Path, runner: Runner) -> dict[str, str]:
    """Tag name -> the commit it points at, peeling annotated tags."""
    done = _git(
        repo,
        ["for-each-ref", "--format=%(refname:short) %(objecttype) %(*objectname) %(objectname)", "refs/tags"],
        runner,
    )
    tags: dict[str, str] = {}
    for line in done.stdout.splitlines():
        parts = line.split()
        if len(parts) < 4:
            continue
        name, object_type, peeled, object_name = parts[0], parts[1], parts[2], parts[3]
        tags[name] = peeled if object_type == "tag" and peeled else object_name
    return tags


def plan_tags(
    root: Path,
    *,
    component: str | None = None,
    runner: Runner = subprocess.run,
    env: Mapping[str, str] | None = None,
) -> TagPlan:
    """Validate the boundary table against the repository and plan the tags.

    Anything suspicious refuses the whole plan: a partial backfill is worse than
    none, because a missing tag silently changes a changelog range.
    """
    boundaries = load_boundaries(root, component) if component else None
    if component is None:
        choices = available_components(root)
        if not choices:
            raise TagError(f"没有找到发布边界表（{BOUNDARIES_DIR.as_posix()}/<组件>.yaml）")
        if len(choices) > 1:
            raise TagError(f"有多个组件的边界表（{', '.join(choices)}），用 --component 指定一个")
        component = choices[0]
        boundaries = load_boundaries(root, component)
    if boundaries is None:
        raise TagError(f"没有找到 {component} 的发布边界表（{boundaries_path(root, component).as_posix()}）")
    if boundaries.component != component:
        raise TagError(f"{component}.yaml 里写的是 component: {boundaries.component}，与文件名不一致")

    sources = {source.name: source for source in load_sources(root, env)}
    source = sources.get(boundaries.component)
    if source is None:
        raise TagError(
            f"{boundaries.component}: 在 changelog-sources.yaml 里找不到同名来源（仓库路径与主干从那里取）"
        )

    plan = TagPlan(component=boundaries.component, repo=source.repo, trunk=source.trunk)
    # Tag messages carry the component's own name (Server / Engine), not a hardcoded one.
    label = source.displayName.get("en") or source.name
    if not source.repo.is_dir():
        plan.problems.append(f"仓库路径不存在：{source.repo}")
        return plan

    numbered = compute_versions(boundaries)
    versions = [version for _delivery, version in numbered]
    duplicates = sorted({version for version in versions if versions.count(version) > 1})
    if duplicates:
        plan.problems.append(f"版本号重复：{', '.join(duplicates)}")

    unverified = [version for delivery, version in numbered if not delivery.verified]
    if unverified:
        plan.problems.append(
            f"有 {len(unverified)} 行还没核对（verified: false）：{', '.join(unverified)}"
        )

    known = existing_tags(source.repo, runner)
    previous_commit: str | None = None
    for delivery, version in numbered:
        name = boundaries.tagFormat.format(version=version)
        sha = resolve_commit(source.repo, delivery.commit, runner)
        if sha is None:
            plan.problems.append(f"{name}: 提交 {delivery.commit} 在仓库里不存在")
            continue
        if not is_on_trunk(source.repo, sha, source.trunk, runner):
            plan.problems.append(f"{name}: 提交 {delivery.commit} 不在主干 {source.trunk} 上")
            continue
        if previous_commit is not None and not is_ancestor(source.repo, previous_commit, sha, runner):
            plan.problems.append(
                f"{name}: 边界顺序不对——{delivery.commit} 不是前一个边界 {previous_commit[:8]} 的后代"
            )
            continue
        previous_commit = sha

        current = known.get(name)
        if current is None:
            plan.tags.append(
                PlannedTag(name, version, delivery.commit, delivery.date, "create", "", label)
            )
        elif current.startswith(delivery.commit):
            plan.tags.append(
                PlannedTag(
                    name, version, delivery.commit, delivery.date, "skip", "同名 tag 已指向同一提交", label
                )
            )
        else:
            plan.problems.append(
                f"{name}: 已存在且指向 {current[:8]}，与边界表的 {delivery.commit} 冲突（不覆盖）"
            )

    # Drift check: tags that look like ours but the table does not cover them. Tags
    # below minVersion are deliberately ignored, so they are not drift.
    prefix = boundaries.tagFormat.split("{version}")[0]
    on_trunk = merged_tag_names(source.repo, source.trunk, runner) or set()
    covered = {tag.name for tag in plan.tags}

    def in_scope(name: str) -> bool:
        match = source.tagPattern.search(name)
        if match is None:
            return False
        key = version_key(match.group("version"))
        return key is not None and (source.minVersion is None or key >= source.minVersion)

    drift = sorted(name for name in on_trunk if name.startswith(prefix) and in_scope(name) and name not in covered)
    if drift:
        plan.notes.append(
            f"主干上有 {len(drift)} 个 {prefix}* tag 不在边界表里（表可能已过期）："
            + ", ".join(drift[:5])
            + (" …" if len(drift) > 5 else "")
        )
    return plan


def apply_tags(plan: TagPlan, *, runner: Runner = subprocess.run, push: bool = False) -> list[str]:
    """Create the planned tags locally; ``push`` also sends them to origin."""
    if not plan.ok:
        raise TagError("计划有未解决的问题，拒绝打 tag：" + "；".join(plan.problems))
    created: list[str] = []
    for tag in plan.to_create:
        done = _git(
            plan.repo,
            ["tag", "-a", tag.name, tag.commit, "-m", tag.message],
            runner,
            env={"GIT_COMMITTER_DATE": tag_timestamp(tag.date)},
        )
        if done.returncode != 0:
            raise TagError(f"打 tag {tag.name} 失败：{(done.stderr or '').strip()}")
        created.append(tag.name)
    if push and created:
        done = _git(plan.repo, ["push", "origin", *created], runner)
        if done.returncode != 0:
            raise TagError(f"推送 tag 失败：{(done.stderr or '').strip()}")
    return created


__all__ = [
    "BOUNDARIES_DIR",
    "PlannedTag",
    "TagError",
    "TagPlan",
    "apply_tags",
    "available_components",
    "boundaries_path",
    "compute_versions",
    "existing_tags",
    "load_boundaries",
    "plan_tags",
    "render_command",
    "resolve_commit",
    "tag_timestamp",
]
