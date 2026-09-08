"""Validate stable document/entity identity and registry relationships."""
from pathlib import Path
import yaml
from pawsql_doc.loaders import Issue
from pawsql_doc.validate import content_files, parse_frontmatter


def validate_registry(root: Path):
    issues, ids, pairs = [], {}, {}
    registry = {}
    canonical = (root / "metadata/documentation/model-version.yaml").is_file()
    for category in ("products", "components", "capabilities"):
        entries = {}
        for path in sorted((root / "metadata" / category).glob("*.yaml")):
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            key = data.get("id")
            if not key or key in entries:
                issues.append(Issue(file=str(path), reason=f"missing or duplicate {category} id: {key}"))
            entries[key] = data
        registry[category] = entries
    for path in content_files(root):
        data, err = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        if not data or err:
            continue
        rel = path.relative_to(root).as_posix()
        if canonical:
            from pawsql_doc.models.governance import SUBTYPES
            for field in ("layout", "language", "translationKey", "product"):
                if not data.get(field):
                    issues.append(Issue(file=rel, field=field, reason="canonical v2 field required"))
            if data.get("type") not in SUBTYPES:
                issues.append(Issue(file=rel, field="type", reason="canonical v2 type required"))
            elif SUBTYPES[data["type"]] and data.get("subtype") not in SUBTYPES[data["type"]]:
                issues.append(Issue(file=rel, field="subtype", reason="canonical v2 subtype required"))
            if data.get("product") != "pawsql":
                issues.append(Issue(file=rel, field="product", reason="single product must be pawsql"))
        key = data.get("id")
        if key in ids:
            issues.append(Issue(file=rel, field="id", reason=f"duplicate id also in {ids[key]}"))
        ids[key] = rel
        pair = (data.get("translationKey"), data.get("language"))
        if all(pair):
            if pair in pairs:
                issues.append(Issue(file=rel, field="translationKey", reason=f"duplicate translation language: {pair}"))
            pairs[pair] = rel
        expected_language = "en" if rel.startswith("docs/en/") else "zh"
        if data.get("language") not in {None, expected_language}:
            issues.append(Issue(file=rel, field="language", reason="language differs from content tree"))
        for category in ("components", "capabilities"):
            for target in data.get(category, []):
                if target not in registry[category]:
                    issues.append(Issue(file=rel, field=category, reason=f"unknown entity: {target}"))
        if data.get("product") and data["product"] not in registry["products"]:
            issues.append(Issue(file=rel, field="product", reason=f"unknown product: {data['product']}"))
    for path in content_files(root):
        data, _ = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        for relation in (data or {}).get("relations", []):
            if relation.get("documentId") not in ids:
                issues.append(Issue(file=str(path), field="relations", reason="unknown documentId"))
    for category, entries in registry.items():
        for identity, item in entries.items():
            if category == "components" and item.get("product") not in registry["products"]:
                issues.append(Issue(file=f"metadata/{category}/{identity}", reason="unknown component product"))
    from pawsql_doc.loaders import load_metadata
    bundle, _ = load_metadata(root)
    rule_ids = {r.id for values in bundle.rules.values() for r in values}
    feature_ids = {f.id for f in bundle.features}
    for kind, rules in bundle.rules.items():
        for rule in rules:
            if rule.kind is not None and rule.kind != kind:
                issues.append(Issue(file=f"rule:{rule.id}", field="kind", reason="kind differs from directory"))
            for target in rule.relatedRules:
                if target not in rule_ids:
                    # Legacy external rule IDs remain reported in completeness, not fabricated.
                    continue
            for field, targets, valid in (("components", rule.components, registry["components"]),
                                          ("capabilities", rule.capabilities, registry["capabilities"]),
                                          ("featureIds", rule.featureIds, feature_ids)):
                for target in targets:
                    if target not in valid:
                        issues.append(Issue(file=f"rule:{rule.id}", field=field, reason=f"unknown entity: {target}"))
    return issues
