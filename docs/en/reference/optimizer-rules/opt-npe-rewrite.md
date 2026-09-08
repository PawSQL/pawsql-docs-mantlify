---
id: en-optimizer-rule-opt-npe-rewrite
title: NPE Rewrite (Null Pointer Exception Prevention)
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-npe-rewrite
tags:
- optimizer-rule
- rewrite
description: Wraps aggregates that can return NULL on all-NULL input (e.g. SUM) in
  a null-handling function so the result is always numeric and apps avoid NPE.
localeOf: optimizer-rule-opt-npe-rewrite
subtype: rule
language: en
translationKey: optimizer-rule-opt-npe-rewrite
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/optimizer/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | opt-npe-rewrite |
| Name | NPE Rewrite (Null Pointer Exception Prevention) |
| Category | rewrite — Rewrite |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

A Null Pointer Exception (NPE) risk appears in SQL when an aggregate column is entirely NULL: functions such as SUM or AVG return NULL instead of a numeric zero. If the application (Java, Python, ...) feeds that NULL straight into arithmetic, it can raise an NPE. PawSQL detects this pattern and wraps the aggregate in a null-handling function so the result is always numeric.

## How to Fix

Wrap the aggregate in the database's null-handling function so the result is 0 instead of NULL when the input is all NULL: NVL() on Oracle, ISNULL() on SQL Server, IFNULL() or COALESCE() on MySQL; COALESCE() is the portable choice.

## Bad Example

```sql
-- when t.b is all NULL, SUM returns NULL and may trigger an NPE in the app
SELECT SUM(t.b) FROM (VALUES ROW(1, NULL)) AS t(a, b);
```

## Good Example

```sql
-- guarantee 0 instead of NULL
SELECT IFNULL(SUM(t.b), 0) FROM (VALUES ROW(1, NULL)) AS t(a, b);
-- Oracle: SELECT NVL(SUM(t.b), 0) FROM ...;
-- SQL Server: SELECT ISNULL(SUM(t.b), 0) FROM ...;
-- portable: SELECT COALESCE(SUM(t.b), 0) FROM ...;
```
