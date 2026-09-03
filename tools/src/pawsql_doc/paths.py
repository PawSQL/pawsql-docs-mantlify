"""Repo-root discovery so tools run from anywhere under the repository."""
from __future__ import annotations

from pathlib import Path
from typing import Optional


def find_repo_root(start: Optional[Path] = None) -> Path:
    """Walk up from `start` (default: cwd) until the PawSQL docs repo root is found.

    Markers: a `metadata/` tree plus `tools/` package. Docs content lives under
    `docs/` whose own `docs.json` makes it the Mintlify content root.
    """
    cur = (start or Path.cwd()).resolve()
    for cand in [cur, *cur.parents]:
        if (cand / "metadata").is_dir() and (cand / "tools").is_dir():
            return cand
    raise FileNotFoundError(
        "Cannot locate repository root: no directory containing 'metadata/' and "
        f"'tools/' found above {cur}"
    )


def resolve_root(start: Optional[str]) -> Path:
    return Path(start).resolve() if start else find_repo_root()
