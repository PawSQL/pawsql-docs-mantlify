---
id: optimizer-rule-opt-data-skew-optimization-for-aggregate-without-gro
title: 无分组的聚集函数导致的数据倾斜优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-data-skew-optimization-for-aggregate-without-gro
tags:
- optimizer-rule
- rewrite
description: 在Hive中，不带GROUP BY的聚集函数（如COUNT、SUM、AVG等）会将所有数据汇聚到单个Reducer进行计算。当数据量较大时，单个Reducer需要处理海量数据，产生严重的性能瓶颈——其他Reducer处于空闲状态，而唯一的Reducer成为整个作业的堵点。
localeOf: en-optimizer-rule-opt-data-skew-optimization-for-aggregate-without-gro
subtype: rule
language: zh
translationKey: optimizer-rule-opt-data-skew-optimization-for-aggregate-without-gro
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-data-skew-optimization-for-aggregate-without-gro |
| 规则名称 | 无分组的聚集函数导致的数据倾斜优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在Hive中，不带GROUP BY的聚集函数（如COUNT、SUM、AVG等）会将所有数据汇聚到单个Reducer进行计算。当数据量较大时，单个Reducer需要处理海量数据，产生严重的性能瓶颈——其他Reducer处于空闲状态，而唯一的Reducer成为整个作业的堵点。
该优化通过两阶段聚合策略来解决此问题：第一阶段使用随机数分组（如`GROUP BY CAST(RAND() * 256 AS INT)`），将数据分散到多个Reducer进行局部聚合；第二阶段再进行全局聚合，汇总局部结果。PawSQL for Hive引擎提供针对此问题的自动重写优化建议。

## 反例

```sql
-- ❌ 不推荐：无GROUP BY的聚集函数，所有数据汇聚到单个Reducer
SELECT customer_type,
       COUNT(*) AS order_count,
       SUM(order_amount) AS total_amount,
       AVG(order_amount) AS avg_amount,
       MAX(order_amount) AS max_amount
FROM orders;
```

## 正例

```sql
-- ✅ 推荐：两阶段聚合，先局部聚合再全局汇总，分散计算压力
SELECT customer_type,
       SUM(count_) AS order_count,
       SUM(sum_) AS total_amount,
       SUM(sum_) / SUM(count_) AS avg_amount,
       MAX(max_) AS max_amount
FROM (
    SELECT customer_type,
           COUNT(*) AS count_,
           SUM(order_amount) AS sum_,
           MAX(order_amount) AS max_
    FROM orders
    GROUP BY CAST(RAND() * 256 AS INT)
) DT_123
GROUP BY customer_type;
```
