---
id: optimizer-rule-opt-joinelimination
title: 表连接消除
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-joinelimination
tags:
- optimizer-rule
- rewrite
description: 连接消除（Join Elimination）通过在不影响最终结果的情况下从查询中删除不必要的表，来简化 SQL 以提高查询性能。通常，当查询包含主键-外键连接且查询中仅引用主表的主键列时，被引用的外表（维度表）可以被消除，从而减少扫描和连接开销。
localeOf: en-optimizer-rule-opt-joinelimination
subtype: rule
language: zh
translationKey: optimizer-rule-opt-joinelimination
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-joinelimination |
| 规则名称 | 表连接消除 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

连接消除（Join Elimination）通过在不影响最终结果的情况下从查询中删除不必要的表，来简化 SQL 以提高查询性能。通常，当查询包含主键-外键连接且查询中仅引用主表的主键列时，被引用的外表（维度表）可以被消除，从而减少扫描和连接开销。
内连接和外连接均可应用此优化。PawSQL 优化引擎会自动检测并执行连接消除重写。

## 反例

```sql
-- ❌ 可优化：内连接的内表仅用于验证外键存在，可被消除
SELECT o.*
FROM orders o
INNER JOIN customer c ON c.c_custkey = o.o_custkey;

-- ❌ 可优化：外连接中仅引用主表列
SELECT o_custkey
FROM orders
LEFT JOIN customer ON c_custkey = o_custkey;
```

## 正例

```sql
-- ✅ 优化后：消除不必要的客户表连接
SELECT *
FROM orders
WHERE o_custkey IS NOT NULL;

-- ✅ 优化后：消除外部连接
SELECT orders.o_custkey FROM orders;
```
