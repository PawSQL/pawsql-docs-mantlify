---
id: en-audit-rule-aud-column-and-table-character-set-mismatch
title: Column and Table Character Set Mismatch
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-column-and-table-character-set-mismatch
tags:
- audit-rule
- ddl
description: Column and table character sets must match to avoid conversion, truncation,
  mojibake, and JOIN index invalidation; columns should inherit the table charset.
localeOf: audit-rule-aud-column-and-table-character-set-mismatch
subtype: rule
language: en
translationKey: audit-rule-aud-column-and-table-character-set-mismatch
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-column-and-table-character-set-mismatch |
| Name | Column and Table Character Set Mismatch |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

When a column-level character set differs from the table-level one, it can cause implicit conversion, data truncation, or mojibake. In multi-language environments, mismatched character sets can also invalidate indexes (in MySQL, JOINing fields with different character sets cannot use an index) and produce query results that do not meet expectations - subtle failures.

Set the character set uniformly at the table level and let columns inherit it, avoiding isolated columns with a different charset. A consistent charset strategy is a basic database-design norm.

## Bad Example

```sql
-- bad: column-level charset differs from the table's
CREATE TABLE t_user (
    name VARCHAR(50) CHARSET latin1
) DEFAULT CHARSET utf8mb4;
```

## Good Example

```sql
-- good: the column inherits the table's charset
CREATE TABLE t_user (
    name VARCHAR(50)
) DEFAULT CHARSET utf8mb4;
```
