---
id: optimizer-rule-opt-projection-pushdown
title: 投影下推(PROJECTION PUSHDOWN)
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-projection-pushdown
tags:
- optimizer-rule
- rewrite
description: 投影下推（Projection Pushdown）指的是通过删除派生表（Derived Table）、CTE或视图子查询中外层查询未使用的列，来减少不必要的IO和网络传输代价。同时，删除无用列后，优化器在进行表访问规划时，有更大概率选择"无需回表"的覆盖索引扫描（Index-Only
  Scan），进一步提升查询性能。
localeOf: en-optimizer-rule-opt-projection-pushdown
subtype: rule
language: zh
translationKey: optimizer-rule-opt-projection-pushdown
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-projection-pushdown |
| 规则名称 | 投影下推(PROJECTION PUSHDOWN) |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

投影下推（Projection Pushdown）指的是通过删除派生表（Derived Table）、CTE或视图子查询中外层查询未使用的列，来减少不必要的IO和网络传输代价。同时，删除无用列后，优化器在进行表访问规划时，有更大概率选择"无需回表"的覆盖索引扫描（Index-Only Scan），进一步提升查询性能。
该优化是查询重写的关键技术之一。许多数据库（如MySQL 5.7+、PostgreSQL 14.0+）已在优化器内部支持部分投影下推优化；但PawSQL的投影下推覆盖更广泛的场景，包括跨查询块的列级分析。

## 正例

```sql
-- ✅ 优化前：派生表中计算了avg(age)，但外层未使用，造成不必要的计算和IO
SELECT count(1) FROM (SELECT c_custkey, avg(age) FROM customer GROUP BY c_custkey) AS derived_t1;

-- ✅ 优化后：投影下推，消除无用列，减少数据访问量
SELECT count(1) FROM (SELECT 1 FROM customer GROUP BY c_custkey) AS derived_t1;
```
