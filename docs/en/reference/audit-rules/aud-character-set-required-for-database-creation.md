---
id: en-audit-rule-aud-character-set-required-for-database-creation
title: Character Set Required for Database Creation
type: reference
status: draft
tags:
- audit-rule
- ddl
description: CREATE DATABASE must set the character set explicitly so defaults do
  not vary by environment and cause mojibake across deployments.
localeOf: audit-rule-aud-character-set-required-for-database-creation
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-character-set-required-for-database-creation |
| Name | Character Set Required for Database Creation |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

When creating a database you must set the character set explicitly to keep data consistent and compatible. If no character set is given, the database uses its default configuration, which can vary with environment, version, or installation, leading to mojibake or inconsistent collation across environments.

Setting the character set explicitly (for example `utf8mb4`) avoids character-encoding problems at storage time and matters most for multi-language workloads.

## Bad Example

```sql
-- bad: creating a database without a character set
CREATE DATABASE mydb;
```

## Good Example

```sql
-- good: creating a database with an explicit character set
CREATE DATABASE mydb DEFAULT CHARACTER SET utf8mb4;
```
