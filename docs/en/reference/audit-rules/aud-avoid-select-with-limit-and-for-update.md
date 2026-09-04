---
id: en-audit-rule-aud-avoid-select-with-limit-and-for-update
title: Avoid SELECT with LIMIT and FOR UPDATE
type: reference
status: draft
tags:
- audit-rule
- dml
description: ORDER BY + LIMIT + FOR UPDATE locks far more rows than it returns; fetch
  the primary keys first, then lock them precisely.
localeOf: audit-rule-aud-avoid-select-with-limit-and-for-update
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-select-with-limit-and-for-update |
| Name | Avoid SELECT with LIMIT and FOR UPDATE |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

`SELECT ... ORDER BY ... LIMIT ... FOR UPDATE` causes serious lock contention in MySQL. Because of the `ORDER BY`, the executor first scans and locks every row that matches the WHERE condition, then sorts and returns only LIMIT rows. In practice far more rows are locked than are returned, creating a lot of needless lock blocking and hurting concurrency.

Do it in two steps instead: first read the primary keys of the target rows with an ordinary SELECT, then run a precise `SELECT ... FOR UPDATE` by those primary keys so the lock scope is exactly the rows you truly need.

## Bad Example

```sql
-- bad: ORDER BY + LIMIT + FOR UPDATE locks far more than needed
SELECT msg_id FROM t_msg WHERE msg_type = 'type' ORDER BY send_time LIMIT 1 FOR UPDATE;
```

## Good Example

```sql
-- good: two steps - get the primary key, then lock precisely
-- step 1: get the primary key (no lock)
SELECT msg_id FROM t_msg WHERE msg_type = 'type' ORDER BY send_time LIMIT 1;
-- step 2: lock precisely by primary key
SELECT * FROM t_msg WHERE msg_id = ? FOR UPDATE;
```
