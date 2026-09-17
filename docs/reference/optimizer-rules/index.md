---
id: optimizer-rules-index
title: 优化算法
description: 优化算法：查阅规则条件、示例和限制。
type: reference
subtype: rule
layout: index
status: draft
translationKey: optimizer-rules-index
language: zh
localeOf: en-optimizer-rules-index
product: pawsql
---

共 40 条规则。


## 索引

| 规则 | ID | 严重级别 |
|---|---|---|
| [ORDER子句重排序优化](/reference/optimizer-rules/opt-order-clause-reorder-optimization) | `opt-order-clause-reorder-optimization` | info |

## 查询重写

| 规则 | ID | 严重级别 |
|---|---|---|
| [ALL修饰的子查询重写](/reference/optimizer-rules/opt-all-qualifier-subquery-rewrite) | `opt-all-qualifier-subquery-rewrite` | error |
| [修饰子查询重写优化](/reference/optimizer-rules/opt-anysomeall-subquery-rewrite-optimization) | `opt-anysomeall-subquery-rewrite-optimization` | info |
| [COUNT 标量子查询重写](/reference/optimizer-rules/opt-count-scalar-subquery-rewrite) | `opt-count-scalar-subquery-rewrite` | info |
| [HIVE中COUNT(DISTINCT...) 导致数据倾斜优化](/reference/optimizer-rules/opt-countdistinct-skew-optimization-in-hive) | `opt-countdistinct-skew-optimization-in-hive` | warning |
| [无分组的聚集函数导致的数据倾斜优化](/reference/optimizer-rules/opt-data-skew-optimization-for-aggregate-without-gro) | `opt-data-skew-optimization-for-aggregate-without-gro` | warning |
| [关联字段不均匀导致数据倾斜优化](/reference/optimizer-rules/opt-data-skew-optimization-for-uneven-join-keys) | `opt-data-skew-optimization-for-uneven-join-keys` | warning |
| [条件标量子查询解关联](/reference/optimizer-rules/opt-decorate-correlated-scalar-subqueries) | `opt-decorate-correlated-scalar-subqueries` | info |
| [深分页优化](/reference/optimizer-rules/opt-deep-pagination-optimization) | `opt-deep-pagination-optimization` | warning |
| [派生表转换为Lateral表关联](/reference/optimizer-rules/opt-derived-table-to-lateral-join-conversion) | `opt-derived-table-to-lateral-join-conversion` | info |
| [HIVE中DISTINCT导致的数据倾斜优化](/reference/optimizer-rules/opt-distinct-skew-optimization-in-hive) | `opt-distinct-skew-optimization-in-hive` | warning |
| [子查询中的DISTINCT消除](/reference/optimizer-rules/opt-eliminate-unnecessary-distinct-in-subqueries) | `opt-eliminate-unnecessary-distinct-in-subqueries` | info |
| [EXISTS 查询转换为表连接](/reference/optimizer-rules/opt-exists-subquery-to-table-join-rewrite) | `opt-exists-subquery-to-table-join-rewrite` | info |
| [过滤谓词下推](/reference/optimizer-rules/opt-filter-predicate-pushdown) | `opt-filter-predicate-pushdown` | info |
| [HIVE中全局排序导致的数据倾斜优化](/reference/optimizer-rules/opt-global-sorting-skew-optimization-in-hive) | `opt-global-sorting-skew-optimization-in-hive` | warning |
| [HIVE中分组字段分布不均匀导致数据倾斜优化](/reference/optimizer-rules/opt-group-by-skew-optimization-in-hive) | `opt-group-by-skew-optimization-in-hive` | warning |
| [为分组显式添加空排序(MySQL 5.7)](/reference/optimizer-rules/opt-group-by-with-order-by-null-optimization) | `opt-group-by-with-order-by-null-optimization` | info |
| [HAVING条件下推](/reference/optimizer-rules/opt-having-clause-pushdown-to-where) | `opt-having-clause-pushdown-to-where` | info |
| [IN子查询优化](/reference/optimizer-rules/opt-in-subquery-rewrite-optimization) | `opt-in-subquery-rewrite-optimization` | info |
| [表连接消除](/reference/optimizer-rules/opt-joinelimination) | `opt-joinelimination` | info |
| [LIMIT下推至UNION分支](/reference/optimizer-rules/opt-limit-pushdown-to-union-branches) | `opt-limit-pushdown-to-union-branches` | info |
| [MAX/MIN子查询重写](/reference/optimizer-rules/opt-maxmin-subquery-rewrite) | `opt-maxmin-subquery-rewrite` | info |
| [NPE 重写（空指针异常预防）](/reference/optimizer-rules/opt-npe-rewrite-null-pointer-exception-prevention) | `opt-npe-rewrite-null-pointer-exception-prevention` | warning |
| [OR 条件 SELECT 重写](/reference/optimizer-rules/opt-or-condition-select-rewrite) | `opt-or-condition-select-rewrite` | info |
| [OR条件的UPDELETE重写](/reference/optimizer-rules/opt-or-condition-updatedelete-rewrite) | `opt-or-condition-updatedelete-rewrite` | info |
| [IN子查询中没有LIMIT的排序消除](/reference/optimizer-rules/opt-order-elimination-in-subquery-without-limit) | `opt-order-elimination-in-subquery-without-limit` | info |
| [Hive中过滤谓词下推到表关联之前计算](/reference/optimizer-rules/opt-predicate-pushdown-before-join-in-hive) | `opt-predicate-pushdown-before-join-in-hive` | info |
| [投影下推(PROJECTION PUSHDOWN)](/reference/optimizer-rules/opt-projection-pushdown) | `opt-projection-pushdown` | info |
| [查询折叠(QUERY FOLDING)](/reference/optimizer-rules/opt-query-folding) | `opt-query-folding` | info |
| [无条件的DELETE建议重写为Truncate](/reference/optimizer-rules/opt-rewrite-unconditional-delete-to-truncate) | `opt-rewrite-unconditional-delete-to-truncate` | info |
| [SATTC重写优化](/reference/optimizer-rules/opt-sattc-rewrite-optimization) | `opt-sattc-rewrite-optimization` | info |
| [选择列标量子查询解关联](/reference/optimizer-rules/opt-scalar-subquery-unnesting-in-select-list) | `opt-scalar-subquery-unnesting-in-select-list` | info |
| [UNION ALL统计查询优化](/reference/optimizer-rules/opt-union-all-count-query-optimization) | `opt-union-all-count-query-optimization` | info |
| [UNION常量重写优化](/reference/optimizer-rules/opt-union-constant-rewrite-optimization) | `opt-union-constant-rewrite-optimization` | error |
| [UNION导致的数据倾斜优化](/reference/optimizer-rules/opt-union-skew-optimization-in-hive) | `opt-union-skew-optimization-in-hive` | warning |
| [使用 = 替代 IN（单值）](/reference/optimizer-rules/opt-use-equals-instead-of-in-with-single-value) | `opt-use-equals-instead-of-in-with-single-value` | info |
| [分布式数据库中使用 IN 替代 OR](/reference/optimizer-rules/opt-use-in-instead-of-or-in-distributed-databases) | `opt-use-in-instead-of-or-in-distributed-databases` | info |
| [使用 INSERT...ON DUPLICATE KEY UPDATE 替代 REPLACE 语句](/reference/optimizer-rules/opt-use-insert-on-duplicate-key-update-instead-of-re) | `opt-use-insert-on-duplicate-key-update-instead-of-re` | warning |
| [使用 UNION ALL 代替 UNION](/reference/optimizer-rules/opt-use-union-all-instead-of-union) | `opt-use-union-all-instead-of-union` | info |
| [窗口分区字段分布不均匀导致数据倾斜](/reference/optimizer-rules/opt-winfuncskewedoptimization) | `opt-winfuncskewedoptimization` | warning |
