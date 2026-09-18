from __future__ import annotations

import json
from pathlib import Path
from typing import List

from pawsql_doc.geo import (
    Response,
    analyze_llms_full,
    analyze_llms_txt,
    analyze_markdown_page,
    analyze_robots,
    analyze_sitemap,
    analyze_structured_data,
    load_expectations,
)

ORG = {
    "id": "https://www.pawsql.com/#organization",
    "name": "PawSQL",
    "url": "https://www.pawsql.com",
    "legalName": "北京图灵睿数科技有限公司",
    "logo": "https://www.pawsql.com/logo.png",
    "sameAs": ["https://github.com/PawSQL"],
}
INSTRUCTIONS = ["PawSQL 是一个产品。", "PawSQL is a single product."]

# A Mintlify-style llms.txt and the ld+json graph it emits for a page.
LLMS_TXT = """# PawSQL

> 让数据库性能优化自动化且可验证。

## 开始使用

- [什么是 PawSQL?](https://docs.pawsql.com/getting-started/index.md): 概览
- [快速开始](https://docs.pawsql.com/getting-started/quickstart.md): 上手
"""


def _text(body: str, status: int = 200, ctype: str = "text/plain; charset=utf-8") -> Response:
    return Response(status=status, content_type=ctype, body=body, headers={})


def _html(body: str) -> Response:
    return Response(status=200, content_type="text/html; charset=utf-8", body=body, headers={})


def _graph_page(org: dict | None = None, types: List[str] | None = None) -> str:
    graph = [{"@type": t} for t in (types or ["Organization", "WebSite", "WebPage"])]
    if org is not None:
        graph[0] = {"@type": "Organization", **org}
    payload = {"@context": "https://schema.org", "@graph": graph}
    return f'<html><head><script type="application/ld+json">{json.dumps(payload, ensure_ascii=False)}</script></head></html>'


def _find(findings, needle: str):
    return next(f for f in findings if needle in f.check)


def _repo(tmp_path: Path, docs_json: dict) -> Path:
    root = tmp_path / "repo"
    (root / "docs").mkdir(parents=True)
    (root / "docs" / "docs.json").write_text(json.dumps(docs_json, ensure_ascii=False), encoding="utf-8")
    return root


# --- llms.txt -------------------------------------------------------------

def test_llms_txt_rejects_spa_html_shell():
    """The old site answered 200 with its JS shell: a fake llms.txt."""
    findings = analyze_llms_txt(
        _html('<!doctype html><html><div id="root"></div>You need to enable JavaScript</html>'),
        INSTRUCTIONS,
    )
    assert _find(findings, "不是 HTML 兜底页").ok is False


def test_llms_txt_flags_duplicate_page_entries():
    body = LLMS_TXT + "- [什么是 PawSQL?](https://docs.pawsql.com/getting-started/index.md): 概览\n"
    findings = analyze_llms_txt(_text(body), INSTRUCTIONS)
    dup = _find(findings, "无重复页面条目")
    assert dup.ok is False
    assert dup.required is True
    assert "getting-started/index.md" in dup.detail


def test_llms_txt_clean_index_passes_but_reports_missing_instructions():
    findings = analyze_llms_txt(_text(LLMS_TXT), INSTRUCTIONS)
    assert _find(findings, "无重复页面条目").ok is True
    assert _find(findings, "含 .md 页面链接").ok is True
    assert _find(findings, "Agent Instructions").ok is False


def test_llms_txt_reports_instructions_when_present():
    body = LLMS_TXT + "> ## Agent Instructions\n> " + INSTRUCTIONS[0] + "\n"
    findings = analyze_llms_txt(_text(body), INSTRUCTIONS)
    assert _find(findings, "含 Agent Instructions 块").ok is True
    assert _find(findings, "instructions 文案落地").ok is True


def test_llms_full_flags_stub_page():
    findings = analyze_llms_full(_text("too short"), INSTRUCTIONS)
    assert _find(findings, "含正文内容").ok is False


# --- robots / sitemap -----------------------------------------------------

def test_robots_allows_when_only_sitemap_declared():
    findings = analyze_robots(_text("User-agent: *\nAllow: /\n\nSitemap: https://docs.pawsql.com/sitemap.xml\n"))
    assert _find(findings, "未整站 Disallow").ok is True
    assert _find(findings, "声明 Sitemap").ok is True


def test_robots_flags_sitewide_disallow():
    findings = analyze_robots(_text("User-agent: *\nDisallow: /\n"))
    assert _find(findings, "未整站 Disallow").ok is False


def test_sitemap_requires_loc_entries():
    findings = analyze_sitemap(_text("<?xml version='1.0'?><urlset></urlset>", ctype="application/xml"))
    assert _find(findings, "含 URL").ok is False


# --- markdown export ------------------------------------------------------

def test_markdown_page_requires_agent_instructions():
    findings = analyze_markdown_page(_text("# 页面\n\n正文\n"), INSTRUCTIONS)
    assert _find(findings, "返回 Markdown 而非 HTML").ok is True
    assert _find(findings, "含 Agent Instructions 块").ok is False


def test_markdown_page_rejects_html_response():
    findings = analyze_markdown_page(_html("<html></html>"), INSTRUCTIONS)
    assert _find(findings, "返回 Markdown 而非 HTML").ok is False


# --- structured data ------------------------------------------------------

def test_structured_data_missing_ld_json_is_hard_failure():
    findings = analyze_structured_data("<html><body>no structured data</body></html>", ORG)
    assert findings[0].ok is False
    assert findings[0].required is True


def test_structured_data_matches_configured_organization():
    findings = analyze_structured_data(_graph_page(ORG), ORG)
    assert all(f.ok for f in findings), [f.detail for f in findings if not f.ok]


def test_structured_data_reports_platform_derived_organization():
    """Mintlify falls back to the site origin when seo.organization is unset."""
    findings = analyze_structured_data(_graph_page({"name": "PawSQL", "url": "https://docs.pawsql.com"}), ORG)
    assert _find(findings, "Organization.url").ok is False
    assert _find(findings, "Organization.sameAs").ok is False


def test_structured_data_optional_fields_warn_instead_of_failing():
    org = {"name": "PawSQL", "url": ORG["url"], "sameAs": ORG["sameAs"]}
    findings = analyze_structured_data(_graph_page(org), ORG)
    optional = [f for f in findings if f.check.startswith("JSON-LD: Organization.") and not f.required]
    assert optional, "legalName / logo / id should be reported as warnings"
    assert all(not f.ok for f in optional)
    assert all(f.ok for f in findings if f.required), [f.detail for f in findings if f.required and not f.ok]


# --- expectations from docs.json ------------------------------------------

def test_load_expectations_reads_organization_and_sample_page(tmp_path: Path):
    root = _repo(tmp_path, {
        "description": "站点描述",
        "seo": {"indexing": "navigable", "organization": ORG},
        "markdown": {"instructions": INSTRUCTIONS},
        "navigation": {"languages": [{"language": "zh", "tabs": [{"tab": "t", "groups": [
            {"group": "g", "root": "a/index", "pages": ["a/index", "a/b"]},
        ]}]}]},
    })
    exp = load_expectations(root)
    assert exp["organization"] == ORG
    assert exp["instructions"] == INSTRUCTIONS
    assert exp["first_page"] == "a/index"
