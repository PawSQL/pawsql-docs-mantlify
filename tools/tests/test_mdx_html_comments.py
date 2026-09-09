from __future__ import annotations

from pawsql_doc.validate import validate_frontmatter

FM = """\
---
id: mdx-guard-test
translationKey: mdx-guard-test
language: zh
title: MDX guard test
description: Minimal page used by the MDX HTML-comment guard test.
type: explanation
layout: detail
product: pawsql
status: draft
---
"""


def _write(repo, name, body):
    p = repo / "docs" / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body, encoding="utf-8")
    return p


def test_mdx_html_comment_is_flagged(repo):
    _write(repo, "mdx-guard-bad.mdx", FM + "\nHello <!-- DATABASE_MATRIX:START --> world\n")
    issues = validate_frontmatter(repo)
    assert any(i.file.endswith("mdx-guard-bad.mdx") and "HTML comment" in i.reason for i in issues)


def test_mdx_jsx_comment_and_fenced_html_comment_pass(repo):
    _write(
        repo,
        "mdx-guard-ok.mdx",
        FM
        + "\n{/* valid MDX comment */}\n\n"
        + "```text\n<!-- HTML comment inside a fence is fine -->\n```\n",
    )
    issues = validate_frontmatter(repo)
    assert not any(i.file.endswith("mdx-guard-ok.mdx") for i in issues)
