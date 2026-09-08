---
id: en-audit-rule-aud-addingcolumnswithdefaultdisallowed
title: AddingColumnsWithDefaultDisallowed
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-addingcolumnswithdefaultdisallowed
tags:
- audit-rule
- ddl
description: Do not add columns with a DEFAULT to populated tables (rebuild/lock/backfill
  risk); add a nullable column, backfill, then set the DEFAULT in stages.
localeOf: audit-rule-aud-addingcolumnswithdefaultdisallowed
subtype: rule
language: en
translationKey: audit-rule-aud-addingcolumnswithdefaultdisallowed
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-addingcolumnswithdefaultdisallowed |
| Name | AddingColumnsWithDefaultDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Adding a column with a DEFAULT to an existing table is disallowed: the change can trigger a table rebuild or a long lock, causes severe I/O and replication delay on large tables, and silently changes write semantics. On tables that already hold data the database must backfill every row with the default, which is slow and can block other operations.

The right way is to add a nullable column first, write values explicitly from the application, complete the backfill, and only then add the DEFAULT and a NOT NULL constraint in stages. This rule is an important safety norm for schema-change management.

## Bad Example

```sql
-- bad: adding columns with an immediate DEFAULT may trigger a table rebuild
ALTER TABLE orders ADD COLUMN status VARCHAR(20) DEFAULT 'pending';
ALTER TABLE orders ADD COLUMN amount DECIMAL(10,2) NOT NULL DEFAULT 0.00;
```

## Good Example

```sql
-- good: add a nullable column first, backfill, then set the DEFAULT
ALTER TABLE orders ADD COLUMN status VARCHAR(20);
-- backfill in the application...
ALTER TABLE orders ALTER COLUMN status SET DEFAULT 'pending';
```
