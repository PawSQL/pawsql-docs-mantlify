---
id: en-audit-rule-aud-cacheexhausted4identitycolumn
title: CacheExhausted4IdentityColumn
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 当自增列的当前值接近其数据类型的最大值时，序列即将耗尽，后续的 INSERT 操作将失败并抛出主键冲突或溢出错误。这在高频写入的核心业务表中尤其致命，可能导致服务中断。
localeOf: audit-rule-aud-cacheexhausted4identitycolumn
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-cacheexhausted4identitycolumn |
| Name | CacheExhausted4IdentityColumn |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

当自增列的当前值接近其数据类型的最大值时，序列即将耗尽，后续的 INSERT 操作将失败并抛出主键冲突或溢出错误。这在高频写入的核心业务表中尤其致命，可能导致服务中断。
建议通过监控预警及时发现序列耗尽风险，并根据使用率提前规划扩容方案（如升级数据类型，从 INT 扩展至 BIGINT）。默认预警阈值为最大值的 80%，可通过配置调整。
