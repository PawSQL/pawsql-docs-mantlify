---
id: en-audit-rule-aud-avoid-scalar-subqueries
title: Avoid Scalar Subqueries
type: reference
status: draft
tags:
- audit-rule
- dml
description: Scalar subqueries run once per outer row and can fail at run time; prefer
  a JOIN or derived table.
localeOf: audit-rule-aud-avoid-scalar-subqueries
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-scalar-subqueries |
| Name | Avoid Scalar Subqueries |
| Category | dml — DML / data modification |
| Severity | info |
| Databases | All supported databases |

## Description

A scalar subquery returns a single row and column, and can appear anywhere a single value can. Scalar subqueries are usually correlated with the outer query: the database executes the subquery once for every row of the outer result. This "row-by-row" execution performs very poorly on large data sets. In addition, whether a scalar subquery really returns one row is only known at run time - if it unexpectedly returns multiple rows, it causes a run-time error.

Prefer replacing scalar subqueries with a JOIN or a derived table so the optimizer can do the work in one batched pass. PawSQL recognizes scalar subqueries and, when feasible, automatically offers a rewrite.

## Bad Example

```sql
-- bad: scalar subquery in the select list runs once per outer row
SELECT id, (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) AS cnt FROM user u;
```

## Good Example

```sql
-- good: replace it with LEFT JOIN + GROUP BY
SELECT u.id, COUNT(o.id) AS cnt
FROM user u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id;
```
