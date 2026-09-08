"""Shared markdown helpers for deterministic reference generation."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import yaml


def slug(value: str) -> str:
    return value.strip().lower().replace("_", "-").replace(".", "-")


def fmt_bool(value: Optional[bool]) -> str:
    return "Yes" if value else "No"


def fmt_list(values: List[str]) -> str:
    return ", ".join(values) if values else "—"


def code_block(language: str, code: str) -> str:
    return f"```{language}\n{code.strip()}\n```\n"


def yaml_frontmatter(data: Dict) -> str:
    body = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{body}\n---\n"


def render_page(frontmatter: Dict, body: str) -> str:
    return yaml_frontmatter(frontmatter) + "\n" + body.strip() + "\n"


def write_page(path: Path, content: str) -> None:
    from pawsql_doc.migration import classify
    from pawsql_doc.validate import parse_frontmatter
    data, error = parse_frontmatter(content)
    if data and not error and "docs" in path.parts:
        route = "/".join(path.parts[path.parts.index("docs") + 1:])
        end = content.find("\n---", 4)
        if end != -1:
            content = yaml_frontmatter(classify(data, route)) + "\n" + content[end + 4:].lstrip("\r\n")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def generated_note(source_glob: str) -> str:
    return (
        "> **Generated file.** Do not edit by hand — change the source metadata "
        f"(`metadata/{source_glob}`) and re-run the generator.\n"
    )


# Markers that delimit a generated region inside an otherwise authored page.
DB_MATRIX_START = "<!-- DATABASE_MATRIX:START -->"
DB_MATRIX_END = "<!-- DATABASE_MATRIX:END -->"


def splice_region(
    text: str,
    fragment: str,
    start: str = DB_MATRIX_START,
    end: str = DB_MATRIX_END,
) -> Optional[str]:
    """Replace the region between two markers with ``fragment``.

    Returns ``None`` when either marker is missing so callers can decide how to
    surface it, and never touches text outside the markers.
    """
    start_at = text.find(start)
    if start_at == -1:
        return None
    end_at = text.find(end, start_at + len(start))
    if end_at == -1:
        return None
    block = start + "\n" + fragment.rstrip("\n") + "\n" + end
    return text[:start_at] + block + text[end_at + len(end):]
