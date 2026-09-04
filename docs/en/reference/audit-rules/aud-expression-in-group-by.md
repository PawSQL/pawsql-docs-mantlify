---
id: audit-rule-aud-expression-in-group-by
title: Expression in GROUP BY Causes Index Invalidation
type: reference
status: draft
tags:
- audit-rule
- index
description: Databases can use index ordering to avoid sorting the GROUP BY columns.
  When a GROUP BY key is an expression or a function (for example LEFT(column, 5)
  or YEAR(date_column)), the database can no longe
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-expression-in-group-by |
| Name | Expression in GROUP BY Causes Index Invalidation |
| Category | index |
| Severity | info |
| Databases | All supported databases |

## Description

Databases can use index ordering to avoid sorting the GROUP BY columns. When a GROUP BY key is an expression or a function (for example LEFT(column, 5) or YEAR(date_column)), the database can no longer use the column index for the grouping pass and falls back to an extra sort or a hash aggregate, degrading performance.

## How to Fix

Group by the bare column (or a precomputed/derived column) rather than an expression so the index can serve the grouping. If grouping by an expression is required by the business logic, consider a functional index or a stored, derived column.

## Bad Example

```sql
-- GROUP BY on an expression defeats the c_phone index
SELECT LEFT(c_phone, 5), COUNT(1) FROM orders GROUP BY LEFT(c_phone, 5);
```

## Good Example

```sql
-- group by a plain/derived column so the index applies
SELECT c_phone_prefix, COUNT(1) FROM orders GROUP BY c_phone_prefix;
```
