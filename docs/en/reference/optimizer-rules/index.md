---
id: en-optimizer-rules-index
title: Optimizer Rule Reference
description: 'Optimizer Rule Reference: conditions, examples and limitations.'
type: reference
subtype: rule
layout: index
status: draft
translationKey: optimizer-rules-index
language: en
localeOf: optimizer-rules-index
product: pawsql
---

5 rules.

| Rule | ID | Category | Severity |
|---|---|---|---|
| [OR predicate rewrite](/en/reference/optimizer-rules/opt-or-union) | `OPT-OR-UNION` | rewrite | info |
| [COUNT Scalar Subquery Rewrite](/en/reference/optimizer-rules/opt-count-to-exists) | `opt-count-to-exists` | rewrite | info |
| [EXISTS Subquery to Table Join Rewrite](/en/reference/optimizer-rules/opt-exists-to-join) | `opt-exists-to-join` | rewrite | info |
| [NPE Rewrite (Null Pointer Exception Prevention)](/en/reference/optimizer-rules/opt-npe-rewrite) | `opt-npe-rewrite` | rewrite | warning |
| [Use UNION ALL Instead of UNION](/en/reference/optimizer-rules/opt-use-union-all) | `opt-use-union-all` | rewrite | info |
