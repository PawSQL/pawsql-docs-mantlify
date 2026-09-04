---
id: contributing-style-guide
title: 风格指南
description: 写作风格、证据要求与 AI Guardrails（设计说明书 §30-§32）
type: reference
product: pawsql-docs
status: draft
owners: [docs-platform]
tags: [content-model, style]
---

# 风格指南

## 总体原则

- 目标读者是数据库工程师与 DBA；直接、具体，避免营销腔。
- 一个页面解决一个意图；先给结论，再给细节。
- 每条事实都要可追溯到 Evidence：Metadata、源码或产品行为。**AI 不负责决定什么是事实**（设计说明书 §48 原则 5）。

## 示例内容标记

尚未与产品核对的种子/示例内容必须：

1. `status: draft`
2. 正文顶部放置生成说明或示例注释，例如生成页顶部由生成器写入：
   `> Generated file. Do not edit by hand — change the source metadata ...`

人工书写页面中的示例数据（规则示例等）若仅为演示，加注 `SAMPLE — 待与产品核对`。

## AI Guardrails（§32）

1. 不得虚构 API、参数、数据库版本支持。
2. 不得虚构性能数据 / benchmark / 客户案例。
3. 不得改变产品语义。
4. 无证据信息标记 `unknown`。
5. 修改已有文档前读取完整上下文；优先最小 Patch。

## SEO 与 LLM 友好写作

站点同时服务 人 / 搜索引擎 / LLM-RAG，页面须“自描述、可引用、可治理”：

1. **`title` / `description` 是检索素材**：`title` ≤ ~60 字符、含核心关键词；`description` 一句话（≤ ~155 字符）、含关键词、点明页面意图。`published` 页必填、人工书写，禁止用“默认/占位”文字（校验器拒绝空值与机器截断）。
2. **一个页面一个意图（single intent）**：每页只回答一个明确问题，H1 与 `description` 对齐；同主题多版本/变体（`-polish`、`_en` 残留、重复编号）是 SEO/RAG 大敌，一律去重为“一份成文 + 中英镜像”。
3. **`status` 是可信度信号**：`draft`/`review` 不进导航、不发布；`published` 页的事实应可回溯到 Evidence（Metadata/源码/产品行为）。AI 检索据此判断“此内容是否可引用”。
4. **镜像配对可校验**：中英两页用 `localeOf` 互指（见 frontmatter），缺失或自指会导致 `hreflang`/canonical 缺失，搜索引擎视为孤立页。
5. **代码块语言标注**：每个代码块显式标注 `sql`/`bash`/`yaml`/`json`，利于代码检索与结构化抽取。
6. **单一事实源**：规则/配置/数据库的正文只存于 `metadata/**`（生成页不手改）；正文中不重复同一事实的多个版本。

## 格式

- 代码块标注语言：`sql`、`bash`、`yaml`、`json`。
- Front Matter 规范见 [frontmatter.md](./frontmatter)。
- 术语用法见 [terminology.md](./terminology)。
