---
id: en-audit-rule-aud-avoid-nondistributed-tables
title: Avoid Non-Distributed Tables
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 'Avoid local/non-distributed tables in distributed databases: they become
  single-node bottlenecks and force redistribution on joins; use HASH distribution.'
localeOf: audit-rule-aud-avoid-nondistributed-tables
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-nondistributed-tables |
| Name | Avoid Non-Distributed Tables |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

In a distributed database, a non-distributed (local) table such as `DISTRIBUTED BY LOCAL` stores its data on a single node, making it a performance bottleneck and a single point of failure. When many queries access the table at once, all requests concentrate on one node and the parallel capabilities of the distributed architecture go unused.

Besides that, joining a non-distributed table with distributed tables usually requires redistributing the distributed table's data onto the local table's node, producing heavy network traffic. Prefer a sound distribution strategy for every business table so the distributed database's horizontal-scaling advantage is fully used.

## Bad Example

```sql
-- bad: creating a local/non-distributed table in a distributed environment
CREATE TABLE large_table (
    id   BIGINT,
    data TEXT
) DISTRIBUTED BY LOCAL;
```

## Good Example

```sql
-- good: HASH distribution spreads data evenly across nodes
CREATE TABLE large_table (
    id   BIGINT,
    data TEXT
) DISTRIBUTED BY HASH (id);
```
