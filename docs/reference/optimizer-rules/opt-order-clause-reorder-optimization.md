---
id: optimizer-rule-opt-order-clause-reorder-optimization
title: ORDER子句重排序优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-order-clause-reorder-optimization
tags:
- optimizer-rule
- index
description: 当一个查询中既包含来自同一个表的 ORDER BY 排序字段也包含 GROUP BY 分组字段，但两者的字段顺序不同时，数据库可能需要进行两次排序（先按分组字段排序，再按
  ORDER BY 字段排序）。如果 ORDER BY 的字段是 GROUP BY 字段的真子集，可以通过调整 GROUP BY 字段的顺序，使其与 ORDER
  BY 字段顺序一致，从而复用一次排序操作，避免重复排序的开销。
localeOf: en-optimizer-rule-opt-order-clause-reorder-optimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-order-clause-reorder-optimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-order-clause-reorder-optimization |
| 规则名称 | ORDER子句重排序优化 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当一个查询中既包含来自同一个表的 ORDER BY 排序字段也包含 GROUP BY 分组字段，但两者的字段顺序不同时，数据库可能需要进行两次排序（先按分组字段排序，再按 ORDER BY 字段排序）。如果 ORDER BY 的字段是 GROUP BY 字段的真子集，可以通过调整 GROUP BY 字段的顺序，使其与 ORDER BY 字段顺序一致，从而复用一次排序操作，避免重复排序的开销。
PawSQL 自动检测此类模式，在确保语义等价的前提下（GROUP BY 中不包含高级 grouping 操作），调整分组字段顺序以匹配排序字段顺序，消除冗余排序。

## 反例

```sql
-- ❌ 不推荐：GROUP BY 与 ORDER BY 的字段顺序不一致，需要两次排序
SELECT o_custkey, o_orderdate, SUM(o_totalprice)
FROM orders
GROUP BY o_custkey, o_orderdate
ORDER BY o_orderdate;
```

## 正例

```sql
-- ✅ 推荐：调整 GROUP BY 字段顺序，与 ORDER BY 保持一致
SELECT o_custkey, o_orderdate, SUM(o_totalprice)
FROM orders
GROUP BY o_orderdate, o_custkey
ORDER BY o_orderdate;
```
