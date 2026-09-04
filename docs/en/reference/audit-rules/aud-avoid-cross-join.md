---
id: en-audit-rule-aud-avoid-cross-join
title: Avoid CROSS JOIN
type: reference
status: draft
tags:
- audit-rule
- dml
description: CROSS JOIN produces a Cartesian product and is almost always a performance
  trap; use an explicit join condition, or document the intent.
localeOf: audit-rule-aud-avoid-cross-join
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-cross-join |
| Name | Avoid CROSS JOIN |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

CROSS JOIN pairs every row of the left table with every row of the right table, producing `left rows x right rows` records - equivalent in theory to an inner join on `1=1`. Although CROSS JOIN has legitimate uses in specific scenarios (generating test data, pivoting rows to columns), in most cases it produces huge numbers of meaningless rows, making the query extremely inefficient and putting heavy pressure on system resources.

PawSQL raises a risk notice on statements that use CROSS JOIN to steer clear of these performance problems. If a Cartesian product is really needed, add an explicit comment explaining the business intent.

## Bad Example

```sql
-- bad: CROSS JOIN produces a Cartesian product and explodes the row count
SELECT *
FROM lineitem
CROSS JOIN orders;
```

## Good Example

```sql
-- good: join with an explicit condition
SELECT *
FROM lineitem l
JOIN orders o ON l.order_id = o.order_id;
```
