"""Changelog source configuration and change classification results.

The mechanical facts (version, tag, date, commit ids) come from git. The LLM only
supplies entry text and its category, so it cannot invent a version or a release date.
"""
from __future__ import annotations

from enum import Enum
from typing import Literal

from pydantic import Field, field_validator

from pawsql_doc.models.governance import Strict

class ChangeCategory(str, Enum):
    """Every tag any component may use, plus a cache-only bucket.

    A component's own vocabulary is a subset — see ``TAG_VOCABULARY``. Tags are not
    language-neutral slugs but the reader-facing labels themselves, because they are
    what Mintlify renders in the filter list.

    ``internal`` is never rendered and never tagged: it exists so a classifier has
    somewhere honest to put commits that are not user-facing, keeping them in the
    cache (and in ``*.commits.json``) without pretending they are a feature.
    """

    # engine
    AUDIT_ENGINE = "审核引擎"
    OPTIMIZER = "优化算法"
    INDEX_ENGINE = "索引引擎"
    SQL_PARSING = "SQL解析与数据库支持"
    # server
    REVIEW_OPTIMIZATION = "SQL 审核与优化"
    SLOW_QUERY_PATROL = "慢查询与巡检"
    WORKSPACE_SOURCES = "工作空间与数据源"
    INTEGRATION_API = "集成与开放接口"
    ACCESS_SECURITY = "权限与安全"
    # cross-cutting
    BUG_FIX = "缺陷修复"
    # cache-only
    INTERNAL = "internal"


# Engine subsystems vs. server platform areas: the two components' work does not
# overlap, so each page declares its own filter list. `缺陷修复` is cross-cutting in
# both: a fix that belongs to an area is grouped there and still tagged 缺陷修复.
TAG_VOCABULARY: dict[str, tuple[str, ...]] = {
    "engine": (
        ChangeCategory.AUDIT_ENGINE.value,
        ChangeCategory.OPTIMIZER.value,
        ChangeCategory.INDEX_ENGINE.value,
        ChangeCategory.SQL_PARSING.value,
        ChangeCategory.BUG_FIX.value,
    ),
    "server": (
        ChangeCategory.REVIEW_OPTIMIZATION.value,
        ChangeCategory.SLOW_QUERY_PATROL.value,
        ChangeCategory.WORKSPACE_SOURCES.value,
        ChangeCategory.INTEGRATION_API.value,
        ChangeCategory.ACCESS_SECURITY.value,
        ChangeCategory.BUG_FIX.value,
    ),
}

CHANGE_TAGS: tuple[str, ...] = tuple(
    dict.fromkeys(tag for tags in TAG_VOCABULARY.values() for tag in tags)
)

CATEGORY_ORDER: tuple[str, ...] = CHANGE_TAGS  # default order when a component is unknown

CATEGORY_LABELS: dict[str, dict[str, str]] = {
    "zh": {tag: tag for tag in CHANGE_TAGS},
    "en": {
        "审核引擎": "Audit engine",
        "优化算法": "Optimization algorithms",
        "索引引擎": "Index engine",
        "SQL解析与数据库支持": "SQL parsing & database support",
        "SQL 审核与优化": "SQL review & optimization",
        "慢查询与巡检": "Slow queries & inspection",
        "工作空间与数据源": "Workspaces & data sources",
        "集成与开放接口": "Integrations & API",
        "权限与安全": "Access & security",
        "缺陷修复": "Bug fixes",
    },
}


def category_order_for(component: str) -> tuple[str, ...]:
    """Render order of the tags used by one component's page."""
    return TAG_VOCABULARY.get(component, CATEGORY_ORDER)

DEFAULT_SKIP_PREFIXES: tuple[str, ...] = ("chore", "docs", "test", "ci", "build", "style")


class ChangelogSource(Strict):
    """One source repository feeding the changelog."""

    name: str = Field(description="Component key, e.g. server.")
    displayName: dict[Literal["zh", "en"], str]
    repo: str = Field(description="Repository path; may contain ${VAR} placeholders.")
    trunk: str = Field(default="main", description="Branch a release tag is expected on.")
    tagPattern: str = Field(description="Regex over tag names with a named group 'version'.")
    minVersion: str | None = Field(
        default=None,
        description=(
            "Ignore tags below this version. Needed where a repository carries legacy "
            "tags that would otherwise each render as a bogus release."
        ),
    )
    pages: dict[Literal["zh", "en"], str] = Field(
        description="Language -> repo-relative changelog page this component writes.",
    )
    pathInclude: list[str] = Field(default_factory=list)
    pathExclude: list[str] = Field(default_factory=list)
    skipPrefixes: list[str] = Field(default_factory=lambda: list(DEFAULT_SKIP_PREFIXES))
    skipMerge: bool = True

    @field_validator("tagPattern")
    @classmethod
    def has_version_group(cls, value: str) -> str:
        import re

        try:
            compiled = re.compile(value)
        except re.error as exc:
            raise ValueError(f"invalid tagPattern: {exc}") from exc
        if "version" not in compiled.groupindex:
            raise ValueError("tagPattern must declare a named group 'version'")
        return value

    @field_validator("pages")
    @classmethod
    def has_a_page(cls, value: dict) -> dict:
        if not value:
            raise ValueError("pages must configure at least one language")
        return value

    @field_validator("minVersion")
    @classmethod
    def looks_like_a_version(cls, value: str | None) -> str | None:
        import re

        if value is None:
            return value
        if not re.fullmatch(r"\d+\.\d+\.\d+", value):
            raise ValueError(f"minVersion must look like X.Y.Z, got {value!r}")
        return value


class ChangelogSources(Strict):
    sources: list[ChangelogSource] = Field(default_factory=list)


class ClassifiedEntry(Strict):
    text: str = Field(min_length=1, description="Entry text in the source commits' language.")
    textEn: str | None = Field(
        default=None,
        description="English mirror of ``text``; the en page falls back to ``text`` when absent.",
    )
    sourceCommits: list[str] = Field(default_factory=list)
    confidence: Literal["high", "medium", "low"] = "medium"
    tags: list[str] = Field(
        default_factory=list,
        description="Subsystem tags for this entry; may hold several, e.g. a fix in a subsystem.",
    )

    @field_validator("tags")
    @classmethod
    def tags_are_known(cls, value: list) -> list:
        unknown = [tag for tag in value if tag not in CHANGE_TAGS]
        if unknown:
            raise ValueError(f"unknown changelog tag(s) {unknown}; expected one of {list(CHANGE_TAGS)}")
        return value

    def text_for(self, lang: str) -> str:
        """The text this language's page shows."""
        if lang == "en":
            return self.textEn or self.text
        return self.text


class ClassifiedSection(Strict):
    category: ChangeCategory
    entries: list[ClassifiedEntry] = Field(default_factory=list)


class ClassifiedPayload(Strict):
    """What the classifier is allowed to decide."""

    sections: list[ClassifiedSection] = Field(default_factory=list)
    unclassifiedCommits: list[str] = Field(default_factory=list)


class ClassifiedDoc(Strict):
    """Mechanical facts from git plus the classified payload."""

    component: str
    componentLabel: dict[Literal["zh", "en"], str]
    version: str
    tag: str
    previousTag: str | None = None
    releaseDate: str
    model: str = ""
    promptVersion: str = ""
    sections: list[ClassifiedSection] = Field(default_factory=list)
    unclassifiedCommits: list[str] = Field(default_factory=list)

    @property
    def commit_count(self) -> int:
        return sum(len(section.entries) for section in self.sections)


class ReleaseBoundary(Strict):
    """One backfilled release: the commit a version ends at, plus its real ship date."""

    commit: str
    date: str = Field(description="Real ship date, ISO YYYY-MM-DD; becomes the tag date.")
    verified: bool = Field(
        default=False,
        description="Set once a human has checked this against the real delivery record.",
    )
    major: bool = Field(
        default=False,
        description="A major release: bumps minor and resets patch instead of bumping patch.",
    )
    note: str | None = None

    @field_validator("commit", mode="before")
    @classmethod
    def coerce_commit(cls, value):
        # An all-digit sha is parsed by YAML as a number; keep it a string.
        return str(value) if value is not None else value

    @field_validator("date", mode="before")
    @classmethod
    def coerce_date(cls, value):
        # Unquoted YAML dates arrive as date/datetime objects.
        import datetime

        if isinstance(value, datetime.datetime):
            return value.date().isoformat()
        if isinstance(value, datetime.date):
            return value.isoformat()
        return value

    @field_validator("commit")
    @classmethod
    def looks_like_a_sha(cls, value: str) -> str:
        import re

        if not re.fullmatch(r"[0-9a-f]{7,40}", value):
            raise ValueError(f"commit must be a 7-40 char hex sha, got {value!r}")
        return value

    @field_validator("date")
    @classmethod
    def looks_like_a_date(cls, value: str) -> str:
        import re

        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError(f"date must be ISO YYYY-MM-DD, got {value!r}")
        return value


class ReleaseBoundaries(Strict):
    """The backfill input: a start version plus the deliveries it numbers in order."""

    component: str
    tagFormat: str = Field(description="Tag name template, e.g. engine-v{version}.")
    start: str = Field(description="Version of the oldest delivery, e.g. 1.2.0.")
    deliveries: list[ReleaseBoundary] = Field(default_factory=list)

    @field_validator("tagFormat")
    @classmethod
    def has_version_slot(cls, value: str) -> str:
        if "{version}" not in value:
            raise ValueError("tagFormat must contain {version}")
        return value

    @field_validator("start")
    @classmethod
    def looks_like_a_version(cls, value: str) -> str:
        import re

        if not re.fullmatch(r"\d+\.\d+\.\d+", value):
            raise ValueError(f"start must look like X.Y.Z, got {value!r}")
        return value

    @field_validator("deliveries")
    @classmethod
    def is_not_empty(cls, value: list) -> list:
        if not value:
            raise ValueError("deliveries must not be empty")
        return value


__all__ = [
    "CATEGORY_LABELS",
    "CATEGORY_ORDER",
    "CHANGE_TAGS",
    "ChangeCategory",
    "ChangelogSource",
    "ChangelogSources",
    "ClassifiedDoc",
    "ClassifiedEntry",
    "ClassifiedPayload",
    "ClassifiedSection",
    "DEFAULT_SKIP_PREFIXES",
    "TAG_VOCABULARY",
    "category_order_for",
]
