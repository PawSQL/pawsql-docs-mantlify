---
id: audit-rule-aud-select-star
title: SELECT * Detection
type: reference
status: draft
tags:
- audit-rule
- select
- mysql
- postgresql
- oracle
description: Flags explicit SELECT * against wide tables. Reading unneeded columns
  forces table or index lookups that a covering index could avoid.
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | AUD-SELECT-STAR |
| Name | SELECT * Detection |
| Category | select |
| Severity | warning |
| Databases | mysql, postgresql, oracle |
| Version Introduced | 8.0.0 |

## Description

Flags explicit SELECT * against wide tables. Reading unneeded columns forces table or index lookups that a covering index could avoid.

## Why It Matters

Explicit column lists make intent explicit, keep the result stable across schema changes, and allow the optimizer to use covering indexes.

## How to Fix

List only the columns actually needed. If the full row is genuinely required, document why the audit rule should be suppressed for that query.

## Bad Example

```sql
SELECT * FROM orders WHERE customer_id = 42;
```

## Good Example

```sql
SELECT id, status, total
FROM orders
WHERE customer_id = 42;
```

## Related Rules

`AUD-EXPLICIT-COLUMNS`
