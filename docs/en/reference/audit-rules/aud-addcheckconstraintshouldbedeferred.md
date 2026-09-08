---
id: en-audit-rule-aud-addcheckconstraintshouldbedeferred
title: AddCheckConstraintShouldBeDeferred
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-addcheckconstraintshouldbedeferred
tags:
- audit-rule
- ddl
description: Adding a CHECK to a populated table should use NO VALID to skip full-table
  validation; validate legacy rows offline in batches.
localeOf: audit-rule-aud-addcheckconstraintshouldbedeferred
subtype: rule
language: en
translationKey: audit-rule-aud-addcheckconstraintshouldbedeferred
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-addcheckconstraintshouldbedeferred |
| Name | AddCheckConstraintShouldBeDeferred |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

When you add a CHECK constraint to a table that already holds data via `ALTER TABLE` without specifying `NO VALID` (or an equivalent non-validating option), the database immediately validates every existing row. On large tables this triggers a long full-table scan and lock hold that blocks concurrent writes and can even make the change time out or fail. Specifying `NO VALID` skips validation of historical rows and only enforces the constraint on newly written data, protecting new-data quality without the performance hit on the existing system.

Validation of legacy rows should be done outside the change window, step by step through batched validation scripts, and the constraint should only be switched to fully enforced once all data is confirmed to satisfy it.

## Bad Example

```sql
-- bad: no NO VALID; the database validates the whole table immediately
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount > 0);
```

## Good Example

```sql
-- good: NO VALID only enforces the constraint on new data
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount > 0) NO VALID;
```
