---
id: en-audit-rule-aud-avoid-replicated-distribution-for-large-tables
title: Avoid Replicated Distribution for Large Tables
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 在分布式数据库中，复制分布（Replicated Distribution）会将表的完整数据拷贝到集群的每一个节点上。对于小表而言，这种策略可以消除跨节点数据交换，提升JOIN性能；但对于大表，采用复制分布会显著增加存储开销（存储量
  = 原始数据大小 x 节点数），且写入操作需要同步到所有节点，丧失分布式并行计算的优势。
localeOf: audit-rule-aud-avoid-replicated-distribution-for-large-tables
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-replicated-distribution-for-large-tables |
| Name | Avoid Replicated Distribution for Large Tables |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

在分布式数据库中，复制分布（Replicated Distribution）会将表的完整数据拷贝到集群的每一个节点上。对于小表而言，这种策略可以消除跨节点数据交换，提升JOIN性能；但对于大表，采用复制分布会显著增加存储开销（存储量 = 原始数据大小 x 节点数），且写入操作需要同步到所有节点，丧失分布式并行计算的优势。
该规则要求当表的数据量超过阈值（默认100,000行）时，不应使用REPLICATED分布方式，而应使用HASH分布或其他分片策略，以确保数据均匀分布在各节点上，充分利用分布式架构的扩展能力。

## Bad Example

```sql
-- ❌ 不推荐：大表使用复制分布，存储开销高且丧失分布式优势
CREATE TABLE large_table (
    id BIGINT,
    data TEXT
) DISTRIBUTED BY REPLICATION;
```

## Good Example

```sql
-- ✅ 推荐：大表使用HASH分布，数据均匀分布在各个节点
CREATE TABLE large_table (
    id BIGINT,
    data TEXT
) DISTRIBUTED BY HASH(id);
```
