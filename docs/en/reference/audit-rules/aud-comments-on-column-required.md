---
id: en-audit-rule-aud-comments-on-column-required
title: Comments on Column Required
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Every column needs a COMMENT so its meaning, purpose, and value domain
  stay clear to developers and DBAs across changes and handover.
localeOf: audit-rule-aud-comments-on-column-required
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-comments-on-column-required |
| Name | Comments on Column Required |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

Every column in a table must have a comment (`COMMENT`) to ease later maintenance and team collaboration. A column comment explains the field's meaning, purpose, value domain, and so on, helping developers and DBAs understand the schema and business logic quickly.

Columns without comments raise communication cost and comprehension difficulty during schema changes, troubleshooting, and handover. Good commenting habits are basic database-design literacy.

## Bad Example

```sql
-- bad: the column has no comment; the field's meaning is unclear
CREATE TABLE t_user (
    name VARCHAR(50)
);
```

## Good Example

```sql
-- good: a clear comment on every column
CREATE TABLE t_user (
    name VARCHAR(50) COMMENT '用户姓名'
);
```
