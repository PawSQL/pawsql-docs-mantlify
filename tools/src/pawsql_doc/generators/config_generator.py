"""Generate a configuration reference page from ConfigMetadata (design 14)."""
from __future__ import annotations

from pathlib import Path

from pawsql_doc.generators.base import code_block, generated_note, render_page, slug, write_page
from pawsql_doc.models import ConfigMetadata


def _facts(cfg: ConfigMetadata) -> list[list[str]]:
    rows = [
        ["Parameter", f"`{cfg.name}`"],
        ["Type", cfg.configType.value],
        ["Default", _fmt_default(cfg)],
    ]
    if cfg.unit:
        rows.append(["Unit", cfg.unit])
    rows.append(["Scope", cfg.scope])
    if cfg.versionIntroduced:
        rows.append(["Version Introduced", cfg.versionIntroduced])
    if cfg.versionDeprecated:
        rows.append(["Version Deprecated", cfg.versionDeprecated])
    if cfg.allowedRange is not None:
        lo = cfg.allowedRange.min
        hi = cfg.allowedRange.max
        bounds = f"{lo if lo is not None else ''} .. {hi if hi is not None else ''}"
        rows.append(["Allowed Range", bounds])
    return rows


def _fmt_default(cfg: ConfigMetadata) -> str:
    if cfg.default is None:
        return "—"
    if isinstance(cfg.default, bool):
        return str(cfg.default).lower()
    return str(cfg.default)


def _table(rows: list[list[str]]) -> str:
    lines = ["| Field | Value |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in rows]
    return "\n".join(lines)


def generate_config_reference(root: Path, cfg: ConfigMetadata) -> Path:
    # English-only page -> secondary /en tree (docs/en/...)
    out_path = root / "docs" / "en" / "reference" / "configuration" / f"{slug(cfg.name)}.md"
    parts = [
        generated_note("configs/*.yaml"),
        _table(_facts(cfg)),
        "",
    ]
    if cfg.description:
        parts.append("## Description\n")
        parts.append(f"{cfg.description}\n")
    if cfg.example:
        parts.append("## Example\n")
        parts.append(code_block("bash", cfg.example))

    frontmatter = {
        "id": f"config-{slug(cfg.name)}",
        "title": cfg.name,
        "type": "reference",
        "status": "draft",
        "tags": [f"config:{cfg.scope}", cfg.configType.value],
    }
    if cfg.description:
        frontmatter["description"] = cfg.description.splitlines()[0][:200]

    write_page(out_path, render_page(frontmatter, "\n".join(parts)))
    return out_path
