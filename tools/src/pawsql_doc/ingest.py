"""Deterministic rule-doc parsing for the P0 bulk migration (P0.0.5 ingest).

Reads one vault rule document (``20-engine/rules/规则文档/*.md``) and turns it
into the structured fields of a RuleMetadata skeleton. It only extracts what
the source actually states -- no translation, no invented prose. Long-form
English body copy is left for human authoring; the skeleton carries the Chinese
content (zh-default site) plus the English ``name`` when the doc provides one.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List, Optional

import yaml

FIELD_RE = re.compile(r"^#{1,6}\s*(英文名|类别|审查对象|SQL样例|默认预警级别|触发条件|可配置|数据库类型|描述|适用数据库)\s*$")

SEVERITY_ZH = {"提示": "info", "警告": "warning", "错误": "error", "严重": "error"}


@dataclass
class RuleDoc:
    zh_name: str = ""
    en_name: Optional[str] = None
    category_path: str = ""
    review_objects: List[str] = field(default_factory=list)
    severity_zh: Optional[str] = None
    severity: Optional[str] = None
    configurable: Optional[str] = None
    triggers: List[str] = field(default_factory=list)
    database_raw: List[str] = field(default_factory=list)
    intro: str = ""  # paragraphs before the first field section
    bad_sql: str = ""
    good_sql: str = ""
    source: Optional[str] = None


def _clean_list_item(value: str) -> str:
    return value.strip().lstrip("-").strip()


def parse_rule_doc(text: str, source: Optional[str] = None) -> RuleDoc:
    """Parse one vault rule document into structured fields."""
    doc = RuleDoc(source=source)
    lines = text.splitlines()

    # first H1 -> Chinese title
    for line in lines:
        m = re.match(r"^#\s+(.+)\s*$", line)
        if m:
            doc.zh_name = m.group(1).strip()
            break

    # locate field sections; intro = text between H1 and the first field heading
    sections: List[tuple] = []  # (key, start_line_idx)
    for idx, line in enumerate(lines):
        m = FIELD_RE.match(line)
        if m:
            sections.append((m.group(1), idx))
    if sections:
        end_first = sections[0][1]
        intro_lines = []
        for line in lines[1:end_first]:
            if line.strip().startswith("```"):
                continue
            s = line.strip()
            if s:
                intro_lines.append(s)
        doc.intro = "\n".join(intro_lines)

    sql_block_start: Optional[int] = None
    for n, (key, start) in enumerate(sections):
        end = sections[n + 1][1] if n + 1 < len(sections) else len(lines)
        body = lines[start + 1:end]
        _consume_field(doc, key, body, start, lines)

    # split the SQL sample block into bad (不推荐/❌) and good (推荐/✅) parts
    doc.bad_sql, doc.good_sql = _split_sql(lines)
    return doc


def _consume_field(doc: RuleDoc, key: str, body: List[str], start: int, lines: List[str]) -> None:
    items = [_clean_list_item(l) for l in body if l.strip() and not l.strip().startswith("```")]
    if key == "英文名":
        doc.en_name = items[0] if items else None
    elif key == "类别":
        doc.category_path = items[0] if items else ""
    elif key == "审查对象":
        doc.review_objects = [i for i in items if i]
    elif key == "默认预警级别":
        joined = " ".join(body).strip()
        for zh in ("提示", "警告", "错误", "严重"):
            if zh in joined:
                doc.severity_zh = zh
                doc.severity = SEVERITY_ZH[zh]
                break
    elif key == "可配置":
        joined = " ".join(items)
        doc.configurable = joined if joined else None
    elif key == "触发条件":
        doc.triggers = items
    elif key == "数据库类型":
        vals = [i for i in items if i]
        doc.database_raw = [] if (not vals or vals[0].upper().startswith("ALL")) else vals


def _split_sql(lines: List[str]) -> tuple:
    """Split SQL sample code into (bad, good) by ❌/✅ or 不推荐/推荐 markers.

    Works inside a single fenced block too (bad then good lines together).
    Lines before any marker are dropped; marker comment lines are kept with
    their segment.
    """
    fenced: List[List[str]] = []
    cur: Optional[List[str]] = None
    for line in lines:
        if line.strip().startswith("```"):
            if cur is None:
                cur = []
            else:
                if cur:
                    fenced.append(cur)
                cur = None
            continue
        if cur is not None:
            cur.append(line)

    def classify(line: str) -> Optional[str]:
        if "❌" in line or "不推荐" in line:
            return "bad"
        if "✅" in line or "推荐" in line:
            return "good"
        return None

    bad, good = [], []
    for block in fenced:
        cur_bucket: Optional[str] = None
        bad_lines, good_lines = [], []
        for line in block:
            kind = classify(line)
            if kind:
                cur_bucket = kind
            if cur_bucket == "bad":
                bad_lines.append(line)
            elif cur_bucket == "good":
                good_lines.append(line)
        if bad_lines:
            bad.append("\n".join(bad_lines).strip())
        if good_lines:
            good.append("\n".join(good_lines).strip())
    return "\n\n".join(bad), "\n\n".join(good)


def build_zh_content(doc: RuleDoc) -> dict:
    """Map a parsed vault doc to the content.zh skeleton (only what the source states)."""
    zh: dict = {"name": doc.zh_name}
    if doc.intro:
        zh["description"] = doc.intro
    return zh


class _BlockDumper(yaml.SafeDumper):
    pass


def _str_repr(dumper: _BlockDumper, data: str):
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


_BlockDumper.add_representer(str, _str_repr)


def render_skeleton(
    rid: str,
    category: str,
    doc: RuleDoc,
    kind: str,
    source: str,
    product_check: bool = True,
) -> str:
    """Render a reviewable RuleMetadata yaml skeleton from a parsed doc.

    Facts (id/category/severity/database) come from the manifest/doc; language
    prose is kept to zh (default language) plus the English ``name`` the doc
    provides. English body copy and rule-id/category confirmation stay TODO.
    """
    data: dict = {"id": rid, "category": category}
    if doc.severity:
        data["severity"] = doc.severity
    if doc.review_objects:
        parts: List[str] = []
        for item in doc.review_objects:
            for part in re.split(r"[、,，]", item):
                part = part.strip().strip("`")
                if part:
                    parts.append(f"review:{part}")
        if parts:
            data["tags"] = parts
    zh = build_zh_content(doc)
    if doc.bad_sql or doc.good_sql:
        zh["badExample"] = doc.bad_sql
        zh["goodExample"] = doc.good_sql
    content: dict = {}
    if zh:
        content["zh"] = zh
    en: dict = {}
    if doc.en_name:
        en["name"] = doc.en_name
    if en:
        content["en"] = en
    data["content"] = content

    head = (
        f"# Canonical source: vault {source}\n"
        f"# TODO(产品核对): {rid} → 规则注册表 Rule ID / category / severity 定稿后再发布。\n"
        "# TODO(内容): 英文正文（description/whyItMatters/howToFix/示例注释）待人工补齐；zh 由源文档提取，需复核。\n"
        "\n"
    )
    return head + yaml.dump(data, Dumper=_BlockDumper, sort_keys=False, allow_unicode=True, width=4096)
