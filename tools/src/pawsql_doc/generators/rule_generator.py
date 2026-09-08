"""Generate a rule reference page from RuleMetadata (design 12, task 007).

zh-default site: the Chinese page lives at the content root
(``docs/reference/{audit,optimizer}-rules``, served at ``/``) when
``content.zh`` is present; the English mirror lives under the secondary
language tree ``docs/en/reference/{audit,optimizer}-rules`` (served at ``/en``)
when ``content.en`` is present. A rule whose zh content is missing produces no
default-language page and is reported by the drift/gate check as not yet
documented in the default language.
"""
from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from pawsql_doc.generators.base import code_block, fmt_list, generated_note, render_page, slug, write_page
from pawsql_doc.models import RuleCategory, RuleContent, RuleMetadata

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

CATEGORY_ZH = {
    "ddl": "对象与结构定义",
    "dml": "数据操作",
    "index": "索引",
    "rewrite": "重写",
    "join": "连接",
    "subquery": "子查询",
    "null": "NULL 与空值",
    "union": "UNION 与集合",
    "predicate": "谓词与过滤",
    "constant": "常量",
    "unknown": "待归类（产品核对中）",
}

CATEGORY_EN = {
    "ddl": "DDL / object design",
    "dml": "DML / data modification",
    "index": "Index",
    "rewrite": "Rewrite",
    "join": "Join",
    "subquery": "Subquery",
    "null": "NULL handling",
    "union": "UNION / set operations",
    "predicate": "Predicate / filtering",
    "constant": "Constant",
    "unknown": "Unknown (pending product mapping)",
}


def _content(rule: RuleMetadata, lang: str) -> Optional[RuleContent]:
    return getattr(rule.content, lang)


def _name(rule: RuleMetadata, lang: str) -> str:
    own = _content(rule, lang)
    value = (own.name if own else None) or rule.id
    return value


def _value(rule: RuleMetadata, lang: str, attr: str) -> str:
    own = _content(rule, lang)
    value = getattr(own, attr) if own else None
    return value or ""


def _seo(rule: RuleMetadata, lang: str) -> str:
    """Human-written one-line description for front matter (B1).

    Prefers the dedicated ``summary``; falls back to the first line of the
    longer prose description only when it stays a one-liner. Never truncates.
    """
    own = _content(rule, lang)
    summary = getattr(own, "summary", None) if own else None
    if summary:
        return summary.splitlines()[0]
    first_line = _value(rule, lang, "description").splitlines()[0] if _value(rule, lang, "description") else ""
    return first_line if len(first_line) <= 200 else ""


def _databases(rule: RuleMetadata, zh: bool) -> str:
    if rule.database:
        return fmt_list(rule.database)
    # An empty list means the rule applies to every supported database
    # (source docs use "ALL").
    return "待验证（尚未声明数据库范围）" if zh else "Unverified (database scope not declared)"


def _category_display(category: RuleCategory, zh: bool) -> str:
    table = CATEGORY_ZH if zh else CATEGORY_EN
    token = category.value
    display = table.get(token, token)
    if zh:
        return f"{token}（{display}）"
    return f"{token} — {display}"


def _facts(rule: RuleMetadata, zh: bool) -> List[List[str]]:
    if zh:
        rows = [
            ["规则 ID", rule.id],
            ["规则名称", _name(rule, "zh")],
            ["类别", _category_display(rule.category, zh=True)],
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
    rows = [
        ["Rule ID", rule.id],
        ["Name", _name(rule, "en")],
        ["Category", _category_display(rule.category, zh=False)],
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


def _page_parts(rule: RuleMetadata, kind: str, lang: str) -> List[str]:
    zh = lang == "zh"
    source_glob = SOURCE_GLOB.format(kind=kind)
    parts = [_generated_note(source_glob, zh=zh), _table(_facts(rule, zh), zh=zh), ""]
    order = ZH_SECTION_ORDER if zh else SECTION_ORDER
    for attr, heading in order:
        value = _value(rule, lang, attr)
        if value:
            parts.append(f"## {heading}\n")
            parts.append(f"{value}\n")
    bad = _value(rule, lang, "badExample")
    if bad:
        parts.append("## 反例\n" if zh else "## Bad Example\n")
        parts.append(code_block("sql", bad))
    good = _value(rule, lang, "goodExample")
    if good:
        parts.append("## 正例\n" if zh else "## Good Example\n")
        parts.append(code_block("sql", good))
    if rule.relatedRules:
        links = ", ".join(f"`{rid}`" for rid in rule.relatedRules)
        parts.append("## 关联规则\n" if zh else "## Related Rules\n")
        parts.append(f"{links}\n")
    for attr, heading in (("prerequisites", "前置条件" if zh else "Prerequisites"), ("exclusions", "排除条件" if zh else "Exclusions")):
        conditions = getattr(rule.applicability, attr)
        if conditions:
            parts.append(f"## {heading}\n")
            parts.extend(f"- {condition.content.get(lang, condition.code)}\n" for condition in conditions)
    if rule.examples:
        parts.append("## 验证案例\n" if zh else "## Verification examples\n")
        for example in rule.examples:
            parts.append(f"### {example.content.get(lang, example.id)}\n")
            parts.append(f"`{example.dialect}` · `{example.expected.comparison}` · `{example.verification}`\n")
            if example.setupSql:
                parts.append(code_block("sql", example.setupSql))
            parts.append(code_block("sql", example.beforeSql))
            if example.afterSql:
                parts.append(code_block("sql", example.afterSql))
    if rule.evidence:
        parts.append("## 事实依据\n" if zh else "## Evidence\n")
        for evidence in rule.evidence:
            parts.append(f"- `{evidence.id}`: `{evidence.status}` ({', '.join(evidence.supports)})\n")
    return parts


def _rule_folder(kind: str) -> str:
    return "optimizer-rules" if kind == "optimizer" else "audit-rules"


def _page_id(kind: str, rule: RuleMetadata, lang: str) -> str:
    stem = slug(rule.id)
    base = f"{kind}-rule-{stem}"
    # Default language (zh) page id is neutral; the mirror carries an en- prefix.
    return f"en-{base}" if lang == "en" else base


def generate_rule_reference(root: Path, kind: str, rule: RuleMetadata) -> List[Path]:
    """Write the rule's reference page(s). Returns every path written."""
    folder = _rule_folder(kind)
    written: List[Path] = []
    has_zh = _content(rule, "zh") is not None
    has_en = _content(rule, "en") is not None
    zh_id = _page_id(kind, rule, "zh")
    en_id = _page_id(kind, rule, "en")

    if has_en:
        en_out_dir = root / "docs" / "en" / "reference" / folder
        en_path = en_out_dir / f"{slug(rule.id)}.md"
        en_frontmatter = {
            "id": en_id,
            "title": _name(rule, "en"),
            "type": "reference",
            "status": rule.content.en.editorial.status,
            "owners": rule.content.en.editorial.owners,
            "entityRef": {"type": "rule", "id": rule.id},
            "tags": [f"{kind}-rule", rule.category.value, *rule.database],
        }
        en_desc = _seo(rule, "en")
        if rule.content.en.editorial.lastReviewed:
            en_frontmatter["lastReviewed"] = rule.content.en.editorial.lastReviewed
        if en_desc:
            en_frontmatter["description"] = en_desc
        if has_zh:
            en_frontmatter["localeOf"] = zh_id
        write_page(en_path, render_page(en_frontmatter, "\n".join(_page_parts(rule, kind, "en"))))
        written.append(en_path)

    if has_zh:
        zh_out_dir = root / "docs" / "reference" / folder
        zh_path = zh_out_dir / f"{slug(rule.id)}.md"
        zh_frontmatter = {
            "id": zh_id,
            "title": _name(rule, "zh"),
            "type": "reference",
            "status": rule.content.zh.editorial.status,
            "owners": rule.content.zh.editorial.owners,
            "entityRef": {"type": "rule", "id": rule.id},
            "tags": [f"{kind}-rule", rule.category.value, *rule.database],
        }
        zh_desc = _seo(rule, "zh")
        if rule.content.zh.editorial.lastReviewed:
            zh_frontmatter["lastReviewed"] = rule.content.zh.editorial.lastReviewed
        if zh_desc:
            zh_frontmatter["description"] = zh_desc
        if has_en:
            zh_frontmatter["localeOf"] = en_id
        write_page(zh_path, render_page(zh_frontmatter, "\n".join(_page_parts(rule, kind, "zh"))))
        written.append(zh_path)

    return written
