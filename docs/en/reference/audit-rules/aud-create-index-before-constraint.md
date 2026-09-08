---
id: en-audit-rule-aud-create-index-before-constraint
title: Create Index Before Constraint
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-create-index-before-constraint
tags:
- audit-rule
- ddl
description: Create the backing index before adding a constraint (unique/FK/CHECK)
  so validation reuses it instead of full-table scanning under lock.
localeOf: audit-rule-aud-create-index-before-constraint
subtype: rule
language: en
translationKey: audit-rule-aud-create-index-before-constraint
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-create-index-before-constraint |
| Name | Create Index Before Constraint |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Before adding a constraint (unique, foreign key, or CHECK), create the backing index first. Constraint enforcement relies on an underlying index to validate data; without one the database must scan the whole table to validate the constraint, which badly hurts DDL performance and can cause long lock waits on large tables.

Creating the index manually up front lets the database reuse it for constraint validation instead of full-table scanning, keeps DDL changes smooth, and gives finer control over index naming and structure.

## Bad Example

```sql
-- bad: adding a unique constraint without its index causes a full-table-scan validation
ALTER TABLE t_order ADD CONSTRAINT uk_order_no UNIQUE (order_no);
```

## Good Example

```sql
-- good: create the index first, then add the constraint reusing it
CREATE UNIQUE INDEX uk_order_no ON t_order (order_no);
ALTER TABLE t_order ADD CONSTRAINT uk_order_no UNIQUE USING INDEX uk_order_no;
```
