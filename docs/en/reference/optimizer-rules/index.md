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

40 rules.


## Index

| Rule | ID | Severity |
|---|---|---|
| [ORDER Clause Reorder Optimization](/en/reference/optimizer-rules/opt-order-clause-reorder-optimization) | `opt-order-clause-reorder-optimization` | info |

## Query Rewrite

| Rule | ID | Severity |
|---|---|---|
| [All Qualifier Subquery Rewrite](/en/reference/optimizer-rules/opt-all-qualifier-subquery-rewrite) | `opt-all-qualifier-subquery-rewrite` | error |
| [ANY/SOME/ALL Subquery Rewrite Optimization](/en/reference/optimizer-rules/opt-anysomeall-subquery-rewrite-optimization) | `opt-anysomeall-subquery-rewrite-optimization` | info |
| [COUNT Scalar Subquery Rewrite](/en/reference/optimizer-rules/opt-count-scalar-subquery-rewrite) | `opt-count-scalar-subquery-rewrite` | info |
| [COUNT(DISTINCT) Skew Optimization in Hive](/en/reference/optimizer-rules/opt-countdistinct-skew-optimization-in-hive) | `opt-countdistinct-skew-optimization-in-hive` | warning |
| [Data Skew Optimization for Aggregate Without GROUP BY](/en/reference/optimizer-rules/opt-data-skew-optimization-for-aggregate-without-gro) | `opt-data-skew-optimization-for-aggregate-without-gro` | warning |
| [Data Skew Optimization for Uneven Join Keys](/en/reference/optimizer-rules/opt-data-skew-optimization-for-uneven-join-keys) | `opt-data-skew-optimization-for-uneven-join-keys` | warning |
| [Decorate Correlated Scalar Subqueries](/en/reference/optimizer-rules/opt-decorate-correlated-scalar-subqueries) | `opt-decorate-correlated-scalar-subqueries` | info |
| [Deep Pagination Optimization](/en/reference/optimizer-rules/opt-deep-pagination-optimization) | `opt-deep-pagination-optimization` | warning |
| [Derived Table to LATERAL Join Conversion](/en/reference/optimizer-rules/opt-derived-table-to-lateral-join-conversion) | `opt-derived-table-to-lateral-join-conversion` | info |
| [DISTINCT Skew Optimization in Hive](/en/reference/optimizer-rules/opt-distinct-skew-optimization-in-hive) | `opt-distinct-skew-optimization-in-hive` | warning |
| [Eliminate Unnecessary DISTINCT in Subqueries](/en/reference/optimizer-rules/opt-eliminate-unnecessary-distinct-in-subqueries) | `opt-eliminate-unnecessary-distinct-in-subqueries` | info |
| [EXISTS Subquery to Table Join Rewrite](/en/reference/optimizer-rules/opt-exists-subquery-to-table-join-rewrite) | `opt-exists-subquery-to-table-join-rewrite` | info |
| [Filter Predicate Pushdown](/en/reference/optimizer-rules/opt-filter-predicate-pushdown) | `opt-filter-predicate-pushdown` | info |
| [Global Sorting Skew Optimization in Hive](/en/reference/optimizer-rules/opt-global-sorting-skew-optimization-in-hive) | `opt-global-sorting-skew-optimization-in-hive` | warning |
| [Group By Skew Optimization in Hive](/en/reference/optimizer-rules/opt-group-by-skew-optimization-in-hive) | `opt-group-by-skew-optimization-in-hive` | warning |
| [GROUP BY with ORDER BY NULL Optimization](/en/reference/optimizer-rules/opt-group-by-with-order-by-null-optimization) | `opt-group-by-with-order-by-null-optimization` | info |
| [HAVING Clause Pushdown to WHERE](/en/reference/optimizer-rules/opt-having-clause-pushdown-to-where) | `opt-having-clause-pushdown-to-where` | info |
| [IN Subquery Rewrite Optimization](/en/reference/optimizer-rules/opt-in-subquery-rewrite-optimization) | `opt-in-subquery-rewrite-optimization` | info |
| [JoinElimination](/en/reference/optimizer-rules/opt-joinelimination) | `opt-joinelimination` | info |
| [LIMIT Pushdown to UNION Branches](/en/reference/optimizer-rules/opt-limit-pushdown-to-union-branches) | `opt-limit-pushdown-to-union-branches` | info |
| [MAX/MIN Subquery Rewrite](/en/reference/optimizer-rules/opt-maxmin-subquery-rewrite) | `opt-maxmin-subquery-rewrite` | info |
| [NPE Rewrite (Null Pointer Exception Prevention)](/en/reference/optimizer-rules/opt-npe-rewrite-null-pointer-exception-prevention) | `opt-npe-rewrite-null-pointer-exception-prevention` | warning |
| [OR predicate rewrite](/en/reference/optimizer-rules/opt-or-condition-select-rewrite) | `opt-or-condition-select-rewrite` | info |
| [OR Condition UPDATE/DELETE Rewrite](/en/reference/optimizer-rules/opt-or-condition-updatedelete-rewrite) | `opt-or-condition-updatedelete-rewrite` | info |
| [Order Elimination in Subquery Without LIMIT](/en/reference/optimizer-rules/opt-order-elimination-in-subquery-without-limit) | `opt-order-elimination-in-subquery-without-limit` | info |
| [Predicate Pushdown Before Join in Hive](/en/reference/optimizer-rules/opt-predicate-pushdown-before-join-in-hive) | `opt-predicate-pushdown-before-join-in-hive` | info |
| [Projection Pushdown](/en/reference/optimizer-rules/opt-projection-pushdown) | `opt-projection-pushdown` | info |
| [Query Folding](/en/reference/optimizer-rules/opt-query-folding) | `opt-query-folding` | info |
| [Rewrite Unconditional DELETE to TRUNCATE](/en/reference/optimizer-rules/opt-rewrite-unconditional-delete-to-truncate) | `opt-rewrite-unconditional-delete-to-truncate` | info |
| [SATTC Rewrite Optimization](/en/reference/optimizer-rules/opt-sattc-rewrite-optimization) | `opt-sattc-rewrite-optimization` | info |
| [Scalar Subquery Unnesting in Select List](/en/reference/optimizer-rules/opt-scalar-subquery-unnesting-in-select-list) | `opt-scalar-subquery-unnesting-in-select-list` | info |
| [UNION ALL Count Query Optimization](/en/reference/optimizer-rules/opt-union-all-count-query-optimization) | `opt-union-all-count-query-optimization` | info |
| [Union Constant Rewrite Optimization](/en/reference/optimizer-rules/opt-union-constant-rewrite-optimization) | `opt-union-constant-rewrite-optimization` | error |
| [UNION Skew Optimization in Hive](/en/reference/optimizer-rules/opt-union-skew-optimization-in-hive) | `opt-union-skew-optimization-in-hive` | warning |
| [Use Equals Instead of IN with Single Value](/en/reference/optimizer-rules/opt-use-equals-instead-of-in-with-single-value) | `opt-use-equals-instead-of-in-with-single-value` | info |
| [Use IN Instead of OR in Distributed Databases](/en/reference/optimizer-rules/opt-use-in-instead-of-or-in-distributed-databases) | `opt-use-in-instead-of-or-in-distributed-databases` | info |
| [Use INSERT ON DUPLICATE KEY UPDATE Instead of REPLACE](/en/reference/optimizer-rules/opt-use-insert-on-duplicate-key-update-instead-of-re) | `opt-use-insert-on-duplicate-key-update-instead-of-re` | warning |
| [Use UNION ALL Instead of UNION](/en/reference/optimizer-rules/opt-use-union-all-instead-of-union) | `opt-use-union-all-instead-of-union` | info |
| [WinFuncSkewedOptimization](/en/reference/optimizer-rules/opt-winfuncskewedoptimization) | `opt-winfuncskewedoptimization` | warning |
