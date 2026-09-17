---
id: optimizer-rule-opt-countdistinct-skew-optimization-in-hive
title: HIVE中COUNT(DISTINCT...) 导致数据倾斜优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-countdistinct-skew-optimization-in-hive
tags:
- optimizer-rule
- rewrite
description: 在 Hive 计算引擎中，`COUNT(DISTINCT column)` 操作需要将所有数据汇聚到单个 Reducer 进行去重计算。当去重字段的基数较大或数据分布不均匀时，该
  Reducer 的处理时间会远超其他任务，形成数据倾斜。严重时可能导致单个任务执行时间过长甚至任务失败。
localeOf: en-optimizer-rule-opt-countdistinct-skew-optimization-in-hive
subtype: rule
language: zh
translationKey: optimizer-rule-opt-countdistinct-skew-optimization-in-hive
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-countdistinct-skew-optimization-in-hive |
| 规则名称 | HIVE中COUNT(DISTINCT...) 导致数据倾斜优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 Hive 计算引擎中，`COUNT(DISTINCT column)` 操作需要将所有数据汇聚到单个 Reducer 进行去重计算。当去重字段的基数较大或数据分布不均匀时，该 Reducer 的处理时间会远超其他任务，形成数据倾斜。严重时可能导致单个任务执行时间过长甚至任务失败。
PawSQL 自动识别此类模式，将 `COUNT(DISTINCT column)` 重写为 `SELECT COUNT(*) FROM (SELECT column FROM table GROUP BY column) t` 的形式。重写后，去重操作被分解为两阶段：首先通过 GROUP BY 在多个 Reducer 上并行去重，再由最终的 COUNT 汇总结果，有效避免单点瓶颈。
> 此规则适用于 Hive 数据仓库环境。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。遵循此规则可以显著减少作业执行时间，避免数据倾斜导致的任务失败。

## 反例

```sql
-- ❌ 不推荐：COUNT(DISTINCT) 将所有去重数据汇聚到单个 Reducer
SELECT COUNT(DISTINCT customer_id) FROM large_transaction_table;
```

## 正例

```sql
-- ✅ 推荐：重写为两阶段去重，并行化计算
SELECT COUNT(*) FROM (
    SELECT customer_id
    FROM large_transaction_table
    GROUP BY customer_id
) t;
```
