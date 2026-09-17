---
id: audit-rule-aud-avoid-order-by-columns-from-different-tables
title: 避免ORDERBY字段来自不同表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-order-by-columns-from-different-tables
tags:
- audit-rule
- index
description: 如果 ORDER BY 子句中的排序字段来自多个不同的表，数据库优化器将无法利用单个索引的有序性来避免显式的排序操作，必须对结果集进行额外的排序步骤（filesort），这会显著增加查询的
  CPU 和内存开销。
localeOf: en-audit-rule-aud-avoid-order-by-columns-from-different-tables
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-order-by-columns-from-different-tables
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-order-by-columns-from-different-tables |
| 规则名称 | 避免ORDERBY字段来自不同表 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

如果 ORDER BY 子句中的排序字段来自多个不同的表，数据库优化器将无法利用单个索引的有序性来避免显式的排序操作，必须对结果集进行额外的排序步骤（filesort），这会显著增加查询的 CPU 和内存开销。
当 WHERE 或 HAVING 子句中存在等值条件时，PawSQL 可以对排序字段进行等值替换，使其全部来自同一张表，从而能够利用该表上的索引来避免排序操作，提升查询性能。

## 反例

```sql
-- ❌ 不推荐：排序字段来自两个表，无法利用索引避免排序
select * from customer c, orders o where o_custkey = c_custkey order by o_custkey, c_name;
```

## 正例

```sql
-- ✅ 推荐：利用等值条件替换，使排序字段来自同一张表
select * from customer c, orders o where o_custkey = c_custkey order by c_custkey, c_name;
```
