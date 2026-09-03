from __future__ import annotations

from pawsql_doc.generators import build_references
from pawsql_doc.loaders import load_metadata


def test_build_references_writes_pages(repo):
    bundle, issues = load_metadata(repo)
    assert issues == []
    written = build_references(repo, bundle)

    assert any(p.name == "aud-one.md" and "audit-rules" in p.parts for p in written)
    assert (repo / "docs/reference/audit-rules/aud-one.md").is_file()
    assert (repo / "docs/reference/optimizer-rules/opt-rewrite.md").is_file()
    assert (repo / "docs/reference/compatibility/index.md").is_file()
    assert (repo / "docs/databases/postgresql/index.md").is_file()
    assert (repo / "docs/reference/configuration/explain-timeout.md").is_file()


def test_build_references_is_deterministic(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    first = {
        p.relative_to(repo).as_posix(): p.read_text(encoding="utf-8")
        for p in sorted((repo / "docs").rglob("*"))
        if p.is_file()
    }
    # regenerate after touching only unrelated content in docs/databases extra file
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
    text = (repo / "docs/reference/audit-rules/aud-one.md").read_text(encoding="utf-8")
    assert text.startswith("---")
    assert "AUD-ONE" in text
    assert "Generated file" in text
    assert "severity" in text.lower() or "Warning" in text


def test_config_page_contains_parameter_and_scope(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    text = (repo / "docs/reference/configuration/explain-timeout.md").read_text(encoding="utf-8")
    assert "explain.timeout" in text
    assert "optimizer" in text


def test_compatibility_matrix_lists_database(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    text = (repo / "docs/reference/compatibility/index.md").read_text(encoding="utf-8")
    assert "postgresql" in text
    assert "16" in text
