---
id: en-optimizer-rule-opt-use-union-all
title: Use UNION ALL Instead of UNION
type: reference
status: draft
tags:
- optimizer-rule
- rewrite
description: Replaces UNION with UNION ALL when no deduplication is needed, skipping
  the sort/hash pass for a large speedup on big result sets.
localeOf: optimizer-rule-opt-use-union-all
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/optimizer/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | opt-use-union-all |
| Name | Use UNION ALL Instead of UNION |
| Category | rewrite — Rewrite |
| Severity | info |
| Databases | All supported databases |

## Description

UNION deduplicates the two result sets, which databases implement through a sort or a hash. When the business logic guarantees there are no duplicates between the branches, or when duplicates are acceptable, UNION ALL should be used instead: it simply concatenates the two result sets with no extra processing, so it is far cheaper, especially on large data volumes.

## How to Fix

Replace UNION with UNION ALL when the branches cannot produce duplicates (or when duplicates are allowed), so the database skips the deduplication pass.

## Bad Example

```sql
-- UNION triggers a deduplication pass that consumes extra CPU/memory
SELECT name FROM t_user_2023
UNION
SELECT name FROM t_user_2024;
```

## Good Example

```sql
-- no deduplication needed: UNION ALL is sufficient and cheaper
SELECT name FROM t_user_2023
UNION ALL
SELECT name FROM t_user_2024;
```
