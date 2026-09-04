---
id: en-audit-rule-aud-avoid-select-with-for-update
title: Avoid SELECT with FOR UPDATE
type: reference
status: draft
tags:
- audit-rule
- dml
description: SELECT ... FOR UPDATE adds row locks that cause waits, blocking, and
  deadlocks under concurrency; use it only when pessimistic locking is truly needed,
  on the fewest rows.
localeOf: audit-rule-aud-avoid-select-with-for-update
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-select-with-for-update |
| Name | Avoid SELECT with FOR UPDATE |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

`SELECT ... FOR UPDATE` takes exclusive locks on the rows the query matches and, until the transaction commits or rolls back, blocks other transactions from modifying or lock-reading those rows. Under concurrency this row-level locking can cause lock waits, blocking, and even deadlocks, hurting the database's concurrency and overall performance.

Use `FOR UPDATE` sparingly - only where pessimistic locking is genuinely needed to guarantee consistency - and keep the lock scope as small as possible (for example, lock only a few rows via an exact primary-key lookup). Never add `FOR UPDATE` to queries that need no locking. PawSQL checks for and reminds about this pattern.

## Bad Example

```sql
-- bad: unnecessary FOR UPDATE causes lock contention
SELECT * FROM user WHERE status = 'active' FOR UPDATE;
```

## Good Example

```sql
-- good: only where pessimistic locking is needed, and lock precisely by primary key
SELECT * FROM user WHERE id = 100 FOR UPDATE;
```
