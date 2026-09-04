---
id: en-audit-rule-aud-changingcolumns-order-disallowed
title: ChangingColumn's Order Disallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Reordering table columns triggers a rebuild and can break position-dependent
  code; fix order at design time and migrate via a new table if needed.
localeOf: audit-rule-aud-changingcolumns-order-disallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-changingcolumns-order-disallowed |
| Name | ChangingColumn's Order Disallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

Reordering the columns of a table is disallowed. Although syntax such as `ALTER TABLE ... MODIFY COLUMN ... AFTER` lets you move a column, it triggers a table rebuild and can break application logic that depends on column order (for example `SELECT *` or code accessing columns by position). On large tables, reordering columns holds locks for a long time and rollback is expensive.

Column order should be fixed at initial design time. If it must change later, do it through a migration that creates a new table rather than altering the existing structure in place.

## Bad Example

```sql
-- bad: reordering columns rebuilds the table and affects dependent programs
ALTER TABLE t MODIFY COLUMN col2 INT AFTER col5;
```

## Good Example

```sql
-- good: define column order in a new table and switch via migration
-- CREATE TABLE t_new (col1 INT, col2 INT, col3 INT, ...);
-- data migration + application switch
```
