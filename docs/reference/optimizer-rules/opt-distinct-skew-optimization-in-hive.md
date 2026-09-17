---
id: optimizer-rule-opt-distinct-skew-optimization-in-hive
title: HIVE中DISTINCT导致的数据倾斜优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-distinct-skew-optimization-in-hive
tags:
- optimizer-rule
- rewrite
description: 在 Hive 计算引擎中，`DISTINCT` 操作需要对数据进行全局去重。当去重字段分布不均匀时，会导致某些 Reducer 处理的数据量远大于其他
  Reducer，形成数据倾斜，严重拖慢整体作业执行时间。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。
localeOf: en-optimizer-rule-opt-distinct-skew-optimization-in-hive
subtype: rule
language: zh
translationKey: optimizer-rule-opt-distinct-skew-optimization-in-hive
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-distinct-skew-optimization-in-hive |
| 规则名称 | HIVE中DISTINCT导致的数据倾斜优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 Hive 计算引擎中，`DISTINCT` 操作需要对数据进行全局去重。当去重字段分布不均匀时，会导致某些 Reducer 处理的数据量远大于其他 Reducer，形成数据倾斜，严重拖慢整体作业执行时间。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。
PawSQL 自动识别此类模式，将 `SELECT DISTINCT` 重写为等效的 `GROUP BY` 形式，使去重操作分布在多个 Reducer 上并行执行，避免数据倾斜导致的单点瓶颈。
> 此规则适用于 Hive 数据仓库环境。遵循此规则可以显著减少作业执行时间，避免数据倾斜导致的任务失败。

## 反例

```sql
-- ❌ 不推荐：DISTINCT 全局去重，可能导致数据倾斜
SELECT DISTINCT customer_id, product_category
FROM sales_table;
```

## 正例

```sql
-- ✅ 推荐：重写为 GROUP BY，并行化去重
SELECT customer_id, product_category
FROM sales_table
GROUP BY customer_id, product_category;
```
