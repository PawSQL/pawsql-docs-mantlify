"""Documentation Gate (design 20/23, tasks 006/014/015).

Detects drift between Metadata and required docs, computes coverage, and
enforces the release gate: required documentation coverage = 100%.

Scope note: the gate here guards docs-self-consistency inside this repository
(metadata -> generated reference / mapping-required doc). Product-PR-driven
policy enforcement (design 19) joins when the Change Analyzer (P1) lands in
the pawsql-doc-agent repository.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple

from pawsql_doc.generators.base import slug
from pawsql_doc.loaders import Issue, load_metadata
from pawsql_doc.models import (
    ConfigMetadata,
    DatabaseMetadata,
    DocRequirement,
    FeatureManifest,
    RuleMetadata,
)

DRIFT_CODE = "DOC-DRIFT"


def _exists(root: Path, path: str) -> bool:
    return (root / path).is_file()


# ---------------------------------------------------------------------------
# Expected reference pages (one per metadata record)
# ---------------------------------------------------------------------------


def rule_reference_path(rule: RuleMetadata, kind: str) -> str:
    # Default-language (zh) rule reference lives at the content root.
    # The /en mirror is validated separately via localeOf pairing.
    folder = "optimizer-rules" if kind == "optimizer" else "audit-rules"
    return f"docs/reference/{folder}/{slug(rule.id)}.md"


def database_reference_path(db: DatabaseMetadata) -> str:
    # Database guides are English-only until P0.6 adds a zh generator,
    # so they still live in the secondary /en tree.
    return f"docs/en/databases/{db.database}/index.md"


def config_reference_path(cfg: ConfigMetadata) -> str:
    # Configuration references are English-only until P0.6.
    return f"docs/en/reference/configuration/{slug(cfg.name)}.md"


# ---------------------------------------------------------------------------
# Missing-doc detection (drift)
# ---------------------------------------------------------------------------


def missing_reference_docs(root: Path, bundle) -> List[Issue]:
    issues: List[Issue] = []
    for kind, rules in sorted(bundle.rules.items()):
        for rule in sorted(rules, key=lambda r: r.id):
            rel = f"metadata/rules/{kind}/{rule.id}.yaml"
            path = rule_reference_path(rule, kind)
            if not _exists(root, path):
                issues.append(Issue(file=rel, field="reference-doc", reason=f"missing generated reference: {path}"))
    for db in sorted(bundle.databases, key=lambda d: d.database):
        rel = f"metadata/databases/{db.database}.yaml"
        if not _exists(root, database_reference_path(db)):
            issues.append(Issue(file=rel, field="reference-doc", reason=f"missing database guide: {database_reference_path(db)}"))
    for cfg in sorted(bundle.configs, key=lambda c: c.name):
        rel = f"metadata/configs/{slug(cfg.name)}.yaml"
        path = config_reference_path(cfg)
        if not _exists(root, path):
            issues.append(Issue(file=rel, field="reference-doc", reason=f"missing configuration reference: {path}"))
    return issues


def missing_required_mapping_docs(root: Path, bundle) -> List[Issue]:
    issues: List[Issue] = []
    for mapping in sorted(bundle.mappings, key=lambda m: m.feature):
        rel = f"metadata/mappings/{mapping.feature}.yaml"
        for doc in mapping.documents:
            if doc.required and not _exists(root, doc.path):
                issues.append(
                    Issue(file=rel, field="documents.path", reason=f"required document does not exist: {doc.path}")
                )
    return issues


def _required_paths(feature: FeatureManifest) -> List[Tuple[str, str]]:
    """(relation, path) for required documentation entries that declare a path."""
    out: List[Tuple[str, str]] = []
    for relation in ("reference", "userGuide", "releaseNote", "blog"):
        req: DocRequirement = getattr(feature.documentation, relation)
        if req.required:
            for path in req.paths:
                out.append((relation, path))
    return out


def missing_required_feature_docs(root: Path, bundle) -> List[Issue]:
    issues: List[Issue] = []
    for feature in sorted(bundle.features, key=lambda f: f.id):
        rel = f"metadata/features/{feature.id}.yaml"
        for relation, path in _required_paths(feature):
            if not _exists(root, path):
                issues.append(
                    Issue(file=rel, field=f"documentation.{relation}.paths", reason=f"required document does not exist: {path}")
                )
    return issues


def find_drift(root: Path, bundle=None) -> List[Issue]:
    """All metadata-to-doc gaps that block the release gate."""
    if bundle is None:
        bundle, _ = load_metadata(root)
    return sorted(
        missing_reference_docs(root, bundle)
        + missing_required_mapping_docs(root, bundle)
        + missing_required_feature_docs(root, bundle),
        key=lambda i: (i.file, i.field or "", i.reason),
    )


# ---------------------------------------------------------------------------
# Coverage (task 014)
# ---------------------------------------------------------------------------


@dataclass
class CoverageLine:
    category: str
    ok: int
    total: int

    @property
    def pct(self) -> float:
        return 100.0 * self.ok / self.total if self.total else 100.0


def _reference_ok(root: Path, bundle, kind: str) -> CoverageLine:
    rules = bundle.rules.get(kind, [])
    ok = sum(1 for r in rules if _exists(root, rule_reference_path(r, kind)))
    return CoverageLine(f"{kind}-rule-reference", ok, len(rules))


def _database_reference_ok(root: Path, bundle) -> CoverageLine:
    dbs = bundle.databases
    ok = sum(1 for db in dbs if _exists(root, database_reference_path(db)))
    return CoverageLine("database-reference", ok, len(dbs))


def _mapping_required_ok(root: Path, bundle) -> CoverageLine:
    required = [d for m in bundle.mappings for d in m.documents if d.required]
    ok = sum(1 for d in required if _exists(root, d.path))
    return CoverageLine("mapping-required-doc", ok, len(required))


def _feature_required_ok(root: Path, bundle) -> CoverageLine:
    entries = [(rel, p) for f in bundle.features for rel, p in _required_paths(f)]
    ok = sum(1 for _, p in entries if _exists(root, p))
    return CoverageLine("feature-required-doc", ok, len(entries))


def coverage_report(root: Path, bundle=None) -> List[CoverageLine]:
    if bundle is None:
        bundle, _ = load_metadata(root)
    lines = [
        _reference_ok(root, bundle, "audit"),
        _reference_ok(root, bundle, "optimizer"),
        _database_reference_ok(root, bundle),
        CoverageLine(
            "config-reference",
            sum(1 for c in bundle.configs if _exists(root, config_reference_path(c))),
            len(bundle.configs),
        ),
        _mapping_required_ok(root, bundle),
        _feature_required_ok(root, bundle),
    ]
    return lines


def run_release_gate(root: Path, bundle=None) -> Tuple[bool, List[CoverageLine], List[Issue]]:
    """Release gate (design 23): True when every category is fully covered."""
    lines = coverage_report(root, bundle)
    missing = find_drift(root, bundle)
    passed = all(line.ok == line.total for line in lines) and not missing
    return passed, lines, missing


def format_issues(missing: List[Issue]) -> List[str]:
    lines = []
    for idx, issue in enumerate(missing, start=1):
        loc = f"{issue.file}::{issue.field}" if issue.field else issue.file
        lines.append(f"{DRIFT_CODE}-{idx:03d} {loc}: {issue.reason}")
    return lines
