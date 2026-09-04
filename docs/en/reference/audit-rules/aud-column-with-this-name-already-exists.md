---
id: en-audit-rule-aud-column-with-this-name-already-exists
title: Column with this Name Already Exists
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 在修改表结构（如添加新列或重命名列）时，新增的列名可能与表中已有列名冲突，导致DDL语句执行失败或产生不可预期的结果。此规则确保在添加新列或修改表结构时，列名在表内是唯一的，从而避免列名冲突。
localeOf: audit-rule-aud-column-with-this-name-already-exists
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-column-with-this-name-already-exists |
| Name | Column with this Name Already Exists |
| Category | ddl — DDL / object design |
| Severity | error |
| Databases | All supported databases |

## Description

在修改表结构（如添加新列或重命名列）时，新增的列名可能与表中已有列名冲突，导致DDL语句执行失败或产生不可预期的结果。此规则确保在添加新列或修改表结构时，列名在表内是唯一的，从而避免列名冲突。
该规则检查`ALTER TABLE ADD COLUMN`和`ALTER TABLE RENAME COLUMN`操作，确保目标列名不与表中现有列名重复，且SQL语句中未添加`IF NOT EXISTS`保护。

## Bad Example

```sql
-- ❌ 不推荐：新增列名与已有列冲突，DDL执行失败
ALTER TABLE users ADD COLUMN email VARCHAR(255);
```

## Good Example

```sql
-- ✅ 推荐：先确认列不存在再添加，或使用IF NOT EXISTS
ALTER TABLE users ADD COLUMN IF NOT EXISTS email VARCHAR(255);
```
