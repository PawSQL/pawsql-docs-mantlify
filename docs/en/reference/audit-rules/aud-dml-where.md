---
id: audit-rule-aud-dml-where
title: UPDATE/DELETE without WHERE
type: reference
status: draft
tags:
- audit-rule
- dml
- mysql
- postgresql
- oracle
description: Flags UPDATE or DELETE statements that carry no WHERE clause, which would
  affect every row in the target table.
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | AUD-DML-WHERE |
| Name | UPDATE/DELETE without WHERE |
| Category | dml |
| Severity | error |
| Databases | mysql, postgresql, oracle |
| Version Introduced | 8.0.0 |

## Description

Flags UPDATE or DELETE statements that carry no WHERE clause, which would affect every row in the target table.

## Why It Matters

A missing WHERE on a DML statement is a frequent source of data-loss incidents. Flagging it before execution adds a safety gate for high-risk changes.

## How to Fix

Add the intended predicate, or explicitly confirm a full-table operation when it is truly required (for example a controlled bulk reset).

## Bad Example

```sql
UPDATE orders SET status = 'closed';
```

## Good Example

```sql
UPDATE orders SET status = 'closed'
WHERE status = 'open';
```

## Related Rules

`AUD-DML-LIMIT`
