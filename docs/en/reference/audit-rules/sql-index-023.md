---
id: en-audit-rule-sql-index-023
title: Redundant Index Detection
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: SQL-INDEX-023
tags:
- audit-rule
- index
- mysql
- postgresql
description: Detects duplicate or redundant indexes whose leading columns another
  index already covers; they only add write and storage cost, so drop them.
localeOf: audit-rule-sql-index-023
subtype: rule
language: en
translationKey: audit-rule-sql-index-023
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | SQL-INDEX-023 |
| Name | Redundant Index Detection |
| Category | index — Index |
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
-- bad: redundant index; idx_name_dup is covered by idx_full
CREATE INDEX idx_full ON user(name, age, email);
CREATE INDEX idx_name_dup ON user(name);
```

## Good Example

```sql
-- good: only create necessary, non-redundant indexes
CREATE INDEX idx_full ON user(name, age, email);
-- idx_full already serves equality/range lookups on name; no extra index needed
```

## Related Rules

`SQL-INDEX-UNUSED`, `SQL-INDEX-DUPLICATE`
