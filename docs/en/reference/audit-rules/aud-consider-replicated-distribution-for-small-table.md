---
id: en-audit-rule-aud-consider-replicated-distribution-for-small-table
title: Consider Replicated Distribution for Small Tables
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 在分布式数据库环境中，表的数据分布方式（分片表或复制表）对查询性能有显著影响。当分布表（Sharding Table）的数据量较小时，若继续采用分片存储，在与其他表进行关联查询时（尤其是非等值关联），可能因跨节点数据交换而导致性能下降。相反，将这些小表设计为复制表（Replicated
  Table），即将完整数据复制到每个节点，可以避免跨节点数据交换，从而提升查询性能。
localeOf: audit-rule-aud-consider-replicated-distribution-for-small-table
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-consider-replicated-distribution-for-small-table |
| Name | Consider Replicated Distribution for Small Tables |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | All supported databases |

## Description

在分布式数据库环境中，表的数据分布方式（分片表或复制表）对查询性能有显著影响。当分布表（Sharding Table）的数据量较小时，若继续采用分片存储，在与其他表进行关联查询时（尤其是非等值关联），可能因跨节点数据交换而导致性能下降。相反，将这些小表设计为复制表（Replicated Table），即将完整数据复制到每个节点，可以避免跨节点数据交换，从而提升查询性能。
该规则检查查询语句中涉及多表关联的场景，通过分析关联条件和表的行数，自动识别出适合改造为复制表的小表。建议对数据量在10万行以下且读多写少的表采用复制表策略。

## Bad Example

```sql
-- ❌ 不推荐：小表t1采用分片分布，非等值关联导致跨节点数据传输
SELECT * FROM t1, t2 WHERE t1.amount > t2.threshold;
```

## Good Example

```sql
-- ✅ 建议：将t1设计为复制表，消除跨节点数据传输
-- (t1改为：CREATE TABLE t1 (...) DISTRIBUTED BY REPLICATION;)
```
