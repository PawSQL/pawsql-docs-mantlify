---
id: optimizer-rule-opt-winfuncskewedoptimization
title: 窗口分区字段分布不均匀导致数据倾斜
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-winfuncskewedoptimization
tags:
- optimizer-rule
- rewrite
description: 在分布式计算引擎（如 Hive）中，当使用 `ROW_NUMBER()`、`RANK()` 或 `DENSE_RANK()` 等窗口函数时，若
  `PARTITION BY` 字段的数据分布严重不均（如 90% 数据集中在个别分区），会导致计算资源向少数 Task 倾斜，引发性能瓶颈。
localeOf: en-optimizer-rule-opt-winfuncskewedoptimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-winfuncskewedoptimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-winfuncskewedoptimization |
| 规则名称 | 窗口分区字段分布不均匀导致数据倾斜 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式计算引擎（如 Hive）中，当使用 `ROW_NUMBER()`、`RANK()` 或 `DENSE_RANK()` 等窗口函数时，若 `PARTITION BY` 字段的数据分布严重不均（如 90% 数据集中在个别分区），会导致计算资源向少数 Task 倾斜，引发性能瓶颈。
PawSQL 通过自动化优化规则检测此类场景，提供分区字段加盐（salting）+ 二阶段聚合的优化建议，将热点分区的数据分散到多个子分区处理，从而充分利用集群并行计算能力。

## 反例

```sql
-- ❌ 不推荐：按热点字段分区的窗口函数，容易数据倾斜
SELECT *
FROM (
    SELECT c_name, RANK() OVER (
        PARTITION BY region
        ORDER BY c_custkey DESC
    ) rn
    FROM customer
    WHERE c_custkey > 100
) c
WHERE rn < 10;
```

## 正例

```sql
-- ✅ 推荐：分区字段加盐 + 二阶段过滤
WITH local_ranked AS (
    SELECT *
    FROM (
        SELECT c_name,
            RANK() OVER (
                PARTITION BY region, CAST(RAND() * 256 AS INT)
                ORDER BY c_custkey DESC
            ) AS local_rank
        FROM customer
        WHERE c_custkey > 100
    ) AS c
    WHERE c.local_rank < 10
)
SELECT *
FROM (
    SELECT c_name, RANK() OVER (
        PARTITION BY region
        ORDER BY c_custkey DESC
    ) AS rn
    FROM local_ranked
) AS c
WHERE local_ranked.rn < 10;
```
