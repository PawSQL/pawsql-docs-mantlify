"""Reference generators (Phase 2). Deterministic, LLM-free."""
from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from pawsql_doc.generators.config_generator import generate_config_reference
from pawsql_doc.generators.database_generator import (
    generate_compatibility_index,
    generate_database_guide,
)
from pawsql_doc.generators.rule_generator import generate_rule_reference
from pawsql_doc.generators.rule_index import build_rule_indexes
from pawsql_doc.loaders import MetadataBundle


def build_references(root: Path, bundle: MetadataBundle) -> List[Path]:
    """Regenerate every metadata-driven reference page. Deterministic."""
    written: List[Path] = []

    for kind, rules in sorted(bundle.rules.items()):
        for rule in sorted(rules, key=lambda r: r.id):
            written.extend(generate_rule_reference(root, kind, rule))

    for db in sorted(bundle.databases, key=lambda d: d.database):
        written.append(generate_database_guide(root, db))
    if bundle.databases:
        written.append(generate_compatibility_index(root, bundle.databases))

    for cfg in sorted(bundle.configs, key=lambda c: c.name):
        written.append(generate_config_reference(root, cfg))

    written.extend(build_rule_indexes(root))

    return written


def _find_rule(bundle: MetadataBundle, kind: str, rule_id: str) -> Optional[object]:
    for rule in bundle.rules.get(kind, []):
        if rule.id.lower() == rule_id.lower():
            return rule
    return None


def generate_single_rule(root: Path, bundle: MetadataBundle, rule_id: str) -> Optional[List[Path]]:
    for kind in ("audit", "optimizer"):
        rule = _find_rule(bundle, kind, rule_id)
        if rule is not None:
            return generate_rule_reference(root, kind, rule)
    return None


def generate_single_database(root: Path, bundle: MetadataBundle, name: str) -> Optional[Path]:
    for db in bundle.databases:
        if db.database.lower() == name.lower():
            return generate_database_guide(root, db)
    return None


def generate_single_config(root: Path, bundle: MetadataBundle, name: str) -> Optional[Path]:
    for cfg in bundle.configs:
        if cfg.name.lower() == name.lower():
            return generate_config_reference(root, cfg)
    return None
