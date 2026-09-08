---
id: en-audit-rule-aud-charsetsontabledatabasemismatch
title: CharsetsOnTable&DatabaseMismatch
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-charsetsontabledatabasemismatch
tags:
- audit-rule
- ddl
description: Table and database character sets must match to avoid implicit conversion,
  mojibake, or data loss; tables should inherit the database default charset.
localeOf: audit-rule-aud-charsetsontabledatabasemismatch
subtype: rule
language: en
translationKey: audit-rule-aud-charsetsontabledatabasemismatch
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-charsetsontabledatabasemismatch |
| Name | CharsetsOnTable&DatabaseMismatch |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

This rule requires a table's character set to match the database's, to avoid the data problems caused by inconsistency. When they differ, cross-table queries or data migrations may trigger an implicit character-set conversion, increasing CPU cost, hurting index efficiency, and in severe cases causing mojibake or data loss.

Prefer not to specify a charset when creating a table so it inherits the database default automatically. If you must specify one, make sure it exactly matches the database.

## Bad Example

```sql
-- bad: table charset differs from the database's
-- assume the database charset is utf8mb4
CREATE TABLE t (id INT) DEFAULT CHARSET = latin1;
```

## Good Example

```sql
-- good: inherit the database default charset so they stay consistent
CREATE TABLE t (id INT);
```
