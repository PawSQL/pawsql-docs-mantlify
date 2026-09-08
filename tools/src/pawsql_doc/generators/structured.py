"""Localized database/configuration references from neutral facts and own prose."""
from pathlib import Path
from pawsql_doc.generators.base import render_page, write_page, slug, code_block


def _page(root, route, identity, lang, title, description, body, editorial=None):
    path = root / "docs" / ("en" if lang == "en" else "") / route
    fm = {"id": identity, "translationKey": identity.removeprefix("en-").removeprefix("zh-"), "language": lang,
          "title": title, "type": "reference", "status": editorial.status if editorial else "draft"}
    fm["entityRef"] = {"type": "database" if "databases/" in route else "configuration" if "configuration/" in route else "compatibility", "id": identity.removeprefix("zh-")}
    if editorial:
        fm["owners"] = editorial.owners
        if editorial.lastReviewed:
            fm["lastReviewed"] = editorial.lastReviewed
    if description:
        fm["description"] = description
    write_page(path, render_page(fm, body))
    return path


def database_pages(root, db):
    written = []
    for lang in ("zh", "en"):
        content = getattr(db.content, lang)
        if content is None and lang == "zh":
            continue
        zh = lang == "zh"
        name = (content.name if content else None) or db.title or db.database
        body = [f"# {name}\n", "| Database | Versions | Capability | Status |", "|---|---|---|---|"]
        if db.compatibility:
            for row in db.compatibility:
                body.append(f"| {db.database} | {', '.join(row.databaseVersions)} | {row.capability} | {row.status} |")
                for limitation in row.limitations:
                    body.append(f"\n- {limitation.content.get(lang, limitation.code)}\n")
        else:
            body.append(f"| {db.database} | {', '.join(db.supportedVersions)} | legacy claims | unknown |")
        own_description = content.description if content else db.description
        if own_description:
            body.append("\n" + own_description)
        for feature in (content.keyFeatures if content else db.keyFeatures):
            body.append(f"\n- {feature}")
        notes = content.notes if content else db.notes
        if notes:
            body.append("\n" + notes)
        body.append("\n兼容性为 unknown 时表示尚未验证。" if zh else "\nUnknown means compatibility has not been verified.")
        identity = ("zh-" if zh else "") + f"database-{db.database}"
        written.append(_page(root, f"databases/{db.database}/index.md", identity, lang, name,
                            content.summary if content else None, "\n".join(body), content.editorial if content else None))
    return written


def config_pages(root, cfg):
    written = []
    for lang in ("zh", "en"):
        content = getattr(cfg.content, lang)
        if content is None and lang == "zh":
            continue
        rows = [("Parameter", cfg.name), ("Type", cfg.configType.value), ("Default", str(cfg.default)),
                ("Unit", cfg.unit or "unknown"), ("Scope", cfg.behavior.scope or cfg.scope),
                ("Activation", cfg.behavior.activation), ("Restart required", str(cfg.behavior.restartRequired)),
                ("Precedence", ", ".join(cfg.behavior.precedence) or "unknown")]
        if cfg.allowedRange:
            rows.append(("Range", f"{cfg.allowedRange.min} .. {cfg.allowedRange.max}"))
        body = ["| Field | Value |", "|---|---|", *[f"| {k} | {v} |" for k, v in rows]]
        description = content.description if content else cfg.description
        if description:
            body.append("\n" + description)
        example = content.example if content else cfg.example
        if example:
            body.append(code_block("text", example))
        identity = ("zh-" if lang == "zh" else "") + f"config-{slug(cfg.name)}"
        written.append(_page(root, f"reference/configuration/{slug(cfg.name)}.md", identity, lang,
                            content.name if content and content.name else cfg.name,
                            content.summary if content else None, "\n".join(body), content.editorial if content else None))
    return written
