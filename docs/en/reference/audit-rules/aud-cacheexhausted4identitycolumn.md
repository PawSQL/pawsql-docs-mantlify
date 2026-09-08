---
id: en-audit-rule-aud-cacheexhausted4identitycolumn
title: CacheExhausted4IdentityColumn
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-cacheexhausted4identitycolumn
tags:
- audit-rule
- ddl
description: Warn when an auto-increment/identity column nears its type maximum (default
  80%); plan capacity (e.g. INT to BIGINT) before inserts fail.
localeOf: audit-rule-aud-cacheexhausted4identitycolumn
subtype: rule
language: en
translationKey: audit-rule-aud-cacheexhausted4identitycolumn
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-cacheexhausted4identitycolumn |
| Name | CacheExhausted4IdentityColumn |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

When an auto-increment column's current value approaches its data type's maximum, the sequence is about to be exhausted and later INSERT operations will fail with primary-key conflicts or overflow errors. This is especially damaging on high-write core business tables and can interrupt service.

Monitor and alert early so the risk of exhaustion is found in time, and plan capacity in advance based on usage (for example upgrading the type from INT to BIGINT). The default alert threshold is 80% of the maximum value and is configurable.
