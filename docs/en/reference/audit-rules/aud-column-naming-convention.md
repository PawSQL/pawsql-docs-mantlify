---
id: en-audit-rule-aud-column-naming-convention
title: Column Naming Convention
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Column names should be lowercase snake_case; uppercase, special, keyword,
  or Chinese names hurt readability and cross-platform migration.
localeOf: audit-rule-aud-column-naming-convention
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-column-naming-convention |
| Name | Column Naming Convention |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | All supported databases |

## Description

The column naming convention requires database object names to follow a uniform rule for team collaboration and code maintainability. Column names should typically use lowercase letters and underscores (snake_case) to keep consistency, readability, and cross-platform compatibility.

Non-conforming names (uppercase letters, special characters, keywords, or Chinese characters) raise communication cost and reduce code readability, and cause trouble especially during cross-team work and cross-platform migration.

## Bad Example

```sql
-- bad: uppercase, Chinese, or special characters in column names
CREATE TABLE t_user (
    "UserID"    INT,
    "用户姓名"  VARCHAR(50)
);
```

## Good Example

```sql
-- good: lowercase letters and underscores
CREATE TABLE t_user (
    user_id   INT,
    user_name VARCHAR(50)
);
```
