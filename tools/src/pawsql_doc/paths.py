"""Repo-root discovery so tools run from anywhere under the repository."""
from __future__ import annotations

from pathlib import Path
from typing import Optional


def find_repo_root(start: Optional[Path] = None) -> Path:
    """Walk up from `start` (default: cwd) until a dir with docs.json + metadata/ is found."""
    cur = (start or Path.cwd()).resolve()
    for cand in [cur, *cur.parents]:
        if (cand / "docs.json").is_file() and (cand / "metadata").is_dir():
            return cand
    raise FileNotFoundError(
        "Cannot locate repository root: no directory containing 'docs.json' and 'metadata/' "
        f"found above {cur}"
    )


def resolve_root(start: Optional[str]) -> Path:
    return Path(start).resolve() if start else find_repo_root()
