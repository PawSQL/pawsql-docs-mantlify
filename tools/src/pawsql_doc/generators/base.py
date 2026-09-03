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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generated_note(source_glob: str) -> str:
    return (
        "> **Generated file.** Do not edit by hand — change the source metadata "
        f"(`metadata/{source_glob}`) and re-run the generator.\n"
    )
