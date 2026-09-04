---
id: en-audit-rule-aud-char-column-length
title: Char Column Length Exceeds Threshold
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Flag CHAR columns longer than the configurable threshold (default 64);
  oversized fixed-width CHAR bloat rows, indexes, and I/O. Recommend VARCHAR instead.
localeOf: audit-rule-aud-char-column-length
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-char-column-length |
| Name | Char Column Length Exceeds Threshold |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | All supported databases |

## Description

When a CHAR column is declared longer than the configured threshold (64 by default) it should be reconsidered as VARCHAR. CHAR is stored at fixed length and consumes the declared width even when the actual data is short; for data with variable width, oversized CHAR columns bloat rows and indexes, increase I/O and memory usage, and reduce cache efficiency.

## Why It Matters

Fixed-width CHAR is only a good fit for values that are nearly always the same width. Switching over-long CHAR columns to VARCHAR enables dynamic storage, saves space, and improves query performance.

## How to Fix

Change CHAR columns whose declared length exceeds the threshold (default 64) to VARCHAR. This rule is configurable.

## Bad Example

```sql
-- CHAR(10000) reserves 10000 chars even for short values
CREATE TABLE t (
    content CHAR(10000)
);
```

## Good Example

```sql
-- use VARCHAR for variable-width data
CREATE TABLE t (
    content VARCHAR(10000)
);
```
