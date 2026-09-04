---
id: audit-rule-aud-avoid-replicated-distribution-for-large-tables
title: 大表不建议使用复制(Replicated)分布
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 大表（默认超 10 万行）不宜用复制分布（存储与写放大）；应改用 HASH 等分片分布。
localeOf: en-audit-rule-aud-avoid-replicated-distribution-for-large-tables
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-replicated-distribution-for-large-tables |
| 规则名称 | 大表不建议使用复制(Replicated)分布 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

在分布式数据库中，复制分布（Replicated Distribution）会将表的完整数据拷贝到集群的每一个节点上。对于小表而言，这种策略可以消除跨节点数据交换，提升JOIN性能；但对于大表，采用复制分布会显著增加存储开销（存储量 = 原始数据大小 x 节点数），且写入操作需要同步到所有节点，丧失分布式并行计算的优势。
该规则要求当表的数据量超过阈值（默认100,000行）时，不应使用REPLICATED分布方式，而应使用HASH分布或其他分片策略，以确保数据均匀分布在各节点上，充分利用分布式架构的扩展能力。

## 反例

```sql
-- ❌ 不推荐：大表使用复制分布，存储开销高且丧失分布式优势
CREATE TABLE large_table (
    id BIGINT,
    data TEXT
) DISTRIBUTED BY REPLICATION;
```

## 正例

```sql
-- ✅ 推荐：大表使用HASH分布，数据均匀分布在各个节点
CREATE TABLE large_table (
    id BIGINT,
    data TEXT
) DISTRIBUTED BY HASH(id);
```
