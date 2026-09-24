"""Changelog generation from source-repository git history.

Two stages, so that page rendering never needs the network:

1. mechanical — tag ranges -> ``git log`` -> filter -> ``reports/changelog/<c>-<v>.commits.json``
2. classification — LLM output -> ``reports/changelog/<c>-<v>.classified.json``

Rendering reads only the cached classified docs, which makes the generated page
reproducible offline. Version, tag, date and commit ids come from git; the
classifier only supplies entry text and categories, so it cannot invent facts.
"""
from __future__ import annotations

import fnmatch
import json
import os
import re
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence

import yaml

from pawsql_doc.generators.base import CHANGELOG_END, CHANGELOG_START, splice_region
from pawsql_doc.models.changelog import (
    CATEGORY_LABELS,
    CATEGORY_ORDER,
    ChangelogSource,
    ChangelogSources,
    ClassifiedDoc,
    ClassifiedEntry,
    ClassifiedPayload,
    ClassifiedSection,
    category_order_for,
)

SOURCES_PATH = Path("metadata/documentation/changelog-sources.yaml")
REPORTS_DIR = Path("reports/changelog")

RECORD_SEP = "\x1e"
FIELD_SEP = "\x1f"
# The record separator leads each record because --name-only appends the changed
# file list *after* the format string; a trailing separator would land between
# the body and the files.
GIT_LOG_FORMAT = "--format=%x1e%H%x1f%h%x1f%cI%x1f%an%x1f%s%x1f%b%x1f"
# for-each-ref does not expand %x1f (unlike git log), so this one is space-separated:
# refnames cannot contain spaces and iso-strict timestamps do not either.
TAG_REF_FORMAT = "%(refname:short) %(objectname) %(creatordate:iso-strict)"

CONVENTIONAL_RE = re.compile(r"^(?P<type>[A-Za-z]+)(?:\((?P<scope>[^)]*)\))?!?:\s*(?P<rest>.*)$")
MERGE_RE = re.compile(r"^Merge (?:\S+ )?branch|^Merge remote-tracking|^Merge pull request")
ENV_RE = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_]*)(?::-([^}]*))?\}")

# MDX parses `{` as the start of a JSX expression and `<` as a tag, so raw commit
# text would break the page. `&` must be escaped first.
_MDX_ESCAPES = (
    ("&", "&amp;"),
    ("<", "&lt;"),
    (">", "&gt;"),
    ("{", "&#123;"),
    ("}", "&#125;"),
    ("`", "&#96;"),
)
_LEADING_MARKER = re.compile(r"^(?:[-*+>]\s+|#{1,6}\s+)")


class GitError(RuntimeError):
    """A git invocation failed in a way the caller cannot recover from."""


@dataclass(frozen=True)
class Commit:
    sha: str
    short: str
    date: str
    author: str
    subject: str
    body: str = ""
    files: tuple[str, ...] = ()


@dataclass(frozen=True)
class Tag:
    name: str
    version: str
    key: tuple[int, ...]
    commit: str
    date: str


@dataclass(frozen=True)
class ChangeSource:
    name: str
    displayName: dict[str, str]
    repo: Path
    trunk: str
    tagPattern: re.Pattern[str]
    pages: tuple[tuple[str, Path], ...] = ()
    minVersion: tuple[int, ...] | None = None
    pathInclude: tuple[str, ...] = ()
    pathExclude: tuple[str, ...] = ()
    skipPrefixes: tuple[str, ...] = ()
    skipMerge: bool = True


@dataclass(frozen=True)
class Classifier:
    """A classifier plus the identity that decides whether a cache is stale."""

    model: str
    promptVersion: str
    classify: Callable[[ChangeSource, Sequence[Commit]], ClassifiedPayload]

    def __call__(self, source: ChangeSource, commits: Sequence[Commit]) -> ClassifiedPayload:
        return self.classify(source, commits)


@dataclass
class RenderedPage:
    """One changelog page and the fragment its component's caches render to."""

    component: str
    lang: str
    page: Path
    fragment: str


@dataclass
class ChangelogResult:
    rendered: list[RenderedPage] = field(default_factory=list)
    written: tuple[Path, ...] = ()
    docs: list[ClassifiedDoc] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    pending: list[str] = field(default_factory=list)


Runner = Callable[..., subprocess.CompletedProcess]


# ---------------------------------------------------------------------------
# source configuration
# ---------------------------------------------------------------------------


def expand_env(value: str, env: Mapping[str, str] | None = None) -> str:
    """Expand ``${VAR}`` and ``${VAR:-default}``; raise when a bare VAR is unset."""
    environ = os.environ if env is None else env

    def repl(match: re.Match[str]) -> str:
        name, default = match.group(1), match.group(2)
        if name in environ:
            return environ[name]
        if default is not None:
            return default
        raise ValueError(f"unset environment variable {name!r} in changelog source config")

    return ENV_RE.sub(repl, value)


def parse_sources(data: dict, env: Mapping[str, str] | None = None) -> list[ChangeSource]:
    parsed = ChangelogSources.model_validate(data or {})
    sources = []
    for source in parsed.sources:
        sources.append(
            ChangeSource(
                name=source.name,
                displayName=dict(source.displayName),
                repo=Path(expand_env(source.repo, env)),
                trunk=source.trunk,
                tagPattern=re.compile(source.tagPattern),
                pages=tuple((lang, Path(rel)) for lang, rel in sorted(source.pages.items())),
                minVersion=version_key(source.minVersion) if source.minVersion else None,
                pathInclude=tuple(source.pathInclude),
                pathExclude=tuple(source.pathExclude),
                skipPrefixes=tuple(source.skipPrefixes),
                skipMerge=source.skipMerge,
            )
        )
    return sources


def load_sources(root: Path, env: Mapping[str, str] | None = None) -> list[ChangeSource]:
    path = root / SOURCES_PATH
    if not path.is_file():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8-sig")) or {}
    return parse_sources(data, env)


# ---------------------------------------------------------------------------
# git
# ---------------------------------------------------------------------------


def _run_git(repo: Path, args: Sequence[str], runner: Runner = subprocess.run) -> str:
    done = runner(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if done.returncode != 0:
        detail = (done.stderr or "").strip()
        raise GitError(f"git {' '.join(args)} failed in {repo}: {detail}")
    return done.stdout or ""


def is_ancestor(repo: Path, old: str, new: str, runner: Runner = subprocess.run) -> bool:
    done = runner(
        ["git", "-C", str(repo), "merge-base", "--is-ancestor", old, new],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return done.returncode == 0


def parse_git_log(text: str) -> list[Commit]:
    """Parse ``GIT_LOG_FORMAT`` output, including the ``--name-only`` file list."""
    commits: list[Commit] = []
    for chunk in text.split(RECORD_SEP):
        chunk = chunk.lstrip("\r\n")
        if not chunk.strip():
            continue
        parts = chunk.split(FIELD_SEP)
        if len(parts) < 6:
            continue
        files_blob = parts[6] if len(parts) > 6 else ""
        files = tuple(line.strip() for line in files_blob.splitlines() if line.strip())
        commits.append(
            Commit(
                sha=parts[0].strip(),
                short=parts[1].strip(),
                date=parts[2].strip()[:10],
                author=parts[3].strip(),
                subject=parts[4].strip(),
                body=parts[5].strip(),
                files=files,
            )
        )
    return commits


def git_log(
    repo: Path,
    rev_range: str,
    source: ChangeSource | None = None,
    runner: Runner = subprocess.run,
) -> list[Commit]:
    args = ["log", GIT_LOG_FORMAT, "--name-only"]
    if source is not None and source.skipMerge:
        args.append("--no-merges")
    args.append(rev_range)
    return parse_git_log(_run_git(repo, args, runner))


def version_key(version: str) -> tuple[int, ...] | None:
    parts = re.split(r"[.\-+]", version)
    if not parts or not all(part.isdigit() for part in parts):
        return None
    return tuple(int(part) for part in parts)


def dedupe_tags(tags: Iterable[Tag]) -> list[Tag]:
    """Keep the highest version per commit; return ascending by version.

    The legacy server repository points several tags at one commit, which would
    otherwise render empty duplicate releases.
    """
    best: dict[str, Tag] = {}
    for tag in sorted(tags, key=lambda item: item.key, reverse=True):
        best.setdefault(tag.commit, tag)
    return sorted(best.values(), key=lambda item: item.key)


def merged_tag_names(repo: Path, trunk: str, runner: Runner = subprocess.run) -> set[str] | None:
    """Tag names reachable from ``trunk``; None when that branch is unavailable.

    Tags left on abandoned branches must not produce changelog entries, but an
    unknown trunk is reported rather than treated as "no tags".
    """
    try:
        output = _run_git(repo, ["tag", "--merged", trunk, "--list"], runner)
    except GitError:
        return None
    return {line.strip() for line in output.splitlines() if line.strip()}


def list_tags(
    repo: Path,
    pattern: re.Pattern[str],
    runner: Runner = subprocess.run,
    allowed: set[str] | None = None,
    min_version: tuple[int, ...] | None = None,
) -> list[Tag]:
    output = _run_git(repo, ["for-each-ref", f"--format={TAG_REF_FORMAT}", "refs/tags"], runner)
    tags: list[Tag] = []
    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split(" ", 2)
        if len(parts) < 3:
            continue
        name, commit, date = parts[0].strip(), parts[1].strip(), parts[2].strip()
        if allowed is not None and name not in allowed:
            continue
        match = pattern.search(name)
        if match is None:
            continue
        key = version_key(match.group("version"))
        if key is None:
            continue
        if min_version is not None and key < min_version:
            continue
        tags.append(Tag(name=name, version=match.group("version"), key=key, commit=commit, date=date[:10]))
    return dedupe_tags(tags)


def tag_ranges(tags: Sequence[Tag]) -> list[tuple[Tag, Tag]]:
    """Consecutive (previous, current) pairs; the oldest tag has no predecessor."""
    return list(zip(tags, tags[1:]))


# ---------------------------------------------------------------------------
# filtering
# ---------------------------------------------------------------------------


def _path_match(path: str, rule: str) -> bool:
    if any(char in rule for char in "*?["):
        return fnmatch.fnmatch(path, rule) or fnmatch.fnmatch(Path(path).name, rule)
    stem = rule.rstrip("/")
    return path == stem or path.startswith(stem + "/")


def _matches_paths(commit: Commit, source: ChangeSource) -> bool:
    files = commit.files
    if source.pathInclude and not any(
        _path_match(name, rule) for name in files for rule in source.pathInclude
    ):
        return False
    if source.pathExclude and files:
        kept = [name for name in files if not any(_path_match(name, rule) for rule in source.pathExclude)]
        if not kept:
            return False
    return True


def filter_commits(commits: Sequence[Commit], source: ChangeSource) -> list[Commit]:
    skip = {prefix.lower() for prefix in source.skipPrefixes}
    kept: list[Commit] = []
    for commit in commits:
        if source.skipMerge and MERGE_RE.match(commit.subject):
            continue
        match = CONVENTIONAL_RE.match(commit.subject)
        if match and match.group("type").lower() in skip:
            continue
        if not _matches_paths(commit, source):
            continue
        kept.append(commit)
    return kept


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------


def escape_mdx(text: str) -> str:
    """Flatten to one plain-text line safe inside MDX prose."""
    flat = " ".join(text.split())
    flat = _LEADING_MARKER.sub("", flat)
    for raw, entity in _MDX_ESCAPES:
        flat = flat.replace(raw, entity)
    return flat


def entries_for(doc: ClassifiedDoc, category: str) -> list:
    """Every entry of one category, across all sections that declare it.

    Guarding against repeated categories matters: a classifier may emit the same
    category twice, and taking only the first section would silently drop the rest.
    """
    return [entry for section in doc.sections if section.category == category for entry in section.entries]


def update_tags(doc: ClassifiedDoc, lang: str = "zh") -> list[str]:
    """Tags for the ``<Update>`` component: every tag its entries carry, in order.

    Derived from the entries rather than hand-kept on purpose: tags live in the
    rendered page, and a re-classification (a different classifier identity)
    rewrites the cache — a hand-maintained tag list would silently disappear then.
    Tags outside the component's own vocabulary are appended rather than dropped, so
    a mis-tagged cache stays visible instead of silently losing a filter.
    """
    present = {tag for section in doc.sections for entry in section.entries for tag in entry.tags}
    order = [tag for tag in category_order_for(doc.component) if tag in present]
    return [CATEGORY_LABELS[lang][tag] for tag in order] + [
        CATEGORY_LABELS[lang].get(tag, tag) for tag in sorted(present - set(order))
    ]


def render_version_section(
    doc: ClassifiedDoc,
    lang: str = "zh",
    include_commits: bool = True,
    show_component: bool = True,
) -> str:
    """One release as a Mintlify ``<Update>`` block.

    Only the reader-facing categories in ``CATEGORY_ORDER`` are rendered; the
    cache's ``internal`` bucket stays out of the page entirely. Body lines are
    indented two spaces, matching Mintlify's own changelog markup.
    """
    label = f"{doc.componentLabel.get(lang) or doc.component} {doc.version}" if show_component else doc.version
    attrs = [f'label="{label}"', f'description="{doc.releaseDate}"']
    tags = update_tags(doc, lang)
    if tags:
        attrs.append("tags={[" + ", ".join(f'"{tag}"' for tag in tags) + "]}")
    lines = [f"<Update {' '.join(attrs)}>"]
    body: list[str] = []

    present = [section.category for section in doc.sections if section.category != "internal"]
    ordered = [category for category in category_order_for(doc.component) if category in present]
    # Anything outside this component's vocabulary still renders, after the known
    # groups: a mis-tagged cache must stay visible rather than silently lose a section.
    extras = sorted({category for category in present} - set(ordered))
    visible = [(category, entries_for(doc, category)) for category in ordered + extras]
    if not any(entries for _category, entries in visible):
        body.append("> 本次发布没有可对外展示的变更。" if lang == "zh" else "> No user-facing changes.")
        body.append("")
    for category, entries in visible:
        if not entries:
            continue
        body.append(f"### {CATEGORY_LABELS[lang][category]}")
        body.append("")
        for entry in sorted(entries, key=lambda item: item.sourceCommits[0] if item.sourceCommits else ""):
            suffix = ""
            if include_commits and entry.sourceCommits:
                suffix = f" ({', '.join(entry.sourceCommits)})"
            body.append(f"- {escape_mdx(entry.text_for(lang))}{suffix}")
        body.append("")

    lines.extend(f"  {line}" if line else "" for line in body)
    lines.append("</Update>")
    return "\n".join(lines)


def render_fragment(
    docs: Sequence[ClassifiedDoc],
    lang: str = "zh",
    include_commits: bool = True,
) -> str:
    """Render the whole generated region from every cached version, newest first.

    The component name is only repeated in a heading when one page carries more
    than one component; per-component pages rely on the page title instead.
    """
    ordered = sorted(
        docs,
        key=lambda doc: (doc.releaseDate, version_key(doc.version) or ()),
        reverse=True,
    )
    show_component = len({doc.component for doc in ordered}) > 1
    blocks = [
        render_version_section(doc, lang, include_commits, show_component).rstrip()
        for doc in ordered
    ]
    return "\n\n".join(block for block in blocks if block) + "\n" if blocks else ""


def splice_changelog(root: Path, fragment: str, page_rel: Path) -> Path | None:
    """Replace the marked region of one changelog page. None when it is absent."""
    page = root / page_rel
    if not page.is_file():
        return None
    text = page.read_text(encoding="utf-8-sig")
    updated = splice_region(text, fragment, CHANGELOG_START, CHANGELOG_END)
    if updated is None:
        raise ValueError(f"changelog markers missing in {page_rel.as_posix()}")
    if updated != text:
        page.write_text(updated, encoding="utf-8", newline="\n")
    return page


# ---------------------------------------------------------------------------
# caches
# ---------------------------------------------------------------------------


def cache_paths(root: Path, component: str, version: str) -> tuple[Path, Path]:
    stem = f"{component}-{version}"
    return (root / REPORTS_DIR / f"{stem}.commits.json", root / REPORTS_DIR / f"{stem}.classified.json")


def write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def load_classified(path: Path) -> ClassifiedDoc | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    try:
        return ClassifiedDoc.model_validate(data)
    except ValueError:
        return None


def list_classified(root: Path) -> list[ClassifiedDoc]:
    """Every cached version, newest first — the same order the page renders in."""
    directory = root / REPORTS_DIR
    if not directory.is_dir():
        return []
    docs = [load_classified(path) for path in sorted(directory.glob("*.classified.json"))]
    loaded = [doc for doc in docs if doc is not None]
    return sorted(
        loaded,
        key=lambda doc: (doc.releaseDate, version_key(doc.version) or ()),
        reverse=True,
    )


def classify_commits(
    source: ChangeSource,
    tag,
    previous,
    commits: Sequence[Commit],
    classifier: Classifier,
) -> ClassifiedDoc:
    """Attach git facts to the classifier payload, dropping invented provenance.

    Granularity is the classifier's job (one entry per commit, splitting a commit
    whose message lists several changes), but **coverage is enforced here**: every
    commit in the range must end up either in an entry or in ``unclassifiedCommits``.
    Anything the classifier skipped is recorded there, so a run can never quietly
    under-report a release.
    """
    payload = classifier(source, commits)
    known = {commit.short for commit in commits}
    sections = [
        ClassifiedSection(
            category=section.category,
            entries=[
                ClassifiedEntry(
                    text=entry.text,
                    textEn=entry.textEn,
                    sourceCommits=[short for short in entry.sourceCommits if short in known],
                    confidence=entry.confidence,
                    tags=list(entry.tags),
                )
                for entry in section.entries
            ],
        )
        for section in payload.sections
    ]
    placed = {short for section in sections for entry in section.entries for short in entry.sourceCommits}
    declared = [short for short in payload.unclassifiedCommits if short in known]
    skipped = sorted(known - placed - set(declared))
    return ClassifiedDoc(
        component=source.name,
        componentLabel=dict(source.displayName),
        version=tag.version,
        tag=tag.name,
        previousTag=previous.name,
        releaseDate=tag.date,
        model=classifier.model,
        promptVersion=classifier.promptVersion,
        sections=sections,
        unclassifiedCommits=sorted(set(declared) | set(skipped)),
    )


def _is_stale(doc: ClassifiedDoc, classifier: Classifier) -> bool:
    return doc.model != classifier.model or doc.promptVersion != classifier.promptVersion


def build_changelog(
    root: Path,
    *,
    components: Sequence[str] | None = None,
    versions: Sequence[str] | None = None,
    classifier: Classifier | None = None,
    refresh_llm: bool = False,
    write: bool = False,
    include_commits: bool = True,
    runner: Runner = subprocess.run,
    env: Mapping[str, str] | None = None,
) -> ChangelogResult:
    """Classify the wanted tag ranges, then render every configured page from the caches.

    ``versions`` only limits which releases are classified in this run; rendering
    always uses every cached version so earlier releases are never dropped. Which
    pages exist comes from each source's ``pages`` config.
    """
    result = ChangelogResult()
    sources = load_sources(root, env)
    wanted = {name.lower() for name in components} if components else None
    if wanted is not None:
        sources = [source for source in sources if source.name.lower() in wanted]
    if not sources:
        result.notes.append(f"没有可用的来源配置（{SOURCES_PATH.as_posix()}）")
        return result

    only = set(versions) if versions else None
    for source in sources:
        if not source.repo.is_dir():
            result.notes.append(f"{source.name}: 仓库路径不存在，已跳过（{source.repo}）")
            continue
        allowed = merged_tag_names(source.repo, source.trunk, runner)
        if allowed is None:
            result.notes.append(
                f"{source.name}: 主干分支 {source.trunk!r} 不可用，未按主干过滤 tag（历史 tag 可能来自废弃分支）"
            )
        tags = list_tags(
            source.repo, source.tagPattern, runner, allowed=allowed, min_version=source.minVersion
        )
        if len(tags) < 2:
            result.notes.append(
                f"{source.name}: 主干上可识别的 tag 少于 2 个（当前 {len(tags)} 个），无法切分区间，已跳过"
            )
            continue
        result.notes.append(
            f"{source.name}: 最旧的 tag {tags[0].name} 没有前驱，作为区间起点不产出条目"
        )
        for previous, tag in tag_ranges(tags):
            if only is not None and tag.version not in only:
                continue
            classified_path = cache_paths(root, source.name, tag.version)[1]
            cached = load_classified(classified_path)
            if classifier is None:
                if cached is None:
                    result.pending.append(f"{source.name} {tag.version}")
                continue
            if not (refresh_llm or cached is None or _is_stale(cached, classifier)):
                continue
            if not is_ancestor(source.repo, previous.name, tag.name, runner):
                result.notes.append(
                    f"{source.name}: {previous.name} 不是 {tag.name} 的祖先，区间可疑，已跳过"
                )
                continue
            commits = filter_commits(git_log(source.repo, f"{previous.name}..{tag.name}", source, runner), source)
            if not commits:
                result.notes.append(f"{source.name} {tag.version}: 区间内没有可收录的提交")
            commits_path, classified_path = cache_paths(root, source.name, tag.version)
            doc = classify_commits(source, tag, previous, commits, classifier)
            if doc.unclassifiedCommits:
                result.notes.append(
                    f"{source.name} {tag.version}: {len(doc.unclassifiedCommits)} 条提交未被归类，"
                    "已记入 unclassifiedCommits（不渲染）"
                )
            if write:
                write_json(commits_path, [asdict(commit) for commit in commits])
                write_json(classified_path, doc.model_dump(mode="json"))

    result.docs = list_classified(root)
    if not result.docs:
        result.notes.append("没有任何已归类的版本缓存，自动区保持原样")
        return result

    # Render from the caches, per component page. A component without caches keeps
    # whatever its page already shows rather than being blanked.
    for source in sources:
        docs = [doc for doc in result.docs if doc.component == source.name]
        if not docs:
            continue
        pending_pages = [rel for _lang, rel in source.pages if not (root / rel).is_file()]
        for rel in pending_pages:
            result.notes.append(
                f"{source.name}: 页面不存在，未写入（{rel.as_posix()}）——先按模板建好带 CHANGELOG 标记的页面"
            )
        for lang, rel in source.pages:
            if not (root / rel).is_file():
                continue
            result.rendered.append(
                RenderedPage(
                    component=source.name,
                    lang=lang,
                    page=rel,
                    fragment=render_fragment(docs, lang, include_commits),
                )
            )
    if write:
        written: list[Path] = []
        for item in result.rendered:
            page = splice_changelog(root, item.fragment, item.page)
            if page is not None:
                written.append(page)
        result.written = tuple(written)
    return result


__all__ = [
    "ChangeSource",
    "ChangelogResult",
    "Classifier",
    "Commit",
    "GitError",
    "REPORTS_DIR",
    "RenderedPage",
    "SOURCES_PATH",
    "Tag",
    "build_changelog",
    "cache_paths",
    "classify_commits",
    "dedupe_tags",
    "entries_for",
    "escape_mdx",
    "expand_env",
    "filter_commits",
    "git_log",
    "is_ancestor",
    "list_classified",
    "list_tags",
    "load_classified",
    "load_sources",
    "merged_tag_names",
    "parse_git_log",
    "parse_sources",
    "render_fragment",
    "render_version_section",
    "splice_changelog",
    "tag_ranges",
    "update_tags",
    "version_key",
]
