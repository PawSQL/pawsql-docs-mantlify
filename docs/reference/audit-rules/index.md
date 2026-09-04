---
id: audit-rules-index
title: 审核规范
description: PawSQL SQL 审核规则全量目录（由 metadata/rules/audit 生成）
type: reference
status: draft
tags:
- audit-rules
- zh
localeOf: en-audit-rules-index
---

> 生成文件：由已生成的规则页汇总，勿手改；`build-references` 会自动重建。

# 审核规范

共 54 条规则。

| 规则 | ID |
|---|---|
| [对象前需添加属主](reference/audit-rules/aud-add-schema-qualifier-before-object-references) | `aud-add-schema-qualifier-before-object-references` |
| [添加CHECK约束时需添加NO VALID](reference/audit-rules/aud-addcheckconstraintshouldbedeferred) | `aud-addcheckconstraintshouldbedeferred` |
| [禁止新增有默认值的列](reference/audit-rules/aud-addingcolumnswithdefaultdisallowed) | `aud-addingcolumnswithdefaultdisallowed` |
| [自增列命名规范](reference/audit-rules/aud-autoincrement-column-naming-convention) | `aud-autoincrement-column-naming-convention` |
| [分布式数据库应避免出现 ANTI JOIN 操作](reference/audit-rules/aud-avoid-anti-join-operations-in-distributed-databa) | `aud-avoid-anti-join-operations-in-distributed-databa` |
| [避免COUNT DISTINCT多个可空列](reference/audit-rules/aud-avoid-count-distinct-on-multiple-nullable-column) | `aud-avoid-count-distinct-on-multiple-nullable-column` |
| [避免使用CROSS JOIN](reference/audit-rules/aud-avoid-cross-join) | `aud-avoid-cross-join` |
| [分布式数据库应避免跨分片的 DML 操作](reference/audit-rules/aud-avoid-crossshard-dml-operations-in-distributed-d) | `aud-avoid-crossshard-dml-operations-in-distributed-d` |
| [避免表引用使用重复的别名](reference/audit-rules/aud-avoid-duplicate-table-aliases) | `aud-avoid-duplicate-table-aliases` |
| [避免有派生表的查询语句使用for update](reference/audit-rules/aud-avoid-for-update-with-derived-tables) | `aud-avoid-for-update-with-derived-tables` |
| [避免GROUP BY选择列的序号](reference/audit-rules/aud-avoid-group-by-column-ordinal-position) | `aud-avoid-group-by-column-ordinal-position` |
| [避免对长字段进行分组](reference/audit-rules/aud-avoid-group-by-on-long-columns) | `aud-avoid-group-by-on-long-columns` |
| [避免表关联字段不是分布键](reference/audit-rules/aud-avoid-joining-on-nondistribution-key-columns) | `aud-avoid-joining-on-nondistribution-key-columns` |
| [避免常量字符串开头或结尾包含空格](reference/audit-rules/aud-avoid-leading-or-trailing-spaces-in-string-liter) | `aud-avoid-leading-or-trailing-spaces-in-string-liter` |
| [避免使用没有通配符的 LIKE 查询](reference/audit-rules/aud-avoid-like-without-wildcards) | `aud-avoid-like-without-wildcards` |
| [避免在SELECT语句中使用LIMIT而没有ORDER BY](reference/audit-rules/aud-avoid-limit-without-order-by-in-select) | `aud-avoid-limit-without-order-by-in-select` |
| [避免在UPDELETE语句中使用LIMIT而没有ORDER](reference/audit-rules/aud-avoid-limit-without-order-by-in-updatedelete) | `aud-avoid-limit-without-order-by-in-updatedelete` |
| [分布键不建议使用多个字段](reference/audit-rules/aud-avoid-multiple-distribution-keys) | `aud-avoid-multiple-distribution-keys` |
| [避免使用NATURAL JOIN](reference/audit-rules/aud-avoid-natural-join) | `aud-avoid-natural-join` |
| [分布式数据库不建议创建非分布表](reference/audit-rules/aud-avoid-nondistributed-tables) | `aud-avoid-nondistributed-tables` |
| [避免ORDER BY选择列的序号](reference/audit-rules/aud-avoid-order-by-column-ordinal-position) | `aud-avoid-order-by-column-ordinal-position` |
| [避免对长字段进行排序](reference/audit-rules/aud-avoid-order-by-on-long-columns) | `aud-avoid-order-by-on-long-columns` |
| [避免使用随机函数排序](reference/audit-rules/aud-avoid-order-by-random-function) | `aud-avoid-order-by-random-function` |
| [大表不建议使用复制(Replicated)分布](reference/audit-rules/aud-avoid-replicated-distribution-for-large-tables) | `aud-avoid-replicated-distribution-for-large-tables` |
| [避免使用标量子查询](reference/audit-rules/aud-avoid-scalar-subqueries) | `aud-avoid-scalar-subqueries` |
| [避免在SELECT语句添加FOR UPDATE](reference/audit-rules/aud-avoid-select-with-for-update) | `aud-avoid-select-with-for-update` |
| [避免limit子句的查询语句使用for update](reference/audit-rules/aud-avoid-select-with-limit-and-for-update) | `aud-avoid-select-with-limit-and-for-update` |
| [自增序列耗尽预警](reference/audit-rules/aud-cacheexhausted4identitycolumn) | `aud-cacheexhausted4identitycolumn` |
| [禁止修改字段名](reference/audit-rules/aud-changingcolumnnamedisallowed) | `aud-changingcolumnnamedisallowed` |
| [禁止修改列的顺序](reference/audit-rules/aud-changingcolumns-order-disallowed) | `aud-changingcolumns-order-disallowed` |
| [禁止修改列的数据类型](reference/audit-rules/aud-changingcolumntypedisallowed) | `aud-changingcolumntypedisallowed` |
| [CHAR 字段长度超过阈值](reference/audit-rules/aud-char-column-length) | `aud-char-column-length` |
| [创建库必须指定数据库字符集](reference/audit-rules/aud-character-set-required-for-database-creation) | `aud-character-set-required-for-database-creation` |
| [禁止指定列的字符集](reference/audit-rules/aud-charsetoncolumndisallowed) | `aud-charsetoncolumndisallowed` |
| [表定义时禁止使用字符集](reference/audit-rules/aud-charsetontabledisallowed) | `aud-charsetontabledisallowed` |
| [表的字符集和数据库不一致](reference/audit-rules/aud-charsetsontabledatabasemismatch) | `aud-charsetsontabledatabasemismatch` |
| [列的字符集和表不一致](reference/audit-rules/aud-column-and-table-character-set-mismatch) | `aud-column-and-table-character-set-mismatch` |
| [列名命名规范](reference/audit-rules/aud-column-naming-convention) | `aud-column-naming-convention` |
| [字段名已存在](reference/audit-rules/aud-column-with-this-name-already-exists) | `aud-column-with-this-name-already-exists` |
| [列必须有注释](reference/audit-rules/aud-comments-on-column-required) | `aud-comments-on-column-required` |
| [表必须有注释](reference/audit-rules/aud-commentsontablerequired) | `aud-commentsontablerequired` |
| [禁止通过COMPRESSED打开字段压缩功能](reference/audit-rules/aud-compressedattributedisallowed) | `aud-compressedattributedisallowed` |
| [小于阈值的分布表建议设计为复制表](reference/audit-rules/aud-consider-replicated-distribution-for-small-table) | `aud-consider-replicated-distribution-for-small-table` |
| [约束名已存在](reference/audit-rules/aud-constraint-with-this-name-already-exists) | `aud-constraint-with-this-name-already-exists` |
| [创建约束前提前创建相关的索引](reference/audit-rules/aud-create-index-before-constraint) | `aud-create-index-before-constraint` |
| [建议使用在线模式创建索引](reference/audit-rules/aud-create-index-using-online-mode) | `aud-create-index-using-online-mode` |
| [避免无条件的 UPDATE/DELETE 语句](reference/audit-rules/aud-dml-where) | `aud-dml-where` |
| [GROUP 字段中有表达式导致索引失效](reference/audit-rules/aud-expression-in-group-by) | `aud-expression-in-group-by` |
| [ORDER 字段中有表达式导致索引失效](reference/audit-rules/aud-expression-in-order-by) | `aud-expression-in-order-by` |
| [INSERT 语句必须包含主键字段](reference/audit-rules/aud-insert-must-include-pk) | `aud-insert-must-include-pk` |
| [UPDATE/DELETE 禁止使用 ORDER 子句](reference/audit-rules/aud-order-by-forbidden-in-dml) | `aud-order-by-forbidden-in-dml` |
| [主键命名规范](reference/audit-rules/aud-pk-naming) | `aud-pk-naming` |
| [避免在查询中使用 SELECT *](reference/audit-rules/aud-select-star) | `aud-select-star` |
| [禁止创建重复索引/冗余索引](reference/audit-rules/sql-index-023) | `sql-index-023` |
