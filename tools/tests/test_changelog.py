from __future__ import annotations

import re
from pathlib import Path
from subprocess import CompletedProcess

from pawsql_doc import changelog as cl

SERVER_PAGE = "docs/changelog/server/index.mdx"
ENGINE_PAGE = "docs/changelog/engine/index.mdx"

PAGE = """---
id: changelog-server-index
title: 服务端变更日志
type: article
status: draft
subtype: release-note
language: zh
translationKey: changelog-server-index
---

# 服务端变更日志

引言保持可编辑。

{{/* CHANGELOG:START */}}
{{/* CHANGELOG:END */}}
"""


def rec(sha, short, date, author, subject, body="", files=()):
    return (
        f"{cl.RECORD_SEP}{sha}{cl.FIELD_SEP}{short}{cl.FIELD_SEP}{date}{cl.FIELD_SEP}"
        f"{author}{cl.FIELD_SEP}{subject}{cl.FIELD_SEP}{body}{cl.FIELD_SEP}\n"
        + "".join(f"{name}\n" for name in files)
    )


class FakeGit:
    """Stands in for subprocess.run so tests never touch a real repository."""

    def __init__(self, *, merged="", refs="", log="", ancestor=True):
        self.merged = merged
        self.refs = refs
        self.log = log
        self.ancestor = ancestor

    def __call__(self, args, **_kwargs):
        sub = args[3] if len(args) > 3 else ""
        if sub == "tag":
            return CompletedProcess(args, 0, self.merged, "")
        if sub == "for-each-ref":
            return CompletedProcess(args, 0, self.refs, "")
        if sub == "merge-base":
            return CompletedProcess(args, 0 if self.ancestor else 1, "", "")
        if sub == "log":
            return CompletedProcess(args, 0, self.log, "")
        return CompletedProcess(args, 1, "", f"unexpected git subcommand {sub!r}")


def make_source(**overrides):
    base = dict(
        name="server",
        displayName={"zh": "服务端", "en": "Server"},
        repo=Path("/tmp/src"),
        trunk="main",
        tagPattern=re.compile(r"^release-v(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$"),
        pages=(("zh", Path(SERVER_PAGE)),),
    )
    base.update(overrides)
    return cl.ChangeSource(**base)


# The default fixture mirrors the end-to-end source ("server"); tests that exercise
# engine-only vocabulary pass component="engine" explicitly.
def doc(component="server", label="服务端", version="0.4.16", date="2023-03-24", **overrides):
    base = dict(
        component=component,
        componentLabel={"zh": label, "en": "Server"},
        version=version,
        tag=f"release-v{version}",
        releaseDate=date,
        sections=[
            cl.ClassifiedSection(
                category="缺陷修复",
                entries=[
                    cl.ClassifiedEntry(
                        text=f"修复 {version}",
                        sourceCommits=[f"{component}01"],
                        tags=["缺陷修复"],
                    )
                ],
            )
        ],
    )
    base.update(overrides)
    return cl.ClassifiedDoc(**base)


# ---------------------------------------------------------------------------
# parsing and filtering (pure)
# ---------------------------------------------------------------------------


def test_parse_git_log_reads_fields_body_and_files():
    text = rec("a" * 40, "aaaaaaa", "2026-09-22T10:00:00+08:00", "tomas", "feat: 新增能力", "细节说明", ["a/b.java", "c/d.java"])
    commits = cl.parse_git_log(text)

    assert len(commits) == 1
    commit = commits[0]
    assert commit.short == "aaaaaaa"
    assert commit.date == "2026-09-22"
    assert commit.subject == "feat: 新增能力"
    assert commit.body == "细节说明"
    assert commit.files == ("a/b.java", "c/d.java")


def test_parse_git_log_skips_trailing_and_malformed_chunks():
    assert cl.parse_git_log("") == []
    assert cl.parse_git_log("\n\n") == []
    assert cl.parse_git_log(f"{cl.RECORD_SEP}only{cl.FIELD_SEP}two") == []


def test_version_key_is_numeric_not_lexicographic():
    assert cl.version_key("0.4.9") < cl.version_key("0.4.76")
    assert cl.version_key("0.3.01") == (0, 3, 1)
    assert cl.version_key("v1") is None


def test_dedupe_tags_keeps_highest_version_per_commit():
    tags = [
        cl.Tag("release-v0.4.12", "0.4.12", (0, 4, 12), "same", "2023-03-24"),
        cl.Tag("release-v0.4.16", "0.4.16", (0, 4, 16), "same", "2023-03-24"),
        cl.Tag("release-v0.4.11", "0.4.11", (0, 4, 11), "other", "2023-03-08"),
    ]
    assert [tag.name for tag in cl.dedupe_tags(tags)] == ["release-v0.4.11", "release-v0.4.16"]


def test_list_tags_applies_pattern_and_allowed_set():
    refs = (
        "release-v0.4.76 abc 2023-06-30T00:00:00+08:00\n"
        "release-v1.0.0 def 2026-01-01T00:00:00+08:00\n"
        "nightly ghi 2026-01-02T00:00:00+08:00\n"
    )
    runner = FakeGit(refs=refs)
    source = make_source()

    tags = cl.list_tags(source.repo, source.tagPattern, runner, allowed={"release-v0.4.76"})

    assert [tag.name for tag in tags] == ["release-v0.4.76"]
    assert tags[0].commit == "abc"
    assert tags[0].date == "2023-06-30"


def test_list_tags_drops_tags_below_min_version():
    refs = (
        "release-v0.4.76 abc 2023-06-30T00:00:00+08:00\n"
        "release-v0.5.0 ccc 2024-10-30T00:00:00+08:00\n"
        "release-v0.5.2 ddd 2024-12-31T00:00:00+08:00\n"
    )
    runner = FakeGit(refs=refs)
    source = make_source()

    tags = cl.list_tags(source.repo, source.tagPattern, runner, min_version=(0, 5, 0))

    assert [tag.name for tag in tags] == ["release-v0.5.0", "release-v0.5.2"]


def test_parse_sources_reads_min_version():
    (source,) = cl.parse_sources(
        {
            "sources": [
                {
                    "name": "server",
                    "displayName": {"zh": "服务端", "en": "Server"},
                    "repo": "/tmp/server",
                    "trunk": "main",
                    "tagPattern": r"^release-v(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$",
                    "minVersion": "0.5.0",
                    "pages": {"zh": "docs/changelog/server/index.mdx"},
                }
            ]
        }
    )

    assert source.minVersion == (0, 5, 0)


def test_filter_commits_drops_merges_and_skipped_prefixes():
    source = make_source(skipPrefixes=("chore", "docs"), skipMerge=True)
    commits = [
        cl.Commit("1", "1111111", "2026-01-01", "a", "feat: 对外能力"),
        cl.Commit("2", "2222222", "2026-01-01", "a", "chore: 依赖升级"),
        cl.Commit("3", "3333333", "2026-01-01", "a", "docs(api): 文档调整"),
        cl.Commit("4", "4444444", "2026-01-01", "a", "Merge branch 'dev'"),
        cl.Commit("5", "5555555", "2026-01-01", "a", "优化sql解析器"),
    ]
    assert [c.short for c in cl.filter_commits(commits, source)] == ["1111111", "5555555"]


def test_filter_commits_drops_commits_touching_only_excluded_paths():
    source = make_source(pathExclude=("docs/", "*.md"))
    only_docs = cl.Commit("1", "1111111", "2026-01-01", "a", "更新说明", files=("docs/x.md",))
    code_and_docs = cl.Commit("2", "2222222", "2026-01-01", "a", "顺带更新说明", files=("src/A.java", "docs/x.md"))

    assert cl.filter_commits([only_docs, code_and_docs], source) == [code_and_docs]


def test_filter_commits_requires_an_included_path_when_configured():
    source = make_source(pathInclude=("paw-indexadvisor/src/",))
    inside = cl.Commit("1", "1111111", "2026-01-01", "a", "改动", files=("paw-indexadvisor/src/A.java",))
    outside = cl.Commit("2", "2222222", "2026-01-01", "a", "改动", files=("config/config.properties",))

    assert cl.filter_commits([inside, outside], source) == [inside]


def test_expand_env_uses_default_then_raises_when_required():
    assert cl.expand_env("${PAWSQL_X:-E:/fallback}", {}) == "E:/fallback"
    assert cl.expand_env("${PAWSQL_X}", {"PAWSQL_X": "E:/real"}) == "E:/real"

    import pytest

    with pytest.raises(ValueError):
        cl.expand_env("${PAWSQL_MISSING}", {})


def test_parse_sources_keeps_the_page_mapping():
    (source,) = cl.parse_sources(
        {
            "sources": [
                {
                    "name": "engine",
                    "displayName": {"zh": "引擎", "en": "Engine"},
                    "repo": "/tmp/engine",
                    "trunk": "master",
                    "tagPattern": r"^v(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$",
                    "pages": {"en": "docs/en/changelog/engine/index.mdx", "zh": ENGINE_PAGE},
                }
            ]
        }
    )

    assert source.pages == (("en", Path("docs/en/changelog/engine/index.mdx")), ("zh", Path(ENGINE_PAGE)))


def test_parse_sources_rejects_a_source_without_pages():
    import pytest

    with pytest.raises(ValueError):
        cl.parse_sources(
            {
                "sources": [
                    {
                        "name": "server",
                        "displayName": {"zh": "服务端", "en": "Server"},
                        "repo": "/tmp/server",
                        "tagPattern": r"^v(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$",
                    }
                ]
            }
        )


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------


def test_escape_mdx_neutralizes_jsx_and_html():
    escaped = cl.escape_mdx("用 {a < b} 判断 <!-- 注释 --> `code`")

    assert "{" not in escaped and "}" not in escaped
    assert "<" not in escaped and ">" not in escaped
    assert "`" not in escaped
    assert "&#123;" in escaped and "&lt;" in escaped
    assert "\n" not in escaped


def test_render_fragment_orders_newest_first_and_is_idempotent():
    older = doc(version="0.4.11", date="2023-03-08")
    newer = doc(version="0.4.76", date="2023-06-30")

    first = cl.render_fragment([older, newer])
    second = cl.render_fragment([newer, older])

    assert first == second
    assert first.index("0.4.76") < first.index("0.4.11")


def test_single_component_page_omits_the_component_name_from_the_label():
    single = cl.render_fragment([doc()])
    assert '<Update label="0.4.16" description="2023-03-24"' in single
    assert "服务端 0.4.16" not in single
    assert single.rstrip().endswith("</Update>")


def test_shared_page_repeats_the_component_name_in_the_label():
    shared = cl.render_fragment([doc(), doc(component="engine", label="引擎", version="1.0.0")])

    assert '<Update label="服务端 0.4.16"' in shared
    assert '<Update label="引擎 1.0.0"' in shared


def test_each_component_orders_its_page_by_its_own_vocabulary():
    """engine and server have different filter lists; each page uses its own."""
    engine = doc(
        component="engine",
        label="引擎",
        sections=[
            cl.ClassifiedSection(category="索引引擎", entries=[cl.ClassifiedEntry(text="索引", sourceCommits=["a1"], tags=["索引引擎"])]),
            cl.ClassifiedSection(category="审核引擎", entries=[cl.ClassifiedEntry(text="规则", sourceCommits=["b2"], tags=["审核引擎"])]),
        ],
    )
    server = doc(
        component="server",
        sections=[
            cl.ClassifiedSection(category="权限与安全", entries=[cl.ClassifiedEntry(text="认证", sourceCommits=["c3"], tags=["权限与安全"])]),
            cl.ClassifiedSection(category="SQL 审核与优化", entries=[cl.ClassifiedEntry(text="审核", sourceCommits=["d4"], tags=["SQL 审核与优化"])]),
        ],
    )

    engine_fragment = cl.render_fragment([engine])
    server_fragment = cl.render_fragment([server])

    # engine order: 审核引擎 before 索引引擎; server order: SQL 审核与优化 before 权限与安全
    assert engine_fragment.index("### 审核引擎") < engine_fragment.index("### 索引引擎")
    assert server_fragment.index("### SQL 审核与优化") < server_fragment.index("### 权限与安全")
    assert cl.update_tags(server) == ["SQL 审核与优化", "权限与安全"]


def test_update_block_tags_are_the_union_of_entry_tags():
    rich = doc(
        component="engine",
        sections=[
            cl.ClassifiedSection(
                category="审核引擎",
                entries=[
                    cl.ClassifiedEntry(text="新能力", sourceCommits=["a1"], tags=["审核引擎"]),
                    cl.ClassifiedEntry(text="修复规则缺陷", sourceCommits=["d4"], tags=["审核引擎", "缺陷修复"]),
                ],
            ),
            cl.ClassifiedSection(category="SQL解析与数据库支持", entries=[cl.ClassifiedEntry(text="新库", sourceCommits=["b2"], tags=["SQL解析与数据库支持"])]),
            cl.ClassifiedSection(category="internal", entries=[cl.ClassifiedEntry(text="内部", sourceCommits=["c3"])]),
        ]
    )

    fragment = cl.render_fragment([rich])

    # vocabulary order, 缺陷修复 last; internal contributes nothing
    assert 'tags={["审核引擎", "SQL解析与数据库支持", "缺陷修复"]}' in fragment
    assert "内部变更" not in fragment
    assert cl.update_tags(rich) == ["审核引擎", "SQL解析与数据库支持", "缺陷修复"]


def test_a_fix_can_sit_in_a_subsystem_group_and_still_be_tagged_as_a_fix():
    grouped = doc(
        component="engine",
        sections=[
            cl.ClassifiedSection(
                category="索引引擎",
                entries=[cl.ClassifiedEntry(text="修复索引推荐排序", sourceCommits=["a1"], tags=["索引引擎", "缺陷修复"])],
            )
        ]
    )

    fragment = cl.render_fragment([grouped])

    assert "### 索引引擎" in fragment and "### 缺陷修复" not in fragment
    assert 'tags={["索引引擎", "缺陷修复"]}' in fragment


def test_update_block_omits_tags_when_only_internal_entries_exist():
    internal_only = doc(
        sections=[cl.ClassifiedSection(category="internal", entries=[cl.ClassifiedEntry(text="内部", sourceCommits=["a1"])])]
    )

    fragment = cl.render_fragment([internal_only])

    assert "<Update label=" in fragment and "tags={" not in fragment
    assert "没有可对外展示的变更" in fragment


def test_update_block_escapes_entry_text_but_keeps_its_own_markup():
    tricky = doc(
        component="engine",
        sections=[
            cl.ClassifiedSection(
                category="SQL解析与数据库支持",
                entries=[cl.ClassifiedEntry(text="修复 {a < b} 与 `code`", sourceCommits=["a1"], tags=["SQL解析与数据库支持"])],
            )
        ]
    )

    fragment = cl.render_fragment([tricky])
    body = fragment.split("\n", 1)[1]

    assert "&#123;a &lt; b&#125;" in body
    assert "&#96;code&#96;" in body
    # the closing tag is the only angle bracket below the opening one
    assert body.replace("</Update>", "").count("<") == 0


def test_render_merges_repeated_categories_instead_of_dropping_them():
    """A classifier may emit the same category twice; none of it may be lost."""
    doc = cl.ClassifiedDoc(
        component="engine",
        componentLabel={"zh": "引擎", "en": "Engine"},
        version="1.0.0",
        tag="engine-v1.0.0",
        releaseDate="2026-01-01",
        sections=[
            cl.ClassifiedSection(category="缺陷修复", entries=[cl.ClassifiedEntry(text="修复甲", sourceCommits=["a1"])]),
            cl.ClassifiedSection(category="缺陷修复", entries=[cl.ClassifiedEntry(text="修复乙", sourceCommits=["b2"])]),
        ],
    )

    fragment = cl.render_fragment([doc])

    assert "修复甲" in fragment and "修复乙" in fragment
    assert fragment.count("### 缺陷修复") == 1
    assert len(cl.entries_for(doc, "缺陷修复")) == 2


def test_render_fragment_notes_a_release_without_entries():
    empty = doc(sections=[cl.ClassifiedSection(category="internal", entries=[])])
    assert "没有可对外展示的变更" in cl.render_fragment([empty])


def test_internal_entries_are_never_rendered():
    with_internal = doc(
        sections=[
            cl.ClassifiedSection(category="internal", entries=[cl.ClassifiedEntry(text="升级依赖", sourceCommits=["x1"])]),
            cl.ClassifiedSection(category="缺陷修复", entries=[cl.ClassifiedEntry(text="修复一个缺陷", sourceCommits=["y2"], tags=["缺陷修复"])]),
        ]
    )

    fragment = cl.render_fragment([with_internal])

    assert "升级依赖" not in fragment
    assert "修复一个缺陷" in fragment
    assert "internal" not in fragment


def test_splice_changelog_replaces_only_the_marked_region(repo):
    page = repo / SERVER_PAGE
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(PAGE.format(), encoding="utf-8")

    written = cl.splice_changelog(repo, "## 0.4.16 — 2023-03-24\n", Path(SERVER_PAGE))

    assert written == page
    text = page.read_text(encoding="utf-8")
    assert "引言保持可编辑。" in text
    assert "## 0.4.16 — 2023-03-24" in text
    assert text.index("引言") < text.index("CHANGELOG:START") < text.index("## 0.4.16")


def test_splice_changelog_returns_none_when_the_page_is_absent(repo):
    assert cl.splice_changelog(repo, "## x\n", Path(SERVER_PAGE)) is None


def test_splice_changelog_raises_when_markers_are_missing(repo):
    page = repo / SERVER_PAGE
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text("---\nid: x\n---\n\n没有标记\n", encoding="utf-8")

    import pytest

    with pytest.raises(ValueError):
        cl.splice_changelog(repo, "## x\n", Path(SERVER_PAGE))


# ---------------------------------------------------------------------------
# end-to-end build
# ---------------------------------------------------------------------------


SOURCE_BLOCK = """  - name: {name}
    displayName:
      zh: {zh}
      en: {en}
    repo: {repo}
    trunk: main
    tagPattern: '{tagPattern}'
    pages:
{pages}
    skipPrefixes: [chore, docs]
    skipMerge: true
"""

PAGE_BLOCK = "{indent}{lang}: {rel}"


def write_sources(root, repo_path, sources=None):
    """Write the source config; each entry is a dict with name/zh/en/pages/tagPattern."""
    entries = sources or [{"name": "server", "zh": "服务端", "en": "Server", "pages": {"zh": SERVER_PAGE}}]
    blocks = []
    for entry in entries:
        pages = "\n".join(
            f"      {lang}: {rel}" for lang, rel in entry["pages"].items()
        )
        blocks.append(
            SOURCE_BLOCK.format(
                name=entry["name"],
                zh=entry["zh"],
                en=entry["en"],
                repo=repo_path,
                tagPattern=entry.get("tagPattern", r"^release-v\.?(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$"),
                pages=pages,
            )
        )
    path = root / cl.SOURCES_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("sources:\n" + "".join(blocks), encoding="utf-8")
    return path


def write_page(root, rel=SERVER_PAGE):
    page = root / rel
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(PAGE.format(), encoding="utf-8")
    return page


def fake_classifier(calls=None, model="claude-opus-5", prompt_version="changelog-classify-1"):
    def classify(source, commits):
        if calls is not None:
            calls.append([c.short for c in commits])
        return cl.ClassifiedPayload(
            sections=[
                cl.ClassifiedSection(
                    category="审核引擎",
                    entries=[
                        cl.ClassifiedEntry(text="新增状态控制接口", sourceCommits=["2222222", "deadbee"], tags=["审核引擎"])
                    ],
                ),
                cl.ClassifiedSection(category="internal", entries=[cl.ClassifiedEntry(text="内部重构", sourceCommits=["3333333"])]),
            ],
            unclassifiedCommits=["9999999"],
        )

    return cl.Classifier(model=model, promptVersion=prompt_version, classify=classify)


def build_runner(ancestor=True):
    refs = "release-v0.4.11 aaa 2023-03-08T00:00:00+08:00\nrelease-v0.4.16 bbb 2023-03-24T00:00:00+08:00\n"
    log = rec("b" * 40, "2222222", "2023-03-20T10:00:00+08:00", "tomas", "feat: 新增状态控制接口", files=["src/A.java"]) + rec(
        "c" * 40, "3333333", "2023-03-21T10:00:00+08:00", "tomas", "chore: 依赖升级", files=["pom.xml"]
    )
    return FakeGit(merged="release-v0.4.11\nrelease-v0.4.16\n", refs=refs, log=log, ancestor=ancestor)


def test_build_changelog_classifies_splices_and_caches(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    page = write_page(repo)
    seen = []

    result = cl.build_changelog(repo, classifier=fake_classifier(seen), write=True, runner=build_runner())

    text = page.read_text(encoding="utf-8")
    assert '<Update label="0.4.16" description="2023-03-24" tags={["审核引擎"]}>' in text
    assert "新增状态控制接口" in text
    assert "(2222222)" in text
    assert "内部重构" not in text  # internal changes stay cached but off the page
    assert [item.page for item in result.rendered] == [Path(SERVER_PAGE)]
    assert result.written == (page,)
    # only the conventional feat survives filtering; the chore commit is dropped
    assert seen == [["2222222"]]
    assert (repo / cl.REPORTS_DIR / "server-0.4.16.classified.json").is_file()
    assert (repo / cl.REPORTS_DIR / "server-0.4.16.commits.json").is_file()


def test_build_changelog_renders_every_configured_language(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    en_rel = "docs/en/changelog/server/index.mdx"
    write_sources(
        repo,
        source_repo,
        sources=[{"name": "server", "zh": "服务端", "en": "Server", "pages": {"zh": SERVER_PAGE, "en": en_rel}}],
    )
    write_page(repo)
    write_page(repo, en_rel)

    result = cl.build_changelog(repo, classifier=fake_classifier(), write=True, runner=build_runner())

    assert sorted(item.lang for item in result.rendered) == ["en", "zh"]
    assert "### Audit engine" in (repo / en_rel).read_text(encoding="utf-8")
    assert "### 审核引擎" in (repo / SERVER_PAGE).read_text(encoding="utf-8")


def test_classify_commits_records_commits_the_classifier_skipped():
    """Coverage is enforced by the pipeline: a skipped commit is never silently lost."""
    commits = [
        cl.Commit("1", "1111111", "2026-01-01", "a", "feat: 甲"),
        cl.Commit("2", "2222222", "2026-01-01", "a", "feat: 乙"),
        cl.Commit("3", "3333333", "2026-01-01", "a", "chore: 丙"),
    ]

    def classify(_source, _commits):
        return cl.ClassifiedPayload(
            sections=[
                cl.ClassifiedSection(
                    category="审核引擎",
                    entries=[cl.ClassifiedEntry(text="甲", sourceCommits=["1111111"], tags=["审核引擎"])],
                )
            ],
            unclassifiedCommits=["3333333"],
        )

    doc = cl.classify_commits(
        make_source(),
        cl.Tag("release-v0.4.16", "0.4.16", (0, 4, 16), "sha", "2026-01-01"),
        cl.Tag("release-v0.4.15", "0.4.15", (0, 4, 15), "prev", "2026-01-01"),
        commits,
        cl.Classifier(model="m", promptVersion="p", classify=classify),
    )

    placed = {short for section in doc.sections for entry in section.entries for short in entry.sourceCommits}
    assert placed == {"1111111"}
    # the classifier declared 3333333, and 2222222 it never mentioned at all
    assert doc.unclassifiedCommits == ["2222222", "3333333"]


def test_build_changelog_notes_commits_the_classifier_skipped(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    write_page(repo)

    def places_nothing(_source, _commits):
        return cl.ClassifiedPayload(sections=[])

    result = cl.build_changelog(
        repo,
        classifier=cl.Classifier(model="m", promptVersion="p", classify=places_nothing),
        write=True,
        runner=build_runner(),
    )

    assert any("未被归类" in note for note in result.notes)
    cached = cl.load_classified(repo / cl.REPORTS_DIR / "server-0.4.16.classified.json")
    assert cached is not None and cached.unclassifiedCommits == ["2222222"]


def test_build_changelog_drops_invented_commit_ids(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    write_page(repo)

    cl.build_changelog(repo, classifier=fake_classifier(), write=True, runner=build_runner())

    cached = cl.load_classified(repo / cl.REPORTS_DIR / "server-0.4.16.classified.json")
    assert cached is not None
    entry = next(e for e in cached.sections[0].entries if e.text == "新增状态控制接口")
    assert entry.sourceCommits == ["2222222"]  # deadbee was not in the range
    assert cached.unclassifiedCommits == []  # 9999999 was invented too


def test_build_changelog_skips_a_source_without_tags(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    write_page(repo)

    result = cl.build_changelog(repo, classifier=fake_classifier(), write=True, runner=FakeGit())

    assert any("tag 少于 2 个" in note for note in result.notes)
    assert result.docs == []


def test_build_changelog_reports_pending_without_classifier(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    page = write_page(repo)
    before = page.read_text(encoding="utf-8")

    result = cl.build_changelog(repo, write=True, runner=build_runner())

    assert result.pending == ["server 0.4.16"]
    assert result.docs == []
    assert page.read_text(encoding="utf-8") == before


def test_build_changelog_reuses_cache_and_reclassifies_when_stale(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    write_page(repo)
    fresh_calls = []

    cl.build_changelog(repo, classifier=fake_classifier(fresh_calls), write=True, runner=build_runner())
    assert len(fresh_calls) == 1

    cached_calls = []
    cl.build_changelog(repo, classifier=fake_classifier(cached_calls), write=True, runner=build_runner())
    assert cached_calls == []  # identity matches, so the cache is reused

    stale_calls = []
    stale = fake_classifier(stale_calls, model="claude-haiku-4-5")
    cl.build_changelog(repo, classifier=stale, write=True, runner=build_runner())
    assert len(stale_calls) == 1  # model changed, so the cache is stale


def test_build_changelog_keeps_every_cached_version_when_one_is_requested(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    write_page(repo)
    cl.build_changelog(repo, classifier=fake_classifier(), write=True, runner=build_runner())
    cl.write_json(
        repo / cl.REPORTS_DIR / "server-0.4.11.classified.json",
        doc(version="0.4.11", date="2023-03-08").model_dump(mode="json"),
    )

    calls = []
    result = cl.build_changelog(repo, versions=["0.4.16"], classifier=fake_classifier(calls), write=True, runner=build_runner())

    assert calls == []  # the requested version was already cached; nothing re-classified
    assert [item.version for item in result.docs] == ["0.4.16", "0.4.11"]
    assert "修复 0.4.11" in result.rendered[0].fragment


def test_build_changelog_sends_each_component_to_its_own_page(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    # engine uses its own tag shape, so the fake git log yields no engine ranges.
    write_sources(
        repo,
        source_repo,
        sources=[
            {"name": "server", "zh": "服务端", "en": "Server", "pages": {"zh": SERVER_PAGE}},
            {
                "name": "engine",
                "zh": "引擎",
                "en": "Engine",
                "pages": {"zh": ENGINE_PAGE},
                "tagPattern": r"^engine-v(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$",
            },
        ],
    )
    write_page(repo)
    write_page(repo, ENGINE_PAGE)
    cl.write_json(
        repo / cl.REPORTS_DIR / "engine-1.0.0.classified.json",
        doc(component="engine", label="引擎", version="1.0.0", date="2026-01-05").model_dump(mode="json"),
    )

    result = cl.build_changelog(repo, classifier=fake_classifier(), write=True, runner=build_runner())

    server_text = (repo / SERVER_PAGE).read_text(encoding="utf-8")
    engine_text = (repo / ENGINE_PAGE).read_text(encoding="utf-8")
    assert "0.4.16" in server_text and "1.0.0" not in server_text
    assert "1.0.0" in engine_text and "0.4.16" not in engine_text
    assert {item.page for item in result.rendered} == {Path(SERVER_PAGE), Path(ENGINE_PAGE)}


def test_build_changelog_notes_a_configured_page_that_does_not_exist_yet(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    cl.write_json(
        repo / cl.REPORTS_DIR / "server-0.4.16.classified.json",
        doc().model_dump(mode="json"),
    )

    result = cl.build_changelog(repo, runner=build_runner())

    assert result.rendered == []
    assert any("页面不存在" in note and SERVER_PAGE in note for note in result.notes)


def test_build_changelog_notes_a_suspicious_tag_interval(repo):
    source_repo = repo / "srcrepo"
    source_repo.mkdir()
    write_sources(repo, source_repo)
    write_page(repo)

    result = cl.build_changelog(
        repo, classifier=fake_classifier(), write=True, runner=build_runner(ancestor=False)
    )

    assert any("不是" in note and "祖先" in note for note in result.notes)
    assert result.docs == []


def test_sources_file_is_not_treated_as_feature_metadata(repo):
    from pawsql_doc.loaders import load_metadata

    write_sources(repo, repo / "srcrepo")
    _bundle, issues = load_metadata(repo)

    assert issues == []
