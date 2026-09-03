---
id: audit-rule-aud-expression-in-order-by
title: Expression in ORDER BY Causes Index Invalidation
type: reference
status: draft
tags:
- audit-rule
- index
description: Databases can use the ordering of an index to avoid sorting the ORDER
  BY column, which speeds up queries. When the ORDER BY key is an expression or a
  function call (for example ORDER BY YEAR(date_colu
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-expression-in-order-by |
| Name | Expression in ORDER BY Causes Index Invalidation |
| Category | index |
| Severity | info |
| Databases | All supported databases |

## Description

Databases can use the ordering of an index to avoid sorting the ORDER BY column, which speeds up queries. When the ORDER BY key is an expression or a function call (for example ORDER BY YEAR(date_column) or ORDER BY LENGTH(name)), the database can no longer use the underlying column index for sorting and falls back to an extra filesort, hurting performance.

## How to Fix

Avoid functions or expressions on the sort column; order by the column itself (for example ORDER BY o_orderdate) so the index ordering can be used. If an expression is unavoidable, consider a functional index or a derived, precomputed column.

## Bad Example

```sql
-- ORDER BY on a function makes the o_orderdate index unusable for sorting
SELECT * FROM orders ORDER BY YEAR(o_orderdate);
SELECT * FROM orders ORDER BY LENGTH(c_name);
```

## Good Example

```sql
-- order by the bare column so the index ordering applies
SELECT * FROM orders ORDER BY o_orderdate;
```
