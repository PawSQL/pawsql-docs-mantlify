---
id: en-audit-rule-aud-avoid-duplicate-table-aliases
title: Avoid Duplicate Table Aliases
type: reference
status: draft
tags:
- audit-rule
- dml
description: Duplicate table aliases (or aliases colliding with real table names)
  destroy readability; every table reference needs a unique, meaningful alias.
localeOf: audit-rule-aud-avoid-duplicate-table-aliases
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-duplicate-table-aliases |
| Name | Avoid Duplicate Table Aliases |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

When a query reuses the same alias for two table references or subqueries, or an alias equals another table's name in the database, readability collapses - readers cannot tell which table each column reference comes from, and later maintenance and troubleshooting suffer.

Within a single query block, every table reference should carry a unique, semantically meaningful alias. This is both good practice and a basic requirement for keeping SQL maintainable in complex business scenarios.

## Bad Example

```sql
-- bad: duplicate table aliases make column provenance impossible to tell
SELECT * FROM t a, t a;
```

## Good Example

```sql
-- good: use unique, meaningful aliases
SELECT * FROM t t1, t t2 WHERE t1.id = t2.parent_id;
```
