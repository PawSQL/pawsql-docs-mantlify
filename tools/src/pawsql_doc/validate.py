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

# Canonical six nav groups -> allowed (type, subtype) where subtype is None
# (type must carry no subtype), '*' (any subtype), or a specific subtype.
NAV_GROUP_TYPES = {
    "开始使用": [("explanation", None), ("guide", "quickstart")],
    "Getting Started": [("explanation", None), ("guide", "quickstart")],
    "安装与接入": [("guide", "installation"), ("guide", "integration"), ("guide", "operation")],
    "Installation and Access": [("guide", "installation"), ("guide", "integration"), ("guide", "operation")],
    "使用 PawSQL": [("guide", "*")],
    "Using PawSQL": [("guide", "*")],
    "能力与原理": [("explanation", None)],
    "Capabilities and Concepts": [("explanation", None)],
    "参考资料": [("reference", "*")],
    "Reference": [("reference", "*")],
    "帮助与排障": [("support", "*")],
    "Help and Troubleshooting": [("support", "*")],
}

# Section slots a published detail page must provide per type (release gate).
# Generated pages are exempt via entityRef; index pages are exempt.
REQUIRED_SECTIONS = {
    "guide": ["goal", "prerequisites", "steps", "expectedResult", "verification"],
    "explanation": ["definition", "nextSteps"],
    "support": ["symptom", "diagnosis", "resolution"],
}


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


def _nav_pages(root: Path) -> List[Tuple[Optional[str], str]]:
    """Flatten docs.json navigation into ``(group, page)`` pairs (both languages)."""
    pairs: List[Tuple[Optional[str], str]] = []
    docs_json = root / "docs" / "docs.json"
    if not docs_json.is_file():
        return pairs
    data = json.loads(docs_json.read_text(encoding="utf-8-sig"))

    def walk(node, group: Optional[str] = None):
        if isinstance(node, dict):
            if isinstance(node.get("group"), str):
                group = node["group"]
            pages = node.get("pages")
            if isinstance(pages, list):
                for page in pages:
                    if isinstance(page, str) and not page.startswith(("GET ", "POST ", "PUT ", "PATCH ", "DELETE ", "https://", "http://")):
                        pairs.append((group, page))
            for value in node.values():
                walk(value, group)
        elif isinstance(node, list):
            for item in node:
                walk(item, group)

    walk((data or {}).get("navigation", {}))
    return pairs


def _resolve_nav_page(root: Path, page: str) -> Optional[Path]:
    content_root = root / "docs"
    for suffix in (".md", ".mdx"):
        candidate = content_root / f"{page}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def _group_type_issue(group, page, fm) -> Optional[Issue]:
    """A nav page must match its six-group canonical content type (#1)."""
    allowed = NAV_GROUP_TYPES.get(group) if group else None
    if not allowed:
        return None
    for (typ, subtype) in allowed:
        if fm.type != typ:
            continue
        if subtype is None:
            ok = fm.subtype is None
        elif subtype == "*":
            ok = True
        else:
            ok = fm.subtype == subtype
        if ok:
            return None
    return Issue(
        file="docs/docs.json",
        field=page,
        reason=f"group '{group}' does not allow type={fm.type.value} subtype={fm.subtype.value if fm.subtype else None}",
    )


def _required_section_issues(path: Path, rel: str, fm) -> List[Issue]:
    """Required per-type section slots for published detail pages (#9)."""
    expected = REQUIRED_SECTIONS.get(fm.type)
    if not expected or fm.layout == "index" or fm.entityRef:
        return []
    headings = {line.lstrip("#").strip() for line in path.read_text(encoding="utf-8-sig").splitlines() if line.startswith("#")}
    sections = fm.sections or {}
    issues = []
    for slot in expected:
        heading = sections.get(slot)
        if not heading or heading not in headings:
            issues.append(Issue(file=rel, field=f"sections.{slot}",
                                reason=f"nav page missing required section '{slot}' (type {fm.type.value})"))
    return issues


def validate_nav(root: Path, *, release: bool = False) -> List[Issue]:
    """Navigation gate (B3, two-phase).

    Preview (default): every docs.json target must exist, carry valid front
    matter and fit its nav group's canonical content type. ``release=True``
    additionally requires targets to be approved/published and their detail
    pages to provide the type's required sections.
    """
    issues: List[Issue] = []
    for group, page in _nav_pages(root):
        path = _resolve_nav_page(root, page)
        if path is None:
            issues.append(Issue(file="docs/docs.json", field=page, reason="navigation target missing"))
            continue
        parsed = _page_frontmatter(root, path)
        if parsed is None:
            issues.append(Issue(file="docs/docs.json", field=page, reason="navigation target has invalid front matter"))
            continue
        rel, fm = parsed
        group_issue = _group_type_issue(group, page, fm)
        if group_issue:
            issues.append(group_issue)
        if release:
            if fm.status not in (DocStatus.APPROVED, DocStatus.PUBLISHED):
                issues.append(
                    Issue(
                        file="docs/docs.json",
                        field=page,
                        reason=f"navigation references {rel} which is still {fm.status.value}; navigation = published/approved only",
                    )
                )
            for issue in _required_section_issues(path, rel, fm):
                issues.append(issue)
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
