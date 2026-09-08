---
id: en-audit-rule-aud-avoid-limit-without-order-by-in-updatedelete
title: Avoid LIMIT Without ORDER BY in UPDATE/DELETE
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-limit-without-order-by-in-updatedelete
tags:
- audit-rule
- dml
description: UPDATE/DELETE ... LIMIT without ORDER BY touches nondeterministic rows;
  pair LIMIT with ORDER BY (or a WHERE subquery on PostgreSQL/openGauss).
localeOf: audit-rule-aud-avoid-limit-without-order-by-in-updatedelete
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-limit-without-order-by-in-updatedelete
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-limit-without-order-by-in-updatedelete |
| Name | Avoid LIMIT Without ORDER BY in UPDATE/DELETE |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Using `LIMIT` in an `UPDATE` or `DELETE` without `ORDER BY` makes the affected rows nondeterministic on every run. With no ordering instruction, databases do not guarantee the order in which rows are processed, so `UPDATE/DELETE ... LIMIT N` can touch a different N rows each time.

This is especially dangerous for data cleanup and batched processing - developers expect rows to be handled in some order, but the actual rows are effectively random. Always pair `LIMIT` with `ORDER BY` so operations are predictable and data stays safe.

> Note: PostgreSQL/openGauss do not support `ORDER BY` inside UPDATE or DELETE; in those databases, locate the target rows with a `WHERE` subquery instead.

## Bad Example

```sql
-- bad: LIMIT without ORDER BY; which rows get deleted is nondeterministic
DELETE FROM t WHERE status = 0 LIMIT 10;
```

## Good Example

```sql
-- good: with ORDER BY, batched processing is stable and predictable
DELETE FROM t WHERE status = 0 ORDER BY created_at LIMIT 10;
```
