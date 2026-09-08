"""Load and validate the YAML metadata tree under <root>/metadata.

Valid entries and per-file issues are returned together so the CLI can
report every problem instead of stopping at the first one.
"""
from __future__ import annotations

import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Type, Tuple

import yaml
from pydantic import BaseModel, ValidationError

from pawsql_doc.models import (
    ConfigMetadata,
    DatabaseMetadata,
    DocumentationMapping,
    DocumentationPolicy,
    FeatureManifest,
    ProductMetadata,
    RuleMetadata,
)


@dataclass
class Issue:
    file: str
    field: Optional[str] = None
    reason: str = ""


def _rel(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def read_yaml(path: Path) -> Tuple[Optional[Any], Optional[str]]:
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        return None, f"cannot read: {exc}"
    try:
        return yaml.safe_load(text), None
    except yaml.YAMLError as exc:
        return None, f"invalid YAML: {exc}"


def _validation_issues(root: Path, path: Path, exc: ValidationError) -> List[Issue]:
    issues = []
    for err in exc.errors():
        loc = ".".join(str(p) for p in err.get("loc", ()))
        issues.append(Issue(file=_rel(root, path), field=loc or None, reason=err.get("msg", "")))
    return issues


def _load_dir(
    root: Path,
    rel_dir: str,
    model: Type[BaseModel],
) -> Tuple[List[BaseModel], List[Issue]]:
    """Load every *.yaml under metadata/<rel_dir> into `model`, collecting issues."""
    base = root / "metadata" / rel_dir
    values: List[BaseModel] = []
    issues: List[Issue] = []
    if not base.is_dir():
        return values, issues
    for path in sorted(base.glob("**/*.yaml")):
        data, yaml_err = read_yaml(path)
        if yaml_err is not None:
            issues.append(Issue(file=_rel(root, path), reason=yaml_err))
            continue
        if not isinstance(data, dict):
            issues.append(Issue(file=_rel(root, path), reason="top-level YAML must be a mapping"))
            continue
        try:
            values.append(model.model_validate(data))
        except ValidationError as exc:
            issues.extend(_validation_issues(root, path, exc))
    return values, issues


@dataclass
class MetadataBundle:
    products: List[ProductMetadata] = field(default_factory=list)
    features: List[FeatureManifest] = field(default_factory=list)
    rules: Dict[str, List[RuleMetadata]] = field(default_factory=dict)
    databases: List[DatabaseMetadata] = field(default_factory=list)
    configs: List[ConfigMetadata] = field(default_factory=list)
    mappings: List[DocumentationMapping] = field(default_factory=list)
    policies: List[DocumentationPolicy] = field(default_factory=list)


def load_metadata(root: Path) -> Tuple[MetadataBundle, List[Issue]]:
    """Load all metadata. Second element holds every schema/parse issue found."""
    bundle = MetadataBundle()
    issues: List[Issue] = []

    products, errs = _load_dir(root, "products", ProductMetadata)
    bundle.products = products
    issues.extend(errs)

    features, errs = _load_dir(root, "features", FeatureManifest)
    bundle.features = features
    issues.extend(errs)

    rules_root = root / "metadata" / "rules"
    if rules_root.is_dir():
        for kind_dir in sorted(rules_root.iterdir()):
            if not kind_dir.is_dir():
                continue
            rules, errs = _load_dir(root, f"rules/{kind_dir.name}", RuleMetadata)
            bundle.rules[kind_dir.name] = rules
            issues.extend(errs)

    databases, errs = _load_dir(root, "databases", DatabaseMetadata)
    bundle.databases = databases
    issues.extend(errs)

    configs, errs = _load_dir(root, "configs", ConfigMetadata)
    bundle.configs = configs
    issues.extend(errs)

    mappings, errs = _load_dir(root, "mappings", DocumentationMapping)
    bundle.mappings = mappings
    issues.extend(errs)

    policies, errs = _load_dir(root, "policies", DocumentationPolicy)
    bundle.policies = policies
    issues.extend(errs)

    # Resolve stable document identity for legacy path-based gate consumers.
    from pawsql_doc.validate import content_files, parse_frontmatter
    docs_by_id = {}
    for path in content_files(root):
        data, error = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        if data and not error:
            docs_by_id.setdefault(data.get("id"), []).append((path, data.get("language")))
    def resolve(document_id, language):
        candidates = [(p, lang) for p, lang in docs_by_id.get(document_id, []) if language is None or language == lang]
        # Missing generated files must remain rebuildable; their identity comes
        # from active metadata, not from the existence of a previous artifact.
        if not candidates:
            from pawsql_doc.generators.rule_generator import _page_id, _rule_folder
            from pawsql_doc.generators.base import slug
            for kind, rules in bundle.rules.items():
                for rule in rules:
                    for lang in ("zh", "en"):
                        if getattr(rule.content, lang) is not None and language in (None, lang) and _page_id(kind, rule, lang) == document_id:
                            candidates.append((root / "docs" / ("en" if lang == "en" else "") / "reference" / _rule_folder(kind) / f"{slug(rule.id)}.md", lang))
        if len(candidates) != 1:
            issues.append(Issue(file="metadata/mappings", field="documentId", reason=f"unresolved or ambiguous document: {document_id}/{language}"))
            return ""
        return candidates[0][0].relative_to(root).as_posix()
    for mapping in bundle.mappings:
        for doc in mapping.documents:
            if doc.documentId:
                resolved = resolve(doc.documentId, doc.language)
                if doc.path and doc.path != resolved:
                    issues.append(Issue(file="metadata/mappings", field="path", reason="path conflicts with documentId"))
                doc.path = resolved
    for feature in bundle.features:
        for requirement in (feature.documentation.reference, feature.documentation.userGuide, feature.documentation.releaseNote, feature.documentation.blog):
            for ref in requirement.documents:
                resolved = resolve(ref.documentId, ref.language)
                if resolved and resolved not in requirement.paths:
                    requirement.paths.append(resolved)
    return bundle, issues


def check_references(bundle: MetadataBundle) -> List[Issue]:
    """Cross-file reference checks that are order-independent (metadata-to-metadata only).

    File-path existence (mapping -> generated doc) is a Phase 3 drift/gate concern
    and is intentionally not enforced here.
    """
    issues: List[Issue] = []
    feature_ids = {f.id for f in bundle.features}
    product_ids = {p.id for p in bundle.products}

    for mapping in bundle.mappings:
        rel = f"metadata/mappings/{mapping.feature}.yaml"
        if mapping.feature not in feature_ids:
            issues.append(
                Issue(file=rel, field="feature", reason=f"feature '{mapping.feature}' not found in metadata/features")
            )

    for feature in bundle.features:
        if feature.product and feature.product not in product_ids:
            rel = f"metadata/features/{feature.id}.yaml"
            issues.append(
                Issue(file=rel, field="product", reason=f"product '{feature.product}' not found in metadata/products")
            )
    return issues


def _print_issues(issues: List[Issue]) -> int:
    for issue in sorted(issues, key=lambda i: (i.file, i.field or "")):
        loc = f"::{issue.field}" if issue.field else ""
        print(f"{issue.file}{loc}: {issue.reason}", file=sys.stderr)
    return len(issues)
