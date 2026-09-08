---
id: en-audit-rule-aud-pk-naming
title: Primary Key Naming Convention
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-pk-naming
tags:
- audit-rule
- ddl
description: Primary-key constraints should follow one naming convention (e.g. pk_<table>_<columns>)
  so the constraint type and table are recognizable at a glance.
localeOf: audit-rule-aud-pk-naming
subtype: rule
language: en
translationKey: audit-rule-aud-pk-naming
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-pk-naming |
| Name | Primary Key Naming Convention |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | Unverified (database scope not declared) |

## Description

Primary-key constraint names should follow a single naming convention (for example pk_<table>_<columns>) so developers and DBAs can recognize the constraint type and the table it belongs to at a glance. Inconsistent names make schemas harder to read and slow down troubleshooting during schema changes or incident response.

## Why It Matters

Constraint naming is a readability and maintainability concern: a primary key whose name does not reveal its table adds cognitive cost in cross-team work and during database structure changes.

## How to Fix

Name primary-key constraints to match the configured pattern ^pk_{table}_{columns}$, e.g. create the primary key as pk_t_user_id for table t_user. This rule is configurable.

## Bad Example

```sql
CREATE TABLE t_user (
    id BIGINT,
    name VARCHAR(50),
    CONSTRAINT pri_user PRIMARY KEY (id)
);
```

## Good Example

```sql
-- name follows pk_{table}_{columns}, e.g. pk_t_user_id
CREATE TABLE t_user (
    id BIGINT,
    name VARCHAR(50),
    CONSTRAINT pk_t_user_id PRIMARY KEY (id)
);
```
