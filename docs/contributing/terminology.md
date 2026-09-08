---
id: contributing-terminology
title: 术语表
description: PawSQL 文档平台与产品使用的统一术语（持续维护）
type: reference
product: pawsql
status: draft
owners:
- docs-platform
tags:
- content-model
- terminology
subtype: glossary
language: zh
translationKey: contributing-terminology
layout: detail
---

# 术语表

写作用词以此表为准；出现冲突时更新本表而不是各自改词。

| 术语 | 含义 |
|---|---|
| PawSQL Optimizer | 优化引擎：代价估算的索引推荐 + 语义级查询重写 |
| Query Rewrite | 语义等价的 SQL 重写（不改变业务结果、改变执行结构） |
| Index Recommendation | 基于 SQL 结构主动设计的推荐索引（非从存量索引中挑选） |
| Audit Rule | SQL 审核规则（对象/DDL/DML/索引/性能等） |
| Optimizer Rule | 优化器使用的重写/优化算法规则 |
| SQL Review | 对 SQL 的规范性/质量审核 |
| Compatibility | 数据库/版本/能力矩阵（`metadata/databases/*.yaml` 单一事实来源） |
| Feature Manifest | 功能清单（`metadata/features/*.yaml`），描述一个功能及其所需文档 |
| Documentation Mapping | 功能→文档映射（`metadata/mappings/*.yaml`） |
| Drift | 产品已变但文档未跟随变化的偏差 |
| Coverage | 必需文档的覆盖统计 |
| Release Gate | 发版前的文档质量闸门（Phase 3 引入） |
| llms.txt | Mintlify 自动提供的站点 AI 清单 |
| MCP | Model Context Protocol（PawSQL 的 AI 工具面） |

## 写法约定

- 数据库名：MySQL、PostgreSQL、Oracle、SQL Server、openGauss（专名首字母大写）。
- 版本号：字符串 `8.5.0`，不写成浮点 `8.5`。
- 产品二进制/命令：`pawsql-optimizer`、`explain.timeout` 用行内代码。
