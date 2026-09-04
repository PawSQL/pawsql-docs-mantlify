---
id: en-optimizer-rule-opt-or-union
title: OR to UNION Optimization
type: reference
status: draft
tags:
- optimizer-rule
- rewrite
- mysql
- postgresql
- oracle
description: Rewrites OR-ed predicates over different columns into UNION / UNION ALL
  branches so each branch can use its own index instead of one fused plan.
localeOf: optimizer-rule-opt-or-union
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/optimizer/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | OPT-OR-UNION |
| Name | OR to UNION Optimization |
| Category | rewrite — Rewrite |
| Severity | info |
| Databases | mysql, postgresql, oracle |
| Version Introduced | 8.5.0 |
| Implementation | `OrToUnionRule` |

## Description

Rewrites queries whose WHERE clause combines OR-ed predicates so the planner can consider separate access paths per branch, instead of one fused plan.

## Why It Matters

When OR-ed branches involve different columns, a single-table plan cannot use an index per branch efficiently. Splitting the branches lets each one pick its own best index, and UNION ALL merges the results when the branches are provably disjoint.

## How to Fix

No manual action: PawSQL applies the rewrite automatically when it is safe. The rule is cost-based and only triggers when the rewritten plan is expected to be cheaper.

## Bad Example

```sql
-- bad: OR over different columns may force a full table scan
SELECT * FROM lineitem
WHERE l_shipdate = DATE '2010-12-01' OR l_partkey < 100;
```

## Good Example

```sql
-- good: rewritten as UNION so each branch uses its own index
SELECT * FROM lineitem WHERE l_shipdate = DATE '2010-12-01'
UNION
SELECT * FROM lineitem WHERE l_partkey < 100;

-- good: when OR branches are disjoint, UNION ALL is cheaper
SELECT * FROM lineitem WHERE l_shipdate = DATE '2010-12-01'
UNION ALL
SELECT * FROM lineitem WHERE l_partkey < 100 AND l_shipdate <> DATE '2010-12-01';
```
