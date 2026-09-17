---
id: optimizer-rule-opt-scalar-subquery-unnesting-in-select-list
title: 选择列标量子查询解关联
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-scalar-subquery-unnesting-in-select-list
tags:
- optimizer-rule
- rewrite
description: 标量子查询返回单行单列的值，它可以出现在 SQL 中任何单值出现的地方。对于 SELECT 列表中出现的相关标量子查询，数据库通常需要为外层查询的每一行执行一次子查询，这种"逐行执行"的模式在大数据量场景下性能极差。
localeOf: en-optimizer-rule-opt-scalar-subquery-unnesting-in-select-list
subtype: rule
language: zh
translationKey: optimizer-rule-opt-scalar-subquery-unnesting-in-select-list
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-scalar-subquery-unnesting-in-select-list |
| 规则名称 | 选择列标量子查询解关联 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

标量子查询返回单行单列的值，它可以出现在 SQL 中任何单值出现的地方。对于 SELECT 列表中出现的相关标量子查询，数据库通常需要为外层查询的每一行执行一次子查询，这种"逐行执行"的模式在大数据量场景下性能极差。
PawSQL 会尝试对选择列表中的相关标量子查询进行解关联，将其重写为 LEFT JOIN + GROUP BY 的形式，使得一次批量关联即可完成计算。同时，如果主体结构相似的多个标量子查询出现在同一选择列表中，PawSQL 在解关联时会将其合并为一个派生表，进一步减少重复计算。

## 反例

```sql
-- ❌ 不推荐：选择列表中的标量子查询，每行执行一次
select c_custkey,
  (select SUM(o_totalprice)
    from ORDERS
    where o_custkey = c_custkey and o_orderdate = '2020-04-16') as total,
  (select count(*)
    from ORDERS
    where o_custkey = c_custkey and o_orderdate = '2020-04-16') as cnt
from CUSTOMER;
```

## 正例

```sql
-- ✅ 推荐：解关联为 LEFT JOIN，多个子查询合并为一次批量计算
select c_custkey, SUM_ as total, count_ as cnt
from CUSTOMER left outer join (
    select o_custkey, SUM(o_totalprice) as SUM_, count(*) as count_
    from ORDERS
    where o_orderdate = '2020-04-16'
    group by o_custkey) as SQ on o_custkey = c_custkey;
```
