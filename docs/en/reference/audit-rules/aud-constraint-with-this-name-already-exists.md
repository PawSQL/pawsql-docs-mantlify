---
id: en-audit-rule-aud-constraint-with-this-name-already-exists
title: Constraint with this Name Already Exists
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Constraint names must be unique per database/table; a duplicate name
  fails the SQL and can break deployment or migration scripts.
localeOf: audit-rule-aud-constraint-with-this-name-already-exists
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-constraint-with-this-name-already-exists |
| Name | Constraint with this Name Already Exists |
| Category | ddl — DDL / object design |
| Severity | error |
| Databases | All supported databases |

## Description

This rule ensures constraint names are unique within the database (or table) when constraints are added, so they do not collide with existing ones. Duplicate constraint names make the SQL fail and can interrupt deployment scripts or data-migration flows.

When the statement adds an `IF NOT EXISTS` clause, this rule does not fire. Consistent constraint naming and uniqueness checks are a basic requirement of schema-change management.

## Bad Example

```sql
-- bad: the constraint name collides with an existing one
ALTER TABLE orders ADD CONSTRAINT pk_orders PRIMARY KEY (order_id);
```

## Good Example

```sql
-- good: use IF NOT EXISTS or a unique constraint name
ALTER TABLE orders ADD CONSTRAINT pk_orders_new PRIMARY KEY (order_id);
```
