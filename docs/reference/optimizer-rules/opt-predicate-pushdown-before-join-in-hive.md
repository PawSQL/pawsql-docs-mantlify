---
id: optimizer-rule-opt-predicate-pushdown-before-join-in-hive
title: Hive中过滤谓词下推到表关联之前计算
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-predicate-pushdown-before-join-in-hive
tags:
- optimizer-rule
- rewrite
description: 在 Hive 查询中，WHERE 条件中的过滤谓词应该尽可能在 JOIN 操作之前执行，这样可以显著减少参与关联的数据量，降低 Shuffle
  阶段的网络传输和磁盘 I/O 开销，从而提升 JOIN 性能。然而，Hive 优化器并非总能自动将过滤条件下推到正确的执行阶段。
localeOf: en-optimizer-rule-opt-predicate-pushdown-before-join-in-hive
subtype: rule
language: zh
translationKey: optimizer-rule-opt-predicate-pushdown-before-join-in-hive
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-predicate-pushdown-before-join-in-hive |
| 规则名称 | Hive中过滤谓词下推到表关联之前计算 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 Hive 查询中，WHERE 条件中的过滤谓词应该尽可能在 JOIN 操作之前执行，这样可以显著减少参与关联的数据量，降低 Shuffle 阶段的网络传输和磁盘 I/O 开销，从而提升 JOIN 性能。然而，Hive 优化器并非总能自动将过滤条件下推到正确的执行阶段。
PawSQL 自动识别此类模式，将 JOIN 后仅涉及单表的过滤条件下推到对应的表扫描阶段，或在子查询中预先过滤，确保 JOIN 操作处理的是尽可能小的数据量。
> 此规则适用于 Hive 数据仓库环境。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。遵循此规则可以显著减少作业执行时间，避免数据倾斜导致的任务失败。

## 反例

```sql
-- ❌ 不推荐：过滤条件在 JOIN 之后全局执行，参与 JOIN 的数据量过大
SELECT *
FROM orders o
JOIN products p ON o.product_id = p.product_id
WHERE o.order_date >= '2024-01-01'
  AND p.category = 'electronics';
```

## 正例

```sql
-- ✅ 推荐：在子查询中先过滤各表，减少 JOIN 数据量
SELECT *
FROM (SELECT * FROM orders WHERE order_date >= '2024-01-01') o
JOIN (SELECT * FROM products WHERE category = 'electronics') p
ON o.product_id = p.product_id;
```
