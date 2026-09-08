---
id: audit-rule-aud-expression-in-order-by
title: ORDER 字段中有表达式导致索引失效
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-expression-in-order-by
tags:
- audit-rule
- index
description: ORDER BY 使用表达式或函数（如 YEAR、LENGTH）会使列索引无法用于排序、退化为文件排序；应直接按列排序。
localeOf: en-audit-rule-aud-expression-in-order-by
subtype: rule
language: zh
translationKey: audit-rule-aud-expression-in-order-by
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-expression-in-order-by |
| 规则名称 | ORDER 字段中有表达式导致索引失效 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

数据库可以利用索引的有序性来避免 ORDER BY 子句中列的排序，从而提升 SQL 性能。然而，当 ORDER BY 字段是一个表达式或函数（如 ORDER BY YEAR(date_column)、ORDER BY LENGTH(name)）时，数据库无法直接使用列上的索引来完成排序，只能执行额外的文件排序操作，导致性能显著下降。

## 如何修复

避免对排序列使用函数或表达式，直接按列本身排序（如 ORDER BY o_orderdate）以便利用索引有序性。若表达式无法避免，可考虑函数索引或物化后的派生列。

## 反例

```sql
-- 不推荐：ORDER BY 使用表达式，导致 o_orderdate 列索引失效
SELECT * FROM orders ORDER BY YEAR(o_orderdate);
-- 不推荐：ORDER BY 使用函数，无法利用索引有序性
SELECT * FROM orders ORDER BY LENGTH(c_name);
```

## 正例

```sql
-- 推荐：避免在 ORDER BY 中使用函数或表达式
SELECT * FROM orders ORDER BY o_orderdate;
```
