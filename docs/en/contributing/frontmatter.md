---
id: contributing-frontmatter
title: Front Matter 规范
description: 页面 Front Matter 字段定义与内容状态约定（对应设计说明书 §7）
type: reference
product: pawsql-docs
status: approved
owners: [docs-platform]
tags: [content-model, frontmatter]
---

# Front Matter 规范

每篇 `docs/**/*.md(x)` 与 `blog/**/*.md(x)` 页面都必须以 `---` Front Matter 开头。模型与校验在 `tools/src/pawsql_doc/models/core.py`，JSON Schema 导出到 `schemas/frontmatter.schema.json`。

## 字段

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | 稳定、URL 安全的页面唯一 id |
| `title` | 是 | 页面标题 |
| `description` | 否 | 一句话摘要；同时用于 AI 检索质量（设计说明书 §29） |
| `type` | 是 | 文档类型，见下表 |
| `product` | 否 | 所属产品 id（引用 `metadata/products/*.yaml` 的 `id`） |
| `versionIntroduced` | 否 | 首次出现的版本 |
| `status` | 是 | 内容状态，见下表 |
| `tags` | 否 | 标签数组 |
| `owners` | 否 | 维护团队 |
| `lastReviewed` | 否 | 上次人工复核日期 |
| `reviewCycle` | 否 | 复核周期（天） |
| `relatedFeatures` | 否 | 关联 Feature id（引用 Feature Manifest） |

## 文档类型（`type`）

`product` · `user-guide` · `tutorial` · `reference` · `faq` · `troubleshooting` · `release-note` · `blog`

## 内容状态（`status`）

`draft` → `review` → `approved` → `scheduled` → `published` → `archived`

未与产品核对、不可直接发布的内容使用 `draft`，并在正文顶部加示例标记（见 style-guide）。

## 示例

```yaml
---
id: optimizer-or-union
title: OR to UNION Optimization
description: Rewrite OR predicates into UNION or UNION ALL
type: user-guide
product: pawsql-optimizer
versionIntroduced: 8.5.0
status: draft
tags: [optimizer, rewrite]
owners: [optimizer-team]
lastReviewed: 2026-09-01
reviewCycle: 180
relatedFeatures: [OPT-OR-UNION]
---
```

## 校验

```bash
cd tools
uv run python -m pawsql_doc validate-frontmatter
```
