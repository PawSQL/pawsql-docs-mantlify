---
id: en-audit-rule-aud-insert-must-include-pk
title: INSERT Must Include Primary Key Column
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-insert-must-include-pk
tags:
- audit-rule
- dml
description: On tables without an auto-increment primary key, INSERT must supply the
  key explicitly to avoid duplicate or unexpected key values and data inconsistency.
localeOf: audit-rule-aud-insert-must-include-pk
subtype: rule
language: en
translationKey: audit-rule-aud-insert-must-include-pk
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-insert-must-include-pk |
| Name | INSERT Must Include Primary Key Column |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

For tables without an auto-increment primary key, INSERT statements should supply the primary-key value explicitly. Even when the primary-key column has a default value, omitting it can produce duplicates or values that do not match business expectations; in production, such statements risk primary-key conflicts and data inconsistency.

## How to Fix

Add the primary-key column to the INSERT column list and provide an explicit value.

## Bad Example

```sql
-- t has a non-auto-increment primary key, but INSERT omits it
INSERT INTO user (name) VALUES ('张三');
```

## Good Example

```sql
-- supply the primary-key value explicitly
INSERT INTO user (id, name) VALUES (1, '张三');
```
