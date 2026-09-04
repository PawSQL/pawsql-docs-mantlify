"""Validation entry points: metadata tree and page front matter."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml
from pydantic import ValidationError

from pawsql_doc.loaders import Issue, check_references, load_metadata
from pawsql_doc.models import DocStatus, FrontMatter

# A description that long is pasted body text, not a human one-liner.
DESCRIPTION_MAX = 320


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


def _description_issues(fm: FrontMatter, rel: str) -> List[Issue]:
    """Governance for `description` (SEO/LLM retrieval material, design 29)."""
    issues: List[Issue] = []
    desc = (fm.description or "").strip()
    published = fm.status in (DocStatus.PUBLISHED, DocStatus.APPROVED, DocStatus.SCHEDULED)
    if published and not desc:
        issues.append(Issue(file=rel, field="description", reason="published page must have a human-written description"))
    if desc.endswith("…"):
        issues.append(Issue(file=rel, field="description", reason="description looks machine-truncated (ends with '…'); use the full human-written value"))
    if len(desc) > DESCRIPTION_MAX:
        issues.append(Issue(file=rel, field="description", reason=f"description is {len(desc)} chars; keep it a one-liner <= ~155 chars"))
    return issues


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
        fm = FrontMatter.model_validate(data)
    except ValidationError as exc:
        issues: List[Issue] = []
        for item in exc.errors():
            loc = ".".join(str(p) for p in item.get("loc", ()))
            issues.append(Issue(file=rel, field=loc or None, reason=item.get("msg", "")))
        return issues
    return _description_issues(fm, rel)


def validate_frontmatter(root: Path) -> List[Issue]:
    issues: List[Issue] = []
    for path in content_files(root):
        issues.extend(validate_frontmatter_file(root, path))
    issues.extend(_validate_localeof(root))
    return issues


def _page_frontmatter(root: Path, path: Path) -> Optional[Tuple[str, FrontMatter]]:
    """Return (relative path, FrontMatter) when the page carries valid front matter."""
    text = path.read_text(encoding="utf-8-sig")
    data, err = parse_frontmatter(text)
    if err is not None or data is None:
        return None
    try:
        return path.relative_to(root).as_posix(), FrontMatter.model_validate(data)
    except ValidationError:
        return None


def _validate_localeof(root: Path) -> List[Issue]:
    """Mirror pairing (B2): every localeOf must point at an existing page id, never itself."""
    issues: List[Issue] = []
    ids: Dict[str, str] = {}
    pages: List[Tuple[str, FrontMatter]] = []
    for path in content_files(root):
        parsed = _page_frontmatter(root, path)
        if parsed is None:
            continue
        rel, fm = parsed
        pages.append((rel, fm))
        ids.setdefault(fm.id, rel)
    for rel, fm in pages:
        if not fm.localeOf:
            continue
        if fm.localeOf == fm.id:
            issues.append(Issue(file=rel, field="localeOf", reason=f"localeOf must not point to the page itself: {fm.localeOf}"))
        elif fm.localeOf not in ids:
            issues.append(Issue(file=rel, field="localeOf", reason=f"localeOf references unknown page id '{fm.localeOf}'"))
    return issues


def _nav_page_targets(root: Path) -> List[str]:
    """Flatten every page string referenced by docs.json navigation (both languages)."""
    targets: List[str] = []
    docs_json = root / "docs" / "docs.json"
    if not docs_json.is_file():
        return targets
    data = json.loads(docs_json.read_text(encoding="utf-8-sig"))
    languages = (data or {}).get("navigation", {}).get("languages", [])
    for lang in languages:
        for tab in lang.get("tabs", []):
            for group in tab.get("groups", []):
                for page in group.get("pages", []):
                    if isinstance(page, str):
                        targets.append(page)
    return targets


def validate_nav(root: Path) -> List[Issue]:
    """Navigation = publish (B3): pages listed in docs.json must not be draft/review.

    Only pages that exist on disk are checked; an aspirational nav may reference
    pages that have not been authored yet (that is a preview concern, not a
    publication one). Enforcement is meaningful once content is promoted to
    published/approved.
    """
    issues: List[Issue] = []
    content_root = root / "docs"
    for page in _nav_page_targets(root):
        path = content_root / f"{page}.md"
        if not path.is_file():
            continue
        parsed = _page_frontmatter(root, path)
        if parsed is None:
            continue
        rel, fm = parsed
        if fm.status in (DocStatus.DRAFT, DocStatus.REVIEW):
            issues.append(
                Issue(
                    file="docs/docs.json",
                    field=page,
                    reason=f"navigation references {rel} which is still {fm.status.value}; navigation = published/approved only",
                )
            )
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
