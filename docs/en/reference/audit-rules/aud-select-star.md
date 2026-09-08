---
id: en-audit-rule-aud-select-star
title: SELECT * Detection
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: AUD-SELECT-STAR
tags:
- audit-rule
- unknown
- mysql
- postgresql
- oracle
description: 'Flags SELECT * on wide tables: unneeded columns cost IO and bandwidth
  and block covering-index optimization; list only the columns you need.'
localeOf: audit-rule-aud-select-star
subtype: rule
language: en
translationKey: audit-rule-aud-select-star
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | AUD-SELECT-STAR |
| Name | SELECT * Detection |
| Category | unknown — Unknown (pending product mapping) |
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
