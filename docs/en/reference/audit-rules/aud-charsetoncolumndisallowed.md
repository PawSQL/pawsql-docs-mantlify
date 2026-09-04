---
id: en-audit-rule-aud-charsetoncolumndisallowed
title: CharsetOnColumnDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Per-column character sets cause implicit conversion on JOIN (index invalidation,
  full scans) and comparison bugs; set the charset uniformly at table level.
localeOf: audit-rule-aud-charsetoncolumndisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-charsetoncolumndisallowed |
| Name | CharsetOnColumnDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

Setting a character set on a single column is disallowed. When a column's character set differs from the table's or database's default, JOINs need an implicit character-set conversion that invalidates indexes and causes full table scans - a subtle, wide-reaching performance problem. Inconsistent character sets can also make data comparisons behave unexpectedly and produce business-logic bugs that are hard to trace.

Set the character set uniformly at the table level so all columns inherit one consistent setting, avoiding column-level special cases.

## Bad Example

```sql
-- bad: a column-level character set can break the index on JOINs
CREATE TABLE t (
    id INT,
    name VARCHAR(100) CHARACTER SET latin1
);
```

## Good Example

```sql
-- good: set the character set uniformly at the table level
CREATE TABLE t (
    id INT,
    name VARCHAR(100)
) DEFAULT CHARSET=utf8mb4;
```
