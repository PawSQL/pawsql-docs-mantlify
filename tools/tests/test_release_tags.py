from __future__ import annotations

from pathlib import Path
from subprocess import CompletedProcess

import pytest

from pawsql_doc import release_tags as rt
from pawsql_doc.models.changelog import ReleaseBoundaries, ReleaseBoundary

SOURCE_TEMPLATE = """sources:
  - name: engine
    displayName:
      zh: 引擎
      en: Engine
    repo: __REPO__
    trunk: master
    tagPattern: '^engine-v(?P<version>[0-9]+\\.[0-9]+\\.[0-9]+)$'
    pages:
      zh: docs/changelog/engine/index.mdx
"""

BOUNDARY_TEMPLATE = """component: engine
tagFormat: 'engine-v{version}'
start: '1.2.0'
deliveries:
  - commit: aaa1111
    date: 2026-01-31
    verified: __V1__
    major: false
  - commit: bbb2222
    date: 2026-02-28
    verified: __V2__
    major: true
  - commit: ccc3333
    date: 2026-03-31
    verified: __V3__
    major: false
"""

SHAS = {
    "aaa1111": "aaa1111" + "0" * 33,
    "bbb2222": "bbb2222" + "0" * 33,
    "ccc3333": "ccc3333" + "0" * 33,
}


class FakeGit:
    """Records every git call; answers from canned state instead of a real repo."""

    def __init__(
        self,
        *,
        tags="",
        trunk_tags="",
        unknown=(),
        off_trunk=(),
        order_bad=False,
        fail_tag=False,
        trunk="master",
    ):
        self.tags = tags
        self.trunk_tags = trunk_tags
        self.unknown = set(unknown)
        self.off_trunk = set(off_trunk)
        self.order_bad = order_bad
        self.fail_tag = fail_tag
        self.trunk = trunk
        self.calls: list[list[str]] = []
        self.envs: list[dict | None] = []

    def __call__(self, args, **kwargs):
        self.calls.append(list(args))
        self.envs.append(kwargs.get("env"))
        tail = args[3:]
        head = tail[0] if tail else ""

        if head == "for-each-ref":
            return CompletedProcess(args, 0, self.tags, "")
        if head == "tag" and len(tail) > 1 and tail[1] == "--merged":
            return CompletedProcess(args, 0, self.trunk_tags, "")
        if head == "rev-parse":
            ref = tail[-1].replace("^{commit}", "")
            if ref in self.unknown:
                return CompletedProcess(args, 1, "", "unknown revision")
            return CompletedProcess(args, 0, SHAS.get(ref, ref) + "\n", "")
        if head == "merge-base":
            old, new = tail[-2], tail[-1]
            if old in {SHAS.get(name, name) for name in self.off_trunk}:
                return CompletedProcess(args, 1, "", "")
            # The order check compares two shas; the trunk check names the branch.
            if self.order_bad and new != self.trunk:
                return CompletedProcess(args, 1, "", "")
            return CompletedProcess(args, 0, "", "")
        if head == "tag":
            return CompletedProcess(args, 1 if self.fail_tag else 0, "", "boom" if self.fail_tag else "")
        if head == "push":
            return CompletedProcess(args, 0, "", "")
        return CompletedProcess(args, 1, "", f"unexpected git subcommand {head!r}")


def write_config(repo: Path, *, source_repo: Path) -> None:
    path = repo / rt.BOUNDARIES_DIR.parent / "changelog-sources.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(SOURCE_TEMPLATE.replace("__REPO__", str(source_repo)), encoding="utf-8")


def write_boundaries(repo: Path, *, verified=True, component="engine") -> None:
    path = rt.boundaries_path(repo, component)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = BOUNDARY_TEMPLATE
    for token, flag in (("__V1__", verified), ("__V2__", verified), ("__V3__", verified)):
        text = text.replace(token, "true" if flag else "false")
    path.write_text(text, encoding="utf-8")


def prepared_repo(repo: Path) -> Path:
    source_repo = repo / "engine-repo"
    source_repo.mkdir()
    write_config(repo, source_repo=source_repo)
    write_boundaries(repo)
    return source_repo


# ---------------------------------------------------------------------------
# version numbering
# ---------------------------------------------------------------------------


def boundaries(start="1.2.0", majors=(False, True, False)):
    return ReleaseBoundaries(
        component="engine",
        tagFormat="engine-v{version}",
        start=start,
        deliveries=[
            ReleaseBoundary(commit=f"{index:07d}", date=f"2026-0{index + 1}-01", verified=True, major=major)
            for index, major in enumerate(majors)
        ],
    )


def test_compute_versions_bumps_patch_and_minor():
    versions = [version for _delivery, version in rt.compute_versions(boundaries())]

    assert versions == ["1.2.0", "1.3.0", "1.3.1"]


def test_compute_versions_starts_at_the_configured_version():
    versions = [version for _delivery, version in rt.compute_versions(boundaries(start="2.5.9", majors=(False,)))]

    assert versions == ["2.5.9"]


def test_tag_timestamp_is_noon_in_the_release_timezone():
    assert rt.tag_timestamp("2026-01-31") == "2026-01-31T12:00:00+08:00"


def test_render_command_pins_the_tag_date_and_message():
    tag = rt.PlannedTag("engine-v1.2.0", "1.2.0", "aaa1111", "2026-01-31", "create", label="Engine")

    command = rt.render_command(Path("E:/repo"), tag)

    assert 'GIT_COMMITTER_DATE="2026-01-31T12:00:00+08:00"' in command
    assert "git -C" in command and "tag -a engine-v1.2.0 aaa1111" in command
    assert "PawSQL Engine 1.2.0" in command


def test_tag_message_uses_the_component_label():
    server = rt.PlannedTag("release-v1.2.3", "1.2.3", "afd8e871", "2026-03-31", "create", label="Server")

    assert server.message == "PawSQL Server 1.2.3 (2026-03-31)"
    assert rt.PlannedTag("release-v1.2.3", "1.2.3", "afd8e871", "2026-03-31", "create").message == (
        "PawSQL 1.2.3 (2026-03-31)"
    )


# ---------------------------------------------------------------------------
# planning
# ---------------------------------------------------------------------------


def test_plan_creates_every_tag_when_the_table_is_clean(repo):
    prepared_repo(repo)

    plan = rt.plan_tags(repo, runner=FakeGit())

    assert plan.ok
    assert [(t.name, t.version) for t in plan.to_create] == [
        ("engine-v1.2.0", "1.2.0"),
        ("engine-v1.3.0", "1.3.0"),
        ("engine-v1.3.1", "1.3.1"),
    ]
    assert plan.tags[0].date == "2026-01-31"


def test_plan_refuses_while_rows_are_unverified(repo):
    source_repo = repo / "engine-repo"
    source_repo.mkdir()
    write_config(repo, source_repo=source_repo)
    write_boundaries(repo, verified=False)

    plan = rt.plan_tags(repo, runner=FakeGit())

    assert not plan.ok
    assert any("还没核对" in problem for problem in plan.problems)


def test_plan_refuses_an_unknown_commit(repo):
    prepared_repo(repo)

    plan = rt.plan_tags(repo, runner=FakeGit(unknown={"bbb2222"}))

    assert not plan.ok
    assert any("不存在" in problem for problem in plan.problems)


def test_plan_refuses_a_commit_off_the_trunk(repo):
    prepared_repo(repo)

    plan = rt.plan_tags(repo, runner=FakeGit(off_trunk={"bbb2222"}))

    assert not plan.ok
    assert any("不在主干" in problem for problem in plan.problems)


def test_plan_refuses_a_table_that_is_out_of_order(repo):
    prepared_repo(repo)

    plan = rt.plan_tags(repo, runner=FakeGit(order_bad=True))

    assert not plan.ok
    assert any("边界顺序不对" in problem for problem in plan.problems)


def test_plan_skips_tags_that_already_point_at_the_same_commit(repo):
    prepared_repo(repo)
    tags = "engine-v1.2.0 tag %s %s\n" % (SHAS["aaa1111"], "9" * 40)

    plan = rt.plan_tags(repo, runner=FakeGit(tags=tags))

    assert plan.ok
    by_name = {tag.name: tag for tag in plan.tags}
    assert by_name["engine-v1.2.0"].action == "skip"
    assert by_name["engine-v1.3.0"].action == "create"


def test_plan_refuses_a_tag_that_points_somewhere_else(repo):
    prepared_repo(repo)
    tags = "engine-v1.2.0 tag %s %s\n" % ("8" * 40, "9" * 40)

    plan = rt.plan_tags(repo, runner=FakeGit(tags=tags))

    assert not plan.ok
    assert any("冲突" in problem and "不覆盖" in problem for problem in plan.problems)


def test_plan_notes_drift_when_the_trunk_has_uncovered_tags(repo):
    prepared_repo(repo)
    tags = "engine-v9.9.9 commit  %s\n" % ("7" * 40)

    plan = rt.plan_tags(repo, runner=FakeGit(tags=tags, trunk_tags="engine-v9.9.9"))

    assert any("不在边界表里" in note for note in plan.notes)


def test_plan_refuses_a_missing_boundary_table(repo):
    with pytest.raises(rt.TagError):
        rt.plan_tags(repo, runner=FakeGit())


def test_plan_requires_a_component_once_several_tables_exist(repo):
    prepared_repo(repo)
    write_boundaries(repo, component="server")

    assert rt.available_components(repo) == ["engine", "server"]
    with pytest.raises(rt.TagError) as excinfo:
        rt.plan_tags(repo, runner=FakeGit())
    assert "--component" in str(excinfo.value)


def test_plan_rejects_a_table_whose_component_disagrees_with_its_filename(repo):
    prepared_repo(repo)
    path = rt.boundaries_path(repo, "server")
    path.write_text(rt.boundaries_path(repo, "engine").read_text(encoding="utf-8"), encoding="utf-8")

    with pytest.raises(rt.TagError) as excinfo:
        rt.plan_tags(repo, component="server", runner=FakeGit())

    assert "不一致" in str(excinfo.value)


# ---------------------------------------------------------------------------
# applying
# ---------------------------------------------------------------------------


def test_apply_creates_tags_with_the_release_date_env(repo):
    prepared_repo(repo)
    runner = FakeGit()
    plan = rt.plan_tags(repo, runner=runner)
    runner.calls.clear()
    runner.envs.clear()

    created = rt.apply_tags(plan, runner=runner)

    assert created == ["engine-v1.2.0", "engine-v1.3.0", "engine-v1.3.1"]
    tag_calls = [call for call in runner.calls if "tag" in call and "-a" in call]
    envs = [env for call, env in zip(runner.calls, runner.envs) if "tag" in call and "-a" in call]
    assert len(tag_calls) == 3
    assert [env["GIT_COMMITTER_DATE"] for env in envs] == [
        "2026-01-31T12:00:00+08:00",
        "2026-02-28T12:00:00+08:00",
        "2026-03-31T12:00:00+08:00",
    ]
    assert not any("push" in call for call in runner.calls)


def test_apply_pushes_only_when_asked(repo):
    prepared_repo(repo)
    runner = FakeGit()
    plan = rt.plan_tags(repo, runner=runner)
    runner.calls.clear()

    rt.apply_tags(plan, runner=runner, push=True)

    push_calls = [call for call in runner.calls if "push" in call]
    assert push_calls == [
        ["git", "-C", str(plan.repo), "push", "origin", "engine-v1.2.0", "engine-v1.3.0", "engine-v1.3.1"]
    ]


def test_apply_refuses_a_plan_with_problems(repo):
    prepared_repo(repo)
    plan = rt.plan_tags(repo, runner=FakeGit(unknown={"aaa1111"}))

    with pytest.raises(rt.TagError):
        rt.apply_tags(plan, runner=FakeGit())


def test_apply_reports_a_failing_git_tag(repo):
    prepared_repo(repo)
    runner = FakeGit()
    plan = rt.plan_tags(repo, runner=runner)

    with pytest.raises(rt.TagError):
        rt.apply_tags(plan, runner=FakeGit(fail_tag=True))


def test_cli_accepts_the_command():
    from pawsql_doc.cli import build_parser

    args = build_parser().parse_args(["tag-releases", "--apply", "--push"])

    assert args.apply and args.push and args.component is None
