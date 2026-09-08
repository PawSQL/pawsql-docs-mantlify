---
id: audit-rules-index
title: 审核规范
description: 审核规范：查阅规则条件、示例和限制。
type: reference
subtype: rule
layout: index
status: draft
translationKey: audit-rules-index
language: zh
localeOf: en-audit-rules-index
product: pawsql
---

共 54 条规则。

| 规则 | ID | 分类 | 严重级别 |
|---|---|---|---|
| [避免无条件的 UPDATE/DELETE 语句](/reference/audit-rules/aud-dml-where) | `AUD-DML-WHERE` | dml | warning |
| [避免在查询中使用 SELECT *](/reference/audit-rules/aud-select-star) | `AUD-SELECT-STAR` | unknown | info |
| [禁止创建重复索引/冗余索引](/reference/audit-rules/sql-index-023) | `SQL-INDEX-023` | index | warning |
| [对象前需添加属主](/reference/audit-rules/aud-add-schema-qualifier-before-object-references) | `aud-add-schema-qualifier-before-object-references` | dml | info |
| [添加CHECK约束时需添加NO VALID](/reference/audit-rules/aud-addcheckconstraintshouldbedeferred) | `aud-addcheckconstraintshouldbedeferred` | ddl | warning |
| [禁止新增有默认值的列](/reference/audit-rules/aud-addingcolumnswithdefaultdisallowed) | `aud-addingcolumnswithdefaultdisallowed` | ddl | warning |
| [自增列命名规范](/reference/audit-rules/aud-autoincrement-column-naming-convention) | `aud-autoincrement-column-naming-convention` | ddl | info |
| [分布式数据库应避免出现 ANTI JOIN 操作](/reference/audit-rules/aud-avoid-anti-join-operations-in-distributed-databa) | `aud-avoid-anti-join-operations-in-distributed-databa` | dml | warning |
| [避免COUNT DISTINCT多个可空列](/reference/audit-rules/aud-avoid-count-distinct-on-multiple-nullable-column) | `aud-avoid-count-distinct-on-multiple-nullable-column` | dml | info |
| [避免使用CROSS JOIN](/reference/audit-rules/aud-avoid-cross-join) | `aud-avoid-cross-join` | dml | warning |
| [分布式数据库应避免跨分片的 DML 操作](/reference/audit-rules/aud-avoid-crossshard-dml-operations-in-distributed-d) | `aud-avoid-crossshard-dml-operations-in-distributed-d` | dml | warning |
| [避免表引用使用重复的别名](/reference/audit-rules/aud-avoid-duplicate-table-aliases) | `aud-avoid-duplicate-table-aliases` | dml | warning |
| [避免有派生表的查询语句使用for update](/reference/audit-rules/aud-avoid-for-update-with-derived-tables) | `aud-avoid-for-update-with-derived-tables` | dml | warning |
| [避免GROUP BY选择列的序号](/reference/audit-rules/aud-avoid-group-by-column-ordinal-position) | `aud-avoid-group-by-column-ordinal-position` | dml | info |
| [避免对长字段进行分组](/reference/audit-rules/aud-avoid-group-by-on-long-columns) | `aud-avoid-group-by-on-long-columns` | dml | warning |
| [避免表关联字段不是分布键](/reference/audit-rules/aud-avoid-joining-on-nondistribution-key-columns) | `aud-avoid-joining-on-nondistribution-key-columns` | ddl | warning |
| [避免常量字符串开头或结尾包含空格](/reference/audit-rules/aud-avoid-leading-or-trailing-spaces-in-string-liter) | `aud-avoid-leading-or-trailing-spaces-in-string-liter` | dml | warning |
| [避免使用没有通配符的 LIKE 查询](/reference/audit-rules/aud-avoid-like-without-wildcards) | `aud-avoid-like-without-wildcards` | dml | warning |
| [避免在SELECT语句中使用LIMIT而没有ORDER BY](/reference/audit-rules/aud-avoid-limit-without-order-by-in-select) | `aud-avoid-limit-without-order-by-in-select` | dml | warning |
| [避免在UPDELETE语句中使用LIMIT而没有ORDER](/reference/audit-rules/aud-avoid-limit-without-order-by-in-updatedelete) | `aud-avoid-limit-without-order-by-in-updatedelete` | dml | warning |
| [分布键不建议使用多个字段](/reference/audit-rules/aud-avoid-multiple-distribution-keys) | `aud-avoid-multiple-distribution-keys` | ddl | warning |
| [避免使用NATURAL JOIN](/reference/audit-rules/aud-avoid-natural-join) | `aud-avoid-natural-join` | dml | warning |
| [分布式数据库不建议创建非分布表](/reference/audit-rules/aud-avoid-nondistributed-tables) | `aud-avoid-nondistributed-tables` | ddl | warning |
| [避免ORDER BY选择列的序号](/reference/audit-rules/aud-avoid-order-by-column-ordinal-position) | `aud-avoid-order-by-column-ordinal-position` | dml | info |
| [避免对长字段进行排序](/reference/audit-rules/aud-avoid-order-by-on-long-columns) | `aud-avoid-order-by-on-long-columns` | dml | warning |
| [避免使用随机函数排序](/reference/audit-rules/aud-avoid-order-by-random-function) | `aud-avoid-order-by-random-function` | dml | warning |
| [大表不建议使用复制(Replicated)分布](/reference/audit-rules/aud-avoid-replicated-distribution-for-large-tables) | `aud-avoid-replicated-distribution-for-large-tables` | ddl | warning |
| [避免使用标量子查询](/reference/audit-rules/aud-avoid-scalar-subqueries) | `aud-avoid-scalar-subqueries` | dml | info |
| [避免在SELECT语句添加FOR UPDATE](/reference/audit-rules/aud-avoid-select-with-for-update) | `aud-avoid-select-with-for-update` | dml | warning |
| [避免limit子句的查询语句使用for update](/reference/audit-rules/aud-avoid-select-with-limit-and-for-update) | `aud-avoid-select-with-limit-and-for-update` | dml | warning |
| [自增序列耗尽预警](/reference/audit-rules/aud-cacheexhausted4identitycolumn) | `aud-cacheexhausted4identitycolumn` | ddl | warning |
| [禁止修改字段名](/reference/audit-rules/aud-changingcolumnnamedisallowed) | `aud-changingcolumnnamedisallowed` | ddl | warning |
| [禁止修改列的顺序](/reference/audit-rules/aud-changingcolumns-order-disallowed) | `aud-changingcolumns-order-disallowed` | ddl | warning |
| [禁止修改列的数据类型](/reference/audit-rules/aud-changingcolumntypedisallowed) | `aud-changingcolumntypedisallowed` | ddl | warning |
| [CHAR 字段长度超过阈值](/reference/audit-rules/aud-char-column-length) | `aud-char-column-length` | ddl | info |
| [创建库必须指定数据库字符集](/reference/audit-rules/aud-character-set-required-for-database-creation) | `aud-character-set-required-for-database-creation` | ddl | warning |
| [禁止指定列的字符集](/reference/audit-rules/aud-charsetoncolumndisallowed) | `aud-charsetoncolumndisallowed` | ddl | warning |
| [表定义时禁止使用字符集](/reference/audit-rules/aud-charsetontabledisallowed) | `aud-charsetontabledisallowed` | ddl | warning |
| [表的字符集和数据库不一致](/reference/audit-rules/aud-charsetsontabledatabasemismatch) | `aud-charsetsontabledatabasemismatch` | ddl | warning |
| [列的字符集和表不一致](/reference/audit-rules/aud-column-and-table-character-set-mismatch) | `aud-column-and-table-character-set-mismatch` | ddl | warning |
| [列名命名规范](/reference/audit-rules/aud-column-naming-convention) | `aud-column-naming-convention` | ddl | info |
| [字段名已存在](/reference/audit-rules/aud-column-with-this-name-already-exists) | `aud-column-with-this-name-already-exists` | ddl | error |
| [列必须有注释](/reference/audit-rules/aud-comments-on-column-required) | `aud-comments-on-column-required` | ddl | warning |
| [表必须有注释](/reference/audit-rules/aud-commentsontablerequired) | `aud-commentsontablerequired` | ddl | warning |
| [禁止通过COMPRESSED打开字段压缩功能](/reference/audit-rules/aud-compressedattributedisallowed) | `aud-compressedattributedisallowed` | ddl | warning |
| [小于阈值的分布表建议设计为复制表](/reference/audit-rules/aud-consider-replicated-distribution-for-small-table) | `aud-consider-replicated-distribution-for-small-table` | ddl | info |
| [约束名已存在](/reference/audit-rules/aud-constraint-with-this-name-already-exists) | `aud-constraint-with-this-name-already-exists` | ddl | error |
| [创建约束前提前创建相关的索引](/reference/audit-rules/aud-create-index-before-constraint) | `aud-create-index-before-constraint` | ddl | warning |
| [建议使用在线模式创建索引](/reference/audit-rules/aud-create-index-using-online-mode) | `aud-create-index-using-online-mode` | ddl | warning |
| [GROUP 字段中有表达式导致索引失效](/reference/audit-rules/aud-expression-in-group-by) | `aud-expression-in-group-by` | index | info |
| [ORDER 字段中有表达式导致索引失效](/reference/audit-rules/aud-expression-in-order-by) | `aud-expression-in-order-by` | index | info |
| [INSERT 语句必须包含主键字段](/reference/audit-rules/aud-insert-must-include-pk) | `aud-insert-must-include-pk` | dml | warning |
| [UPDATE/DELETE 禁止使用 ORDER 子句](/reference/audit-rules/aud-order-by-forbidden-in-dml) | `aud-order-by-forbidden-in-dml` | dml | warning |
| [主键命名规范](/reference/audit-rules/aud-pk-naming) | `aud-pk-naming` | ddl | info |
