"""Rule-reference directory (landing) indexes, generated after rule pages.

Produces, for each language and rule kind, an ``index.md`` that lists every
generated rule page (zh default tree under ``docs/reference/{kind}-rules``,
en under ``docs/en/reference/{kind}-rules``). Kept deterministic: reads only
the page set + each page's front-matter ``title``.
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

import yaml

KINDS = ("audit", "optimizer")
LANGS = ("zh", "en")

TITLES = {
    ("audit", "zh"): ("审核规范", "PawSQL SQL 审核规则全量目录（由 metadata/rules/audit 生成）"),
    ("optimizer", "zh"): ("优化算法", "PawSQL 优化器规则/算法全量目录（由 metadata/rules/optimizer 生成）"),
    ("audit", "en"): ("Audit Rule Reference", "Catalog of PawSQL SQL audit rules (generated)"),
    ("optimizer", "en"): ("Optimizer Rule Reference", "Catalog of PawSQL optimizer rules (generated)"),
}
IDS = {
    ("audit", "zh"): "audit-rules-index", ("optimizer", "zh"): "optimizer-rules-index",
    ("audit", "en"): "en-audit-rules-index", ("optimizer", "en"): "en-optimizer-rules-index",
}


def _page_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    if not text.startswith("---"):
        return ""
    parts = text.split("---", 2)
    if len(parts) < 3:
        return ""
    try:
        data = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return ""
    return data.get("title") or ""


def _build_one(root: Path, kind: str, lang: str) -> Tuple[Path, int]:
    base = root / "docs" / ("en" if lang == "en" else "") / "reference" / f"{kind}-rules"
    rules = sorted(p for p in base.glob("*.md") if p.name != "index.md")
    zh = lang == "zh"
    title, desc = TITLES[(kind, lang)]
    note = (
        "> 生成文件：由已生成的规则页汇总，勿手改；`build-references` 会自动重建。\n"
        if zh
        else "> Generated: aggregated from the rule pages; rebuilt by `build-references`. "
        "Do not edit by hand.\n"
    )
    heading, count_line, row_head = (
        (title, f"共 {len(rules)} 条规则。\n", "| 规则 | ID |") if zh
        else (title, f"{len(rules)} rules.\n", "| Rule | ID |")
    )
    rows = []
    for p in rules:
        slug = p.name[: -len(p.suffix)]
        route = f"{'en/' if lang == 'en' else ''}reference/{kind}-rules/{slug}"
        rows.append(f"| [{_page_title(p) or slug}]({route}) | `{slug}` |")

    fm = {
        "id": IDS[(kind, lang)],
        "title": title,
        "description": desc,
        "type": "reference",
        "status": "draft",
        "tags": [f"{kind}-rules", lang],
        "localeOf": IDS[(kind, "en" if zh else "zh")],
    }
    body = [note, f"# {heading}\n", count_line, row_head, "|---|---|", *rows, ""]
    content = (
        "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
        + "\n---\n\n" + "\n".join(body)
    )
    out = base / "index.md"
    out.write_text(content, encoding="utf-8")
    return out, len(rules)


def build_rule_indexes(root: Path) -> List[Path]:
    """Write every rule landing index. Returns paths written."""
    from pawsql_doc.generators.catalog import build_rule_indexes as canonical
    return canonical(root)
