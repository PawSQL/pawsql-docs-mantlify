---
id: optimizer-rule-opt-union-skew-optimization-in-hive
title: UNION导致的数据倾斜优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-union-skew-optimization-in-hive
tags:
- optimizer-rule
- rewrite
description: 在 Hive 等分布式计算平台中，`UNION` 操作在合并多个数据集的同时需要对结果进行全局去重。这个去重操作可能会被集中到单个 Reducer
  执行，当数据量较大时容易产生数据倾斜，导致单个任务处理时间过长甚至无法完成。
localeOf: en-optimizer-rule-opt-union-skew-optimization-in-hive
subtype: rule
language: zh
translationKey: optimizer-rule-opt-union-skew-optimization-in-hive
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-union-skew-optimization-in-hive |
| 规则名称 | UNION导致的数据倾斜优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 Hive 等分布式计算平台中，`UNION` 操作在合并多个数据集的同时需要对结果进行全局去重。这个去重操作可能会被集中到单个 Reducer 执行，当数据量较大时容易产生数据倾斜，导致单个任务处理时间过长甚至无法完成。
PawSQL 建议使用 `UNION ALL` 代替 `UNION`，然后通过 `GROUP BY` 进行去重。`UNION ALL` 不进行去重操作，避免了单点瓶颈；后续的 `GROUP BY` 去重可以在多个 Reducer 上并行执行，有效缓解数据倾斜问题。
> 此规则适用于 Hive 数据仓库环境。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。

## 反例

```sql
-- ❌ 不推荐：UNION 进行全局去重，可能产生单 Reducer 瓶颈
SELECT user_id FROM table_2024
UNION
SELECT user_id FROM table_2023;
```

## 正例

```sql
-- ✅ 推荐：使用 UNION ALL + GROUP BY，去重操作可并行化
SELECT user_id FROM (
    SELECT user_id FROM table_2024
    UNION ALL
    SELECT user_id FROM table_2023
) t
GROUP BY user_id;
```
