---
id: en-audit-rules-index
title: Audit Rule Reference
description: Catalog of PawSQL SQL audit rules (generated)
type: reference
status: draft
tags:
- audit-rules
- en
localeOf: audit-rules-index
---

> Generated: aggregated from the rule pages. Do not edit by hand; re-run the index helper after rule additions.

# Audit Rule Reference

## Overview

54 rules.

| Rule | ID |
|---|---|
| [Add Schema Qualifier Before Object References](en/reference/audit-rules/aud-add-schema-qualifier-before-object-references) | `aud-add-schema-qualifier-before-object-references` |
| [AddCheckConstraintShouldBeDeferred](en/reference/audit-rules/aud-addcheckconstraintshouldbedeferred) | `aud-addcheckconstraintshouldbedeferred` |
| [AddingColumnsWithDefaultDisallowed](en/reference/audit-rules/aud-addingcolumnswithdefaultdisallowed) | `aud-addingcolumnswithdefaultdisallowed` |
| [Auto-increment column naming convention](en/reference/audit-rules/aud-autoincrement-column-naming-convention) | `aud-autoincrement-column-naming-convention` |
| [Avoid ANTI JOIN Operations in Distributed Databases](en/reference/audit-rules/aud-avoid-anti-join-operations-in-distributed-databa) | `aud-avoid-anti-join-operations-in-distributed-databa` |
| [Avoid COUNT DISTINCT on Multiple Nullable Columns](en/reference/audit-rules/aud-avoid-count-distinct-on-multiple-nullable-column) | `aud-avoid-count-distinct-on-multiple-nullable-column` |
| [Avoid CROSS JOIN](en/reference/audit-rules/aud-avoid-cross-join) | `aud-avoid-cross-join` |
| [Avoid Cross-Shard DML Operations in Distributed Databases](en/reference/audit-rules/aud-avoid-crossshard-dml-operations-in-distributed-d) | `aud-avoid-crossshard-dml-operations-in-distributed-d` |
| [Avoid Duplicate Table Aliases](en/reference/audit-rules/aud-avoid-duplicate-table-aliases) | `aud-avoid-duplicate-table-aliases` |
| [Avoid FOR UPDATE with Derived Tables](en/reference/audit-rules/aud-avoid-for-update-with-derived-tables) | `aud-avoid-for-update-with-derived-tables` |
| [Avoid GROUP BY Column Ordinal Position](en/reference/audit-rules/aud-avoid-group-by-column-ordinal-position) | `aud-avoid-group-by-column-ordinal-position` |
| [Avoid GROUP BY on Long Columns](en/reference/audit-rules/aud-avoid-group-by-on-long-columns) | `aud-avoid-group-by-on-long-columns` |
| [Avoid Joining on Non-Distribution Key Columns](en/reference/audit-rules/aud-avoid-joining-on-nondistribution-key-columns) | `aud-avoid-joining-on-nondistribution-key-columns` |
| [Avoid Leading or Trailing Spaces in String Literals](en/reference/audit-rules/aud-avoid-leading-or-trailing-spaces-in-string-liter) | `aud-avoid-leading-or-trailing-spaces-in-string-liter` |
| [Avoid LIKE Without Wildcards](en/reference/audit-rules/aud-avoid-like-without-wildcards) | `aud-avoid-like-without-wildcards` |
| [Avoid LIMIT Without ORDER BY in SELECT](en/reference/audit-rules/aud-avoid-limit-without-order-by-in-select) | `aud-avoid-limit-without-order-by-in-select` |
| [Avoid LIMIT Without ORDER BY in UPDATE/DELETE](en/reference/audit-rules/aud-avoid-limit-without-order-by-in-updatedelete) | `aud-avoid-limit-without-order-by-in-updatedelete` |
| [Avoid Multiple Distribution Keys](en/reference/audit-rules/aud-avoid-multiple-distribution-keys) | `aud-avoid-multiple-distribution-keys` |
| [Avoid NATURAL JOIN](en/reference/audit-rules/aud-avoid-natural-join) | `aud-avoid-natural-join` |
| [Avoid Non-Distributed Tables](en/reference/audit-rules/aud-avoid-nondistributed-tables) | `aud-avoid-nondistributed-tables` |
| [Avoid ORDER BY Column Ordinal Position](en/reference/audit-rules/aud-avoid-order-by-column-ordinal-position) | `aud-avoid-order-by-column-ordinal-position` |
| [Avoid ORDER BY on Long Columns](en/reference/audit-rules/aud-avoid-order-by-on-long-columns) | `aud-avoid-order-by-on-long-columns` |
| [Avoid ORDER BY Random Function](en/reference/audit-rules/aud-avoid-order-by-random-function) | `aud-avoid-order-by-random-function` |
| [Avoid Replicated Distribution for Large Tables](en/reference/audit-rules/aud-avoid-replicated-distribution-for-large-tables) | `aud-avoid-replicated-distribution-for-large-tables` |
| [Avoid Scalar Subqueries](en/reference/audit-rules/aud-avoid-scalar-subqueries) | `aud-avoid-scalar-subqueries` |
| [Avoid SELECT with FOR UPDATE](en/reference/audit-rules/aud-avoid-select-with-for-update) | `aud-avoid-select-with-for-update` |
| [Avoid SELECT with LIMIT and FOR UPDATE](en/reference/audit-rules/aud-avoid-select-with-limit-and-for-update) | `aud-avoid-select-with-limit-and-for-update` |
| [CacheExhausted4IdentityColumn](en/reference/audit-rules/aud-cacheexhausted4identitycolumn) | `aud-cacheexhausted4identitycolumn` |
| [ChangingColumnNameDisallowed](en/reference/audit-rules/aud-changingcolumnnamedisallowed) | `aud-changingcolumnnamedisallowed` |
| [ChangingColumn's Order Disallowed](en/reference/audit-rules/aud-changingcolumns-order-disallowed) | `aud-changingcolumns-order-disallowed` |
| [ChangingColumnTypeDisallowed](en/reference/audit-rules/aud-changingcolumntypedisallowed) | `aud-changingcolumntypedisallowed` |
| [Char Column Length Exceeds Threshold](en/reference/audit-rules/aud-char-column-length) | `aud-char-column-length` |
| [Character Set Required for Database Creation](en/reference/audit-rules/aud-character-set-required-for-database-creation) | `aud-character-set-required-for-database-creation` |
| [CharsetOnColumnDisallowed](en/reference/audit-rules/aud-charsetoncolumndisallowed) | `aud-charsetoncolumndisallowed` |
| [CharsetOnTableDisallowed](en/reference/audit-rules/aud-charsetontabledisallowed) | `aud-charsetontabledisallowed` |
| [CharsetsOnTable&DatabaseMismatch](en/reference/audit-rules/aud-charsetsontabledatabasemismatch) | `aud-charsetsontabledatabasemismatch` |
| [Column and Table Character Set Mismatch](en/reference/audit-rules/aud-column-and-table-character-set-mismatch) | `aud-column-and-table-character-set-mismatch` |
| [Column Naming Convention](en/reference/audit-rules/aud-column-naming-convention) | `aud-column-naming-convention` |
| [Column with this Name Already Exists](en/reference/audit-rules/aud-column-with-this-name-already-exists) | `aud-column-with-this-name-already-exists` |
| [Comments on Column Required](en/reference/audit-rules/aud-comments-on-column-required) | `aud-comments-on-column-required` |
| [CommentsOnTableRequired](en/reference/audit-rules/aud-commentsontablerequired) | `aud-commentsontablerequired` |
| [CompressedAttributeDisallowed](en/reference/audit-rules/aud-compressedattributedisallowed) | `aud-compressedattributedisallowed` |
| [Consider Replicated Distribution for Small Tables](en/reference/audit-rules/aud-consider-replicated-distribution-for-small-table) | `aud-consider-replicated-distribution-for-small-table` |
| [Constraint with this Name Already Exists](en/reference/audit-rules/aud-constraint-with-this-name-already-exists) | `aud-constraint-with-this-name-already-exists` |
| [Create Index Before Constraint](en/reference/audit-rules/aud-create-index-before-constraint) | `aud-create-index-before-constraint` |
| [Create Index Using Online Mode](en/reference/audit-rules/aud-create-index-using-online-mode) | `aud-create-index-using-online-mode` |
| [UPDATE/DELETE without WHERE](en/reference/audit-rules/aud-dml-where) | `aud-dml-where` |
| [Expression in GROUP BY Causes Index Invalidation](en/reference/audit-rules/aud-expression-in-group-by) | `aud-expression-in-group-by` |
| [Expression in ORDER BY Causes Index Invalidation](en/reference/audit-rules/aud-expression-in-order-by) | `aud-expression-in-order-by` |
| [INSERT Must Include Primary Key Column](en/reference/audit-rules/aud-insert-must-include-pk) | `aud-insert-must-include-pk` |
| [ORDER BY Forbidden in UPDATE/DELETE](en/reference/audit-rules/aud-order-by-forbidden-in-dml) | `aud-order-by-forbidden-in-dml` |
| [Primary Key Naming Convention](en/reference/audit-rules/aud-pk-naming) | `aud-pk-naming` |
| [SELECT * Detection](en/reference/audit-rules/aud-select-star) | `aud-select-star` |
| [Redundant Index Detection](en/reference/audit-rules/sql-index-023) | `sql-index-023` |
