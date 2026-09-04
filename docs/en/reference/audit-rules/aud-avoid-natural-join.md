---
id: en-audit-rule-aud-avoid-natural-join
title: Avoid NATURAL JOIN
type: reference
status: draft
tags:
- audit-rule
- dml
description: NATURAL JOIN's implicit join conditions hurt readability and silently
  change when the schema changes; use explicit JOIN ... ON.
localeOf: audit-rule-aud-avoid-natural-join
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-natural-join |
| Name | Avoid NATURAL JOIN |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

NATURAL JOIN is a special equi-join usable with inner, outer, and full joins. It automatically matches every pair of same-named, same-typed columns across the two tables and joins on them. NATURAL JOIN shortens the statement, but its implicit join conditions badly hurt readability: readers cannot see which columns the tables are joined on and cannot easily reason about the relationship.

More dangerously, when the schema changes (a same-named column is added or removed), NATURAL JOIN's join conditions silently change and can produce wrong results without any error. PawSQL raises a risk notice on NATURAL JOIN statements to avoid these correctness problems.

## Bad Example

```sql
-- bad: NATURAL JOIN implicitly matches same-named columns; hard to read and error-prone
SELECT * FROM orders NATURAL JOIN customers;
```

## Good Example

```sql
-- good: explicit JOIN ... ON makes the join condition obvious
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.id;
```
