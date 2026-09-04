---
id: en-optimizer-rule-opt-count-to-exists
title: COUNT Scalar Subquery Rewrite
type: reference
status: draft
tags:
- optimizer-rule
- rewrite
description: Rewrites (SELECT COUNT(*) ...) > 0 presence tests into EXISTS, which
  short-circuits on the first match instead of aggregating every row.
localeOf: optimizer-rule-opt-count-to-exists
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/optimizer/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | opt-count-to-exists |
| Name | COUNT Scalar Subquery Rewrite |
| Category | rewrite — Rewrite |
| Severity | info |
| Databases | All supported databases |

## Description

A COUNT scalar subquery used as a presence test, such as (SELECT COUNT(*) FROM ...) > 0, can be rewritten into an EXISTS subquery. COUNT(*) > 0 must aggregate over every matching row before producing an answer, while EXISTS can short-circuit as soon as the first matching row is found, avoiding an unnecessary full count and lowering I/O and CPU cost.

## How to Fix

No manual action required: PawSQL recognizes this pattern and rewrites the correlated COUNT(*) > 0 subquery into EXISTS so the optimizer can pick a more efficient, semantically equivalent strategy.

## Bad Example

```sql
-- COUNT scalar subquery aggregates every matching row first
SELECT * FROM customer
WHERE (SELECT COUNT(*) FROM orders WHERE c_custkey = o_custkey) > 0;
```

## Good Example

```sql
-- rewritten as EXISTS: short-circuits on the first match
SELECT * FROM customer
WHERE EXISTS (SELECT 1 FROM orders WHERE c_custkey = o_custkey);
```
