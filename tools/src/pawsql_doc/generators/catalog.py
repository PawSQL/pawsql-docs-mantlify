"""Rule catalogs from active metadata rather than existing files."""
from collections import defaultdict
from pathlib import Path
from pawsql_doc.generators.base import render_page, slug, write_page

# Display order and labels for the controlled RuleCategory vocabulary.
CATEGORY_ORDER = ("ddl", "dml", "index", "rewrite", "join", "subquery", "null", "union", "predicate", "constant", "unknown")
CATEGORY_LABELS = {
    "ddl": {"zh": "对象设计（DDL）", "en": "Schema & Object Design (DDL)"},
    "dml": {"zh": "数据操作（DML）", "en": "Data Manipulation (DML)"},
    "index": {"zh": "索引", "en": "Index"},
    "rewrite": {"zh": "查询重写", "en": "Query Rewrite"},
    "join": {"zh": "表关联", "en": "Joins"},
    "subquery": {"zh": "子查询", "en": "Subqueries"},
    "null": {"zh": "NULL 处理", "en": "NULL Handling"},
    "union": {"zh": "UNION", "en": "UNION"},
    "predicate": {"zh": "谓词", "en": "Predicates"},
    "constant": {"zh": "常量", "en": "Constants"},
    "unknown": {"zh": "待分类", "en": "Unclassified"},
}


def build_rule_indexes(root: Path, bundle=None):
    if bundle is None:
        from pawsql_doc.loaders import load_metadata
        bundle, issues = load_metadata(root)
        if issues:
            raise ValueError("invalid metadata")
    written = []
    for kind in ("audit", "optimizer"):
        for lang in ("zh", "en"):
            entries = sorted([(r, getattr(r.content, lang)) for r in bundle.rules.get(kind, []) if getattr(r.content, lang) is not None], key=lambda item: item[0].id)
            title = ({"audit": "审核规范", "optimizer": "优化算法"}[kind] if lang == "zh" else {"audit": "Audit Rule Reference", "optimizer": "Optimizer Rule Reference"}[kind])
            prefix = "en/" if lang == "en" else ""
            base = f"{kind}-rules-index"
            status = "approved" if entries and all(c.editorial.status in {"approved", "published"} for _, c in entries) else "draft"
            fm = {"id": ("en-" if lang == "en" else "") + base, "title": title,
                  "description": title + ("：查阅规则条件、示例和限制。" if lang == "zh" else ": conditions, examples and limitations."),
                  "type": "reference", "subtype": "rule", "layout": "index", "status": status,
                  "translationKey": base, "language": lang,
                  "localeOf": ("en-" if lang == "zh" else "") + base}
            zh = lang == "zh"
            groups: dict = defaultdict(list)
            for rule, content in entries:
                groups[rule.category.value].append((rule, content))
            ordered = [c for c in CATEGORY_ORDER if c in groups] + sorted(set(groups) - set(CATEGORY_ORDER))
            body = [f"{len(entries)} rules.\n" if lang == "en" else f"共 {len(entries)} 条规则。\n"]
            for cat in ordered:
                label = CATEGORY_LABELS.get(cat, {}).get("zh" if zh else "en", cat)
                body.append(f"\n## {label}\n")
                body.append("| 规则 | ID | 严重级别 |" if zh else "| Rule | ID | Severity |")
                body.append("|---|---|---|")
                for rule, content in groups[cat]:
                    name = (content.name or rule.id).replace("|", "\\|").replace("\n", " ")
                    body.append(f"| [{name}](/{prefix}reference/{kind}-rules/{slug(rule.id)}) | `{rule.id}` | {rule.severity.value} |")
            path = root / "docs" / prefix / "reference" / f"{kind}-rules" / "index.md"
            write_page(path, render_page(fm, "\n".join(body)))
            written.append(path)
    return written
