from __future__ import annotations

from pawsql_doc.generators import build_references
from pawsql_doc.loaders import load_metadata


def test_build_references_writes_pages(repo):
    bundle, issues = load_metadata(repo)
    assert issues == []
    written = build_references(repo, bundle)

    assert any(p.name == "aud-one.md" and "audit-rules" in p.parts for p in written)
    assert (repo / "docs/en/reference/audit-rules/aud-one.md").is_file()
    assert (repo / "docs/en/reference/optimizer-rules/opt-rewrite.md").is_file()
    assert not (repo / "docs/en/reference/compatibility/index.md").exists()
    assert (repo / "docs/en/reference/database/postgresql/index.md").is_file()
    assert (repo / "docs/en/reference/configuration/explain-timeout.md").is_file()


def test_build_references_is_deterministic(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    first = {
        p.relative_to(repo).as_posix(): p.read_text(encoding="utf-8")
        for p in sorted((repo / "docs").rglob("*"))
        if p.is_file()
    }
    build_references(repo, bundle)
    second = {
        p.relative_to(repo).as_posix(): p.read_text(encoding="utf-8")
        for p in sorted((repo / "docs").rglob("*"))
        if p.is_file()
    }
    assert first == second


def test_rule_page_contains_sections(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    text = (repo / "docs/en/reference/audit-rules/aud-one.md").read_text(encoding="utf-8")
    assert text.startswith("---")
    assert "AUD-ONE" in text
    assert "Generated file" in text
    assert "severity" in text.lower() or "Warning" in text


def test_config_page_contains_parameter_and_scope(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    text = (repo / "docs/en/reference/configuration/explain-timeout.md").read_text(encoding="utf-8")
    assert "explain.timeout" in text
    assert "optimizer" in text


def test_database_page_lists_database(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    text = (repo / "docs/en/reference/database/postgresql/index.md").read_text(encoding="utf-8")
    assert "postgresql" in text
    assert "16" in text
    assert "SQL Review" in text
    assert "Performance Inspection" in text


def test_splice_region_edits_only_between_markers():
    from pawsql_doc.generators.base import DB_MATRIX_START, DB_MATRIX_END, splice_region

    text = f"head\n{DB_MATRIX_START}\nold\n{DB_MATRIX_END}\ntail\n"
    out = splice_region(text, "NEW")
    assert out is not None
    assert "NEW" in out and "old" not in out
    assert out.startswith("head\n") and out.endswith("\ntail\n")


def test_sync_database_matrix_injects_and_is_idempotent(repo):
    from pawsql_doc.generators.base import DB_MATRIX_START, DB_MATRIX_END
    from pawsql_doc.generators.structured import sync_database_matrix

    rels = ("docs/getting-started/supported-databases.mdx", "docs/en/getting-started/supported-databases.mdx")
    for rel in rels:
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# x\n\n{DB_MATRIX_START}\nplaceholder\n{DB_MATRIX_END}\n", encoding="utf-8")
    bundle, _ = load_metadata(repo)
    sync_database_matrix(repo, bundle)
    first = {rel: (repo / rel).read_text(encoding="utf-8") for rel in rels}
    assert all("postgresql" in text.lower() and "placeholder" not in text for text in first.values())
    sync_database_matrix(repo, bundle)
    assert first == {rel: (repo / rel).read_text(encoding="utf-8") for rel in rels}


def test_sync_database_matrix_raises_without_markers(repo):
    import pytest
    from pawsql_doc.generators.structured import sync_database_matrix

    path = repo / "docs/getting-started/supported-databases.mdx"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# x\nno markers here\n", encoding="utf-8")
    bundle, _ = load_metadata(repo)
    with pytest.raises(ValueError):
        sync_database_matrix(repo, bundle)


def test_bilingual_rule_writes_dual_pages(repo):
    import yaml

    (repo / "metadata/rules/audit/aud-biling.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "AUD-BILING",
                "name": "Audit Bilingual",
                "category": "dml",
                "severity": "info",
                "database": ["mysql"],
                "description": "English description.",
                "zh": {
                    "name": "双语规则",
                    "description": "中文说明。",
                    "badExample": "-- 反例\nSELECT * FROM t;",
                    "goodExample": "SELECT id FROM t;",
                },
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    bundle, issues = load_metadata(repo)
    assert issues == []
    written = build_references(repo, bundle)

    # zh-default site: Chinese page at content root, English in /en secondary tree
    en = repo / "docs/en/reference/audit-rules/aud-biling.md"
    zh = repo / "docs/reference/audit-rules/aud-biling.md"
    assert en.is_file()
    assert zh.is_file()
    assert zh in written and en in written

    en_text = en.read_text(encoding="utf-8")
    assert "English description" in en_text
    assert "双语规则" not in en_text
    # mirror page id uses the en- prefix; zh default page id is neutral
    assert "id: en-audit-rule-aud-biling" in en_text
    assert "localeOf: audit-rule-aud-biling" in en_text

    zh_text = zh.read_text(encoding="utf-8")
    assert "id: audit-rule-aud-biling" in zh_text
    assert "双语规则" in zh_text
    assert "中文说明" in zh_text
    assert "反例" in zh_text
    assert "正例" in zh_text
    assert "localeOf: en-audit-rule-aud-biling" in zh_text


def test_english_only_rule_writes_no_zh_page(repo):
    import yaml

    (repo / "metadata/rules/audit/aud-enonly.yaml").write_text(
        yaml.safe_dump(
            {
                "id": "AUD-ENONLY",
                "category": "dml",
                "content": {"en": {"name": "En Only", "description": "No Chinese yet."}},
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    bundle, issues = load_metadata(repo)
    assert issues == []
    written = build_references(repo, bundle)
    # EN-only rule has no Chinese page at the zh-default content root
    assert (repo / "docs/en/reference/audit-rules/aud-enonly.md").is_file()
    assert not (repo / "docs/reference/audit-rules/aud-enonly.md").exists()
    # without a zh page the default-language mirror pair is not claimed
    en_text = (repo / "docs/en/reference/audit-rules/aud-enonly.md").read_text(encoding="utf-8")
    assert "localeOf" not in en_text


def test_build_references_writes_rule_indexes(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)

    zh_audit = repo / "docs/reference/audit-rules/index.md"
    en_audit = repo / "docs/en/reference/audit-rules/index.md"
    zh_opt = repo / "docs/reference/optimizer-rules/index.md"
    assert zh_audit.is_file() and en_audit.is_file() and zh_opt.is_file()

    text = zh_audit.read_text(encoding="utf-8")
    assert "审核规范" in text
    assert "aud-one" in text  # lists the fixture audit rule
    assert "localeOf: en-audit-rules-index" in text

    en_text = en_audit.read_text(encoding="utf-8")
    assert "Audit Rule Reference" in en_text
    assert "localeOf: audit-rules-index" in en_text

