---
id: optimizer-rule-opt-maxmin-subquery-rewrite
title: MAX/MIN子查询重写
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-maxmin-subquery-rewrite
tags:
- optimizer-rule
- rewrite
description: 对于使用 `MAX`/`MIN` 聚合函数的标量子查询（如 `WHERE col = (SELECT MAX(col) FROM ...)`），PawSQL
  将其重写为 `ORDER BY + LIMIT 1` 的形式。这种重写可以利用列上索引的有序性，通过索引扫描直接定位极值记录，避免全表聚集运算，大幅降低 I/O
  和计算开销。
localeOf: en-optimizer-rule-opt-maxmin-subquery-rewrite
subtype: rule
language: zh
translationKey: optimizer-rule-opt-maxmin-subquery-rewrite
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-maxmin-subquery-rewrite |
| 规则名称 | MAX/MIN子查询重写 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于使用 `MAX`/`MIN` 聚合函数的标量子查询（如 `WHERE col = (SELECT MAX(col) FROM ...)`），PawSQL 将其重写为 `ORDER BY + LIMIT 1` 的形式。这种重写可以利用列上索引的有序性，通过索引扫描直接定位极值记录，避免全表聚集运算，大幅降低 I/O 和计算开销。
例如，`WHERE c_custkey = (SELECT MAX(o_custkey) FROM orders)` 可重写为 `WHERE c_custkey = (SELECT o_custkey FROM orders ORDER BY o_custkey DESC LIMIT 1)`，数据库可利用 `o_custkey` 上的索引直接返回第一条记录。

## 反例

```sql
-- ❌ 不推荐：MAX 标量子查询需要全表聚集运算
SELECT * FROM customer
WHERE c_custkey = (SELECT MAX(o_custkey) FROM orders);
```

## 正例

```sql
-- ✅ 推荐（PostgreSQL/Oracle）：利用索引有序性，避免聚集运算
SELECT * FROM customer
WHERE c_custkey = (SELECT o_custkey FROM orders ORDER BY o_custkey DESC NULLS LAST LIMIT 1);

-- ✅ 推荐（MySQL）：同样利用索引有序性
SELECT * FROM customer
WHERE c_custkey = (SELECT o_custkey FROM orders ORDER BY o_custkey DESC LIMIT 1);
```
