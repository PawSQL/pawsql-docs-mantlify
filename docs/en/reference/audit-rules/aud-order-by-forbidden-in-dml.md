---
id: en-audit-rule-aud-order-by-forbidden-in-dml
title: ORDER BY Forbidden in UPDATE/DELETE
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-order-by-forbidden-in-dml
tags:
- audit-rule
- dml
description: ORDER BY is meaningless in UPDATE/DELETE, adds cost, and is a syntax
  error in some databases; remove it or move the ordered selection into a subquery.
localeOf: audit-rule-aud-order-by-forbidden-in-dml
subtype: rule
language: en
translationKey: audit-rule-aud-order-by-forbidden-in-dml
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-order-by-forbidden-in-dml |
| Name | ORDER BY Forbidden in UPDATE/DELETE |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

ORDER BY is usually meaningless in UPDATE or DELETE statements: the goal of a DML statement is to change data, not to return an ordered result set. Sorting adds unnecessary cost and can worsen the execution plan. In some databases (for example PostgreSQL) DELETE ... ORDER BY is even a syntax error unless combined with LIMIT, so the statement would fail outright.

## How to Fix

Remove the pointless ORDER BY from the DML statement. When ordering is actually needed to pick rows (for example the first N by some key), move the ordered selection into a subquery and drive the DML with a WHERE IN (...).

## Bad Example

```sql
-- DELETE/UPDATE with an ORDER BY that adds no value
DELETE FROM t ORDER BY id LIMIT 10;
UPDATE t SET status = 1 ORDER BY created_at;
```

## Good Example

```sql
-- pick the rows in a subquery, then run the DML without ORDER BY
DELETE FROM t WHERE id IN (SELECT id FROM t ORDER BY id LIMIT 10);
UPDATE t SET status = 1 WHERE id IN (
    SELECT id FROM t WHERE status = 0 ORDER BY created_at LIMIT 100
);
```
