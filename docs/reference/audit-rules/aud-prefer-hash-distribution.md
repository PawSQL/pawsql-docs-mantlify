---
id: audit-rule-aud-prefer-hash-distribution
title: 分布方式建议使用 HASH 分布
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-prefer-hash-distribution
tags:
- audit-rule
- ddl
description: 哈希分布（HASH distribution）通过哈希函数将数据均匀分散到各个节点，避免数据倾斜，是分布式数据库最推荐的分布方式。相较于
  RANGE 分布可能导致数据的冷热不均、LIST 分布依赖于有限枚举值、以及 ROUND-ROBIN 分布完全不考虑数据亲和性，HASH 分布能够在数据均匀性、查询路由效率、以及关联操作的本地化之间取得最佳平衡。
localeOf: en-audit-rule-aud-prefer-hash-distribution
subtype: rule
language: zh
translationKey: audit-rule-aud-prefer-hash-distribution
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-prefer-hash-distribution |
| 规则名称 | 分布方式建议使用 HASH 分布 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

哈希分布（HASH distribution）通过哈希函数将数据均匀分散到各个节点，避免数据倾斜，是分布式数据库最推荐的分布方式。相较于 RANGE 分布可能导致数据的冷热不均、LIST 分布依赖于有限枚举值、以及 ROUND-ROBIN 分布完全不考虑数据亲和性，HASH 分布能够在数据均匀性、查询路由效率、以及关联操作的本地化之间取得最佳平衡。
选择 HASH 分布可以确保数据在各节点间均匀分布，减少跨节点数据重分布，提升查询性能并实现负载均衡。

## 反例

```sql
-- ❌ 不推荐：使用 ROUND-ROBIN 分布，关联操作无法本地化
CREATE TABLE t_orders (
    order_id    BIGINT,
    customer_id BIGINT
) DISTRIBUTED BY ROUNDROBIN;
```

## 正例

```sql
-- ✅ 推荐：使用 HASH 分布，确保数据均匀分散和关联本地化
CREATE TABLE t_orders (
    order_id    BIGINT,
    customer_id BIGINT
) DISTRIBUTED BY HASH (order_id);
```
