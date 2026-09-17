---
id: en-audit-rule-aud-avoid-unconditional-updatedelete-statements
title: UPDATE/DELETE without WHERE
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-unconditional-updatedelete-statements
tags:
- audit-rule
- dml
- mysql
- postgresql
- oracle
description: UPDATE/DELETE without a WHERE clause affects the whole table and is a
  common data-loss source; add a predicate, or use TRUNCATE deliberately to clear
  it.
localeOf: audit-rule-aud-avoid-unconditional-updatedelete-statements
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-unconditional-updatedelete-statements
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-unconditional-updatedelete-statements |
| Name | UPDATE/DELETE without WHERE |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | mysql, postgresql, oracle |
| Version Introduced | 8.0.0 |

## Description

Flags UPDATE or DELETE statements that carry no WHERE clause, which would affect every row in the target table.

## Why It Matters

A missing WHERE on a DML statement is a frequent source of data-loss incidents. Flagging it before execution adds a safety gate for high-risk changes.

## How to Fix

Prefer TRUNCATE when the whole table must be cleared, or add the intended predicate. When every row must change, write the always-true condition explicitly (for example WHERE 1=1) to show it is intentional.

## Bad Example

```sql
-- bad: unconditional DELETE wipes the whole table
DELETE FROM t;
```

## Good Example

```sql
-- good: use TRUNCATE to clear a table (faster, explicit intent)
TRUNCATE TABLE t;

-- good: DELETE with a WHERE clause only removes the target rows
DELETE FROM t WHERE created_at < '2024-01-01';
```

## Related Rules

`AUD-DML-LIMIT`
