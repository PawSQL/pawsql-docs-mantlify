---
id: en-optimizer-rule-opt-or-union
title: OR predicate rewrite
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: OPT-OR-UNION
tags:
- optimizer-rule
- rewrite
- mysql
- postgresql
- oracle
description: Preserve NULL semantics and row multiplicity when splitting OR branches,
  then verify performance.
localeOf: optimizer-rule-opt-or-union
subtype: rule
language: en
translationKey: optimizer-rule-opt-or-union
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/optimizer/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | OPT-OR-UNION |
| Name | OR predicate rewrite |
| Category | rewrite — Rewrite |
| Severity | info |
| Databases | mysql, postgresql, oracle |
| Version Introduced | 8.5.0 |
| Implementation | `OrToUnionRule` |

## Description

Splitting OR predicates may enable separate access paths. Benefit depends on the database, data distribution and indexes. These examples describe semantic constraints, not verified PawSQL version or triggering behavior.

## Why It Matters

OR retains input multiplicity. UNION deduplicates, while a simple inequality excludes NULL rows.

## How to Fix

For deterministic predicates, restrict the second branch to rows where the first predicate is not true and combine with UNION ALL. Verify dialect support, semantics and performance before applying.

## Prerequisites

- Branch exclusion must preserve SQL three-valued NULL semantics.

- Preserve row multiplicity; UNION deduplication is not an unconditional replacement for OR.

## Exclusions

- Volatile or side-effecting predicates require separate proof.

## Verification examples

### Normal branch splitting

`postgresql` · `multiset-equal` · `pending`

```sql
CREATE TABLE demo(a integer, b integer);
INSERT INTO demo VALUES (1, 0), (2, 1), (2, 0);
```

```sql
SELECT * FROM demo WHERE a = 1 OR b = 1;
```

```sql
SELECT * FROM demo WHERE a = 1
UNION ALL
SELECT * FROM demo WHERE b = 1 AND (a <> 1 OR a IS NULL);
```

### NULL values, duplicates and overlapping branches

`postgresql` · `multiset-equal` · `pending`

```sql
CREATE TABLE demo(a integer, b integer);
INSERT INTO demo VALUES (NULL, 1), (1, 1), (1, 1), (2, 1), (2, NULL);
```

```sql
SELECT * FROM demo WHERE a = 1 OR b = 1;
```

```sql
SELECT * FROM demo WHERE a = 1
UNION ALL
SELECT * FROM demo WHERE b = 1 AND (a <> 1 OR a IS NULL);
```
