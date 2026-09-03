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

## 格式

- 代码块标注语言：`sql`、`bash`、`yaml`、`json`。
- Front Matter 规范见 [frontmatter.md](./frontmatter)。
- 术语用法见 [terminology.md](./terminology)。
