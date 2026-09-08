---
id: en-audit-rule-aud-avoid-order-by-random-function
title: Avoid ORDER BY Random Function
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-order-by-random-function
tags:
- audit-rule
- dml
description: ORDER BY RAND()/RANDOM() sorts every row just to keep a few; sample via
  a random key range or TABLESAMPLE instead.
localeOf: audit-rule-aud-avoid-order-by-random-function
subtype: rule
language: en
translationKey: audit-rule-aud-avoid-order-by-random-function
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-order-by-random-function |
| Name | Avoid ORDER BY Random Function |
| Category | dml — DML / data modification |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

MySQL's `RAND()` and PostgreSQL's `RANDOM()` return a random float between 0 and 1.0. Some developers use `ORDER BY RAND() LIMIT N` to fetch a random sample of a data set. This works acceptably below about 10,000 rows, but on tables with millions of rows the cost becomes unacceptable - the database must compute a random value for every row, sort all of them, and then keep only a tiny few.

Far more efficient ways to sample randomly exist, for example filtering on a random primary-key range or using table sampling (TABLESAMPLE). See [details](https://app.pawsql.com/docs/rule/RuleOrderByRandomWarning) for this optimization.

## Bad Example

```sql
-- bad: computing and sorting a random value for every row is very slow
select * from orders order by rand() limit 1;
```

## Good Example

```sql
-- good: sample efficiently, for example from a random primary-key range
-- assume id ranges from 1 to 1000000
select * from orders where id >= (select floor(rand() * max(id)) from orders) limit 1;
```
