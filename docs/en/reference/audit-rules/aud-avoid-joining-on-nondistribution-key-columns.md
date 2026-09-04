---
id: en-audit-rule-aud-avoid-joining-on-nondistribution-key-columns
title: Avoid Joining on Non-Distribution Key Columns
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Joining on a non-distribution key in a distributed database forces cross-node
  data redistribution and network cost; align high-frequency join keys with the distribution
  key.
localeOf: audit-rule-aud-avoid-joining-on-nondistribution-key-columns
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-joining-on-nondistribution-key-columns |
| Name | Avoid Joining on Non-Distribution Key Columns |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

In distributed databases, when the join columns of a JOIN are not the distribution key (Shard Key), the join may need to move data between nodes (data redistribution): one table's data is broadcast or redistributed onto the nodes holding the other table before the join can complete. That cross-node data transfer creates significant network overhead and becomes a query performance bottleneck.

In real business environments it may be impractical for every join column to be a distribution key, so you must balance table distribution strategy against query performance. Prefer aligning the join columns of high-frequency JOINs with the distribution key so the join completes on local nodes and makes full use of the distributed database's parallel processing.

## Bad Example

```sql
-- bad: join column is not the distribution key; may trigger cross-node redistribution
SELECT * FROM t1 JOIN t2 ON t1.non_shard_key = t2.col;
```

## Good Example

```sql
-- good: join on the distribution key; the join can complete on local nodes
SELECT * FROM t1 JOIN t2 ON t1.shard_key = t2.shard_key;
```
