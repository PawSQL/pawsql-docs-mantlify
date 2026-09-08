---
id: en-audit-rule-aud-avoid-anti-join-operations-in-distributed-databa
title: Avoid ANTI JOIN Operations in Distributed Databases
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-anti-join-operations-in-distributed-databa
tags:
- audit-rule
- dml
description: Avoid NOT IN/NOT EXISTS anti-joins in distributed databases (full-data
  pull + huge memory/network); prefer materialization, split steps, or LEFT JOIN ...
  IS NULL.
localeOf: audit-rule-aud-avoid-anti-join-operations-in-distributed-databa
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-anti-join-operations-in-distributed-databa
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-anti-join-operations-in-distributed-databa |
| Name | Avoid ANTI JOIN Operations in Distributed Databases |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Anti-join queries written with `NOT IN` or `NOT EXISTS` are very hard to optimize in distributed environments. They usually force the full data of both tables to be pulled to the proxy or coordinator node for a Cartesian-style full comparison, with enormous memory and network cost, and can trigger OOM or query timeouts.

Avoid anti-join operations in distributed databases where possible. Reduce the load on distributed compute by materializing incremental data into a temporary table first, splitting the SQL into steps executed in the application layer, or using an alternative such as `LEFT JOIN ... IS NULL`.

## Bad Example

```sql
-- bad: NOT IN subqueries perform very poorly in distributed environments
DELETE FROM t1 WHERE t1.id NOT IN (SELECT t2.id FROM t2);
```

## Good Example

```sql
-- good: split into application-layer steps, or use LEFT JOIN + IS NULL
DELETE t1
FROM t1
LEFT JOIN t2 ON t1.id = t2.id
WHERE t2.id IS NULL;
```
