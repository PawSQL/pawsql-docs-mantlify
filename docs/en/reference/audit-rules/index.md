---
id: en-audit-rules-index
title: Audit Rule Reference
description: 'Audit Rule Reference: conditions, examples and limitations.'
type: reference
subtype: rule
layout: index
status: draft
translationKey: audit-rules-index
language: en
localeOf: audit-rules-index
product: pawsql
---

54 rules.

| Rule | ID | Category | Severity |
|---|---|---|---|
| [UPDATE/DELETE without WHERE](/en/reference/audit-rules/aud-dml-where) | `AUD-DML-WHERE` | dml | warning |
| [SELECT * Detection](/en/reference/audit-rules/aud-select-star) | `AUD-SELECT-STAR` | unknown | info |
| [Redundant Index Detection](/en/reference/audit-rules/sql-index-023) | `SQL-INDEX-023` | index | warning |
| [Add Schema Qualifier Before Object References](/en/reference/audit-rules/aud-add-schema-qualifier-before-object-references) | `aud-add-schema-qualifier-before-object-references` | dml | info |
| [AddCheckConstraintShouldBeDeferred](/en/reference/audit-rules/aud-addcheckconstraintshouldbedeferred) | `aud-addcheckconstraintshouldbedeferred` | ddl | warning |
| [AddingColumnsWithDefaultDisallowed](/en/reference/audit-rules/aud-addingcolumnswithdefaultdisallowed) | `aud-addingcolumnswithdefaultdisallowed` | ddl | warning |
| [Auto-increment column naming convention](/en/reference/audit-rules/aud-autoincrement-column-naming-convention) | `aud-autoincrement-column-naming-convention` | ddl | info |
| [Avoid ANTI JOIN Operations in Distributed Databases](/en/reference/audit-rules/aud-avoid-anti-join-operations-in-distributed-databa) | `aud-avoid-anti-join-operations-in-distributed-databa` | dml | warning |
| [Avoid COUNT DISTINCT on Multiple Nullable Columns](/en/reference/audit-rules/aud-avoid-count-distinct-on-multiple-nullable-column) | `aud-avoid-count-distinct-on-multiple-nullable-column` | dml | info |
| [Avoid CROSS JOIN](/en/reference/audit-rules/aud-avoid-cross-join) | `aud-avoid-cross-join` | dml | warning |
| [Avoid Cross-Shard DML Operations in Distributed Databases](/en/reference/audit-rules/aud-avoid-crossshard-dml-operations-in-distributed-d) | `aud-avoid-crossshard-dml-operations-in-distributed-d` | dml | warning |
| [Avoid Duplicate Table Aliases](/en/reference/audit-rules/aud-avoid-duplicate-table-aliases) | `aud-avoid-duplicate-table-aliases` | dml | warning |
| [Avoid FOR UPDATE with Derived Tables](/en/reference/audit-rules/aud-avoid-for-update-with-derived-tables) | `aud-avoid-for-update-with-derived-tables` | dml | warning |
| [Avoid GROUP BY Column Ordinal Position](/en/reference/audit-rules/aud-avoid-group-by-column-ordinal-position) | `aud-avoid-group-by-column-ordinal-position` | dml | info |
| [Avoid GROUP BY on Long Columns](/en/reference/audit-rules/aud-avoid-group-by-on-long-columns) | `aud-avoid-group-by-on-long-columns` | dml | warning |
| [Avoid Joining on Non-Distribution Key Columns](/en/reference/audit-rules/aud-avoid-joining-on-nondistribution-key-columns) | `aud-avoid-joining-on-nondistribution-key-columns` | ddl | warning |
| [Avoid Leading or Trailing Spaces in String Literals](/en/reference/audit-rules/aud-avoid-leading-or-trailing-spaces-in-string-liter) | `aud-avoid-leading-or-trailing-spaces-in-string-liter` | dml | warning |
| [Avoid LIKE Without Wildcards](/en/reference/audit-rules/aud-avoid-like-without-wildcards) | `aud-avoid-like-without-wildcards` | dml | warning |
| [Avoid LIMIT Without ORDER BY in SELECT](/en/reference/audit-rules/aud-avoid-limit-without-order-by-in-select) | `aud-avoid-limit-without-order-by-in-select` | dml | warning |
| [Avoid LIMIT Without ORDER BY in UPDATE/DELETE](/en/reference/audit-rules/aud-avoid-limit-without-order-by-in-updatedelete) | `aud-avoid-limit-without-order-by-in-updatedelete` | dml | warning |
| [Avoid Multiple Distribution Keys](/en/reference/audit-rules/aud-avoid-multiple-distribution-keys) | `aud-avoid-multiple-distribution-keys` | ddl | warning |
| [Avoid NATURAL JOIN](/en/reference/audit-rules/aud-avoid-natural-join) | `aud-avoid-natural-join` | dml | warning |
| [Avoid Non-Distributed Tables](/en/reference/audit-rules/aud-avoid-nondistributed-tables) | `aud-avoid-nondistributed-tables` | ddl | warning |
| [Avoid ORDER BY Column Ordinal Position](/en/reference/audit-rules/aud-avoid-order-by-column-ordinal-position) | `aud-avoid-order-by-column-ordinal-position` | dml | info |
| [Avoid ORDER BY on Long Columns](/en/reference/audit-rules/aud-avoid-order-by-on-long-columns) | `aud-avoid-order-by-on-long-columns` | dml | warning |
| [Avoid ORDER BY Random Function](/en/reference/audit-rules/aud-avoid-order-by-random-function) | `aud-avoid-order-by-random-function` | dml | warning |
| [Avoid Replicated Distribution for Large Tables](/en/reference/audit-rules/aud-avoid-replicated-distribution-for-large-tables) | `aud-avoid-replicated-distribution-for-large-tables` | ddl | warning |
| [Avoid Scalar Subqueries](/en/reference/audit-rules/aud-avoid-scalar-subqueries) | `aud-avoid-scalar-subqueries` | dml | info |
| [Avoid SELECT with FOR UPDATE](/en/reference/audit-rules/aud-avoid-select-with-for-update) | `aud-avoid-select-with-for-update` | dml | warning |
| [Avoid SELECT with LIMIT and FOR UPDATE](/en/reference/audit-rules/aud-avoid-select-with-limit-and-for-update) | `aud-avoid-select-with-limit-and-for-update` | dml | warning |
| [CacheExhausted4IdentityColumn](/en/reference/audit-rules/aud-cacheexhausted4identitycolumn) | `aud-cacheexhausted4identitycolumn` | ddl | warning |
| [ChangingColumnNameDisallowed](/en/reference/audit-rules/aud-changingcolumnnamedisallowed) | `aud-changingcolumnnamedisallowed` | ddl | warning |
| [ChangingColumn's Order Disallowed](/en/reference/audit-rules/aud-changingcolumns-order-disallowed) | `aud-changingcolumns-order-disallowed` | ddl | warning |
| [ChangingColumnTypeDisallowed](/en/reference/audit-rules/aud-changingcolumntypedisallowed) | `aud-changingcolumntypedisallowed` | ddl | warning |
| [Char Column Length Exceeds Threshold](/en/reference/audit-rules/aud-char-column-length) | `aud-char-column-length` | ddl | info |
| [Character Set Required for Database Creation](/en/reference/audit-rules/aud-character-set-required-for-database-creation) | `aud-character-set-required-for-database-creation` | ddl | warning |
| [CharsetOnColumnDisallowed](/en/reference/audit-rules/aud-charsetoncolumndisallowed) | `aud-charsetoncolumndisallowed` | ddl | warning |
| [CharsetOnTableDisallowed](/en/reference/audit-rules/aud-charsetontabledisallowed) | `aud-charsetontabledisallowed` | ddl | warning |
| [CharsetsOnTable&DatabaseMismatch](/en/reference/audit-rules/aud-charsetsontabledatabasemismatch) | `aud-charsetsontabledatabasemismatch` | ddl | warning |
| [Column and Table Character Set Mismatch](/en/reference/audit-rules/aud-column-and-table-character-set-mismatch) | `aud-column-and-table-character-set-mismatch` | ddl | warning |
| [Column Naming Convention](/en/reference/audit-rules/aud-column-naming-convention) | `aud-column-naming-convention` | ddl | info |
| [Column with this Name Already Exists](/en/reference/audit-rules/aud-column-with-this-name-already-exists) | `aud-column-with-this-name-already-exists` | ddl | error |
| [Comments on Column Required](/en/reference/audit-rules/aud-comments-on-column-required) | `aud-comments-on-column-required` | ddl | warning |
| [CommentsOnTableRequired](/en/reference/audit-rules/aud-commentsontablerequired) | `aud-commentsontablerequired` | ddl | warning |
| [CompressedAttributeDisallowed](/en/reference/audit-rules/aud-compressedattributedisallowed) | `aud-compressedattributedisallowed` | ddl | warning |
| [Consider Replicated Distribution for Small Tables](/en/reference/audit-rules/aud-consider-replicated-distribution-for-small-table) | `aud-consider-replicated-distribution-for-small-table` | ddl | info |
| [Constraint with this Name Already Exists](/en/reference/audit-rules/aud-constraint-with-this-name-already-exists) | `aud-constraint-with-this-name-already-exists` | ddl | error |
| [Create Index Before Constraint](/en/reference/audit-rules/aud-create-index-before-constraint) | `aud-create-index-before-constraint` | ddl | warning |
| [Create Index Using Online Mode](/en/reference/audit-rules/aud-create-index-using-online-mode) | `aud-create-index-using-online-mode` | ddl | warning |
| [Expression in GROUP BY Causes Index Invalidation](/en/reference/audit-rules/aud-expression-in-group-by) | `aud-expression-in-group-by` | index | info |
| [Expression in ORDER BY Causes Index Invalidation](/en/reference/audit-rules/aud-expression-in-order-by) | `aud-expression-in-order-by` | index | info |
| [INSERT Must Include Primary Key Column](/en/reference/audit-rules/aud-insert-must-include-pk) | `aud-insert-must-include-pk` | dml | warning |
| [ORDER BY Forbidden in UPDATE/DELETE](/en/reference/audit-rules/aud-order-by-forbidden-in-dml) | `aud-order-by-forbidden-in-dml` | dml | warning |
| [Primary Key Naming Convention](/en/reference/audit-rules/aud-pk-naming) | `aud-pk-naming` | ddl | info |
