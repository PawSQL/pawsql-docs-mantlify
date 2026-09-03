"""Content model for the PawSQL documentation platform.

Mirrors the metadata shapes defined in the Mintlify design document
(sections 7-9, 14, 19). Models are the single source of truth; JSON
Schemas in ../../schemas are exported from them (see export_schemas.py).
"""
from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


# ---------------------------------------------------------------------------
# Page front matter (design section 7)
# ---------------------------------------------------------------------------


class DocType(str, Enum):
    PRODUCT = "product"
    USER_GUIDE = "user-guide"
    TUTORIAL = "tutorial"
    REFERENCE = "reference"
    FAQ = "faq"
    TROUBLESHOOTING = "troubleshooting"
    RELEASE_NOTE = "release-note"
    BLOG = "blog"


class DocStatus(str, Enum):
    DRAFT = "draft"
    REVIEW = "review"
    APPROVED = "approved"
    SCHEDULED = "scheduled"
    PUBLISHED = "published"
    ARCHIVED = "archived"


class FrontMatter(BaseModel):
    """Document page front matter (design 7.1).

    Extra keys are allowed so Mintlify-specific page options and
    out-of-band annotations do not fail validation.
    """

    model_config = ConfigDict(extra="allow")

    id: str = Field(description="Stable unique id of the page (URL-safe slug).")
    title: str = Field(description="Page title.")
    description: Optional[str] = Field(
        default=None, description="One-line summary; also used for AI retrieval quality."
    )
    type: DocType = Field(description="Document type (design 7.2).")
    product: Optional[str] = Field(default=None, description="Product id this page belongs to.")
    versionIntroduced: Optional[str] = None
    status: DocStatus = DocStatus.DRAFT
    tags: List[str] = Field(default_factory=list)
    owners: Optional[List[str]] = None
    lastReviewed: Optional[date] = None
    reviewCycle: Optional[int] = Field(
        default=None, ge=1, description="Review interval in days."
    )
    relatedFeatures: Optional[List[str]] = Field(
        default=None, description="Feature ids (Feature Manifest) this page documents."
    )


# ---------------------------------------------------------------------------
# Feature Manifest (design 8.1)
# ---------------------------------------------------------------------------


class FeatureStatus(str, Enum):
    PLANNED = "planned"
    BETA = "beta"
    RELEASED = "released"
    DEPRECATED = "deprecated"


class ProductKind(str, Enum):
    OPTIMIZER = "optimizer"
    CLOUD = "cloud"
    ADVISOR = "advisor"
    PATROLLER = "patroller"
    PLAN_VISUALIZER = "plan-visualizer"
    VSCODE = "vscode"
    JETBRAINS = "jetbrains"
    MCP = "mcp"
    COMMUNITY = "community"
    ENTERPRISE = "enterprise"


class DocRequirement(_StrictModel):
    required: bool = False
    paths: List[str] = Field(default_factory=list)


class DocumentationRequirements(_StrictModel):
    reference: DocRequirement = Field(default_factory=DocRequirement)
    userGuide: DocRequirement = Field(default_factory=DocRequirement)
    releaseNote: DocRequirement = Field(default_factory=DocRequirement)
    blog: DocRequirement = Field(default_factory=DocRequirement)


class FeatureManifest(_StrictModel):
    """One product feature and the docs it requires (design 8.1)."""

    id: str = Field(description="Stable feature id, e.g. OPT-OR-UNION.")
    name: str
    type: ProductKind
    product: str = Field(description="Product id the feature ships in, e.g. pawsql-optimizer.")
    status: FeatureStatus = FeatureStatus.RELEASED
    introducedVersion: Optional[str] = None
    databases: List[str] = Field(default_factory=list)
    sourcePaths: List[str] = Field(default_factory=list)
    documentation: DocumentationRequirements = Field(default_factory=DocumentationRequirements)


# ---------------------------------------------------------------------------
# Rule Metadata (design 8.2)
# ---------------------------------------------------------------------------


class Severity(str, Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


class RuleMetadata(_StrictModel):
    """One audit or optimizer rule (design 8.2). Used to generate rule reference pages."""

    id: str
    name: str
    category: str = Field(description="Rule category, e.g. index / select / join / ddl.")
    severity: Severity = Severity.WARNING
    database: List[str] = Field(default_factory=list)
    introducedVersion: Optional[str] = None
    deprecatedVersion: Optional[str] = None
    implementationClass: Optional[str] = None
    description: Optional[str] = None
    badExample: Optional[str] = None
    goodExample: Optional[str] = None
    whyItMatters: Optional[str] = None
    howToFix: Optional[str] = None
    relatedRules: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Database Metadata (design 8.3)
# ---------------------------------------------------------------------------


class DatabaseMetadata(_StrictModel):
    """Supported database versions and capability matrix (design 8.3)."""

    database: str = Field(description="Database slug, e.g. postgresql.")
    title: Optional[str] = Field(default=None, description="Display name, e.g. PostgreSQL.")
    supportedVersions: List[str] = Field(default_factory=list)
    features: Dict[str, bool] = Field(
        default_factory=dict,
        description="Capability flags, e.g. {optimizer: true, audit: true, planVisualizer: false}.",
    )
    description: Optional[str] = None
    keyFeatures: List[str] = Field(default_factory=list)
    notes: Optional[str] = None


# ---------------------------------------------------------------------------
# Configuration Metadata (design 14)
# ---------------------------------------------------------------------------


class ConfigType(str, Enum):
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    STRING = "string"


class AllowedRange(_StrictModel):
    min: Optional[float] = None
    max: Optional[float] = None


class ConfigMetadata(_StrictModel):
    """One configuration item (design 14). Used to generate configuration reference pages."""

    id: str
    name: str = Field(description="Full config name, e.g. explain.timeout.")
    configType: ConfigType = Field(default=ConfigType.STRING)
    default: Optional[Union[int, float, bool, str]] = None
    unit: Optional[str] = None
    scope: str = Field(default="optimizer", description="Scope, e.g. optimizer / cloud.")
    versionIntroduced: Optional[str] = None
    versionDeprecated: Optional[str] = None
    allowedRange: Optional[AllowedRange] = None
    description: Optional[str] = None
    example: Optional[str] = None


class ProductMetadata(_StrictModel):
    """Product registry entry under metadata/products (referenced by FeatureManifest.product)."""

    id: str = Field(description="Product id, e.g. pawsql-optimizer. Referenced by feature manifests.")
    name: str
    kind: ProductKind
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Documentation Mapping (design 9) and Policy (design 19)
# ---------------------------------------------------------------------------


class RelationKind(str, Enum):
    REFERENCE = "reference"
    USER_GUIDE = "user-guide"
    RELEASE_NOTE = "release-note"
    BLOG = "blog"
    DATABASE_GUIDE = "database-guide"
    COMPATIBILITY = "compatibility"
    TUTORIAL = "tutorial"
    MIGRATION_GUIDE = "migration-guide"


class MappingDocument(_StrictModel):
    path: str
    relation: RelationKind
    required: bool = False


class DocumentationMapping(_StrictModel):
    """Maps a feature / rule / capability to the docs that must cover it (design 9).

    The Gate (Phase 3) will consume these; in Phase 0-2 the file is only data.
    """

    feature: str
    documents: List[MappingDocument] = Field(default_factory=list)


class RequirementLevel(str, Enum):
    REQUIRED = "required"
    CONDITIONAL = "conditional"
    RECOMMENDED = "recommended"
    OPTIONAL = "optional"


class DocumentationPolicy(_StrictModel):
    """Per-change-kind documentation requirements (design 19). Consumed by the Gate in Phase 3."""

    policies: Dict[str, Dict[str, RequirementLevel]] = Field(default_factory=dict)
