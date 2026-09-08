---
id: en-audit-rule-aud-changingcolumntypedisallowed
title: ChangingColumnTypeDisallowed
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-changingcolumntypedisallowed
tags:
- audit-rule
- ddl
description: 'Do not change a column type in place (full rewrite/lock/truncation risk);
  use a staged migration: new column, dual-write, batched backfill, switch, drop old.'
localeOf: audit-rule-aud-changingcolumntypedisallowed
subtype: rule
language: en
translationKey: audit-rule-aud-changingcolumntypedisallowed
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-changingcolumntypedisallowed |
| Name | ChangingColumnTypeDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Directly changing a column's data type is disallowed. Changing a column type usually triggers a full table rewrite and a long lock: the database must convert and rewrite all rows under the new type. In high-concurrency production this can invalidate indexes, change execution plans suddenly, and, through implicit type conversion, truncate data or change semantics - a hard-to-recover data-corruption risk.

The right approach is a staged gray migration: add a column with the new type, keep both columns in sync (dual-write or triggers), backfill and validate in batches, switch the application, and finally drop the old column - each step verifiable and rollback-capable.

## Bad Example

```sql
-- bad: changing the column type directly rewrites the table and may truncate data
ALTER TABLE t MODIFY col VARCHAR(100);
```

## Good Example

```sql
-- good: staged gray migration
-- 1. ALTER TABLE t ADD COLUMN col_new VARCHAR(100);
-- 2. dual-write both columns (application / triggers)
-- 3. UPDATE t SET col_new = col WHERE col_new IS NULL;  -- batched backfill
-- 4. switch the application to col_new
-- 5. ALTER TABLE t DROP COLUMN col;
```
