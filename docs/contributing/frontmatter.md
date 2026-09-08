---
id: contributing-frontmatter
title: Front Matter 规范
description: 页面 Front Matter 字段定义与内容状态约定（对应设计说明书 §7）
type: guide
product: pawsql
status: approved
owners:
- docs-platform
tags:
- content-model
- frontmatter
language: zh
translationKey: contributing-frontmatter
layout: detail
subtype: operation
---

# Front Matter 规范

每篇 `docs/**/*.md(x)` 与 `blog/**/*.md(x)` 页面都必须以 `---` Front Matter 开头。模型与校验在 `tools/src/pawsql_doc/models/core.py`，JSON Schema 导出到 `schemas/frontmatter.schema.json`。

## 字段

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | 是 | 稳定、URL 安全的页面唯一 id（语言约定见下） |
| `title` | 是 | 页面标题；含关键词、≤ ~60 字符（搜索引擎截断阈值） |
| `description` | 是* | 一句话摘要；`published` 页**必填**、人工书写、含检索关键词、≤ ~155 字符（搜索引擎截断阈值）。用于 SEO meta 与 LLM/RAG 检索质量（设计说明书 §29）。生成页由生成器取 metadata 各语言的 `summary`（无则取正文首行且 ≤ 200 字符），不机器截断 |
| `type` | 是 | 文档类型，见下表 |
| `product` | 否 | 所属产品 id（引用 `metadata/products/*.yaml` 的 `id`） |
| `versionIntroduced` | 否 | 首次出现的版本 |
| `status` | 是 | 内容状态，见下表；`published/approved` 才允许入 `docs.json` 导航 |
| `tags` | 否 | 标签数组 |
| `owners` | 否 | 维护团队 |
| `lastReviewed` | 否 | 上次人工复核日期 |
| `reviewCycle` | 否 | 复核周期（天） |
| `relatedFeatures` | 否 | 关联 Feature id（引用 Feature Manifest） |
| `localeOf` | 否 | 镜像配对：本页为另一语言页的翻译时，填对应语言页的 `id`（如 en 页 `localeOf: <zh 页 id>`）；校验成对存在且不指向自身 |
| `keywords` / `aliases` | 否 | 检索别名数组；用于规则英文名 ↔ 中文名、旧术语 ↔ 新术语的检索桥 |
| `category` | 否 | 受控分类词表，见下 |

## 文档类型（`type`）

`product` · `user-guide` · `tutorial` · `reference` · `faq` · `troubleshooting` · `release-note` · `blog`

## 内容状态（`status`）

`draft` → `review` → `approved` → `scheduled` → `published` → `archived`

未与产品核对、不可直接发布的内容使用 `draft`，并在正文顶部加示例标记（见 style-guide）。

## 语言与 id 约定

站点以**中文为默认语言**（内容根 `docs/`，路由 `/…`）；英文为镜像副语言（`docs/en/`，路由 `/en/…`）。对应约定：

- 默认语言（zh）页 `id` 中性无前缀；英文镜像页 `id` 用 `en-` 前缀，并以 `localeOf` 指向中文页 id。
- 生成页已按本节落地：zh 默认页 id 中性（如 `audit-rule-aud-pk-naming`）、en 镜像页 `en-` 前缀（如 `en-audit-rule-aud-pk-naming`），两页互写 `localeOf`（见 `CONTENT-MODEL-CHANGES.md` A1/A2）。
- 同一主题的中英两页互为镜像，必须成对校验（`localeOf` 存在且指向彼此，禁止自指）。

## 受控分类词表（`category`）

规则/配置类页面用受控短词，取值需落在枚举内（未知值校验报错）：

`ddl` · `dml` · `index` · `rewrite` · `join` · `subquery` · `null` · `union` · `predicate` · `constant` · `unknown`

词表最终定稿以 `CONTENT-MODEL-CHANGES.md` A3 为准；`unknown` 仅作待产品确认的临时占位，不进入发布。

## 导航 = 发布

`docs.json` 导航只收录 `status: published`（或经产品确认的 `approved`）页面；`draft`/`review` 仅存在于分支或本地，不进生产导航、不被抓取。发布前校验器会核对导航与 `status` 的一致性。

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
keywords: [OR-to-UNION, 谓词改写, union-rewrite]
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
