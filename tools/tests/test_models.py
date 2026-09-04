from __future__ import annotations

import pytest
from pydantic import ValidationError

from pawsql_doc.models import (
    ConfigMetadata,
    DatabaseMetadata,
    DocType,
    FeatureManifest,
    FrontMatter,
    RuleMetadata,
)


class TestFeatureManifest:
    def test_minimal_valid(self):
        f = FeatureManifest(id="OPT-OR-UNION", name="Or to Union", type="optimizer", product="pawsql-optimizer")
        assert f.id == "OPT-OR-UNION"
        assert f.status.value == "released"
        assert f.documentation.releaseNote.required is False

    def test_bad_status_rejected(self):
        with pytest.raises(ValidationError):
            FeatureManifest(id="X", name="x", type="optimizer", product="p", status="not-a-status")

    def test_unknown_key_rejected(self):
        with pytest.raises(ValidationError):
            FeatureManifest(id="X", name="x", type="optimizer", product="p", bogus=1)


class TestRuleMetadata:
    def test_minimal_valid(self):
        r = RuleMetadata(id="AUD-SELECT-STAR", name="SELECT *", category="dml")
        assert r.severity.value == "warning"
        assert r.database == []
        # legacy root prose is migrated into content.en on read
        assert r.content.en.name == "SELECT *"

    def test_bad_severity_rejected(self):
        with pytest.raises(ValidationError):
            RuleMetadata(id="X", name="x", category="dml", severity="loud")

    def test_legacy_zh_mirror_parsed(self):
        r = RuleMetadata(
            id="AUD-ZH", name="Rule", category="dml",
            zh={"name": "规则", "description": "中文说明"},
        )
        assert r.content.zh.name == "规则"
        assert r.content.zh.description == "中文说明"
        assert r.content.zh.whyItMatters is None
        assert r.content.en.name == "Rule"

    def test_bad_category_rejected(self):
        with pytest.raises(ValidationError):
            RuleMetadata(id="X", name="x", category="select")

    def test_zh_unknown_key_rejected(self):
        with pytest.raises(ValidationError):
            RuleMetadata(id="X", name="x", category="dml", zh={"name": "n", "bogus": 1})

    def test_canonical_content_shape(self):
        r = RuleMetadata(
            id="AUD-NEW",
            category="index",
            content={
                "en": {"name": "New Rule", "summary": "Short line.", "description": "Long text."},
                "zh": {"name": "新规则", "description": "中文正文。"},
            },
        )
        assert r.content.en.summary == "Short line."
        assert r.content.zh.name == "新规则"
        assert r.category.value == "index"


class TestDatabaseMetadata:
    def test_valid(self):
        d = DatabaseMetadata(database="postgresql", supportedVersions=["16"], features={"optimizer": True})
        assert d.features["optimizer"] is True

    def test_version_must_be_string(self):
        with pytest.raises(ValidationError):
            DatabaseMetadata(database="postgresql", supportedVersions=[14])


class TestConfigMetadata:
    def test_valid(self):
        c = ConfigMetadata(id="C", name="explain.timeout", configType="integer", default=30)
        assert c.scope == "optimizer"

    def test_bad_type_rejected(self):
        with pytest.raises(ValidationError):
            ConfigMetadata(id="C", name="x", configType="interval")


class TestFrontMatter:
    def test_required_fields(self):
        f = FrontMatter(id="p1", title="Page", type=DocType.PRODUCT, status="draft")
        assert f.type == DocType.PRODUCT

    def test_missing_title_rejected(self):
        with pytest.raises(ValidationError):
            FrontMatter(id="p1", type=DocType.PRODUCT)

    def test_mintlify_extra_keys_allowed(self):
        f = FrontMatter(
            id="p1", title="Page", type="reference", status="draft",
            sidebarTitle="Short", ogImage="/img.png",
        )
        assert f.model_extra == {"sidebarTitle": "Short", "ogImage": "/img.png"}
        assert f.title == "Page"
