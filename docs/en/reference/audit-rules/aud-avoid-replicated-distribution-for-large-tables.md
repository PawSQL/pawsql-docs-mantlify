---
id: en-audit-rule-aud-avoid-replicated-distribution-for-large-tables
title: Avoid Replicated Distribution for Large Tables
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-replicated-distribution-for-large-tables
tags:
- audit-rule
- ddl
description: Replicated distribution copies a table to every node; above the size
  threshold (default 100k rows) use HASH/sharded distribution instead.
localeOf: audit-rule-aud-avoid-replicated-distribution-for-large-tables
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-replicated-distribution-for-large-tables
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-replicated-distribution-for-large-tables |
| Name | Avoid Replicated Distribution for Large Tables |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

In a distributed database, replicated distribution copies the full table to every node in the cluster. For small tables this removes cross-node data exchange and improves JOIN performance; but for large tables it multiplies storage cost (storage size = data size x node count) and every write must be replicated to all nodes, losing the advantage of distributed parallel computing.

This rule requires that once a table's row count exceeds the threshold (100,000 rows by default), REPLICATED distribution must not be used; use HASH or another sharding strategy so data is spread evenly and the architecture's scaling capability is fully used.

## Bad Example

```sql
-- bad: replicated distribution on a large table is costly and loses distributed benefits
CREATE TABLE large_table (
    id BIGINT,
    data TEXT
) DISTRIBUTED BY REPLICATION;
```

## Good Example

```sql
-- good: HASH distribution spreads a large table evenly across nodes
CREATE TABLE large_table (
    id BIGINT,
    data TEXT
) DISTRIBUTED BY HASH(id);
```
