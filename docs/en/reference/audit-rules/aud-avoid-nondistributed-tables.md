---
id: en-audit-rule-aud-avoid-nondistributed-tables
title: Avoid Non-Distributed Tables
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 在分布式数据库中，非分布表（如 `DISTRIBUTED BY LOCAL`）的数据仅存储在单个节点上，容易成为性能瓶颈和单点故障。当多个查询同时访问该表时，所有请求都会集中到一个节点，无法充分利用分布式架构的并行计算能力。
localeOf: audit-rule-aud-avoid-nondistributed-tables
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-nondistributed-tables |
| Name | Avoid Non-Distributed Tables |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

在分布式数据库中，非分布表（如 `DISTRIBUTED BY LOCAL`）的数据仅存储在单个节点上，容易成为性能瓶颈和单点故障。当多个查询同时访问该表时，所有请求都会集中到一个节点，无法充分利用分布式架构的并行计算能力。
此外，非分布表与分布表进行关联操作时，通常需要将分布表的数据重分布到非分布表所在的节点，产生大量的网络传输开销。建议所有业务表均使用合理的分布策略，充分利用分布式数据库的水平扩展优势。

## Bad Example

```sql
-- ❌ 不推荐：在分布式环境中创建本地表/非分布表
CREATE TABLE large_table (
    id   BIGINT,
    data TEXT
) DISTRIBUTED BY LOCAL;
```

## Good Example

```sql
-- ✅ 推荐：使用 HASH 分布，数据均匀分散到各节点
CREATE TABLE large_table (
    id   BIGINT,
    data TEXT
) DISTRIBUTED BY HASH (id);
```
