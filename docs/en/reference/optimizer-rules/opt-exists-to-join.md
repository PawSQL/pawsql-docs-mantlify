---
id: en-optimizer-rule-opt-exists-to-join
title: EXISTS Subquery to Table Join Rewrite
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-exists-to-join
tags:
- optimizer-rule
- rewrite
description: Rewrites convertible EXISTS subqueries into an equivalent inner join
  so the optimizer can choose the driving table freely.
localeOf: optimizer-rule-opt-exists-to-join
subtype: rule
language: en
translationKey: optimizer-rule-opt-exists-to-join
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/optimizer/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | opt-exists-to-join |
| Name | EXISTS Subquery to Table Join Rewrite |
| Category | rewrite — Rewrite |
| Severity | info |
| Databases | Unverified (database scope not declared) |

## Description

An EXISTS subquery returns a boolean telling whether any matching row exists. When the correlation is an equality, the subquery result is unique, and the subquery has neither GROUP BY nor LIMIT, the EXISTS subquery can be rewritten into a JOIN. Rewriting to a join lets the optimizer choose the driving table freely and produce a better plan.

## How to Fix

No manual action required: PawSQL detects convertible EXISTS subqueries and rewrites them into an equivalent inner join automatically, widening the set of plans the optimizer can consider.

## Bad Example

```sql
-- EXISTS subquery restricts which table the optimizer can drive from
SELECT * FROM lineitem l
WHERE EXISTS (SELECT * FROM part p WHERE p.p_partkey = l.l_partkey AND p.p_name = 'a');
```

## Good Example

```sql
-- rewritten as a JOIN so the optimizer can pick the driving table
SELECT l.* FROM lineitem AS l, part AS p
WHERE p.p_partkey = l.l_partkey AND p.p_name = 'a';
```
