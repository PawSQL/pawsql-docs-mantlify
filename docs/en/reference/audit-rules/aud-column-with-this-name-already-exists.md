---
id: en-audit-rule-aud-column-with-this-name-already-exists
title: Column with this Name Already Exists
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Adding or renaming a column to a name that already exists fails the DDL;
  guard with IF NOT EXISTS or confirm the name is unique first.
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

When altering table structure (adding or renaming a column), a new column name can collide with an existing column and make the DDL fail or produce unexpected results. This rule ensures column names stay unique within a table when columns are added or the structure is changed.

It checks `ALTER TABLE ADD COLUMN` and `ALTER TABLE RENAME COLUMN` so the target column name does not duplicate an existing one, and flags statements that lack an `IF NOT EXISTS` guard.

## Bad Example

```sql
-- bad: the new column name collides with an existing column; the DDL fails
ALTER TABLE users ADD COLUMN email VARCHAR(255);
```

## Good Example

```sql
-- good: confirm the column is absent first, or use IF NOT EXISTS
ALTER TABLE users ADD COLUMN IF NOT EXISTS email VARCHAR(255);
```
