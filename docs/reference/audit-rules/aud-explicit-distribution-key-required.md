---
id: audit-rule-aud-explicit-distribution-key-required
title: 必须显式的指定分布键
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-explicit-distribution-key-required
tags:
- audit-rule
- ddl
description: 在分布式数据库中，如果建表时未显式指定分布键（`DISTRIBUTED BY` / `SHARDKEY` / `DISTRIBUTE BY`），数据库将采用默认策略（如随机分布或按首列分布）自动选择分布键。这种"隐式"行为看似便捷，实则暗藏风险：自动选择的分布键未必是最优的，可能导致数据分布不均（数据倾斜）、频繁的跨节点数据重分布、以及关键查询退化为全节点扫描，严重影响查询性能与集群稳定性。
localeOf: en-audit-rule-aud-explicit-distribution-key-required
subtype: rule
language: zh
translationKey: audit-rule-aud-explicit-distribution-key-required
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-explicit-distribution-key-required |
| 规则名称 | 必须显式的指定分布键 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式数据库中，如果建表时未显式指定分布键（`DISTRIBUTED BY` / `SHARDKEY` / `DISTRIBUTE BY`），数据库将采用默认策略（如随机分布或按首列分布）自动选择分布键。这种"隐式"行为看似便捷，实则暗藏风险：自动选择的分布键未必是最优的，可能导致数据分布不均（数据倾斜）、频繁的跨节点数据重分布、以及关键查询退化为全节点扫描，严重影响查询性能与集群稳定性。
显式指定分布键，意味着开发者基于业务语义主动声明数据的分布策略，确保数据在各节点间均匀分布、关联操作本地化执行，从而充分利用分布式数据库的并行计算能力。该规则是分布式数据库表设计的核心规范之一。

## 反例

```sql
-- ❌ 不推荐：未显式指定分布键，依赖数据库默认策略
CREATE TABLE orders (
    order_id    BIGINT NOT NULL,
    customer_id BIGINT NOT NULL,
    order_date  DATE   NOT NULL
);
```

## 正例

```sql
-- ✅ 推荐：显式指定分布键（以 openGauss/PostgreSQL-XL 语法为例）
CREATE TABLE orders (
    order_id    BIGINT NOT NULL,
    customer_id BIGINT NOT NULL,
    order_date  DATE   NOT NULL
) DISTRIBUTED BY HASH(order_id);

-- ✅ 推荐：显式指定分布键（以 TDSQL 语法为例）
CREATE TABLE orders (
    order_id    BIGINT NOT NULL,
    customer_id BIGINT NOT NULL,
    order_date  DATE   NOT NULL
) shardkey=order_id;
```
