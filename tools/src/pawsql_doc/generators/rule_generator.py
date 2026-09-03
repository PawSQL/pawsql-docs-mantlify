"""Generate a rule reference page from RuleMetadata (design 12, task 007)."""
from __future__ import annotations

from pathlib import Path
from typing import List

from pawsql_doc.generators.base import code_block, fmt_list, generated_note, render_page, slug, write_page
from pawsql_doc.models import RuleMetadata

SECTION_ORDER = [
    ("description", "Description"),
    ("whyItMatters", "Why It Matters"),
    ("howToFix", "How to Fix"),
]

SOURCE_GLOB = "rules/{kind}/*.yaml"


def _facts(rule: RuleMetadata) -> List[List[str]]:
    rows = [
        ["Rule ID", rule.id],
        ["Name", rule.name],
        ["Category", rule.category],
        ["Severity", rule.severity.value],
        ["Databases", fmt_list(rule.database)],
    ]
    if rule.introducedVersion:
        rows.append(["Version Introduced", rule.introducedVersion])
    if rule.deprecatedVersion:
        rows.append(["Version Deprecated", rule.deprecatedVersion])
    if rule.implementationClass:
        rows.append(["Implementation", f"`{rule.implementationClass}`"])
    return rows


def _table(rows: List[List[str]]) -> str:
    lines = ["| Field | Value |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in rows]
    return "\n".join(lines)


def generate_rule_reference(root: Path, kind: str, rule: RuleMetadata) -> Path:
    out_dir = root / "docs" / "reference"
    if kind == "optimizer":
        out_dir = out_dir / "optimizer-rules"
    else:
        out_dir = out_dir / "audit-rules"
    out_path = out_dir / f"{slug(rule.id)}.md"

    parts = [
        generated_note(SOURCE_GLOB.format(kind=kind)),
        _table(_facts(rule)),
        "",
    ]

    for attr, heading in SECTION_ORDER:
        value = getattr(rule, attr)
        if value:
            parts.append(f"## {heading}\n")
            parts.append(f"{value}\n")

    if rule.badExample:
        parts.append("## Bad Example\n")
        parts.append(code_block("sql", rule.badExample))

    if rule.goodExample:
        parts.append("## Good Example\n")
        parts.append(code_block("sql", rule.goodExample))

    if rule.relatedRules:
        links = ", ".join(f"`{rid}`" for rid in rule.relatedRules)
        parts.append("## Related Rules\n")
        parts.append(f"{links}\n")

    frontmatter = {
        "id": f"{kind}-rule-{slug(rule.id)}",
        "title": rule.name,
        "type": "reference",
        "status": "draft",
        "tags": [f"{kind}-rule", rule.category, *rule.database],
    }
    if rule.description:
        frontmatter["description"] = rule.description.splitlines()[0][:200]

    write_page(out_path, render_page(frontmatter, "\n".join(parts)))
    return out_path
