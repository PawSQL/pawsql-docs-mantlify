from collections import Counter
import json
import sqlite3

import pytest
import yaml
from pydantic import ValidationError

from pawsql_doc.models import FrontMatter, ConfigMetadata, RuleMetadata
from pawsql_doc.models.governance import Evidence, Editorial, prose_digest
from pawsql_doc.migration import classify, migrate
from pawsql_doc.generators import build_references
from pawsql_doc.loaders import load_metadata
from pawsql_doc.validate import validate_nav, parse_frontmatter
from pawsql_doc.build import build


def test_classification_legacy_conversion_idempotent():
    data = {"id": "installation", "title": "Install", "type": "user-guide", "product": "pawsql-advisor"}
    converted = classify(data, "en/user-guide/setup.mdx")
    assert converted["type"] == "guide" and converted["product"] == "pawsql"
    assert converted["components"] == ["advisor"]
    assert classify(converted, "en/user-guide/setup.mdx") == converted
    assert data["product"] == "pawsql-advisor"


def test_invalid_type_subtype():
    with pytest.raises(ValidationError):
        FrontMatter(id="x", title="x", type="guide", subtype="rule")


@pytest.mark.parametrize("kwargs", [
    {"configType": "integer", "default": "abc"},
    {"configType": "boolean", "default": 5},
    {"configType": "integer", "default": 4, "allowedRange": {"min": 8, "max": 2}},
    {"configType": "integer", "default": 8, "allowedRange": {"min": 1, "max": 3}},
    {"configType": "string", "default": "x", "enumValues": ["y"]},
])
def test_configuration_constraints(kwargs):
    with pytest.raises(ValidationError):
        ConfigMetadata(id="x", name="x", **kwargs)


def test_verified_evidence_requires_real_source():
    with pytest.raises(ValidationError):
        Evidence(id="x", source={}, status="verified")


def test_translation_hash_ignores_review_but_detects_prose():
    rule = RuleMetadata(id="x", content={"zh": {"name": "中文"}})
    before = prose_digest(rule.content.zh)
    rule.content.zh.editorial.status = "review"
    assert prose_digest(rule.content.zh) == before
    rule.content.zh.name = "新版中文"
    assert prose_digest(rule.content.zh) != before


def test_rule_generation_preserves_status_and_does_not_mix_languages(repo):
    bundle, _ = load_metadata(repo)
    rule = bundle.rules["audit"][0]
    rule.content.zh.description = "ONLY CHINESE"
    rule.content.en.description = None
    rule.content.en.editorial = Editorial(status="approved", owners=["team"], lastReviewed="2026-09-08")
    paths = build_references(repo, bundle)
    english = next(p for p in paths if "en" in p.parts and p.name == "aud-one.md")
    text = english.read_text(encoding="utf-8")
    assert "ONLY CHINESE" not in text
    assert "status: approved" in text
    assert "lastReviewed:" in text


def test_catalog_excludes_stale_files_and_handles_empty_collection(repo):
    bundle, _ = load_metadata(repo)
    build_references(repo, bundle)
    bundle.rules["audit"] = []
    build_references(repo, bundle)
    catalog = (repo / "docs/reference/audit-rules/index.md").read_text(encoding="utf-8")
    assert "aud-one" not in catalog
    assert "0 条规则" in catalog
    assert (repo / "docs/reference/audit-rules/aud-one.md").exists()  # no broad deletion


def test_build_manifest_protects_manually_edited_output(repo):
    build(repo)
    path = repo / "docs/reference/audit-rules/aud-one.md"
    path.write_text(path.read_text(encoding="utf-8") + "human edit", encoding="utf-8")
    with pytest.raises(ValueError, match="modified outside build"):
        build(repo)
    assert path.read_text(encoding="utf-8").endswith("human edit")


def test_release_rejection_does_not_create_output(repo, tmp_path):
    output = tmp_path / "release"
    with pytest.raises(ValueError, match="release not ready"):
        build(repo, "release", output)
    assert not output.exists()


def test_nav_checks_nested_mdx_and_missing_page(repo):
    p = repo / "docs/a.mdx"
    p.parent.mkdir(exist_ok=True)
    p.write_text("---\nid: a\ntitle: A\ntype: explanation\nstatus: draft\n---\n", encoding="utf-8")
    (repo / "docs/docs.json").write_text(json.dumps({"navigation": {"groups": [{"group": "Outer", "pages": [{"group": "Inner", "pages": ["a", "missing"]}]}]}}), encoding="utf-8")
    issues = validate_nav(repo, release=True)
    assert {i.field for i in issues if not i.field.startswith("sections.")} == {"a", "missing"}


def test_migration_preserves_body_and_is_repeatable(repo):
    p = repo / "docs/a.mdx"
    p.parent.mkdir(exist_ok=True)
    body = "\n\n# User content\n\nKeep **all** changes.\n"
    p.write_text("---\nid: a\ntitle: A\ntype: user-guide\n---" + body, encoding="utf-8")
    migrate(repo, True)
    assert p.read_text(encoding="utf-8").endswith(body)
    assert migrate(repo, False) == []


def test_or_rewrite_null_overlap_and_duplicates():
    # Semantic regression only: SQLite is not evidence of PawSQL/PostgreSQL support.
    db = sqlite3.connect(":memory:")
    db.executescript("CREATE TABLE demo(a integer,b integer); INSERT INTO demo VALUES(NULL,1),(1,1),(1,1),(2,1),(2,NULL);")
    original = Counter(db.execute("SELECT * FROM demo WHERE a=1 OR b=1"))
    rewritten = Counter(db.execute("SELECT * FROM demo WHERE a=1 UNION ALL SELECT * FROM demo WHERE b=1 AND (a<>1 OR a IS NULL)"))
    assert original == rewritten
    incorrect = Counter(db.execute("SELECT * FROM demo WHERE a=1 UNION ALL SELECT * FROM demo WHERE b=1 AND a<>1"))
    assert incorrect != original
    db.close()


def test_canonical_schema_accepts_migration_and_rejects_wrong_subtype(tmp_path):
    import jsonschema
    from pawsql_doc.export_schemas import export_schemas
    export_schemas(tmp_path)
    schema = json.loads((tmp_path / "schemas/frontmatter-v2.schema.json").read_text(encoding="utf-8"))
    data = classify({"id": "a", "title": "A", "type": "user-guide"}, "user-guide/a.mdx")
    jsonschema.validate(data, schema)
    FrontMatter.model_validate(data)
    data["subtype"] = "rule"
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, schema)
    with pytest.raises(ValidationError):
        FrontMatter.model_validate(data)


def test_stable_document_mapping_resolves_language(repo):
    page = repo / "docs/en/a.mdx"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text("---\nid: en-a\ntitle: A\ntype: explanation\nlanguage: en\n---\n", encoding="utf-8")
    mapping = repo / "metadata/mappings/stable.yaml"
    mapping.parent.mkdir(parents=True, exist_ok=True)
    mapping.write_text("feature: F-OPT-1\ndocuments:\n- documentId: en-a\n  language: en\n  relation: user-guide\n  required: true\n", encoding="utf-8")
    bundle, errors = load_metadata(repo)
    assert errors == []
    assert next(m for m in bundle.mappings if m.documents and m.documents[0].documentId).documents[0].path == "docs/en/a.mdx"


def test_missing_generated_rule_identity_resolves_from_metadata(repo):
    from pawsql_doc.generators.rule_generator import _page_id
    bundle, errors = load_metadata(repo)
    assert errors == []
    kind, rules = next((k, v) for k, v in bundle.rules.items() if v)
    rule = rules[0]
    lang = next(lang for lang in ("zh", "en") if getattr(rule.content, lang))
    mapping = repo / "metadata/mappings/generated.yaml"
    mapping.parent.mkdir(parents=True, exist_ok=True)
    mapping.write_text(yaml.safe_dump({"feature": "F-OPT-1", "documents": [{"documentId": _page_id(kind, rule, lang), "language": lang, "relation": "reference", "required": True}]}), encoding="utf-8")
    _, errors = load_metadata(repo)
    assert errors == []


def test_invalid_navigation_frontmatter_blocks_release(repo):
    (repo / "docs").mkdir(exist_ok=True)
    (repo / "docs/invalid.mdx").write_text("No frontmatter", encoding="utf-8")
    (repo / "docs/docs.json").write_text(json.dumps({"navigation": {"pages": ["invalid"]}}), encoding="utf-8")
    assert validate_nav(repo)[0].reason == "navigation target has invalid front matter"


def test_release_success_excludes_unlisted_draft(tmp_path):
    root = tmp_path / "source"
    (root / "docs").mkdir(parents=True)
    (root / "metadata/products").mkdir(parents=True)
    (root / "metadata/products/pawsql.yaml").write_text("id: pawsql\nname: PawSQL\n", encoding="utf-8")
    approved = {"id": "home", "title": "Home", "type": "explanation", "product": "pawsql", "status": "approved", "description": "Intro", "owners": ["team"], "lastReviewed": "2026-09-08", "sections": {k: "Content" for k in ("definition", "purpose", "mechanism", "limitations", "nextSteps")}}
    (root / "docs/index.mdx").write_text("---\n" + yaml.safe_dump(approved) + "---\n# Content\nReviewed content.\n", encoding="utf-8")
    (root / "docs/draft.mdx").write_text("---\nid: draft\ntitle: Draft\ntype: explanation\nstatus: draft\n---\nUnreviewed text\n", encoding="utf-8")
    (root / "docs/docs.json").write_text(json.dumps({"navigation": {"groups": [{"group": "Start", "pages": ["index"]}]}}), encoding="utf-8")
    output = tmp_path / "published"
    build(root, "release", output)
    assert (output / "index.mdx").exists()
    assert not (output / "draft.mdx").exists()
    assert (root / "docs/draft.mdx").exists()


def test_build_reports_removed_rule_without_deleting(repo):
    build(repo)
    source = next((repo / "metadata/rules/audit").glob("*.yaml"))
    source.unlink()
    _, stale = build(repo)
    assert any("aud-one.md" in p for p in stale)
    assert (repo / "docs/reference/audit-rules/aud-one.md").exists()
