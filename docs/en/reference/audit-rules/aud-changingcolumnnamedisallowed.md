---
id: en-audit-rule-aud-changingcolumnnamedisallowed
title: ChangingColumnNameDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 'Do not rename a column directly (breaks every dependent app/report/ETL/view);
  when required use a staged rollout: new column, dual-write, switch, drop old.'
localeOf: audit-rule-aud-changingcolumnnamedisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-changingcolumnnamedisallowed |
| Name | ChangingColumnNameDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

Renaming a column (`RENAME COLUMN` / `CHANGE COLUMN`) is disallowed. A rename affects every application, report, ETL script, and view that depends on the column and can interrupt production instantly. In architectures that cannot deploy without downtime, such a change must coordinate many upstream and downstream systems inside a maintenance window, which is very risky.

If a rename is truly required, a DBA should intervene by hand only after fully assessing dependencies, using a staged rollout (e.g. add the new column, dual-write, switch, then drop the old column) rather than executing a bare `RENAME`.

## Bad Example

```sql
-- bad: renaming a column directly breaks upstream/downstream dependencies
ALTER TABLE t CHANGE old_name new_name VARCHAR(50);
```

## Good Example

```sql
-- good: staged rollout
-- 1. ALTER TABLE t ADD COLUMN new_name VARCHAR(50);
-- 2. dual-write + backfill of historical data
-- 3. switch every consumer to new_name
-- 4. ALTER TABLE t DROP COLUMN old_name;
```
