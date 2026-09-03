---
id: config-explain-timeout
title: explain.timeout
type: reference
status: draft
tags:
- config:optimizer
- integer
description: Time budget the optimizer uses when executing EXPLAIN to gather real
  execution statistics before recommending an index.
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/configs/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Parameter | `explain.timeout` |
| Type | integer |
| Default | 30 |
| Unit | second |
| Scope | optimizer |
| Version Introduced | 8.2.0 |
| Allowed Range | 1.0 .. 300.0 |

## Description

Time budget the optimizer uses when executing EXPLAIN to gather real execution statistics before recommending an index.

## Example

```bash
-- pawsql.conf
explain.timeout = 60
```
