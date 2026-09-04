---
id: en-audit-rule-aud-consider-replicated-distribution-for-small-table
title: Consider Replicated Distribution for Small Tables
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Small distributed tables (below ~100k rows, read-heavy) are often better
  as replicated tables so joins avoid cross-node data exchange.
localeOf: audit-rule-aud-consider-replicated-distribution-for-small-table
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-consider-replicated-distribution-for-small-table |
| Name | Consider Replicated Distribution for Small Tables |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | All supported databases |

## Description

In a distributed database, a table's distribution method (sharded vs. replicated) strongly affects query performance. When a sharding table is small but stays sharded, joining it with other tables - especially with a non-equi-join - can degrade performance because of cross-node data exchange. Making such small tables replicated tables instead (a full copy on every node) removes cross-node data exchange and improves query performance.

This rule inspects multi-table join scenarios, analyzes join conditions and row counts, and automatically identifies small tables that would be better as replicated tables. Prefer the replicated strategy for tables below 100,000 rows that are read-heavy and write-light.

## Bad Example

```sql
-- bad: a small sharded table; a non-equi join causes cross-node data transfer
SELECT * FROM t1, t2 WHERE t1.amount > t2.threshold;
```

## Good Example

```sql
-- good: make t1 a replicated table to remove cross-node data transfer
-- (t1 becomes: CREATE TABLE t1 (...) DISTRIBUTED BY REPLICATION;)
```
