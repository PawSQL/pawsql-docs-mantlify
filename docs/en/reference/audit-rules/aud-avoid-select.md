---
id: en-audit-rule-aud-avoid-select
title: SELECT * Detection
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-select
tags:
- audit-rule
- dml
- mysql
- postgresql
- oracle
description: 'Flags SELECT * on wide tables: unneeded columns cost IO and bandwidth
  and block covering-index optimization; list only the columns you need.'
localeOf: audit-rule-aud-avoid-select
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-select
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-select |
| Name | SELECT * Detection |
| Category | dml — DML / data modification |
| Severity | info |
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
-- bad: SELECT * fetches unneeded columns, wasting IO and bandwidth
SELECT * FROM user WHERE id = 1;
```

## Good Example

```sql
-- good: only fetch the columns you need
SELECT id, name, email FROM user WHERE id = 1;
```

## Related Rules

`AUD-EXPLICIT-COLUMNS`
