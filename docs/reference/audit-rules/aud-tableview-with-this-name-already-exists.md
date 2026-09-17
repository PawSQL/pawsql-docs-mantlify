---
id: audit-rule-aud-tableview-with-this-name-already-exists
title: 表/视图名已存在
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-tableview-with-this-name-already-exists
tags:
- audit-rule
- ddl
description: 此规则确保在创建新表或视图时，名称在数据库中（或模式内）是唯一的，避免与现有对象冲突。重复的对象名称会导致 `CREATE` 语句执行失败，可能中断部署流程或数据迁移任务。
localeOf: en-audit-rule-aud-tableview-with-this-name-already-exists
subtype: rule
language: zh
translationKey: audit-rule-aud-tableview-with-this-name-already-exists
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-tableview-with-this-name-already-exists |
| 规则名称 | 表/视图名已存在 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则确保在创建新表或视图时，名称在数据库中（或模式内）是唯一的，避免与现有对象冲突。重复的对象名称会导致 `CREATE` 语句执行失败，可能中断部署流程或数据迁移任务。
如果 SQL 语句添加了 `IF NOT EXISTS` 子句，则不会触发此规则告警。建议在自动化脚本中始终添加 `IF NOT EXISTS` 以提高容错性。

## 反例

```sql
-- ❌ 不推荐：创建表/视图时名称与已存在的对象冲突
CREATE TABLE orders (id INT PRIMARY KEY);
```

## 正例

```sql
-- ✅ 推荐：添加 IF NOT EXISTS 避免冲突
CREATE TABLE IF NOT EXISTS orders (id INT PRIMARY KEY);
```
