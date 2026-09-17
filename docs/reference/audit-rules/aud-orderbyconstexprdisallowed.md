---
id: audit-rule-aud-orderbyconstexprdisallowed
title: 禁止对非整形常量进行ORDER BY
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-orderbyconstexprdisallowed
tags:
- audit-rule
- dml
description: 对非整数常量进行排序实际上没有意义——这种写法通常是开发者在编写 SQL 时误将列名或位置指示符写成了字符串常量。与 `GROUP BY`
  类似，PostgreSQL 中这种写法会语法报错，但在 MySQL 中却不会，返回的结果看似正确但排序逻辑完全错误，难以在测试阶段发现问题。
localeOf: en-audit-rule-aud-orderbyconstexprdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-orderbyconstexprdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-orderbyconstexprdisallowed |
| 规则名称 | 禁止对非整形常量进行ORDER BY |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对非整数常量进行排序实际上没有意义——这种写法通常是开发者在编写 SQL 时误将列名或位置指示符写成了字符串常量。与 `GROUP BY` 类似，PostgreSQL 中这种写法会语法报错，但在 MySQL 中却不会，返回的结果看似正确但排序逻辑完全错误，难以在测试阶段发现问题。
该规则要求在 SQL 审计中检测并禁止在 `ORDER BY` 子句中使用常量值，确保排序字段始终为有效的列名或列位置指示符（整数）。

## 反例

```sql
-- ❌ 不推荐：ORDER BY 常量无意义，MySQL 静默执行但排序无效
SELECT l_orderkey
FROM lineitem
ORDER BY '1';
```

## 正例

```sql
-- ✅ 推荐：ORDER BY 使用列名或整数位置
SELECT l_orderkey
FROM lineitem
ORDER BY l_orderkey;
-- 或
SELECT l_orderkey
FROM lineitem
ORDER BY 1;
```
