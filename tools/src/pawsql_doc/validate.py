"""Validation entry points: metadata tree and page front matter."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml
from pydantic import ValidationError

from pawsql_doc.loaders import Issue, check_references, load_metadata
from pawsql_doc.models import FrontMatter


def parse_frontmatter(text: str) -> Tuple[Optional[Dict], Optional[str]]:
    """Return (front-matter dict, error) for a markdown/mdx document."""
    if not text.startswith("---"):
        return None, None
    lines = text.splitlines(keepends=True)
    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        i += 1
    if i >= len(lines):
        return None, "front matter block is not closed"
    block = "".join(lines[1:i])
    try:
        data = yaml.safe_load(block) or {}
    except yaml.YAMLError as exc:
        return None, f"invalid YAML in front matter: {exc}"
    if not isinstance(data, dict):
        return None, "front matter must be a YAML mapping"
    return data, None


def content_files(root: Path) -> List[Path]:
    out: List[Path] = []
    for base in ("docs", "blog"):
        for path in sorted((root / base).rglob("*")):
            if path.is_file() and path.suffix in {".md", ".mdx"}:
                out.append(path)
    return out


def validate_frontmatter_file(root: Path, path: Path) -> List[Issue]:
    rel = path.relative_to(root).as_posix()
    try:
        text = path.read_text(encoding="utf-8-sig")
    except OSError as exc:
        return [Issue(file=rel, reason=f"cannot read: {exc}")]
    data, err = parse_frontmatter(text)
    if err is not None:
        return [Issue(file=rel, reason=err)]
    if data is None:
        return [Issue(file=rel, reason="missing front matter block (must start with ---)")]
    try:
        FrontMatter.model_validate(data)
        return []
    except ValidationError as exc:
        issues: List[Issue] = []
        for item in exc.errors():
            loc = ".".join(str(p) for p in item.get("loc", ()))
            issues.append(Issue(file=rel, field=loc or None, reason=item.get("msg", "")))
        return issues


def validate_frontmatter(root: Path) -> List[Issue]:
    issues: List[Issue] = []
    for path in content_files(root):
        issues.extend(validate_frontmatter_file(root, path))
    return issues


def validate_metadata(root: Path) -> Tuple[List[Issue], dict]:
    bundle, schema_issues = load_metadata(root)
    ref_issues = check_references(bundle)
    counts = {
        "products": len(bundle.products),
        "features": len(bundle.features),
        "rules": sum(len(v) for v in bundle.rules.values()),
        "databases": len(bundle.databases),
        "configs": len(bundle.configs),
        "mappings": len(bundle.mappings),
        "policies": len(bundle.policies),
    }
    return schema_issues + ref_issues, counts
