from __future__ import annotations

from pawsql_doc.loaders import check_references, load_metadata
from pawsql_doc.validate import parse_frontmatter, validate_metadata


def test_load_metadata_counts(repo):
    bundle, issues = load_metadata(repo)
    assert issues == []
    assert len(bundle.products) == 1
    assert len(bundle.features) == 1
    assert sum(len(v) for v in bundle.rules.values()) == 2
    assert bundle.rules["audit"][0].id == "AUD-ONE"
    assert len(bundle.databases) == 1
    assert len(bundle.configs) == 1


def test_bad_metadata_reports_file_and_field(repo):
    target = repo / "metadata" / "features" / "f1.yaml"
    target.write_text("id: F-OPT-1\nname: Feature One\ntype: rocket\nproduct: p\n", encoding="utf-8")
    bundle, issues = load_metadata(repo)
    assert any(i.file == "metadata/features/f1.yaml" and i.field == "type" for i in issues)
    # valid files still load
    assert bundle.products


def test_reference_checks_ok_when_consistent(repo):
    bundle, _ = load_metadata(repo)
    assert check_references(bundle) == []


def test_reference_checks_unknown_product(repo):
    product = repo / "metadata" / "products" / "optimizer.yaml"
    product.write_text("id: pawsql-something-else\nname: N\nkind: optimizer\n", encoding="utf-8")
    bundle, _ = load_metadata(repo)
    issues = check_references(bundle)
    assert any(i.field == "product" for i in issues)


def test_validate_metadata_smoke(repo):
    issues, counts = validate_metadata(repo)
    assert issues == []
    assert counts["features"] == 1


def test_parse_frontmatter_basic():
    text = "---\nid: x\ntitle: T\n---\nbody"
    data, err = parse_frontmatter(text)
    assert err is None
    assert data["title"] == "T"


def test_parse_frontmatter_missing_block_returns_none():
    data, err = parse_frontmatter("no front matter here")
    assert data is None and err is None
