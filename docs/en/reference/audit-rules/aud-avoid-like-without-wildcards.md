---
id: en-audit-rule-aud-avoid-like-without-wildcards
title: Avoid LIKE Without Wildcards
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-like-without-wildcards
tags:
- audit-rule
- dml
description: LIKE without wildcards equals an equality and usually signals a forgotten
  wildcard; use '=' or add the wildcards deliberately.
localeOf: audit-rule-aud-avoid-like-without-wildcards
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-like-without-wildcards
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-like-without-wildcards |
| Name | Avoid LIKE Without Wildcards |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

A LIKE without wildcards (`%` or `_`) is logically identical to an equality comparison (`=`), but reads ambiguously - readers cannot tell whether the developer deliberately wanted pattern matching or accidentally used LIKE where they meant equality. More importantly, this is usually a slip: the developer may have intended `LIKE '%keyword%'` and forgotten the wildcards.

Replace wildcard-less LIKE with an equality comparison (`=`) so the semantics are precise and clear. Pay attention to this notice and confirm it reflects your real intent.

## Bad Example

```sql
-- bad: LIKE without wildcards is equivalent to equality and may be a slip
SELECT * FROM t WHERE name LIKE 'test';
```

## Good Example

```sql
-- good: use equality instead
SELECT * FROM t WHERE name = 'test';

-- for real fuzzy matching, add the wildcards explicitly
SELECT * FROM t WHERE name LIKE '%test%';
```
