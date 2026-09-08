"""Separate existence, completeness and publication readiness reports."""
from __future__ import annotations
import json
from pathlib import Path
from pawsql_doc.loaders import load_metadata
from pawsql_doc.gate import find_drift
from pawsql_doc.validate import content_files, parse_frontmatter, validate_frontmatter, validate_metadata, validate_nav
from pawsql_doc.registry import validate_registry
from pawsql_doc.models.governance import prose_digest

SECTIONS = {
    "explanation": ["definition", "purpose", "mechanism", "limitations", "nextSteps"],
    "guide": ["goal", "prerequisites", "steps", "expectedResult", "verification", "troubleshooting"],
    "use-case": ["audience", "problem", "goal", "workflow", "dependencies", "successCriteria"],
    "reference": ["identity", "facts", "applicability", "limitations", "examples", "evidence"],
    "support": ["symptom", "diagnosis", "resolution", "verification"],
    "article": ["topic", "body", "sources", "responsibility", "date"],
}


def quality_report(root: Path, publication=False):
    bundle, errors = load_metadata(root)
    metadata_errors, _ = validate_metadata(root)
    structure = metadata_errors + validate_frontmatter(root) + validate_registry(root)
    report = {"structure": [str(x) for x in structure], "existence": [], "completeness": [], "release": []}
    if not errors:
        report["existence"] = [str(x) for x in find_drift(root)]
    report["release"] = [str(x) for x in validate_nav(root, release=publication)]
    for path in content_files(root):
        text = path.read_text(encoding="utf-8-sig")
        data, error = parse_frontmatter(text)
        if error or not data:
            continue
        rel = path.relative_to(root).as_posix()
        if publication and data.get("status") not in {"approved", "published"}:
            continue  # required/nav draft pages are caught by their respective gates
        if data.get("layout") == "index":
            continue
        if not data.get("description"):
            report["completeness"].append(f"{rel}: missing description")
        if data.get("entityRef"):
            continue
        # Section references are optional in drafts and explicit for publication.
        sections = data.get("sections", {})
        expected = SECTIONS.get(data.get("type"), [])
        for section in expected:
            heading = sections.get(section)
            if not heading or not any(line.lstrip("#").strip() == heading for line in text.splitlines() if line.startswith("#")):
                report["completeness"].append(f"{rel}: missing section mapping/body heading: {section}")
        if data.get("status") in {"approved", "published"} and (not data.get("owners") or not data.get("lastReviewed")):
            report["release"].append(f"{rel}: approved content requires owners and lastReviewed")
    for kind, rules in bundle.rules.items():
        seen = set()
        for rule in rules:
            prefix = f"rule:{rule.id}"
            if rule.id in seen:
                report["structure"].append(f"{prefix}: duplicate rule id")
            seen.add(rule.id)
            if rule.applicability.status != "reviewed" or not rule.applicability.prerequisites:
                report["completeness"].append(f"{prefix}: applicability not reviewed/complete")
            if not rule.applicability.exclusions and not rule.applicability.noExclusionsReason:
                report["completeness"].append(f"{prefix}: exclusions or no-exclusion rationale required")
            evidence = {e.id: e for e in rule.evidence}
            covered = {field for e in rule.evidence if e.status == "verified" for field in e.supports}
            for field in ("id", "applicability"):
                if field not in covered:
                    report["release"].append(f"{prefix}: no verified evidence for {field}")
            for field in ("introducedVersion", "deprecatedVersion", "implementationClass", "database"):
                if getattr(rule, field) and field not in covered:
                    report["release"].append(f"{prefix}: unverified {field}")
            if rule.category.value == "unknown":
                report["release"].append(f"{prefix}: category pending")
            if not rule.examples:
                report["completeness"].append(f"{prefix}: structured examples missing")
            if kind == "optimizer" and not any(e.purpose == "boundary" for e in rule.examples):
                report["completeness"].append(f"{prefix}: boundary example missing")
            for example in rule.examples:
                if any(key not in evidence for key in example.evidenceIds):
                    report["structure"].append(f"{prefix}/{example.id}: unknown evidence reference")
                if example.verification != "passed" or not any(evidence.get(key) and evidence[key].status == "verified" for key in example.evidenceIds):
                    report["release"].append(f"{prefix}/{example.id}: execution verification pending")
            for lang in ("zh", "en"):
                content = getattr(rule.content, lang)
                if content is None:
                    if lang == "zh":
                        report["completeness"].append(f"{prefix}: default-language content missing")
                    continue
                if publication and lang == "en" and content.editorial.status not in {"approved", "published"}:
                    continue  # secondary translation may be withheld independently
                for field in ("name", "summary", "description", "howToFix"):
                    if not getattr(content, field):
                        report["completeness"].append(f"{prefix}/{lang}: missing {field}")
                if content.editorial.status not in {"approved", "published"}:
                    report["release"].append(f"{prefix}/{lang}: editorial {content.editorial.status}")
                if content.editorial.status in {"approved", "published"} and (not content.editorial.owners or not content.editorial.lastReviewed):
                    report["release"].append(f"{prefix}/{lang}: missing review ownership/date")
                if content.translation:
                    source = getattr(rule.content, content.translation.sourceLanguage)
                    if source is None or content.translation.sourceLanguage == lang or prose_digest(source) != content.translation.sourceDigest:
                        report["release"].append(f"{prefix}/{lang}: translation source missing, invalid or stale")
    for db in bundle.databases:
        if not db.compatibility:
            report["completeness"].append(f"database:{db.database}: compatibility records missing")
        evidence = {e.id: e for e in db.evidence}
        for row in db.compatibility:
            if row.status == "unknown" or not any(evidence.get(k) and evidence[k].status == "verified" for k in row.evidenceIds):
                report["release"].append(f"database:{db.database}/{row.capability}: support unverified")
    for cfg in bundle.configs:
        if not cfg.behavior.scope or cfg.behavior.activation == "unknown":
            report["completeness"].append(f"config:{cfg.id}: scope/activation not confirmed")
    for entity, identity in [(db, f"database:{db.database}") for db in bundle.databases] + [(cfg, f"config:{cfg.id}") for cfg in bundle.configs]:
        for lang in ("zh", "en"):
            content = getattr(entity.content, lang)
            if content is None:
                if lang == "zh":
                    report["completeness"].append(f"{identity}: default-language content missing")
                continue
            if publication and lang == "en" and content.editorial.status not in {"approved", "published"}:
                continue
            for field in ("name", "summary", "description"):
                if not getattr(content, field):
                    report["completeness"].append(f"{identity}/{lang}: missing {field}")
            if content.editorial.status not in {"approved", "published"}:
                report["release"].append(f"{identity}/{lang}: review pending")
            elif not content.editorial.owners or not content.editorial.lastReviewed:
                report["release"].append(f"{identity}/{lang}: missing review ownership/date")
            if content.translation:
                source = getattr(entity.content, content.translation.sourceLanguage)
                if source is None or content.translation.sourceLanguage == lang or prose_digest(source) != content.translation.sourceDigest:
                    report["release"].append(f"{identity}/{lang}: translation source missing, invalid or stale")
    rule_ids = {r.id for values in bundle.rules.values() for r in values}
    for rules in bundle.rules.values():
        for rule in rules:
            for related in rule.relatedRules:
                if related not in rule_ids:
                    report["completeness"].append(f"rule:{rule.id}: unresolved relatedRules {related}")
    for feature in bundle.features:
        for name in ("reference", "userGuide", "releaseNote", "blog"):
            req = getattr(feature.documentation, name)
            if req.required and not req.paths:
                report["completeness"].append(f"feature:{feature.id}: required {name} has no document reference")
    api = root / "docs/openapi/pawsql-openapi.yaml"
    if api.exists() and "placeholder" in api.read_text(encoding="utf-8").lower():
        report["release"].append("openapi: placeholder contract must be replaced or removed before publication")
    return {key: sorted(set(values)) for key, values in report.items()}


def write_report(root, report):
    out = root / "reports/content-quality.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return out
