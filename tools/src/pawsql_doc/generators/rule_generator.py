"""Generate a rule reference page from RuleMetadata (design 12, task 007).

When the rule metadata carries a ``zh`` block the generator also emits a
Chinese mirror page under ``docs/zh/reference/...`` (bilingual dual output).
"""
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

ZH_SECTION_ORDER = [
    ("description", "说明"),
    ("whyItMatters", "为什么重要"),
    ("howToFix", "如何修复"),
]

SOURCE_GLOB = "rules/{kind}/*.yaml"

SEVERITY_ZH = {"error": "错误", "warning": "警告", "info": "提示"}


def _databases(rule: RuleMetadata, zh: bool) -> str:
    if rule.database:
        return fmt_list(rule.database)
    # An empty list means the rule applies to every supported database
    # (source docs use "ALL").
    return "所有支持数据库" if zh else "All supported databases"


def _facts(rule: RuleMetadata) -> List[List[str]]:
    rows = [
        ["Rule ID", rule.id],
        ["Name", rule.name],
        ["Category", rule.category],
        ["Severity", rule.severity.value],
        ["Databases", _databases(rule, zh=False)],
    ]
    if rule.introducedVersion:
        rows.append(["Version Introduced", rule.introducedVersion])
    if rule.deprecatedVersion:
        rows.append(["Version Deprecated", rule.deprecatedVersion])
    if rule.implementationClass:
        rows.append(["Implementation", f"`{rule.implementationClass}`"])
    return rows


def _facts_zh(rule: RuleMetadata) -> List[List[str]]:
    zh = rule.zh
    rows = [
        ["规则 ID", rule.id],
        ["规则名称", zh.name if zh and zh.name else rule.name],
        ["类别", rule.category],
        ["预警级别", SEVERITY_ZH.get(rule.severity.value, rule.severity.value)],
        ["适用数据库", _databases(rule, zh=True)],
    ]
    if rule.introducedVersion:
        rows.append(["引入版本", rule.introducedVersion])
    if rule.deprecatedVersion:
        rows.append(["弃用版本", rule.deprecatedVersion])
    if rule.implementationClass:
        rows.append(["实现", f"`{rule.implementationClass}`"])
    return rows


def _table(rows: List[List[str]], zh: bool) -> str:
    if zh:
        lines = ["| 字段 | 值 |", "|---|---|"]
    else:
        lines = ["| Field | Value |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in rows]
    return "\n".join(lines)


def _generated_note(source_glob: str, zh: bool) -> str:
    if zh:
        return (
            "> **生成文件，请勿手改。** 如需修改请更新源元数据 "
            f"(`metadata/{source_glob}`) 并重新运行生成器。\n"
        )
    return generated_note(source_glob)


def _zh_value(rule: RuleMetadata, attr: str) -> str:
    zh = rule.zh
    zh_value = getattr(zh, attr) if zh else None
    return zh_value if zh_value else (getattr(rule, attr) or "")


def _page_parts(rule: RuleMetadata, kind: str, zh: bool) -> List[str]:
    source_glob = SOURCE_GLOB.format(kind=kind)
    if zh:
        parts = [_generated_note(source_glob, zh=True), _table(_facts_zh(rule), zh=True), ""]
        for attr, heading in ZH_SECTION_ORDER:
            value = _zh_value(rule, attr)
            if value:
                parts.append(f"## {heading}\n")
                parts.append(f"{value}\n")
        bad = _zh_value(rule, "badExample")
        if bad:
            parts.append("## 反例\n")
            parts.append(code_block("sql", bad))
        good = _zh_value(rule, "goodExample")
        if good:
            parts.append("## 正例\n")
            parts.append(code_block("sql", good))
        return parts

    parts = [_generated_note(source_glob, zh=False), _table(_facts(rule), zh=False), ""]
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
    return parts


def _rule_folder(kind: str) -> str:
    return "optimizer-rules" if kind == "optimizer" else "audit-rules"


def generate_rule_reference(root: Path, kind: str, rule: RuleMetadata) -> List[Path]:
    """Write the rule's reference page(s). Returns every path written.

    English page under ``docs/reference/{audit,optimizer}-rules`` is always
    written; when ``rule.zh`` is present a Chinese mirror is also written
    under ``docs/zh/reference/{audit,optimizer}-rules``.
    """
    folder = _rule_folder(kind)
    written: List[Path] = []

    out_dir = root / "docs" / "reference" / folder
    out_path = out_dir / f"{slug(rule.id)}.md"
    en_frontmatter = {
        "id": f"{kind}-rule-{slug(rule.id)}",
        "title": rule.name,
        "type": "reference",
        "status": "draft",
        "tags": [f"{kind}-rule", rule.category, *rule.database],
    }
    if rule.description:
        en_frontmatter["description"] = rule.description.splitlines()[0][:200]
    write_page(out_path, render_page(en_frontmatter, "\n".join(_page_parts(rule, kind, zh=False))))
    written.append(out_path)

    if rule.zh is not None:
        zh_out_dir = root / "docs" / "zh" / "reference" / folder
        zh_path = zh_out_dir / f"{slug(rule.id)}.md"
        zh_frontmatter = {
            "id": f"zh-{kind}-rule-{slug(rule.id)}",
            "title": rule.zh.name or rule.name,
            "type": "reference",
            "status": "draft",
            "tags": [f"{kind}-rule", "zh", rule.category, *rule.database],
        }
        zh_desc = rule.zh.description or rule.description
        if zh_desc:
            zh_frontmatter["description"] = zh_desc.splitlines()[0][:200]
        write_page(zh_path, render_page(zh_frontmatter, "\n".join(_page_parts(rule, kind, zh=True))))
        written.append(zh_path)

    return written
