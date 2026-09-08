---
id: en-audit-rule-aud-avoid-order-by-on-long-columns
title: Avoid ORDER BY on Long Columns
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-order-by-on-long-columns
tags:
- audit-rule
- dml
description: Sorting by over-long columns (CHAR/VARCHAR above 128 or CLOB/TEXT) is
  costly; sort by a prefix or hash instead.
localeOf: audit-rule-aud-avoid-order-by-on-long-columns
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-order-by-on-long-columns
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-order-by-on-long-columns |
| Name | Avoid ORDER BY on Long Columns |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Sorting is an O(n log n) operation; when many rows must be sorted, the length of a single column significantly affects efficiency - longer values make every comparison costlier and need more temporary space. This rule compares each sort column's length against a user-set threshold to assess risk.

The default threshold is 128 characters. It warns when a CHAR/VARCHAR sort column exceeds the threshold or is a large-object type such as CLOB/TEXT. Prefer sorting by a prefix or a hash instead of the full column.

## Bad Example

```sql
-- bad: sorting by a VARCHAR above the threshold is inefficient
SELECT * FROM articles ORDER BY content;
```

## Good Example

```sql
-- good: sort by a prefix or a hash
SELECT * FROM articles ORDER BY LEFT(content, 64);
```
