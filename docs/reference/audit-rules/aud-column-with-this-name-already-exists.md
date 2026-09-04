---
id: audit-rule-aud-column-with-this-name-already-exists
title: 字段名已存在
type: reference
status: draft
tags:
- audit-rule
- ddl
description: ADD/RENAME COLUMN 的列名不能与表内已有列冲突；可用 IF NOT EXISTS 或先确认唯一。
localeOf: en-audit-rule-aud-column-with-this-name-already-exists
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-column-with-this-name-already-exists |
| 规则名称 | 字段名已存在 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 所有支持数据库 |

## 说明

在修改表结构（如添加新列或重命名列）时，新增的列名可能与表中已有列名冲突，导致DDL语句执行失败或产生不可预期的结果。此规则确保在添加新列或修改表结构时，列名在表内是唯一的，从而避免列名冲突。
该规则检查`ALTER TABLE ADD COLUMN`和`ALTER TABLE RENAME COLUMN`操作，确保目标列名不与表中现有列名重复，且SQL语句中未添加`IF NOT EXISTS`保护。

## 反例

```sql
-- ❌ 不推荐：新增列名与已有列冲突，DDL执行失败
ALTER TABLE users ADD COLUMN email VARCHAR(255);
```

## 正例

```sql
-- ✅ 推荐：先确认列不存在再添加，或使用IF NOT EXISTS
ALTER TABLE users ADD COLUMN IF NOT EXISTS email VARCHAR(255);
```
