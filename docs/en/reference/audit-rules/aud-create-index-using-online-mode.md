---
id: en-audit-rule-aud-create-index-using-online-mode
title: Create Index Using Online Mode
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-create-index-using-online-mode
tags:
- audit-rule
- ddl
description: Create indexes online (MySQL ALGORITHM=INPLACE LOCK=NONE, PostgreSQL
  CONCURRENTLY) to avoid long locks and DML blocking on large tables.
localeOf: audit-rule-aud-create-index-using-online-mode
subtype: rule
language: en
translationKey: audit-rule-aud-create-index-using-online-mode
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-create-index-using-online-mode |
| Name | Create Index Using Online Mode |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Create indexes in online mode (for example `ALGORITHM=INPLACE, LOCK=NONE` on MySQL or `CONCURRENTLY` on PostgreSQL) because online mode sharply reduces lock-hold time and the risk of blocking business during index creation, limits impact on read/write traffic, and makes change windows more controllable.

The traditional offline approach takes an exclusive lock on the target table for the whole operation and blocks all DML. On large tables index creation can last minutes or hours, causing a long business outage. Online mode avoids that, but assess the resource cost against concurrent load and log/rollback-segment capacity.

## Bad Example

```sql
-- bad: traditional index creation may lock the table and block DML while running
CREATE INDEX idx_name ON large_table(name);
```

## Good Example

```sql
-- good: online DDL does not block concurrent reads and writes
ALTER TABLE large_table ADD INDEX idx_name(name), ALGORITHM=INPLACE, LOCK=NONE;

-- good (PostgreSQL): use the CONCURRENTLY mode
CREATE INDEX CONCURRENTLY idx_name ON large_table(name);
```
