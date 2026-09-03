---
id: audit-rule-sql-index-023
title: Redundant Index Detection
type: reference
status: draft
tags:
- audit-rule
- index
- mysql
- postgresql
description: Detects an index whose leading columns are already covered by another
  index, making the shorter one redundant for reads and a pure cost for writes.
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | SQL-INDEX-023 |
| Name | Redundant Index Detection |
| Category | index |
| Severity | warning |
| Databases | mysql, postgresql |
| Version Introduced | 8.4.0 |
| Implementation | `RedundantIndexRule` |

## Description

Detects an index whose leading columns are already covered by another index, making the shorter one redundant for reads and a pure cost for writes.

## Why It Matters

Every redundant index still consumes disk and must be maintained on writes, slowing down DML without helping any query. Removing it reduces write cost and storage without losing read performance.

## How to Fix

Drop the index that is a strict prefix of another index. Keep the longer index if it serves the workload; when unsure, verify with the query plan before dropping.

## Bad Example

```sql
CREATE INDEX idx_a   ON t (a);
CREATE INDEX idx_ab  ON t (a, b);
```

## Good Example

```sql
-- idx_a is redundant because idx_ab already covers (a)
CREATE INDEX idx_ab ON t (a, b);
```

## Related Rules

`SQL-INDEX-UNUSED`, `SQL-INDEX-DUPLICATE`
