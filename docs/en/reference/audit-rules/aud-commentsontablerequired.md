---
id: en-audit-rule-aud-commentsontablerequired
title: CommentsOnTableRequired
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-commentsontablerequired
tags:
- audit-rule
- ddl
description: CREATE TABLE should carry a table COMMENT (business purpose, data source,
  lifecycle); applies to engines supporting table comments such as MySQL.
localeOf: audit-rule-aud-commentsontablerequired
subtype: rule
language: en
translationKey: audit-rule-aud-commentsontablerequired
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-commentsontablerequired |
| Name | CommentsOnTableRequired |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

A table must carry a comment (`COMMENT`) when it is created. A thorough table comment helps developers and maintainers quickly understand the table's purpose, field meanings, and business logic, improving code readability and team collaboration. In production, tables without comments raise communication cost noticeably during handover and maintenance.

This rule applies to databases that support table comments, such as MySQL. The comment should describe the table's business purpose, data source, and lifecycle.

## Bad Example

```sql
-- bad: the table has no comment
CREATE TABLE t (id INT);
```

## Good Example

```sql
-- good: comment on the table at creation
CREATE TABLE t (id INT) COMMENT = '用户信息表，记录系统注册用户的基本资料';
```
