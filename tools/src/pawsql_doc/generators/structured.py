"""Localized database/configuration references from neutral facts and own prose.

Database reference pages and the aggregate capability matrix are generated from
``metadata/databases/*.yaml`` (single source of truth). The aggregate matrix is
spliced between stable markers inside the otherwise-authored supported-databases
pages, so prose edits outside the markers are preserved.
"""
from pathlib import Path
from pawsql_doc.generators.base import (
    render_page, write_page, slug, code_block, splice_region,
    DB_MATRIX_START, DB_MATRIX_END,
)
from pawsql_doc.models.core import DB_CAPABILITY_SLUGS


_CAPABILITY_EN = {
    "sql-audit": "SQL Review",
    "sql-rewrite": "Query Rewrite",
    "index-recommendation": "Index Recommendation",
    "performance-validation": "Performance Validation",
    "plan-visualization": "Plan Visualization",
    "performance-inspection": "Performance Inspection",
}
_STATUS_EN = {
    "supported": "Supported",
    "partial": "Partial (database/version-limited)",
    "unsupported": "Unsupported",
}

# Matrix display order for the 16 registered databases.
_MATRIX_ORDER = [
    "mysql", "postgresql", "mariadb", "oracle", "sqlserver", "db2",
    "opengauss", "gaussdb", "kingbasees", "dameng", "mogdb",
    "oceanbase", "tdsql", "goldendb", "polardbx", "hive",
]
_MATRIX_HEADERS_ZH = ["SQL 规范审核", "查询重写", "索引推荐", "性能验证", "执行计划分析", "生产治理"]
_MATRIX_HEADERS_EN = ["SQL Review", "Query Rewrite", "Index Advisor", "Performance Validation", "Plan Analysis", "Production Governance"]
_DB_NAMES_ZH = {
    "mysql": "MySQL", "postgresql": "PostgreSQL", "mariadb": "MariaDB",
    "oracle": "Oracle", "sqlserver": "SQL Server", "db2": "IBM Db2",
    "opengauss": "openGauss", "gaussdb": "GaussDB", "kingbasees": "KingbaseES",
    "dameng": "达梦数据库", "mogdb": "MogDB", "oceanbase": "OceanBase",
    "tdsql": "TDSQL", "goldendb": "GoldenDB", "polardbx": "PolarDB-X",
    "hive": "Apache Hive",
}
_GLYPH = {"supported": "✓", "partial": "◐", "unsupported": "—"}


def _page(root, route, identity, lang, title, description, body, editorial=None):
    path = root / "docs" / ("en" if lang == "en" else "") / route
    fm = {"id": identity, "translationKey": identity.removeprefix("en-").removeprefix("zh-"), "language": lang,
          "title": title, "type": "reference", "status": editorial.status if editorial else "draft"}
    fm["entityRef"] = {"type": "database" if "databases/" in route else "configuration" if "configuration/" in route else "compatibility", "id": identity.removeprefix("zh-")}
    if editorial:
        fm["owners"] = editorial.owners
        if editorial.lastReviewed:
            fm["lastReviewed"] = editorial.lastReviewed
    if description:
        fm["description"] = description
    write_page(path, render_page(fm, body))
    return path


def _db_display(db, lang: str) -> str:
    if lang == "zh":
        return _DB_NAMES_ZH.get(db.database, db.title or db.database)
    return db.title or db.database


def database_pages(root, db):
    written = []
    for lang in ("zh", "en"):
        content = getattr(db.content, lang)
        if content is None and lang == "zh":
            continue
        zh = lang == "zh"
        name = (content.name if content else None) or _db_display(db, lang)
        body = [f"# {name}\n"]
        if db.supportedVersions:
            body.append(f"**Supported versions:** {', '.join(db.supportedVersions)}\n")
        if db.capabilities:
            body += ["| Capability | Status |", "|---|---|"]
            for capability in DB_CAPABILITY_SLUGS:
                status = db.capabilities.get(capability)
                if status is not None:
                    body.append(f"| {_CAPABILITY_EN[capability]} | {_STATUS_EN[status]} |")
        elif db.compatibility:
            body += ["| Database | Versions | Capability | Status |", "|---|---|---|---|"]
            for row in db.compatibility:
                body.append(f"| {db.database} | {', '.join(row.databaseVersions)} | {row.capability} | {row.status} |")
                for limitation in row.limitations:
                    body.append(f"\n- {limitation.content.get(lang, limitation.code)}\n")
        else:
            body.append(f"| {db.database} | {', '.join(db.supportedVersions)} | legacy claims | unknown |")
        own_description = content.description if content else db.description
        if own_description:
            body.append("\n" + own_description)
        for feature in (content.keyFeatures if content else db.keyFeatures):
            body.append(f"\n- {feature}")
        notes = content.notes if content else db.notes
        if notes:
            body.append("\n" + notes)
        body.append("\nStatus: supported / partial (database- or version-limited) / unsupported." if not zh
                    else "\n状态：supported 完整支持 / partial 存在限制 / unsupported 不支持。")
        identity = ("zh-" if zh else "") + f"database-{db.database}"
        written.append(_page(root, f"databases/{db.database}/index.md", identity, lang, name,
                            content.summary if content else None, "\n".join(body), content.editorial if content else None))
    return written


def database_matrix_fragment(bundle, lang: str) -> str:
    """Markdown region (table + legend) of the per-database capability matrix."""
    zh = lang == "zh"
    headers = _MATRIX_HEADERS_ZH if zh else _MATRIX_HEADERS_EN
    ordered = sorted(
        (db for db in bundle.databases if db.capabilities),
        key=lambda db: _MATRIX_ORDER.index(db.database) if db.database in _MATRIX_ORDER else len(_MATRIX_ORDER),
    )
    lines = ["| " + " | ".join(["数据库" if zh else "Database"] + headers) + " |",
             "| ---" + "|:---:" * len(headers) + "|"]
    for db in ordered:
        cells = [_GLYPH.get(db.capabilities.get(cap, ""), "—") for cap in DB_CAPABILITY_SLUGS]
        lines.append("| " + " | ".join([_db_display(db, lang)] + cells) + " |")
    lines += [
        "",
        "**" + ("图例" if zh else "Legend") + "**",
        "",
        "- **✓** " + ("完整支持" if zh else "Fully supported"),
        "- **◐** " + ("支持，但存在数据库或版本相关限制" if zh else "Supported with database- or version-specific limitations"),
        "- **—** " + ("不适用或当前暂不支持" if zh else "Not applicable or currently unavailable"),
    ]
    return "\n".join(lines)


def sync_database_matrix(root: Path, bundle):
    """Splice the aggregate matrix into both supported-databases pages."""
    written = []
    for lang, rel in (
        ("zh", "docs/getting-started/supported-databases.mdx"),
        ("en", "docs/en/getting-started/supported-databases.mdx"),
    ):
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        spliced = splice_region(text, database_matrix_fragment(bundle, lang))
        if spliced is None:
            raise ValueError(f"{rel}: missing {DB_MATRIX_START} / {DB_MATRIX_END} markers")
        if spliced != text:
            path.write_text(spliced, encoding="utf-8", newline="\n")
            written.append(path)
    return written


def config_pages(root, cfg):
    written = []
    for lang in ("zh", "en"):
        content = getattr(cfg.content, lang)
        if content is None and lang == "zh":
            continue
        rows = [("Parameter", cfg.name), ("Type", cfg.configType.value), ("Default", str(cfg.default)),
                ("Unit", cfg.unit or "unknown"), ("Scope", cfg.behavior.scope or cfg.scope),
                ("Activation", cfg.behavior.activation), ("Restart required", str(cfg.behavior.restartRequired)),
                ("Precedence", ", ".join(cfg.behavior.precedence) or "unknown")]
        if cfg.allowedRange:
            rows.append(("Range", f"{cfg.allowedRange.min} .. {cfg.allowedRange.max}"))
        body = ["| Field | Value |", "|---|---|", *[f"| {k} | {v} |" for k, v in rows]]
        description = content.description if content else cfg.description
        if description:
            body.append("\n" + description)
        example = content.example if content else cfg.example
        if example:
            body.append(code_block("text", example))
        identity = ("zh-" if lang == "zh" else "") + f"config-{slug(cfg.name)}"
        written.append(_page(root, f"reference/configuration/{slug(cfg.name)}.md", identity, lang,
                            content.name if content and content.name else cfg.name,
                            content.summary if content else None, "\n".join(body), content.editorial if content else None))
    return written
