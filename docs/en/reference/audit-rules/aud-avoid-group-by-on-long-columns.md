---
id: en-audit-rule-aud-avoid-group-by-on-long-columns
title: Avoid GROUP BY on Long Columns
type: reference
status: draft
tags:
- audit-rule
- dml
description: Grouping by over-long columns (CHAR/VARCHAR above 128 or CLOB/TEXT) is
  slow; group by a prefix or hash instead.
localeOf: audit-rule-aud-avoid-group-by-on-long-columns
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-group-by-on-long-columns |
| Name | Avoid GROUP BY on Long Columns |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | All supported databases |

## Description

GROUP BY is usually implemented by sorting or hashing, whose time and memory cost scale with the amount of data and the length of the grouped columns. With many rows to group, a long column degrades performance noticeably - longer values make each comparison or hash more expensive and consume more temporary space.

This rule compares each grouped column's length against a user-set threshold (128 characters by default). It warns when a CHAR/VARCHAR grouping column exceeds the threshold or is a large-object type such as CLOB/TEXT.

## Bad Example

```sql
-- bad: grouping by a VARCHAR longer than the threshold is inefficient
SELECT long_description, COUNT(*) FROM products GROUP BY long_description;
```

## Good Example

```sql
-- good: group by a hash or a prefix of the column
SELECT LEFT(long_description, 64), COUNT(*) FROM products GROUP BY LEFT(long_description, 64);
```
