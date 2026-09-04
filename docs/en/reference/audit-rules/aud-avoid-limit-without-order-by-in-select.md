---
id: en-audit-rule-aud-avoid-limit-without-order-by-in-select
title: Avoid LIMIT Without ORDER BY in SELECT
type: reference
status: draft
tags:
- audit-rule
- dml
description: SELECT ... LIMIT without ORDER BY returns nondeterministic rows; always
  add ORDER BY to define which rows are returned.
localeOf: audit-rule-aud-avoid-limit-without-order-by-in-select
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-limit-without-order-by-in-select |
| Name | Avoid LIMIT Without ORDER BY in SELECT |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

Using `LIMIT` in a `SELECT` without an `ORDER BY` leaves the result undefined from run to run. With no ordering instruction, databases do not guarantee the order in which rows are returned - it depends on physical storage order, details of the execution plan, and other factors that can change across time and versions.

If business logic relies on LIMIT returning the "first N" rows, you must also give an `ORDER BY` to define what "first" means, keeping results repeatable and correct. PawSQL checks for and reminds about this pattern.

## Bad Example

```sql
-- bad: LIMIT without ORDER BY; the returned rows can differ each run
SELECT * FROM user LIMIT 10;
```

## Good Example

```sql
-- good: explicit ORDER BY keeps the result stable and repeatable
SELECT * FROM user ORDER BY id LIMIT 10;
```
