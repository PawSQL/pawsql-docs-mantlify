---
id: audit-rule-aud-avoid-natural-join
title: 避免使用NATURAL JOIN
type: reference
status: draft
tags:
- audit-rule
- dml
description: 避免 NATURAL JOIN（隐式连接条件可读性差、表结构变化会悄然改变语义）；用显式 JOIN ... ON。
localeOf: en-audit-rule-aud-avoid-natural-join
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-natural-join |
| 规则名称 | 避免使用NATURAL JOIN |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

NATURAL JOIN 是一种特殊的等值连接，它可以与内连接、外连接及全连接配合使用。它会自动搜索两张表中所有相同列名和类型的列，并以这些列为条件进行等值连接。虽然 NATURAL JOIN 可以简化语句书写，但其隐式连接条件严重降低了代码的可读性：阅读者无法直观看出两张表基于哪些列关联，也不利于理解表之间的关系。
更危险的是，当表结构发生变化（如新增或删除同名列）时，NATURAL JOIN 的连接条件会悄然改变，可能产生错误的查询结果而不会触发任何错误提示。PawSQL 对使用 NATURAL JOIN 的语句进行风险提示，以避免其引发的正确性问题。

## 反例

```sql
-- ❌ 不推荐：NATURAL JOIN 隐式匹配同名列，可读性差且易出错
SELECT * FROM orders NATURAL JOIN customers;
```

## 正例

```sql
-- ✅ 推荐：使用显式的 JOIN ... ON 语法，连接条件一目了然
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.id;
```
