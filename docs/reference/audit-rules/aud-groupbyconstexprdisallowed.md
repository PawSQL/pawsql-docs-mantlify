---
id: audit-rule-aud-groupbyconstexprdisallowed
title: 禁止对非整形常量进行GROUP BY
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-groupbyconstexprdisallowed
tags:
- audit-rule
- dml
description: 对非整数常量进行分组实际上没有意义——这种写法通常是开发者在编写 SQL 时误将列名或表达式写成了字符串常量。在 PostgreSQL 中，这种写法会导致语法报错，从而快速暴露问题；但在
  MySQL 中却不会报错，静默执行后返回的结果看似正常但逻辑完全错误，排查难度极大。
localeOf: en-audit-rule-aud-groupbyconstexprdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-groupbyconstexprdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-groupbyconstexprdisallowed |
| 规则名称 | 禁止对非整形常量进行GROUP BY |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对非整数常量进行分组实际上没有意义——这种写法通常是开发者在编写 SQL 时误将列名或表达式写成了字符串常量。在 PostgreSQL 中，这种写法会导致语法报错，从而快速暴露问题；但在 MySQL 中却不会报错，静默执行后返回的结果看似正常但逻辑完全错误，排查难度极大。
该规则要求在 SQL 审计中检测并禁止在 `GROUP BY` 子句中使用常量值，确保分组字段始终为有效的列名或表达式。

## 反例

```sql
-- ❌ 不推荐：GROUP BY 常量无意义，MySQL 静默执行但不正确
SELECT l_orderkey, sum(l_quantity)
FROM lineitem
GROUP BY '1';
```

## 正例

```sql
-- ✅ 推荐：GROUP BY 使用列名或有效表达式
SELECT l_orderkey, sum(l_quantity)
FROM lineitem
GROUP BY l_orderkey;
```
