---
id: optimizer-rule-opt-anysomeall-subquery-rewrite-optimization
title: 修饰子查询重写优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-anysomeall-subquery-rewrite-optimization
tags:
- optimizer-rule
- rewrite
description: '`ANY`/`SOME`/`ALL` 修饰的子查询源自 SQL-92 标准，通常用于检查某个值与子查询返回的全部值或任意值的大小关系（如
  `x < ALL(subquery)` 或 `x > ANY(subquery)`）。使用这类修饰子查询的执行效率低下，因为数据库需要对子查询的结果集逐行进行比较，随着结果集大小的增加，性能线性下降。'
localeOf: en-optimizer-rule-opt-anysomeall-subquery-rewrite-optimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-anysomeall-subquery-rewrite-optimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-anysomeall-subquery-rewrite-optimization |
| 规则名称 | 修饰子查询重写优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`ANY`/`SOME`/`ALL` 修饰的子查询源自 SQL-92 标准，通常用于检查某个值与子查询返回的全部值或任意值的大小关系（如 `x < ALL(subquery)` 或 `x > ANY(subquery)`）。使用这类修饰子查询的执行效率低下，因为数据库需要对子查询的结果集逐行进行比较，随着结果集大小的增加，性能线性下降。
通过查询重写可以将 `ANY`/`SOME`/`ALL` 修饰的子查询转换为等价的 `MIN`/`MAX` 聚合子查询，配合 `LIMIT` 可以有效利用索引加速。PawSQL 支持针对 MySQL、PostgreSQL、Oracle 等不同数据库自动生成最优的重写方案。

## 反例

```sql
-- ❌ 优化前：ALL 修饰的子查询，需要逐行比较
SELECT *
FROM orders
WHERE o_orderdate < ALL (
    SELECT o_orderdate FROM orders WHERE o_custkey > 100
);
```

## 正例

```sql
-- ✅ 优化后（MySQL）：重写为 MIN + LIMIT，利用索引加速
SELECT *
FROM orders
WHERE o_orderdate < (
    SELECT o_orderdate
    FROM orders
    WHERE o_custkey > 100
    ORDER BY o_orderdate ASC
    LIMIT 1
);
```
