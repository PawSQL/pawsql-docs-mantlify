---
id: en-audit-rule-aud-autoincrement-column-naming-convention
title: Auto-increment column naming convention
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Auto-increment columns should follow one naming pattern (default `id`);
  inconsistent names raise a notice but do not block DDL.
localeOf: audit-rule-aud-autoincrement-column-naming-convention
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-autoincrement-column-naming-convention |
| Name | Auto-increment column naming convention |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | All supported databases |

## Description

This rule defines the naming convention for auto-increment columns: they should follow a clear naming pattern, usually `id`, so teams can recognize auto-increment columns at a glance. Consistent auto-increment column naming noticeably improves ORM integration, automated code generation, and database maintenance.

The default pattern is `id` (regex `^id$`) and can be changed through configuration. Auto-increment columns that do not follow the pattern raise a notice during review but do not block the DDL.

## Bad Example

```sql
-- bad: auto-increment column name does not follow the convention
CREATE TABLE orders (order_auto_id INT AUTO_INCREMENT PRIMARY KEY);
```

## Good Example

```sql
-- good: follows the id naming convention
CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY);
```
