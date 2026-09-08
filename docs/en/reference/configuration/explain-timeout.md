---
id: config-explain-timeout
translationKey: config-explain-timeout
language: en
title: explain.timeout
type: reference
status: draft
entityRef:
  type: configuration
  id: config-explain-timeout
owners: []
subtype: configuration
layout: detail
product: pawsql
---

| Field | Value |
|---|---|
| Parameter | explain.timeout |
| Type | integer |
| Default | 30 |
| Unit | second |
| Scope | optimizer |
| Activation | unknown |
| Restart required | None |
| Precedence | unknown |
| Range | 1.0 .. 300.0 |

Time budget the optimizer uses when executing EXPLAIN to gather real execution statistics before recommending an index.
```text
-- pawsql.conf
explain.timeout = 60
```
