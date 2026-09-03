"""Generate database guide and compatibility matrix from DatabaseMetadata (design 13, task 008)."""
from __future__ import annotations

from pathlib import Path
from typing import List

from pawsql_doc.generators.base import (
    fmt_bool,
    fmt_list,
    generated_note,
    render_page,
    write_page,
)
from pawsql_doc.models import DatabaseMetadata

KNOWN_FEATURES = ["optimizer", "audit", "planVisualizer", "advisor"]


def _feature_keys(databases: List[DatabaseMetadata]) -> List[str]:
    seen = {f for db in databases for f in db.features}
    ordered = [f for f in KNOWN_FEATURES if f in seen]
    ordered += sorted(seen - set(KNOWN_FEATURES))
    return ordered


def _display_name(db: DatabaseMetadata) -> str:
    return db.title or db.database


def generate_database_guide(root: Path, db: DatabaseMetadata) -> Path:
    out_path = root / "docs" / "databases" / db.database / "index.md"
    parts = [
        generated_note(f"databases/{db.database}.yaml"),
        "## Supported Versions\n",
    ]
    parts.append(f"| Database | Versions |\n|---|---|\n| {_display_name(db)} | {fmt_list(db.supportedVersions)} |\n")

    if db.features:
        rows = "".join(f"| {k} | {fmt_bool(db.features.get(k))} |\n" for k in _feature_keys([db]))
        parts.append("## Feature Support\n")
        parts.append(f"| Feature | Supported |\n|---|---|\n{rows}")

    if db.keyFeatures:
        bullets = "".join(f"- {f}\n" for f in db.keyFeatures)
        parts.append("## Key Features\n")
        parts.append(bullets)

    if db.description:
        parts.append("## Overview\n")
        parts.append(f"{db.description}\n")

    if db.notes:
        parts.append(f"> Note: {db.notes}\n")

    frontmatter = {
        "id": f"database-{db.database}",
        "title": f"{_display_name(db)} Support",
        "type": "reference",
        "status": "draft",
        "tags": ["database", db.database],
    }
    if db.description:
        frontmatter["description"] = db.description.splitlines()[0][:200]

    write_page(out_path, render_page(frontmatter, "\n".join(parts)))
    return out_path


def generate_compatibility_index(root: Path, databases: List[DatabaseMetadata]) -> Path:
    out_path = root / "docs" / "reference" / "compatibility" / "index.md"
    keys = _feature_keys(databases)

    header = "| Database | Versions | " + " | ".join(keys) + " |"
    sep = "|---|" + "---|" * (1 + len(keys))
    rows = []
    for db in sorted(databases, key=lambda d: d.database):
        cells = [fmt_list(db.supportedVersions)] + [fmt_bool(db.features.get(k)) for k in keys]
        rows.append("| " + _display_name(db) + " | " + " | ".join(cells) + " |")

    parts = [
        generated_note("databases/*.yaml"),
        "Version and capability support across the databases PawSQL can optimize and audit. "
        "Keep the authoritative data in `metadata/databases/`, not in this table.\n",
        header,
        sep,
        *rows,
        "",
    ]

    frontmatter = {
        "id": "database-compatibility-index",
        "title": "Database Compatibility Matrix",
        "type": "reference",
        "status": "draft",
        "tags": ["database", "compatibility"],
    }
    write_page(out_path, render_page(frontmatter, "\n".join(parts)))
    return out_path
