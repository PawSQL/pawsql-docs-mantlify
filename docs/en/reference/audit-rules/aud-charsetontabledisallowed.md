---
id: en-audit-rule-aud-charsetontabledisallowed
title: CharsetOnTableDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Do not override the character set at table level; tables should inherit
  the database default to avoid cross-table implicit conversion.
localeOf: audit-rule-aud-charsetontabledisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-charsetontabledisallowed |
| Name | CharsetOnTableDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

Setting a character set at table definition time is disallowed, to avoid the data problems caused when a table-level charset differs from the database charset. When they differ, cross-table operations may need an implicit character-set conversion, hurting query performance and possibly producing mojibake.

Character sets should be managed at the database (or column) level; tables should inherit the database default rather than override it at the table level.

## Bad Example

```sql
-- bad: table-level charset may differ from the database's
CREATE TABLE t (id INT) DEFAULT CHARSET = utf8;
```

## Good Example

```sql
-- good: inherit the database default charset, do not set it per table
CREATE TABLE t (id INT);
```
