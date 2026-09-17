---
id: audit-rule-aud-use-table-aliases-in-multitable-queries
title: 在一个查询块中引用多表应使用别名
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-table-aliases-in-multitable-queries
tags:
- audit-rule
- dml
description: 如果在一个查询块中存在多个表的引用，应当为每个表起一个简单易认的别名，并为所有的字段添加别名前缀。这样做可以显著提升SQL代码的可读性，方便开发人员进行代码阅读以及后续维护。缺少别名的多表查询在字段来源不明确时，容易引发歧义，增加调试和排错的成本。
localeOf: en-audit-rule-aud-use-table-aliases-in-multitable-queries
subtype: rule
language: zh
translationKey: audit-rule-aud-use-table-aliases-in-multitable-queries
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-table-aliases-in-multitable-queries |
| 规则名称 | 在一个查询块中引用多表应使用别名 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

如果在一个查询块中存在多个表的引用，应当为每个表起一个简单易认的别名，并为所有的字段添加别名前缀。这样做可以显著提升SQL代码的可读性，方便开发人员进行代码阅读以及后续维护。缺少别名的多表查询在字段来源不明确时，容易引发歧义，增加调试和排错的成本。
该规则适用于所有包含多表引用的DML查询语句，是SQL编码规范中的基础要求。

## 反例

```sql
-- ❌ 不推荐：多表查询缺少别名，字段来源不明确
SELECT col1, col2 FROM table1, table2;
```

## 正例

```sql
-- ✅ 推荐：为每个表起别名，并为字段添加别名前缀
SELECT t1.col1, t2.col2 FROM table1 t1, table2 t2;

-- ✅ 推荐：使用JOIN语法并添加别名
SELECT o.order_id, c.customer_name
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```
