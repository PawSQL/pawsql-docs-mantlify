---
id: en-audit-rule-aud-avoid-leading-or-trailing-spaces-in-string-liter
title: Avoid Leading or Trailing Spaces in String Literals
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-leading-or-trailing-spaces-in-string-liter
tags:
- audit-rule
- dml
description: Spaces at the start or end of string literals are usually typos but change
  matches; remove them, or use TRIM() when spaces are intended.
localeOf: audit-rule-aud-avoid-leading-or-trailing-spaces-in-string-liter
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-leading-or-trailing-spaces-in-string-liter
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-leading-or-trailing-spaces-in-string-liter |
| Name | Avoid Leading or Trailing Spaces in String Literals |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Leading or trailing spaces in SQL string literals usually carry no business meaning and often come from a typo (for example copy-pasting that drags extra spaces in). But they can change query results directly - `WHERE name = ' test '` and `WHERE name = 'test'` match different data.

Take these notices seriously and check whether surrounding spaces in a string literal are intentional. If it is a typo, clean it up; if you really must match data with spaces, use `TRIM()` or add a comment stating the intent.

## Bad Example

```sql
-- bad: a string literal with leading/trailing spaces, possibly a typo
SELECT * FROM t WHERE name = ' test ';
```

## Good Example

```sql
-- good: drop the meaningless spaces
SELECT * FROM t WHERE name = 'test';

-- to actually match data that may carry spaces, use TRIM or state the intent
SELECT * FROM t WHERE TRIM(name) = 'test';
```
