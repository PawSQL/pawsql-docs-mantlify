"""Rule catalogs from active metadata rather than existing files."""
from pathlib import Path
from pawsql_doc.generators.base import render_page, slug, write_page


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
            body = [f"{len(entries)} rules.\n" if lang == "en" else f"共 {len(entries)} 条规则。\n",
                    "| 规则 | ID | 分类 | 严重级别 |" if lang == "zh" else "| Rule | ID | Category | Severity |", "|---|---|---|---|"]
            for rule, content in entries:
                name = (content.name or rule.id).replace("|", "\\|").replace("\n", " ")
                body.append(f"| [{name}](/{prefix}reference/{kind}-rules/{slug(rule.id)}) | `{rule.id}` | {rule.category.value} | {rule.severity.value} |")
            path = root / "docs" / prefix / "reference" / f"{kind}-rules" / "index.md"
            write_page(path, render_page(fm, "\n".join(body)))
            written.append(path)
    return written
