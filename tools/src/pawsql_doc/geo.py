"""Online GEO acceptance checks (GEO-PLAN G2-1).

Mintlify generates llms.txt, llms-full.txt, per-page Markdown and JSON-LD
structured data on its hosting layer -- none of it is visible in
``mintlify dev``. These checks therefore run against a deployed base URL and
compare what the live site serves against what ``docs/docs.json`` declares.

GitHub-hosted CI must not depend on the production site, so this stays a
manually invoked command (see GEO-PLAN G2-1).
"""
from __future__ import annotations

import html as html_mod
import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

# A crawler UA that a site might accidentally block; if /llms.txt answers
# differently for this than for a plain UA, AI tooling is locked out.
AI_BOT_UA = "Mozilla/5.0 (compatible; GPTBot/1.2; +https://openai.com/gptbot)"

LD_JSON_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.S | re.I,
)


@dataclass
class Finding:
    """One check result. `required` failures make the command exit non-zero."""

    check: str
    ok: bool
    detail: str
    required: bool = True


@dataclass
class Response:
    status: int
    content_type: str
    body: str
    headers: Dict[str, str]

    @property
    def is_html(self) -> bool:
        return "text/html" in self.content_type.lower()


# --------------------------------------------------------------------------
# expectations from docs.json
# --------------------------------------------------------------------------

def load_expectations(root: Path) -> Dict[str, object]:
    """Read the values the deployed site must reflect from docs/docs.json."""
    path = root / "docs" / "docs.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    seo = data.get("seo") or {}
    return {
        "description": data.get("description") or "",
        "instructions": [(s or "").strip() for s in (data.get("markdown") or {}).get("instructions") or []],
        "organization": seo.get("organization") or {},
        "first_page": _first_nav_page(data),
    }


def _first_nav_page(data: dict) -> Optional[str]:
    """First page id in the default language's first tab, used as a sample."""
    languages = ((data.get("navigation") or {}).get("languages")) or []
    for lang in languages:
        for tab in lang.get("tabs") or []:
            for group in tab.get("groups") or []:
                found = _find_page(group.get("pages") or [])
                if found:
                    return found
    return None


def _find_page(pages: list) -> Optional[str]:
    for entry in pages:
        if isinstance(entry, str):
            return entry
        if isinstance(entry, dict):
            found = _find_page(entry.get("pages") or [])
            if found:
                return found
    return None


# --------------------------------------------------------------------------
# pure analyzers (no network -- unit tested directly)
# --------------------------------------------------------------------------

def analyze_llms_txt(resp: Response, instructions: List[str]) -> List[Finding]:
    out: List[Finding] = []
    out.append(Finding(
        "llms.txt: HTTP 200", resp.status == 200, f"status={resp.status}",
    ))
    # The old SPA answered 200 with its HTML shell: a "fake" llms.txt.
    out.append(Finding(
        "llms.txt: 不是 HTML 兜底页",
        resp.status == 200 and not resp.is_html,
        f"content-type={resp.content_type or '(空)'}",
    ))
    if resp.status != 200 or resp.is_html:
        return out
    body = resp.body
    out.append(Finding(
        "llms.txt: 以站点标题 H1 开头",
        body.lstrip().startswith("# "),
        body.lstrip()[:40].replace("\n", " ") or "(空)",
    ))
    md_links = re.findall(r"\]\(([^)]+\.md)\)", body)
    out.append(Finding(
        "llms.txt: 含 .md 页面链接",
        bool(md_links),
        f"{len(md_links)} 个 .md 链接",
    ))
    # A group's `root` page must not also appear in its `pages`, or Mintlify
    # lists it twice. Verified 2026-09-18: the group header itself navigates to
    # the root page, so the `pages` entry is a pure duplicate (GEO-PLAN G0-11).
    dupes = sorted({link for link in md_links if md_links.count(link) > 1})
    out.append(Finding(
        "llms.txt: 无重复页面条目",
        not dupes,
        (
            f"{len(dupes)} 个链接重复（分组的 `root` 页又列在 `pages` 里，应从 `pages` 移除）: "
            + ", ".join(dupes[:3])
        ) if dupes else "无重复",
    ))
    out.extend(_check_instructions_present(body, instructions, "llms.txt"))
    return out


def analyze_llms_full(resp: Response, instructions: List[str]) -> List[Finding]:
    out: List[Finding] = [
        Finding("llms-full.txt: HTTP 200", resp.status == 200, f"status={resp.status}"),
        Finding(
            "llms-full.txt: 不是 HTML 兜底页",
            resp.status == 200 and not resp.is_html,
            f"content-type={resp.content_type or '(空)'}",
        ),
        Finding(
            "llms-full.txt: 含正文内容",
            resp.status == 200 and len(resp.body) > 10_000,
            f"{len(resp.body)} 字节",
        ),
    ]
    if resp.status == 200 and not resp.is_html:
        out.extend(_check_instructions_present(resp.body, instructions, "llms-full.txt"))
    return out


def analyze_robots(resp: Response) -> List[Finding]:
    body = resp.body if resp.status == 200 else ""
    blocks_root = re.search(r"(?im)^\s*disallow:\s*/\s*$", body) is not None
    return [
        Finding("robots.txt: HTTP 200", resp.status == 200, f"status={resp.status}"),
        Finding(
            "robots.txt: 声明 Sitemap",
            bool(re.search(r"(?im)^\s*sitemap:", body)),
            "找到 Sitemap 指令" if re.search(r"(?im)^\s*sitemap:", body) else "未找到 Sitemap 指令",
        ),
        Finding(
            "robots.txt: 未整站 Disallow",
            not blocks_root,
            "存在 `Disallow: /`，AI bot 会被挡住" if blocks_root else "未整站禁止抓取",
        ),
    ]


def analyze_sitemap(resp: Response) -> List[Finding]:
    body = resp.body if resp.status == 200 else ""
    has_root = ("<urlset" in body) or ("<sitemapindex" in body)
    urls = len(re.findall(r"<loc>", body))
    return [
        Finding("sitemap.xml: HTTP 200", resp.status == 200, f"status={resp.status}"),
        Finding("sitemap.xml: 结构有效", has_root, "含 urlset/sitemapindex" if has_root else "未见 urlset/sitemapindex"),
        Finding("sitemap.xml: 含 URL", urls > 0, f"{urls} 条 <loc>"),
    ]


def analyze_markdown_page(resp: Response, instructions: List[str]) -> List[Finding]:
    out = [
        Finding("页面 .md 端点: HTTP 200", resp.status == 200, f"status={resp.status}"),
        Finding(
            "页面 .md 端点: 返回 Markdown 而非 HTML",
            resp.status == 200 and not resp.is_html,
            f"content-type={resp.content_type or '(空)'}",
        ),
    ]
    if resp.status == 200 and not resp.is_html:
        out.extend(_check_instructions_present(resp.body, instructions, "页面 .md"))
    return out


def analyze_structured_data(page_html: str, organization: Dict[str, object]) -> List[Finding]:
    """Verify the JSON-LD @graph carries the Organization we configured."""
    out: List[Finding] = []
    blocks = LD_JSON_RE.findall(page_html)
    if not blocks:
        return [Finding(
            "JSON-LD: 页面含结构化数据",
            False,
            "未找到 application/ld+json script（托管层才会输出；本地 dev 不输出）",
        )]
    out.append(Finding("JSON-LD: 页面含结构化数据", True, f"{len(blocks)} 个 ld+json 块"))

    nodes: List[dict] = []
    parse_errors: List[str] = []
    for raw in blocks:
        try:
            payload = json.loads(html_mod.unescape(raw.strip()))
        except json.JSONDecodeError as exc:
            parse_errors.append(str(exc))
            continue
        if isinstance(payload, dict) and isinstance(payload.get("@graph"), list):
            nodes.extend(n for n in payload["@graph"] if isinstance(n, dict))
        elif isinstance(payload, list):
            nodes.extend(n for n in payload if isinstance(n, dict))
        elif isinstance(payload, dict):
            nodes.append(payload)

    out.append(Finding("JSON-LD: 可解析", not parse_errors, "; ".join(parse_errors) or "全部解析成功"))
    if parse_errors:
        return out

    types = {t for n in nodes for t in _types_of(n)}
    for wanted in ("Organization", "WebSite", "WebPage"):
        out.append(Finding(f"JSON-LD: 含 {wanted}", wanted in types, "类型齐全" if wanted in types else f"实际类型: {sorted(types)}"))

    org_node = next((n for n in nodes if "Organization" in _types_of(n)), None)
    if org_node is None:
        return out
    for field in ("name", "url"):
        want = organization.get(field)
        if want:
            out.append(Finding(
                f"JSON-LD: Organization.{field}",
                org_node.get(field) == want,
                f"期望 {want!r}，实际 {org_node.get(field)!r}",
            ))
    if organization.get("sameAs"):
        got = set(org_node.get("sameAs") or [])
        want = set(organization["sameAs"])
        out.append(Finding(
            "JSON-LD: Organization.sameAs",
            want <= got,
            f"缺失 {sorted(want - got)}" if want - got else "全部命中",
        ))
    # Mintlify may omit optional fields; report without failing the run.
    for field in ("id", "legalName", "logo"):
        want = organization.get(field)
        if want:
            out.append(Finding(
                f"JSON-LD: Organization.{field}",
                org_node.get(field) == want,
                f"期望 {want!r}，实际 {org_node.get(field)!r}",
                required=False,
            ))
    return out


def _types_of(node: dict) -> List[str]:
    raw = node.get("@type")
    if isinstance(raw, str):
        return [raw]
    if isinstance(raw, list):
        return [t for t in raw if isinstance(t, str)]
    return []


def _check_instructions_present(body: str, instructions: List[str], where: str) -> List[Finding]:
    if not instructions:
        return []
    return [
        Finding(
            f"{where}: 含 Agent Instructions 块",
            "## Agent Instructions" in body,
            "已注入" if "## Agent Instructions" in body else "未见 `## Agent Instructions`",
        ),
        Finding(
            f"{where}: instructions 文案落地",
            instructions[0] in body,
            "首条命中" if instructions[0] in body else "首条未出现（docs.json 已改但站点未重新部署？）",
        ),
    ]


# --------------------------------------------------------------------------
# network + orchestration
# --------------------------------------------------------------------------

DEFAULT_BASE_URL = "https://docs.pawsql.com"


def fetch(url: str, user_agent: Optional[str] = None, timeout: float = 20.0) -> Response:
    """GET a URL; transport failures come back as status 0 so callers can report."""
    request = urllib.request.Request(
        url, headers={"User-Agent": user_agent or "pawsql-doc-geo-check", "Accept": "*/*"}
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as resp:
            return Response(
                status=resp.status,
                content_type=resp.headers.get("Content-Type", "") or "",
                body=resp.read().decode("utf-8", errors="replace"),
                headers=dict(resp.headers),
            )
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace") if hasattr(exc, "read") else ""
        headers = dict(exc.headers) if exc.headers else {}
        return Response(exc.code, headers.get("Content-Type", "") or "", body, headers)
    except (urllib.error.URLError, OSError) as exc:
        return Response(0, "", "", {"error": str(exc)})


def _transport_failed(resp: Response) -> bool:
    return resp.status == 0


def check_geo(root: Path, base_url: str = DEFAULT_BASE_URL, timeout: float = 20.0) -> List[Finding]:
    """Run every G2-1 check against a deployed site."""
    base = base_url.rstrip("/")
    expectations = load_expectations(root)
    instructions: List[str] = list(expectations["instructions"])  # type: ignore[arg-type]
    organization: Dict[str, object] = dict(expectations["organization"])  # type: ignore[arg-type]
    first_page = expectations["first_page"]

    findings: List[Finding] = []

    llms = fetch(f"{base}/llms.txt", timeout=timeout)
    if _transport_failed(llms):
        return [Finding(
            "站点可达",
            False,
            f"无法连接 {base}（{llms.headers.get('error', '未知错误')}）——"
            "站点尚未部署，或本机网络不可达",
        )]
    findings.extend(analyze_llms_txt(llms, instructions))
    findings.extend(analyze_llms_full(fetch(f"{base}/llms-full.txt", timeout=timeout), instructions))
    findings.extend(analyze_robots(fetch(f"{base}/robots.txt", timeout=timeout)))
    findings.extend(analyze_sitemap(fetch(f"{base}/sitemap.xml", timeout=timeout)))

    # The llms.txt spec's .well-known alias must resolve too.
    well_known = fetch(f"{base}/.well-known/llms.txt", timeout=timeout)
    findings.append(Finding(
        "/.well-known/llms.txt: 可达且非 HTML",
        well_known.status == 200 and not well_known.is_html,
        f"status={well_known.status} content-type={well_known.content_type or '(空)'}",
    ))

    if first_page:
        findings.extend(analyze_markdown_page(fetch(f"{base}/{first_page}.md", timeout=timeout), instructions))
        page_html = fetch(f"{base}/{first_page}", timeout=timeout).body
        findings.extend(analyze_structured_data(page_html, organization))
    else:
        findings.append(Finding("样例页", False, "未能从 docs/docs.json 导航中解析出首页 id"))

    # robots.txt policies are the usual cause of an AI bot getting locked out.
    bot = fetch(f"{base}/llms.txt", user_agent=AI_BOT_UA, timeout=timeout)
    findings.append(Finding(
        "AI bot UA 未被拦截",
        bot.status == llms.status and bot.body == llms.body,
        f"GPTBot UA -> status={bot.status}；普通 UA -> status={llms.status}",
    ))
    return findings

