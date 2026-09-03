---
id: audit-rule-aud-insert-must-include-pk
title: INSERT Must Include Primary Key Column
type: reference
status: draft
tags:
- audit-rule
- dml
description: For tables without an auto-increment primary key, INSERT statements should
  supply the primary-key value explicitly. Even when the primary-key column has a
  default value, omitting it can produce duplic
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-insert-must-include-pk |
| Name | INSERT Must Include Primary Key Column |
| Category | dml |
| Severity | warning |
| Databases | All supported databases |

## Description

For tables without an auto-increment primary key, INSERT statements should supply the primary-key value explicitly. Even when the primary-key column has a default value, omitting it can produce duplicates or values that do not match business expectations; in production, such statements risk primary-key conflicts and data inconsistency.

## How to Fix

Add the primary-key column to the INSERT column list and provide an explicit value.

## Bad Example

```sql
-- t has a non-auto-increment primary key, but INSERT omits it
INSERT INTO user (name) VALUES ('张三');
```

## Good Example

```sql
-- supply the primary-key value explicitly
INSERT INTO user (id, name) VALUES (1, '张三');
```
