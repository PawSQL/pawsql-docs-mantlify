---
id: en-audit-rule-aud-avoid-multiple-distribution-keys
title: Avoid Multiple Distribution Keys
type: reference
status: draft
tags:
- audit-rule
- ddl
description: Multiple-column distribution keys limit horizontal scaling, raise hashing
  cost, and block local joins unless every key matches; prefer a single, frequently-joined
  column.
localeOf: audit-rule-aud-avoid-multiple-distribution-keys
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-multiple-distribution-keys |
| Name | Avoid Multiple Distribution Keys |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

Using multiple columns as the distribution key restricts the table's horizontal scalability and hurts sharding flexibility and routing efficiency. A multi-column distribution key raises hash-computation complexity, and table joins only localize when every distribution-key column matches, making it harder for the optimizer to build efficient plans.

Multi-column distribution keys also increase the cost of moving data between nodes, because redistribution must be computed over all distribution-key columns. Prefer a single-column distribution key, ideally the column most frequently used as a join key in queries.

## Bad Example

```sql
-- bad: multiple columns as the distribution key
CREATE TABLE t_sales (
    region    VARCHAR(50),
    product   VARCHAR(50),
    amount    DECIMAL(10, 2)
) DISTRIBUTED BY HASH (region, product);
```

## Good Example

```sql
-- good: a single column as the distribution key
CREATE TABLE t_sales (
    region    VARCHAR(50),
    product   VARCHAR(50),
    amount    DECIMAL(10, 2)
) DISTRIBUTED BY HASH (region);
```
