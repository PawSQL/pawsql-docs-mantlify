---
id: en-audit-rule-aud-avoid-crossshard-dml-operations-in-distributed-d
title: Avoid Cross-Shard DML Operations in Distributed Databases
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-crossshard-dml-operations-in-distributed-d
tags:
- audit-rule
- dml
description: DML whose WHERE does not pin the distribution key spans shards and needs
  slow, deadlock-prone distributed transactions; add a distribution-key equality.
localeOf: audit-rule-aud-avoid-crossshard-dml-operations-in-distributed-d
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-crossshard-dml-operations-in-distributed-d
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-crossshard-dml-operations-in-distributed-d |
| Name | Avoid Cross-Shard DML Operations in Distributed Databases |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

A DML operation (such as `UPDATE` or `DELETE`) that touches multiple shards - that is, whose `WHERE` condition does not pin the distribution key - must open a distributed transaction across nodes. Distributed transactions are far slower than single-node transactions and, under high concurrency, easily cause distributed deadlocks.

To keep write performance and transaction success rates high, keep every DML transaction's impact within a single shard: the `WHERE` clause should include an equality condition on the distribution key.

## Bad Example

```sql
-- bad: WHERE has no distribution key; the update may run across shards
UPDATE t_user SET status = 1 WHERE user_id = 100;
```

## Good Example

```sql
-- good: WHERE includes the distribution key so the transaction stays on one shard
UPDATE t_user SET status = 1 WHERE id = 1000;
```
