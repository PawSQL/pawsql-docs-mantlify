from __future__ import annotations

import json
from pathlib import Path

import yaml

from pawsql_doc.validate import (
    validate_frontmatter,
    validate_nav,
)


def _write_page(root: Path, rel: str, fm: dict) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip() + "\n---\nbody\n"
    path.write_text(text, encoding="utf-8")


def test_published_without_description_fails(repo):
    _write_page(repo, "docs/published.md", {"id": "p", "title": "P", "type": "reference", "status": "published"})
    issues = validate_frontmatter(repo)
    assert any(i.field == "description" for i in issues)


def test_machine_truncated_description_fails(repo):
    _write_page(repo, "docs/draft.md", {
        "id": "d", "title": "D", "type": "reference", "status": "draft",
        "description": "this line was cut off…",
    })
    issues = validate_frontmatter(repo)
    assert any(i.field == "description" for i in issues)


def test_localeof_unknown_target_fails(repo):
    _write_page(repo, "docs/zh-page.md", {
        "id": "zh-x", "title": "X", "type": "reference", "status": "draft", "localeOf": "en-missing",
    })
    issues = validate_frontmatter(repo)
    assert any(i.field == "localeOf" for i in issues)


def test_localeof_self_reference_fails(repo):
    _write_page(repo, "docs/self.md", {
        "id": "self", "title": "S", "type": "reference", "status": "draft", "localeOf": "self",
    })
    issues = validate_frontmatter(repo)
    assert any(i.field == "localeOf" for i in issues)


def test_nav_reports_draft_page(repo):
    (repo / "docs").mkdir(parents=True, exist_ok=True)
    _write_page(repo, "docs/guide/index.md", {"id": "g", "title": "G", "type": "user-guide", "status": "draft"})
    _write_page(repo, "docs/released.md", {"id": "rel", "title": "R", "type": "reference", "status": "published"})
    nav = {
        "navigation": {
            "languages": [
                {"language": "zh", "tabs": [{"tab": "T", "groups": [{"group": "G", "pages": ["guide/index", "released"]}]}]}
            ]
        }
    }
    docs_json = repo / "docs" / "docs.json"
    docs_json.write_text(json.dumps(nav), encoding="utf-8")
    issues = validate_nav(repo)
    assert any(i.field == "guide/index" for i in issues)
    assert not any(i.field == "released" for i in issues)


def test_nav_clean_when_all_published(repo):
    (repo / "docs").mkdir(parents=True, exist_ok=True)
    _write_page(repo, "docs/released.md", {"id": "rel", "title": "R", "type": "reference", "status": "published"})
    nav = {
        "navigation": {
            "languages": [
                {"language": "zh", "tabs": [{"tab": "T", "groups": [{"group": "G", "pages": ["released"]}]}]}
            ]
        }
    }
    docs_json = repo / "docs" / "docs.json"
    docs_json.write_text(json.dumps(nav), encoding="utf-8")
    assert validate_nav(repo) == []
