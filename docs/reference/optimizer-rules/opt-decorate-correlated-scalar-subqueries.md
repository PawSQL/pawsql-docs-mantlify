---
id: optimizer-rule-opt-decorate-correlated-scalar-subqueries
title: 条件标量子查询解关联
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-decorate-correlated-scalar-subqueries
tags:
- optimizer-rule
- rewrite
description: 标量子查询返回单行单列的一个值，它可以出现在SQL语句中任何单值出现的位置。对于出现在WHERE和HAVING子句中的相关标量子查询，数据库通常对外部表的每一行都要执行一次子查询，形成嵌套循环执行模式，当外部表行数较多时性能极差。
localeOf: en-optimizer-rule-opt-decorate-correlated-scalar-subqueries
subtype: rule
language: zh
translationKey: optimizer-rule-opt-decorate-correlated-scalar-subqueries
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-decorate-correlated-scalar-subqueries |
| 规则名称 | 条件标量子查询解关联 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

标量子查询返回单行单列的一个值，它可以出现在SQL语句中任何单值出现的位置。对于出现在WHERE和HAVING子句中的相关标量子查询，数据库通常对外部表的每一行都要执行一次子查询，形成嵌套循环执行模式，当外部表行数较多时性能极差。
PawSQL优化器尝试对相关标量子查询进行解关联——将标量子查询转换为派生表，通过GROUP BY和JOIN的方式重写SQL，使子查询只需执行一次，再与外部表进行关联。PawSQL的代价模型会自动评估解关联后的代价是否更低，仅在优化有益时才触发此重写。

## 正例

```sql
-- ✅ 优化前：相关标量子查询，对外部表每一行执行一次
SELECT c_custkey
FROM CUSTOMER
WHERE 1000000 < (SELECT SUM(o_totalprice)
                 FROM ORDERS
                 WHERE o_custkey = c_custkey
                   AND o_orderdate = '2020-04-16');

-- ✅ 优化后：解关联为派生表+JOIN，子查询仅执行一次
SELECT c_custkey
FROM CUSTOMER, (
    SELECT SUM(o_totalprice) AS SUM_, o_custkey
    FROM ORDERS
    WHERE o_orderdate = CAST('2020-04-16' AS DATE)
    GROUP BY o_custkey
) AS SQ
WHERE 1000000 < SUM_ AND o_custkey = CUSTOMER.c_custkey;
```
