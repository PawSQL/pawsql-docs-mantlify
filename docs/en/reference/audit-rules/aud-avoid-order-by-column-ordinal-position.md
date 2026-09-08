---
id: en-audit-rule-aud-avoid-order-by-column-ordinal-position
title: Avoid ORDER BY Column Ordinal Position
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-order-by-column-ordinal-position
tags:
- audit-rule
- dml
description: ORDER BY 1,2 (column ordinals) silently changes meaning when the SELECT
  list changes; always name the columns or expressions.
localeOf: audit-rule-aud-avoid-order-by-column-ordinal-position
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-order-by-column-ordinal-position
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-order-by-column-ordinal-position |
| Name | Avoid ORDER BY Column Ordinal Position |
| Category | dml — DML / data modification |
| Severity | info |
| Databases | Unverified (database scope not declared) |

## Description

You can sort by a column's ordinal position in the SELECT list (for example `ORDER BY 1, 2`) instead of naming the column or expression. That saves a little typing but badly hurts readability and maintainability - when the order of columns in the SELECT list changes, the semantics of ORDER BY silently change in a way reviewers can easily miss, inviting subtle bugs.

Always use explicit column names or expressions in ORDER BY so the intent is visible and later maintenance and refactoring stay safe.

## Bad Example

```sql
-- bad: ORDER BY by column ordinal is hard to read
SELECT id, name FROM t ORDER BY 2;
```

## Good Example

```sql
-- good: ORDER BY with explicit column names
SELECT id, name FROM t ORDER BY name;
```
