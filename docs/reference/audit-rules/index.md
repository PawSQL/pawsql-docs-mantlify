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

共 220 条规则。


## 对象设计（DDL）

| 规则 | ID | 严重级别 |
|---|---|---|
| [添加CHECK约束时需添加NO VALID](/reference/audit-rules/aud-addcheckconstraintshouldbedeferred) | `aud-addcheckconstraintshouldbedeferred` | warning |
| [禁止新增有默认值的列](/reference/audit-rules/aud-addingcolumnswithdefaultdisallowed) | `aud-addingcolumnswithdefaultdisallowed` | warning |
| [自增列命名规范](/reference/audit-rules/aud-autoincrement-column-naming-convention) | `aud-autoincrement-column-naming-convention` | info |
| [避免表关联字段不是分布键](/reference/audit-rules/aud-avoid-joining-on-nondistribution-key-columns) | `aud-avoid-joining-on-nondistribution-key-columns` | warning |
| [分布键不建议使用多个字段](/reference/audit-rules/aud-avoid-multiple-distribution-keys) | `aud-avoid-multiple-distribution-keys` | warning |
| [分布式数据库不建议创建非分布表](/reference/audit-rules/aud-avoid-nondistributed-tables) | `aud-avoid-nondistributed-tables` | warning |
| [大表不建议使用复制(Replicated)分布](/reference/audit-rules/aud-avoid-replicated-distribution-for-large-tables) | `aud-avoid-replicated-distribution-for-large-tables` | warning |
| [自增序列耗尽预警](/reference/audit-rules/aud-cacheexhausted4identitycolumn) | `aud-cacheexhausted4identitycolumn` | warning |
| [禁止修改字段名](/reference/audit-rules/aud-changingcolumnnamedisallowed) | `aud-changingcolumnnamedisallowed` | warning |
| [禁止修改列的顺序](/reference/audit-rules/aud-changingcolumns-order-disallowed) | `aud-changingcolumns-order-disallowed` | warning |
| [禁止修改列的数据类型](/reference/audit-rules/aud-changingcolumntypedisallowed) | `aud-changingcolumntypedisallowed` | warning |
| [CHAR 字段长度超过阈值](/reference/audit-rules/aud-char-column-length-exceeds-threshold) | `aud-char-column-length-exceeds-threshold` | info |
| [创建库必须指定数据库字符集](/reference/audit-rules/aud-character-set-required-for-database-creation) | `aud-character-set-required-for-database-creation` | warning |
| [禁止指定列的字符集](/reference/audit-rules/aud-charsetoncolumndisallowed) | `aud-charsetoncolumndisallowed` | warning |
| [表定义时禁止使用字符集](/reference/audit-rules/aud-charsetontabledisallowed) | `aud-charsetontabledisallowed` | warning |
| [表的字符集和数据库不一致](/reference/audit-rules/aud-charsetsontabledatabasemismatch) | `aud-charsetsontabledatabasemismatch` | warning |
| [列的字符集和表不一致](/reference/audit-rules/aud-column-and-table-character-set-mismatch) | `aud-column-and-table-character-set-mismatch` | warning |
| [列名命名规范](/reference/audit-rules/aud-column-naming-convention) | `aud-column-naming-convention` | info |
| [字段名已存在](/reference/audit-rules/aud-column-with-this-name-already-exists) | `aud-column-with-this-name-already-exists` | error |
| [列必须有注释](/reference/audit-rules/aud-comments-on-column-required) | `aud-comments-on-column-required` | warning |
| [表必须有注释](/reference/audit-rules/aud-commentsontablerequired) | `aud-commentsontablerequired` | warning |
| [禁止通过COMPRESSED打开字段压缩功能](/reference/audit-rules/aud-compressedattributedisallowed) | `aud-compressedattributedisallowed` | warning |
| [小于阈值的分布表建议设计为复制表](/reference/audit-rules/aud-consider-replicated-distribution-for-small-table) | `aud-consider-replicated-distribution-for-small-table` | info |
| [约束名已存在](/reference/audit-rules/aud-constraint-with-this-name-already-exists) | `aud-constraint-with-this-name-already-exists` | error |
| [创建约束前提前创建相关的索引](/reference/audit-rules/aud-create-index-before-constraint) | `aud-create-index-before-constraint` | warning |
| [建议使用在线模式创建索引](/reference/audit-rules/aud-create-index-using-online-mode) | `aud-create-index-using-online-mode` | warning |
| [禁止使用CHECK约束](/reference/audit-rules/aud-createcheckconstraintdisallowed) | `aud-createcheckconstraintdisallowed` | warning |
| [CTAS 命名规范](/reference/audit-rules/aud-ctas-naming-convention) | `aud-ctas-naming-convention` | info |
| [数据库命名规范](/reference/audit-rules/aud-database-naming-convention) | `aud-database-naming-convention` | info |
| [主键列的数据类型限制](/reference/audit-rules/aud-datatypelimitofprimarykey) | `aud-datatypelimitofprimarykey` | warning |
| [禁止使用的数据类型](/reference/audit-rules/aud-datatypesdisallowed) | `aud-datatypesdisallowed` | warning |
| [禁止修改降低字段精度](/reference/audit-rules/aud-decreasingprecisiondisallowed) | `aud-decreasingprecisiondisallowed` | warning |
| [数据库需指定默认排序规则（Collate）](/reference/audit-rules/aud-default-collation-required-for-database) | `aud-default-collation-required-for-database` | warning |
| [非空列需指定带默认值](/reference/audit-rules/aud-default-value-required-for-not-null-columns) | `aud-default-value-required-for-not-null-columns` | warning |
| [时间列未设置默认值或默认值为空](/reference/audit-rules/aud-default-value-required-for-time-columns) | `aud-default-value-required-for-time-columns` | warning |
| [时间戳列需指定默认值](/reference/audit-rules/aud-default-value-required-for-timestamp-columns) | `aud-default-value-required-for-timestamp-columns` | warning |
| [主外键的数据类型不一致](/reference/audit-rules/aud-diffdatatypesofricolumns) | `aud-diffdatatypesofricolumns` | warning |
| [分布键的数据类型限制](/reference/audit-rules/aud-distribution-key-data-type-restriction) | `aud-distribution-key-data-type-restriction` | warning |
| [分布键的长度不得超过阈值](/reference/audit-rules/aud-distribution-key-length-must-not-exceed-threshol) | `aud-distribution-key-length-must-not-exceed-threshol` | warning |
| [分片表的分布键应设置非空约束](/reference/audit-rules/aud-distribution-key-must-have-not-null-constraint) | `aud-distribution-key-must-have-not-null-constraint` | info |
| [分布键的需使用指定的排序规则](/reference/audit-rules/aud-distribution-key-must-use-specified-collation) | `aud-distribution-key-must-use-specified-collation` | warning |
| [只能删除指定命名规范的列](/reference/audit-rules/aud-drop-columns-only-with-specified-naming-conventi) | `aud-drop-columns-only-with-specified-naming-conventi` | warning |
| [只能删除指定命名规范的表和视图](/reference/audit-rules/aud-drop-tablesviews-only-with-specified-naming-conv) | `aud-drop-tablesviews-only-with-specified-naming-conv` | warning |
| [禁止删除字段](/reference/audit-rules/aud-droppingcolumnsdisallowed) | `aud-droppingcolumnsdisallowed` | warning |
| [禁止删除索引中的列](/reference/audit-rules/aud-droppingcolumnsusedinindexdisallowed) | `aud-droppingcolumnsusedinindexdisallowed` | warning |
| [禁止删除索引](/reference/audit-rules/aud-droppingindexdisallowed) | `aud-droppingindexdisallowed` | warning |
| [禁止删除表/视图](/reference/audit-rules/aud-droptableviewdisallowed) | `aud-droptableviewdisallowed` | warning |
| [禁止对象名称与关键字重名](/reference/audit-rules/aud-duplicatedobjectnameswithkeywords) | `aud-duplicatedobjectnameswithkeywords` | warning |
| [禁止使用ENUM数据类型](/reference/audit-rules/aud-enumdatatypedisallowed) | `aud-enumdatatypedisallowed` | warning |
| [必须显式的指定分布键](/reference/audit-rules/aud-explicit-distribution-key-required) | `aud-explicit-distribution-key-required` | warning |
| [禁止创建外键](/reference/audit-rules/aud-foreignkeydisallowed) | `aud-foreignkeydisallowed` | warning |
| [脏页率超过阈值，建议进行回收](/reference/audit-rules/aud-high-dirty-page-ratio) | `aud-high-dirty-page-ratio` | warning |
| [Hive内部表需使用orc/parquet存储格式](/reference/audit-rules/aud-hive-internal-tables-must-use-orcparquet-format) | `aud-hive-internal-tables-must-use-orcparquet-format` | error |
| [Hive表需使用指定的压缩格式](/reference/audit-rules/aud-hive-table-compression-format-required) | `aud-hive-table-compression-format-required` | error |
| [删除表/视图/索引时需指定 IF EXISTS](/reference/audit-rules/aud-if-exists-required-for-dropping-objects) | `aud-if-exists-required-for-dropping-objects` | warning |
| [创建表/视图/索引时需指定 IF NOT EXISTS](/reference/audit-rules/aud-if-not-exists-required-for-creating-objects) | `aud-if-not-exists-required-for-creating-objects` | warning |
| [主键禁止使用自增](/reference/audit-rules/aud-inccolumn4primarykeydisallowed) | `aud-inccolumn4primarykeydisallowed` | warning |
| [主键应使用自增列](/reference/audit-rules/aud-inccolumn4primarykeyrequired) | `aud-inccolumn4primarykeyrequired` | warning |
| [索引名已存在](/reference/audit-rules/aud-index-with-this-name-already-exists) | `aud-index-with-this-name-already-exists` | error |
| [索引名不存在](/reference/audit-rules/aud-index-with-this-name-doest-exists) | `aud-index-with-this-name-doest-exists` | error |
| [自增列的初始值应从0/1开始](/reference/audit-rules/aud-initvalue4identitycolumn) | `aud-initvalue4identitycolumn` | warning |
| [必须使用INNODB存储引擎](/reference/audit-rules/aud-innodb-storage-engine-required) | `aud-innodb-storage-engine-required` | warning |
| [禁止为列表中的列设置非空默认值](/reference/audit-rules/aud-largeobjectdefaultnonnulldisallowed) | `aud-largeobjectdefaultnonnulldisallowed` | warning |
| [行数超过阈值的单表建议设计为分片表](/reference/audit-rules/aud-largetableshouldbesharded) | `aud-largetableshouldbesharded` | info |
| [禁止设置MAXVALUE默认分区](/reference/audit-rules/aud-maxvaluedefaultpartitiondisallowed) | `aud-maxvaluedefaultpartitiondisallowed` | info |
| [禁止为列新增默认值](/reference/audit-rules/aud-modifyingcolumnadddefaultdisallowed) | `aud-modifyingcolumnadddefaultdisallowed` | warning |
| [禁止为列新增非空约束](/reference/audit-rules/aud-modifyingcolumnaddnotnulldisallowed) | `aud-modifyingcolumnaddnotnulldisallowed` | warning |
| [禁止为列修改默认值](/reference/audit-rules/aud-modifyingcolumnchangedefaultdisallowed) | `aud-modifyingcolumnchangedefaultdisallowed` | warning |
| [禁止修改分布键字段类型](/reference/audit-rules/aud-modifyingdistributionkeytypedisallowed) | `aud-modifyingdistributionkeytypedisallowed` | warning |
| [禁止修改表的默认字符集](/reference/audit-rules/aud-modifytablecharsetdisallowed) | `aud-modifytablecharsetdisallowed` | warning |
| [非列表中的列应设置非空默认值](/reference/audit-rules/aud-nonnull-default-value-required-for-nonexcluded-c) | `aud-nonnull-default-value-required-for-nonexcluded-c` | warning |
| [禁止为列表中的列设置非空约束](/reference/audit-rules/aud-nonnullconstraint4columnsinlistdisallowed) | `aud-nonnullconstraint4columnsinlistdisallowed` | warning |
| [表的列数不建议超过阈值](/reference/audit-rules/aud-numofcolumnsexceedthreshold) | `aud-numofcolumnsexceedthreshold` | warning |
| [主键的列数目不得超过阈值](/reference/audit-rules/aud-numofpkcolumnsexceed) | `aud-numofpkcolumnsexceed` | warning |
| [对象名称长度不得超过阈值](/reference/audit-rules/aud-object-name-length-must-not-exceed-threshold) | `aud-object-name-length-must-not-exceed-threshold` | warning |
| [对象命名规范](/reference/audit-rules/aud-object-naming-convention) | `aud-object-naming-convention` | info |
| [每个表只能有一个自增列](/reference/audit-rules/aud-oneidentitycolumnallowed) | `aud-oneidentitycolumnallowed` | warning |
| [分区键的长度不得超过阈值](/reference/audit-rules/aud-partition-key-length-must-not-exceed-threshold) | `aud-partition-key-length-must-not-exceed-threshold` | warning |
| [禁止使用分区表](/reference/audit-rules/aud-partitionedtabledisallowed) | `aud-partitionedtabledisallowed` | info |
| [分布方式建议使用 HASH 分布](/reference/audit-rules/aud-prefer-hash-distribution) | `aud-prefer-hash-distribution` | warning |
| [表必须建主键](/reference/audit-rules/aud-primarykeyrequired) | `aud-primarykeyrequired` | error |
| [模式命名规范](/reference/audit-rules/aud-schema-naming-convention) | `aud-schema-naming-convention` | info |
| [禁止使用SET数据类型](/reference/audit-rules/aud-setdatatypedisallowed) | `aud-setdatatypedisallowed` | warning |
| [禁止修改降低字段长度](/reference/audit-rules/aud-shortendatatypelengthdisallowed) | `aud-shortendatatypelengthdisallowed` | warning |
| [自增列不得使用有符号整数](/reference/audit-rules/aud-signedinteger4identitycolumndisallowed) | `aud-signedinteger4identitycolumndisallowed` | warning |
| [创建库或模式时必须使用指定字符集](/reference/audit-rules/aud-specific-character-set-required-for-database-cre) | `aud-specific-character-set-required-for-database-cre` | warning |
| [创建库或模式时使用规定的排序规则](/reference/audit-rules/aud-specific-collation-required-for-database-creatio) | `aud-specific-collation-required-for-database-creatio` | error |
| [表上应使用指定的字符集](/reference/audit-rules/aud-specificcharset4tablerequired) | `aud-specificcharset4tablerequired` | warning |
| [表上应使用指定的排序规则](/reference/audit-rules/aud-specificcollation4tablerequired) | `aud-specificcollation4tablerequired` | warning |
| [表必须包含的列名及数据类型](/reference/audit-rules/aud-specificcolumnsrequired) | `aud-specificcolumnsrequired` | warning |
| [定义约束时需指定DISABLE和NONVALIDATE](/reference/audit-rules/aud-specify-disable-and-nonvalidate-for-hive-constra) | `aud-specify-disable-and-nonvalidate-for-hive-constra` | warning |
| [禁止使用存储过程](/reference/audit-rules/aud-stored-procedure-disallowed) | `aud-stored-procedure-disallowed` | warning |
| [表名命名规范](/reference/audit-rules/aud-table-naming-convention) | `aud-table-naming-convention` | info |
| [表/视图名已存在](/reference/audit-rules/aud-tableview-with-this-name-already-exists) | `aud-tableview-with-this-name-already-exists` | error |
| [表/视图名不存在](/reference/audit-rules/aud-tableview-with-this-name-doest-exists) | `aud-tableview-with-this-name-doest-exists` | error |
| [不允许使用时间戳类型](/reference/audit-rules/aud-timestamp-data-type-disallowed) | `aud-timestamp-data-type-disallowed` | warning |
| [禁止使用触发器](/reference/audit-rules/aud-triggerdisallowed) | `aud-triggerdisallowed` | warning |
| [表需定义更新时间戳列](/reference/audit-rules/aud-updatetimestampcolumnsrequired) | `aud-updatetimestampcolumnsrequired` | warning |
| [禁止更新索引中的列](/reference/audit-rules/aud-updatingcolumnsusedinindexdisallowed) | `aud-updatingcolumnsusedinindexdisallowed` | warning |
| [TDSQL中使用ALTER设置自增列的起始值](/reference/audit-rules/aud-use-alter-table-to-set-auto-increment-start-in-t) | `aud-use-alter-table-to-set-auto-increment-start-in-t` | info |
| [大的Hive表应该使用分桶策略](/reference/audit-rules/aud-use-bucketing-strategy-for-large-hive-tables) | `aud-use-bucketing-strategy-for-large-hive-tables` | warning |
| [分布键应使用区分度大的字段](/reference/audit-rules/aud-use-high-cardinality-distribution-keys) | `aud-use-high-cardinality-distribution-keys` | warning |
| [整型建议采用 INT(10) 或 BIGINT(20)](/reference/audit-rules/aud-use-int10-or-bigint20-for-integer-columns) | `aud-use-int10-or-bigint20-for-integer-columns` | info |
| [大的Hive应该使用分区表](/reference/audit-rules/aud-use-partitioned-tables-for-large-hive-tables) | `aud-use-partitioned-tables-for-large-hive-tables` | warning |
| [大表建议使用分区表](/reference/audit-rules/aud-use-partitioned-tables-for-large-tables) | `aud-use-partitioned-tables-for-large-tables` | info |
| [应使用主键作为分布键](/reference/audit-rules/aud-use-primary-key-as-distribution-key) | `aud-use-primary-key-as-distribution-key` | warning |
| [应使用指定的数据分布方式](/reference/audit-rules/aud-use-specified-data-distribution-method) | `aud-use-specified-data-distribution-method` | warning |
| [精确浮点数建议使用Decimal或Number](/reference/audit-rules/aud-usedecimalfornumericcolumns) | `aud-usedecimalfornumericcolumns` | warning |
| [禁止创建自定义函数](/reference/audit-rules/aud-userdefinedfunctionudf-disallowed) | `aud-userdefinedfunctionudf-disallowed` | error |
| [禁止创建自定义类型](/reference/audit-rules/aud-userdefinedtypeudt-disallowed) | `aud-userdefinedtypeudt-disallowed` | warning |
| [禁止使用SYSDATE作为默认值](/reference/audit-rules/aud-usesysdateasdefaultdisallowed) | `aud-usesysdateasdefaultdisallowed` | warning |
| [VARCHAR字段长度超过阈值](/reference/audit-rules/aud-varchar-column-length-exceeds-threshold) | `aud-varchar-column-length-exceeds-threshold` | warning |
| [禁止使用视图](/reference/audit-rules/aud-viewdisallowed) | `aud-viewdisallowed` | warning |

## 数据操作（DML）

| 规则 | ID | 严重级别 |
|---|---|---|
| [对象前需添加属主](/reference/audit-rules/aud-add-schema-qualifier-before-object-references) | `aud-add-schema-qualifier-before-object-references` | info |
| [分布式数据库应避免出现 ANTI JOIN 操作](/reference/audit-rules/aud-avoid-anti-join-operations-in-distributed-databa) | `aud-avoid-anti-join-operations-in-distributed-databa` | warning |
| [避免COUNT DISTINCT多个可空列](/reference/audit-rules/aud-avoid-count-distinct-on-multiple-nullable-column) | `aud-avoid-count-distinct-on-multiple-nullable-column` | info |
| [避免使用CROSS JOIN](/reference/audit-rules/aud-avoid-cross-join) | `aud-avoid-cross-join` | warning |
| [分布式数据库应避免跨分片的 DML 操作](/reference/audit-rules/aud-avoid-crossshard-dml-operations-in-distributed-d) | `aud-avoid-crossshard-dml-operations-in-distributed-d` | warning |
| [避免表引用使用重复的别名](/reference/audit-rules/aud-avoid-duplicate-table-aliases) | `aud-avoid-duplicate-table-aliases` | warning |
| [避免有派生表的查询语句使用for update](/reference/audit-rules/aud-avoid-for-update-with-derived-tables) | `aud-avoid-for-update-with-derived-tables` | warning |
| [避免GROUP BY选择列的序号](/reference/audit-rules/aud-avoid-group-by-column-ordinal-position) | `aud-avoid-group-by-column-ordinal-position` | info |
| [避免对长字段进行分组](/reference/audit-rules/aud-avoid-group-by-on-long-columns) | `aud-avoid-group-by-on-long-columns` | warning |
| [避免常量字符串开头或结尾包含空格](/reference/audit-rules/aud-avoid-leading-or-trailing-spaces-in-string-liter) | `aud-avoid-leading-or-trailing-spaces-in-string-liter` | warning |
| [避免使用没有通配符的 LIKE 查询](/reference/audit-rules/aud-avoid-like-without-wildcards) | `aud-avoid-like-without-wildcards` | warning |
| [避免在SELECT语句中使用LIMIT而没有ORDER BY](/reference/audit-rules/aud-avoid-limit-without-order-by-in-select) | `aud-avoid-limit-without-order-by-in-select` | warning |
| [避免在UPDELETE语句中使用LIMIT而没有ORDER](/reference/audit-rules/aud-avoid-limit-without-order-by-in-updatedelete) | `aud-avoid-limit-without-order-by-in-updatedelete` | warning |
| [避免使用NATURAL JOIN](/reference/audit-rules/aud-avoid-natural-join) | `aud-avoid-natural-join` | warning |
| [避免ORDER BY选择列的序号](/reference/audit-rules/aud-avoid-order-by-column-ordinal-position) | `aud-avoid-order-by-column-ordinal-position` | info |
| [避免对长字段进行排序](/reference/audit-rules/aud-avoid-order-by-on-long-columns) | `aud-avoid-order-by-on-long-columns` | warning |
| [避免使用随机函数排序](/reference/audit-rules/aud-avoid-order-by-random-function) | `aud-avoid-order-by-random-function` | warning |
| [避免使用标量子查询](/reference/audit-rules/aud-avoid-scalar-subqueries) | `aud-avoid-scalar-subqueries` | info |
| [避免在查询中使用 SELECT *](/reference/audit-rules/aud-avoid-select) | `aud-avoid-select` | info |
| [避免在SELECT语句添加FOR UPDATE](/reference/audit-rules/aud-avoid-select-with-for-update) | `aud-avoid-select-with-for-update` | warning |
| [避免limit子句的查询语句使用for update](/reference/audit-rules/aud-avoid-select-with-limit-and-for-update) | `aud-avoid-select-with-limit-and-for-update` | warning |
| [避免无条件且无分组的SELECT语句](/reference/audit-rules/aud-avoid-select-without-where-and-group-by) | `aud-avoid-select-without-where-and-group-by` | info |
| [避免使用STRAIGHT JOIN](/reference/audit-rules/aud-avoid-straight-join) | `aud-avoid-straight-join` | warning |
| [避免无条件的 UPDATE/DELETE 语句](/reference/audit-rules/aud-avoid-unconditional-updatedelete-statements) | `aud-avoid-unconditional-updatedelete-statements` | warning |
| [避免使用不必要的内置函数](/reference/audit-rules/aud-avoid-unnecessary-builtin-functions) | `aud-avoid-unnecessary-builtin-functions` | info |
| [避免不必要的去重操作](/reference/audit-rules/aud-avoid-unnecessary-distinct-operations) | `aud-avoid-unnecessary-distinct-operations` | info |
| [避免不必要的更新操作](/reference/audit-rules/aud-avoid-unnecessary-update-operations) | `aud-avoid-unnecessary-update-operations` | info |
| [避免更新主键的值](/reference/audit-rules/aud-avoid-updating-primary-key-values) | `aud-avoid-updating-primary-key-values` | warning |
| [避免更新唯一约束的值](/reference/audit-rules/aud-avoid-updating-unique-constraint-values) | `aud-avoid-updating-unique-constraint-values` | warning |
| [HIVE中关联字段分桶数应保持整数倍](/reference/audit-rules/aud-bucket-count-integer-multiple-for-join-in-hive) | `aud-bucket-count-integer-multiple-for-join-in-hive` | info |
| [DELETE/UPDATE禁止使用连接](/reference/audit-rules/aud-deleteupdate-forbidden-with-table-join) | `aud-deleteupdate-forbidden-with-table-join` | warning |
| [对分片表的INSERT/REPLACE时字段必须包含分布键](/reference/audit-rules/aud-distribution-key-required-in-insertreplace-for-s) | `aud-distribution-key-required-in-insertreplace-for-s` | error |
| [数据操作语句影响的行数不得超过阈值](/reference/audit-rules/aud-dml-affected-rows-must-not-exceed-threshold) | `aud-dml-affected-rows-must-not-exceed-threshold` | error |
| [过滤条件中必须使用主键或索引列](/reference/audit-rules/aud-filter-condition-must-use-primary-key-or-index-c) | `aud-filter-condition-must-use-primary-key-or-index-c` | info |
| [提前过滤不合法的值避免多余计算](/reference/audit-rules/aud-filter-invalid-values-early-to-avoid-unnecessary) | `aud-filter-invalid-values-early-to-avoid-unnecessary` | info |
| [经常更新的表应使用本地表](/reference/audit-rules/aud-frequentlyupdatedtablesshoulduselocaltables) | `aud-frequentlyupdatedtablesshoulduselocaltables` | info |
| [分组字段不包含分布键](/reference/audit-rules/aud-group-by-fields-must-include-distribution-key) | `aud-group-by-fields-must-include-distribution-key` | warning |
| [禁止对非整形常量进行GROUP BY](/reference/audit-rules/aud-groupbyconstexprdisallowed) | `aud-groupbyconstexprdisallowed` | warning |
| [INSERT 语句必须包含主键字段](/reference/audit-rules/aud-insert-must-include-primary-key-column) | `aud-insert-must-include-primary-key-column` | warning |
| [INSERT语句中值的数量超过阈值](/reference/audit-rules/aud-insert-value-count-exceeds-threshold) | `aud-insert-value-count-exceeds-threshold` | info |
| [INSERT...VALUES列和值数量一致](/reference/audit-rules/aud-insert-values-column-and-value-count-match) | `aud-insert-values-column-and-value-count-match` | error |
| [INSERT...VALUES应该指定列名](/reference/audit-rules/aud-insert-values-must-specify-column-names) | `aud-insert-values-must-specify-column-names` | error |
| [表关联字段数据类型长度不一致](/reference/audit-rules/aud-joincolumndatatypemismatch) | `aud-joincolumndatatypemismatch` | info |
| [表连接缺少连接条件](/reference/audit-rules/aud-missingjoincondition) | `aud-missingjoincondition` | info |
| [禁止修改分区键的值](/reference/audit-rules/aud-modifyingpartitionkeyvaluedisallowed) | `aud-modifyingpartitionkeyvaluedisallowed` | warning |
| [禁止修改分片键的值](/reference/audit-rules/aud-modifyingshardkeyvaluedisallowed) | `aud-modifyingshardkeyvaluedisallowed` | warning |
| [分区键上的过滤条件禁止使用 TO_DATE/TO_TIMESTAMP 函数](/reference/audit-rules/aud-no-todatetotimestamp-on-partition-key-in-filter-) | `aud-no-todatetotimestamp-on-partition-key-in-filter-` | error |
| [HIVE中使用非分桶字段进行表关联](/reference/audit-rules/aud-nonbucket-column-table-join-in-hive) | `aud-nonbucket-column-table-join-in-hive` | info |
| [IN可空子查询可能导致结果集不符合预期](/reference/audit-rules/aud-nullable-in-subquery-may-produce-unexpected-resu) | `aud-nullable-in-subquery-may-produce-unexpected-resu` | error |
| [禁止使用=NULL判断空值](/reference/audit-rules/aud-nullvaluecomparisondisallowed) | `aud-nullvaluecomparisondisallowed` | warning |
| [查询中表连接的个数超过阈值](/reference/audit-rules/aud-number-of-joined-tables-exceeds-threshold) | `aud-number-of-joined-tables-exceeds-threshold` | warning |
| [禁止表关联数目超过阈值（严重）](/reference/audit-rules/aud-numberofjoinedtablesexceedcriticalthreshold) | `aud-numberofjoinedtablesexceedcriticalthreshold` | error |
| [复制表与分片表外关联的查询优化](/reference/audit-rules/aud-optimize-outer-join-between-replicated-and-shard) | `aud-optimize-outer-join-between-replicated-and-shard` | info |
| [UPDATE/DELETE 禁止使用 ORDER 子句](/reference/audit-rules/aud-order-by-forbidden-in-updatedelete) | `aud-order-by-forbidden-in-updatedelete` | warning |
| [禁止对非整形常量进行ORDER BY](/reference/audit-rules/aud-orderbyconstexprdisallowed) | `aud-orderbyconstexprdisallowed` | warning |
| [外连接优化](/reference/audit-rules/aud-outer-join-to-inner-join-conversion) | `aud-outer-join-to-inner-join-conversion` | info |
| [分区字段上有运算导致无法进行分区裁剪](/reference/audit-rules/aud-partition-column-operation-prevents-partition-pr) | `aud-partition-column-operation-prevents-partition-pr` | warning |
| [访问分区表没有使用分区字段过滤](/reference/audit-rules/aud-partition-table-queried-without-partition-key-fi) | `aud-partition-table-queried-without-partition-key-fi` | info |
| [同表同字段比较](/reference/audit-rules/aud-same-table-same-column-comparison) | `aud-same-table-same-column-comparison` | warning |
| [SELECT 语句必须带LIMIT](/reference/audit-rules/aud-select-statement-must-have-limit) | `aud-select-statement-must-have-limit` | info |
| [分片表不支持 UPDATE 更新的值为子查询](/reference/audit-rules/aud-sharded-table-update-does-not-support-subquery-v) | `aud-sharded-table-update-does-not-support-subquery-v` | error |
| [SQL长度超过阈值](/reference/audit-rules/aud-sql-length-exceeds-threshold) | `aud-sql-length-exceeds-threshold` | info |
| [禁止使用常见 SQL 注入函数](/reference/audit-rules/aud-sqlinjectionfuncsdisallowed) | `aud-sqlinjectionfuncsdisallowed` | warning |
| [子查询的嵌套层次超过阈值](/reference/audit-rules/aud-subquery-nesting-depth-exceeds-threshold) | `aud-subquery-nesting-depth-exceeds-threshold` | warning |
| [INSERT语句禁止使用SYSDATE函数](/reference/audit-rules/aud-sysdate-function-forbidden-in-insert) | `aud-sysdate-function-forbidden-in-insert` | warning |
| [UPDATE/DELETE操作使用 LIMIT 子句](/reference/audit-rules/aud-updatedelete-with-limit-warning) | `aud-updatedelete-with-limit-warning` | warning |
| [批量删除建议使用分区表删除分区](/reference/audit-rules/aud-use-drop-partition-instead-of-batch-delete) | `aud-use-drop-partition-instead-of-batch-delete` | info |
| [使用日期时间字段删除建议改为分区表删除分区](/reference/audit-rules/aud-use-drop-partition-instead-of-delete-for-datebas) | `aud-use-drop-partition-instead-of-delete-for-datebas` | warning |
| [建议使用'<>'代替'!='](/reference/audit-rules/aud-use-instead-of) | `aud-use-instead-of` | warning |
| [在一个查询块中引用多表应使用别名](/reference/audit-rules/aud-use-table-aliases-in-multitable-queries) | `aud-use-table-aliases-in-multitable-queries` | info |
| [应通过唯一性索引来进行数据更新操作](/reference/audit-rules/aud-use-unique-index-for-data-update-operations) | `aud-use-unique-index-for-data-update-operations` | info |
| [对于入参建议使用变量绑定](/reference/audit-rules/aud-use-variable-binding-for-parameters) | `aud-use-variable-binding-for-parameters` | warning |
| [视图展开](/reference/audit-rules/aud-viewexpansion) | `aud-viewexpansion` | info |

## 索引

| 规则 | ID | 严重级别 |
|---|---|---|
| [避免%开头的LIKE查询](/reference/audit-rules/aud-avoid-like-pattern-starting-with-wildcard) | `aud-avoid-like-pattern-starting-with-wildcard` | warning |
| [避免对条件字段使用负向查询](/reference/audit-rules/aud-avoid-negative-queries-on-filter-columns) | `aud-avoid-negative-queries-on-filter-columns` | warning |
| [避免不同字段的OR条件](/reference/audit-rules/aud-avoid-or-conditions-on-different-columns) | `aud-avoid-or-conditions-on-different-columns` | warning |
| [避免ORDERBY字段来自不同表](/reference/audit-rules/aud-avoid-order-by-columns-from-different-tables) | `aud-avoid-order-by-columns-from-different-tables` | info |
| [避免查询排序时指定COLLATION](/reference/audit-rules/aud-avoid-specifying-collation-in-order-by) | `aud-avoid-specifying-collation-in-order-by` | warning |
| [索引中避免使用可空列](/reference/audit-rules/aud-avoidusingnullablecolumnsinindex) | `aud-avoidusingnullablecolumnsinindex` | warning |
| [禁止索引创建时指定collation](/reference/audit-rules/aud-collation4indexdisallowed) | `aud-collation4indexdisallowed` | warning |
| [索引中不应该有重复列](/reference/audit-rules/aud-duplicatecolumnsinindex) | `aud-duplicatecolumnsinindex` | warning |
| [GROUP 字段中有表达式导致索引失效](/reference/audit-rules/aud-expression-in-group-by-causes-index-invalidation) | `aud-expression-in-group-by-causes-index-invalidation` | info |
| [ORDER 字段中有表达式导致索引失效](/reference/audit-rules/aud-expression-in-order-by-causes-index-invalidation) | `aud-expression-in-order-by-causes-index-invalidation` | info |
| [外键命名规范](/reference/audit-rules/aud-foreign-key-naming-convention) | `aud-foreign-key-naming-convention` | info |
| [禁止使用全文索引](/reference/audit-rules/aud-fulltextindexdisallowed) | `aud-fulltextindexdisallowed` | warning |
| [禁止使用函数索引](/reference/audit-rules/aud-functionalindexdisallowed) | `aud-functionalindexdisallowed` | warning |
| [禁止在分布式表上创建全局索引](/reference/audit-rules/aud-globalindexondistributedtabledisallowed) | `aud-globalindexondistributedtabledisallowed` | warning |
| [禁止在分区表上创建全局索引](/reference/audit-rules/aud-globalindexonpartitionedtabledisallowed) | `aud-globalindexonpartitionedtabledisallowed` | warning |
| [GROUPBY字段来自不同表](/reference/audit-rules/aud-group-by-columns-from-multiple-tables) | `aud-group-by-columns-from-multiple-tables` | info |
| [隐式类型转换导致索引失效](/reference/audit-rules/aud-implicit-type-conversion-causes-index-invalidati) | `aud-implicit-type-conversion-causes-index-invalidati` | warning |
| [建议索引字段对区分度大于阈值](/reference/audit-rules/aud-index-column-selectivity-should-exceed-threshold) | `aud-index-column-selectivity-should-exceed-threshold` | info |
| [索引失效或不可见](/reference/audit-rules/aud-index-invalid-or-invisible) | `aud-index-invalid-or-invisible` | warning |
| [索引命名规范](/reference/audit-rules/aud-index-naming-convention) | `aud-index-naming-convention` | info |
| [索引必须要有名字](/reference/audit-rules/aud-indexnamerequired) | `aud-indexnamerequired` | info |
| [连接字段类型不匹配导致索引失效](/reference/audit-rules/aud-join-column-type-mismatch-causes-index-invalidat) | `aud-join-column-type-mismatch-causes-index-invalidat` | warning |
| [索引的字段长度不应超过阈值](/reference/audit-rules/aud-longlengthcolumns4indexdisallowed) | `aud-longlengthcolumns4indexdisallowed` | warning |
| [排序字段方向不同导致索引失效](/reference/audit-rules/aud-mixed-sort-directions-cause-index-inefficiency) | `aud-mixed-sort-directions-cause-index-inefficiency` | info |
| [单表的索引个数超过阈值](/reference/audit-rules/aud-number-of-indexes-exceeds-threshold) | `aud-number-of-indexes-exceeds-threshold` | warning |
| [索引中的字段数目超过阈值](/reference/audit-rules/aud-numberofcolumnsinindexexceedthreshold) | `aud-numberofcolumnsinindexexceedthreshold` | warning |
| [主键命名规范](/reference/audit-rules/aud-primary-key-naming-convention) | `aud-primary-key-naming-convention` | info |
| [禁止创建重复索引/冗余索引](/reference/audit-rules/aud-redundantindexdisallowed) | `aud-redundantindexdisallowed` | warning |
| [索引列上的运算导致索引失效](/reference/audit-rules/aud-rulefuncwithcolumninpredicate) | `aud-rulefuncwithcolumninpredicate` | info |
| [索引中的字段不可以为TEXT和LOB类型](/reference/audit-rules/aud-textlobcolumnsinindexdisallowed) | `aud-textlobcolumnsinindexdisallowed` | warning |
| [索引长度不得超过阈值](/reference/audit-rules/aud-totalindexlengthexceedthreshold) | `aud-totalindexlengthexceedthreshold` | info |
| [唯一性索引命名规范](/reference/audit-rules/aud-unique-key-naming-convention) | `aud-unique-key-naming-convention` | info |
| [长度大于阈值的字段建立索引时使用前缀](/reference/audit-rules/aud-use-prefix-index-for-long-varchar-columns) | `aud-use-prefix-index-for-long-varchar-columns` | warning |

## 待分类

| 规则 | ID | 严重级别 |
|---|---|---|
| [使用不存在的列](/reference/audit-rules/aud-column-with-this-name-does-not-exist) | `aud-column-with-this-name-does-not-exist` | error |
