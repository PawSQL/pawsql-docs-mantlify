"""Language-neutral governance and reference contracts (content model v2)."""
from __future__ import annotations

import hashlib
import json
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


SUBTYPES = {
    "explanation": {None},
    "guide": {"quickstart", "installation", "operation", "integration", "upgrade", "migration"},
    "use-case": {None},
    "reference": {"rule", "database", "configuration", "api", "cli", "error-code", "glossary"},
    "support": {"faq", "troubleshooting"},
    "article": {"blog", "release-note"},
}
LEGACY_TYPES = {
    "product": ("explanation", None), "user-guide": ("guide", "operation"),
    "tutorial": ("guide", "operation"), "faq": ("support", "faq"),
    "troubleshooting": ("support", "troubleshooting"),
    "release-note": ("article", "release-note"), "blog": ("article", "blog"),
}


class Editorial(Strict):
    status: Literal["draft", "review", "approved", "scheduled", "published", "archived"] = "draft"
    owners: list[str] = Field(default_factory=list)
    lastReviewed: str | None = None
    reviewCycle: int | None = Field(default=None, ge=1)


class Translation(Strict):
    sourceLanguage: Literal["zh", "en"]
    sourceDigest: str


class DocumentRef(Strict):
    documentId: str
    language: Literal["zh", "en"] | None = None


class LocalizedText(Strict):
    name: str | None = None
    summary: str | None = None
    description: str | None = None
    notes: str | None = None
    keyFeatures: list[str] = Field(default_factory=list)
    example: str | None = None
    editorial: Editorial = Field(default_factory=Editorial)
    translation: Translation | None = None


class TextBundle(Strict):
    zh: LocalizedText | None = None
    en: LocalizedText | None = None


class Source(Strict):
    repository: str | None = None
    path: str | None = None
    revision: str | None = None
    url: str | None = None


class Evidence(Strict):
    id: str
    source: Source
    supports: list[str] = Field(default_factory=list)
    status: Literal["pending", "verified", "rejected"] = "pending"
    verifiedBy: str | None = None
    verifiedAt: str | None = None

    @model_validator(mode="after")
    def verified_source(self):
        if self.status == "verified":
            if not self.supports or not self.verifiedBy or not self.verifiedAt:
                raise ValueError("verified evidence requires supports, verifiedBy and verifiedAt")
            if not (self.source.url or (self.source.path and self.source.revision)):
                raise ValueError("verified evidence requires URL or revision-pinned source path")
        return self


class Condition(Strict):
    code: str
    content: dict[Literal["zh", "en"], str] = Field(default_factory=dict)


class Applicability(Strict):
    status: Literal["pending", "reviewed"] = "pending"
    prerequisites: list[Condition] = Field(default_factory=list)
    exclusions: list[Condition] = Field(default_factory=list)
    noExclusionsReason: str | None = None


class Remediation(Strict):
    mode: Literal["advisory", "conditional-auto", "auto"] = "advisory"
    requiresPerformanceValidation: bool = True


class ExampleExpected(Strict):
    comparison: Literal["multiset-equal", "ordered-equal", "triggers", "does-not-trigger"]


class RuleExample(Strict):
    id: str
    dialect: str
    purpose: Literal["normal", "boundary"] = "normal"
    setupSql: str | None = None
    beforeSql: str
    afterSql: str | None = None
    expected: ExampleExpected
    verification: Literal["pending", "passed", "failed"] = "pending"
    evidenceIds: list[str] = Field(default_factory=list)
    content: dict[Literal["zh", "en"], str] = Field(default_factory=dict)


class Compatibility(Strict):
    databaseVersions: list[str]
    product: Literal["pawsql"] = "pawsql"
    component: str | None = None
    productVersionRange: str | None = None
    capability: str
    status: Literal["supported", "partial", "unsupported", "unknown"] = "unknown"
    limitations: list[Condition] = Field(default_factory=list)
    evidenceIds: list[str] = Field(default_factory=list)


class ConfigBehavior(Strict):
    scope: str | None = None
    activation: Literal["immediate", "next-request", "restart", "unknown"] = "unknown"
    restartRequired: bool | None = None
    precedence: list[str] = Field(default_factory=list)
    dependencies: list[str] = Field(default_factory=list)
    conflicts: list[str] = Field(default_factory=list)


def prose_digest(content) -> str:
    """Hash only translatable content, excluding review/translation bookkeeping."""
    data = content.model_dump(mode="json", exclude={"editorial", "translation"})
    return hashlib.sha256(json.dumps(data, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
