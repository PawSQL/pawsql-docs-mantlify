---
id: en-audit-rule-aud-avoid-for-update-with-derived-tables
title: Avoid FOR UPDATE with Derived Tables
type: reference
status: draft
tags:
- audit-rule
- dml
description: SELECT ... FOR UPDATE over a derived table can lock the internal temporary
  table instead of the base rows; lock the base table directly.
localeOf: audit-rule-aud-avoid-for-update-with-derived-tables
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-for-update-with-derived-tables |
| Name | Avoid FOR UPDATE with Derived Tables |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

`SELECT ... FROM (subquery) ... FOR UPDATE` has a serious lock-miss risk. In MySQL, when the FROM clause contains a derived table (subquery), the database first materializes the subquery into a temporary table, and the `FOR UPDATE` locks may be taken on that internal temporary table rather than on the real base-table rows. The lock then does not actually protect the base rows you intended, so the business's data-consistency requirement is not met.

The right approach is to run `SELECT ... FOR UPDATE` directly on the base table. If you must filter through a subquery before locking, confirm with `EXPLAIN` that no `DERIVED` temporary table is produced, or replace the subquery with a JOIN.

## Bad Example

```sql
-- bad: FOR UPDATE over a derived table may lock the temporary table, not the base rows
SELECT * FROM (SELECT * FROM t WHERE id_seq = ?) a FOR UPDATE;
```

## Good Example

```sql
-- good: lock the base table directly
SELECT * FROM t WHERE id_seq = ? FOR UPDATE;
```
