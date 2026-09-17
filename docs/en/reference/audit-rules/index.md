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

220 rules.


## Schema & Object Design (DDL)

| Rule | ID | Severity |
|---|---|---|
| [AddCheckConstraintShouldBeDeferred](/en/reference/audit-rules/aud-addcheckconstraintshouldbedeferred) | `aud-addcheckconstraintshouldbedeferred` | warning |
| [AddingColumnsWithDefaultDisallowed](/en/reference/audit-rules/aud-addingcolumnswithdefaultdisallowed) | `aud-addingcolumnswithdefaultdisallowed` | warning |
| [Auto-increment column naming convention](/en/reference/audit-rules/aud-autoincrement-column-naming-convention) | `aud-autoincrement-column-naming-convention` | info |
| [Avoid Joining on Non-Distribution Key Columns](/en/reference/audit-rules/aud-avoid-joining-on-nondistribution-key-columns) | `aud-avoid-joining-on-nondistribution-key-columns` | warning |
| [Avoid Multiple Distribution Keys](/en/reference/audit-rules/aud-avoid-multiple-distribution-keys) | `aud-avoid-multiple-distribution-keys` | warning |
| [Avoid Non-Distributed Tables](/en/reference/audit-rules/aud-avoid-nondistributed-tables) | `aud-avoid-nondistributed-tables` | warning |
| [Avoid Replicated Distribution for Large Tables](/en/reference/audit-rules/aud-avoid-replicated-distribution-for-large-tables) | `aud-avoid-replicated-distribution-for-large-tables` | warning |
| [CacheExhausted4IdentityColumn](/en/reference/audit-rules/aud-cacheexhausted4identitycolumn) | `aud-cacheexhausted4identitycolumn` | warning |
| [ChangingColumnNameDisallowed](/en/reference/audit-rules/aud-changingcolumnnamedisallowed) | `aud-changingcolumnnamedisallowed` | warning |
| [ChangingColumn's Order Disallowed](/en/reference/audit-rules/aud-changingcolumns-order-disallowed) | `aud-changingcolumns-order-disallowed` | warning |
| [ChangingColumnTypeDisallowed](/en/reference/audit-rules/aud-changingcolumntypedisallowed) | `aud-changingcolumntypedisallowed` | warning |
| [Char Column Length Exceeds Threshold](/en/reference/audit-rules/aud-char-column-length-exceeds-threshold) | `aud-char-column-length-exceeds-threshold` | info |
| [Character Set Required for Database Creation](/en/reference/audit-rules/aud-character-set-required-for-database-creation) | `aud-character-set-required-for-database-creation` | warning |
| [CharsetOnColumnDisallowed](/en/reference/audit-rules/aud-charsetoncolumndisallowed) | `aud-charsetoncolumndisallowed` | warning |
| [CharsetOnTableDisallowed](/en/reference/audit-rules/aud-charsetontabledisallowed) | `aud-charsetontabledisallowed` | warning |
| [CharsetsOnTable&DatabaseMismatch](/en/reference/audit-rules/aud-charsetsontabledatabasemismatch) | `aud-charsetsontabledatabasemismatch` | warning |
| [Column and Table Character Set Mismatch](/en/reference/audit-rules/aud-column-and-table-character-set-mismatch) | `aud-column-and-table-character-set-mismatch` | warning |
| [Column Naming Convention](/en/reference/audit-rules/aud-column-naming-convention) | `aud-column-naming-convention` | info |
| [Column with this Name Already Exists](/en/reference/audit-rules/aud-column-with-this-name-already-exists) | `aud-column-with-this-name-already-exists` | error |
| [Comments on Column Required](/en/reference/audit-rules/aud-comments-on-column-required) | `aud-comments-on-column-required` | warning |
| [CommentsOnTableRequired](/en/reference/audit-rules/aud-commentsontablerequired) | `aud-commentsontablerequired` | warning |
| [CompressedAttributeDisallowed](/en/reference/audit-rules/aud-compressedattributedisallowed) | `aud-compressedattributedisallowed` | warning |
| [Consider Replicated Distribution for Small Tables](/en/reference/audit-rules/aud-consider-replicated-distribution-for-small-table) | `aud-consider-replicated-distribution-for-small-table` | info |
| [Constraint with this Name Already Exists](/en/reference/audit-rules/aud-constraint-with-this-name-already-exists) | `aud-constraint-with-this-name-already-exists` | error |
| [Create Index Before Constraint](/en/reference/audit-rules/aud-create-index-before-constraint) | `aud-create-index-before-constraint` | warning |
| [Create Index Using Online Mode](/en/reference/audit-rules/aud-create-index-using-online-mode) | `aud-create-index-using-online-mode` | warning |
| [CreateCheckConstraintDisallowed](/en/reference/audit-rules/aud-createcheckconstraintdisallowed) | `aud-createcheckconstraintdisallowed` | warning |
| [CTAS Naming Convention](/en/reference/audit-rules/aud-ctas-naming-convention) | `aud-ctas-naming-convention` | info |
| [Database Naming Convention](/en/reference/audit-rules/aud-database-naming-convention) | `aud-database-naming-convention` | info |
| [DataTypeLimitOfPrimaryKey](/en/reference/audit-rules/aud-datatypelimitofprimarykey) | `aud-datatypelimitofprimarykey` | warning |
| [DataTypesDisallowed](/en/reference/audit-rules/aud-datatypesdisallowed) | `aud-datatypesdisallowed` | warning |
| [DecreasingPrecisionDisallowed](/en/reference/audit-rules/aud-decreasingprecisiondisallowed) | `aud-decreasingprecisiondisallowed` | warning |
| [Default Collation Required for Database](/en/reference/audit-rules/aud-default-collation-required-for-database) | `aud-default-collation-required-for-database` | warning |
| [Default Value Required for NOT NULL Columns](/en/reference/audit-rules/aud-default-value-required-for-not-null-columns) | `aud-default-value-required-for-not-null-columns` | warning |
| [Default Value Required for Time Columns](/en/reference/audit-rules/aud-default-value-required-for-time-columns) | `aud-default-value-required-for-time-columns` | warning |
| [Default Value Required for Timestamp Columns](/en/reference/audit-rules/aud-default-value-required-for-timestamp-columns) | `aud-default-value-required-for-timestamp-columns` | warning |
| [DiffDataTypesOfRIColumns](/en/reference/audit-rules/aud-diffdatatypesofricolumns) | `aud-diffdatatypesofricolumns` | warning |
| [Distribution Key Data Type Restriction](/en/reference/audit-rules/aud-distribution-key-data-type-restriction) | `aud-distribution-key-data-type-restriction` | warning |
| [Distribution Key Length Must Not Exceed Threshold](/en/reference/audit-rules/aud-distribution-key-length-must-not-exceed-threshol) | `aud-distribution-key-length-must-not-exceed-threshol` | warning |
| [Distribution Key Must Have NOT NULL Constraint](/en/reference/audit-rules/aud-distribution-key-must-have-not-null-constraint) | `aud-distribution-key-must-have-not-null-constraint` | info |
| [Distribution Key Must Use Specified Collation](/en/reference/audit-rules/aud-distribution-key-must-use-specified-collation) | `aud-distribution-key-must-use-specified-collation` | warning |
| [Drop Columns Only with Specified Naming Convention](/en/reference/audit-rules/aud-drop-columns-only-with-specified-naming-conventi) | `aud-drop-columns-only-with-specified-naming-conventi` | warning |
| [Drop Tables/Views Only with Specified Naming Convention](/en/reference/audit-rules/aud-drop-tablesviews-only-with-specified-naming-conv) | `aud-drop-tablesviews-only-with-specified-naming-conv` | warning |
| [DroppingColumnsDisallowed](/en/reference/audit-rules/aud-droppingcolumnsdisallowed) | `aud-droppingcolumnsdisallowed` | warning |
| [DroppingColumnsUsedInIndexDisallowed](/en/reference/audit-rules/aud-droppingcolumnsusedinindexdisallowed) | `aud-droppingcolumnsusedinindexdisallowed` | warning |
| [DroppingIndexDisallowed](/en/reference/audit-rules/aud-droppingindexdisallowed) | `aud-droppingindexdisallowed` | warning |
| [DropTable/ViewDisallowed](/en/reference/audit-rules/aud-droptableviewdisallowed) | `aud-droptableviewdisallowed` | warning |
| [DuplicatedObjectNamesWithKeywords](/en/reference/audit-rules/aud-duplicatedobjectnameswithkeywords) | `aud-duplicatedobjectnameswithkeywords` | warning |
| [EnumDataTypeDisallowed](/en/reference/audit-rules/aud-enumdatatypedisallowed) | `aud-enumdatatypedisallowed` | warning |
| [Explicit Distribution Key Required](/en/reference/audit-rules/aud-explicit-distribution-key-required) | `aud-explicit-distribution-key-required` | warning |
| [ForeignKeyDisallowed](/en/reference/audit-rules/aud-foreignkeydisallowed) | `aud-foreignkeydisallowed` | warning |
| [High dirty page ratio](/en/reference/audit-rules/aud-high-dirty-page-ratio) | `aud-high-dirty-page-ratio` | warning |
| [Hive Internal Tables Must Use ORC/Parquet Format](/en/reference/audit-rules/aud-hive-internal-tables-must-use-orcparquet-format) | `aud-hive-internal-tables-must-use-orcparquet-format` | error |
| [Hive Table Compression Format Required](/en/reference/audit-rules/aud-hive-table-compression-format-required) | `aud-hive-table-compression-format-required` | error |
| [IF EXISTS Required for Dropping Objects](/en/reference/audit-rules/aud-if-exists-required-for-dropping-objects) | `aud-if-exists-required-for-dropping-objects` | warning |
| [IF NOT EXISTS Required for Creating Objects](/en/reference/audit-rules/aud-if-not-exists-required-for-creating-objects) | `aud-if-not-exists-required-for-creating-objects` | warning |
| [IncColumn4PrimaryKeyDisallowed](/en/reference/audit-rules/aud-inccolumn4primarykeydisallowed) | `aud-inccolumn4primarykeydisallowed` | warning |
| [IncColumn4PrimaryKeyRequired](/en/reference/audit-rules/aud-inccolumn4primarykeyrequired) | `aud-inccolumn4primarykeyrequired` | warning |
| [Index with this Name Already Exists](/en/reference/audit-rules/aud-index-with-this-name-already-exists) | `aud-index-with-this-name-already-exists` | error |
| [Index with this Name Does't Exists](/en/reference/audit-rules/aud-index-with-this-name-doest-exists) | `aud-index-with-this-name-doest-exists` | error |
| [InitValue4IdentityColumn](/en/reference/audit-rules/aud-initvalue4identitycolumn) | `aud-initvalue4identitycolumn` | warning |
| [InnoDB Storage Engine Required](/en/reference/audit-rules/aud-innodb-storage-engine-required) | `aud-innodb-storage-engine-required` | warning |
| [LargeObjectDefaultNonNullDisallowed](/en/reference/audit-rules/aud-largeobjectdefaultnonnulldisallowed) | `aud-largeobjectdefaultnonnulldisallowed` | warning |
| [LargeTableShouldBeSharded](/en/reference/audit-rules/aud-largetableshouldbesharded) | `aud-largetableshouldbesharded` | info |
| [MaxValueDefaultPartitionDisallowed](/en/reference/audit-rules/aud-maxvaluedefaultpartitiondisallowed) | `aud-maxvaluedefaultpartitiondisallowed` | info |
| [ModifyingColumnAddDefaultDisallowed](/en/reference/audit-rules/aud-modifyingcolumnadddefaultdisallowed) | `aud-modifyingcolumnadddefaultdisallowed` | warning |
| [ModifyingColumnAddNotNullDisallowed](/en/reference/audit-rules/aud-modifyingcolumnaddnotnulldisallowed) | `aud-modifyingcolumnaddnotnulldisallowed` | warning |
| [ModifyingColumnChangeDefaultDisallowed](/en/reference/audit-rules/aud-modifyingcolumnchangedefaultdisallowed) | `aud-modifyingcolumnchangedefaultdisallowed` | warning |
| [ModifyingDistributionKeyTypeDisallowed](/en/reference/audit-rules/aud-modifyingdistributionkeytypedisallowed) | `aud-modifyingdistributionkeytypedisallowed` | warning |
| [ModifyTableCharSetDisallowed](/en/reference/audit-rules/aud-modifytablecharsetdisallowed) | `aud-modifytablecharsetdisallowed` | warning |
| [Non-Null Default Value Required for Non-Excluded Columns](/en/reference/audit-rules/aud-nonnull-default-value-required-for-nonexcluded-c) | `aud-nonnull-default-value-required-for-nonexcluded-c` | warning |
| [NonNullConstraint4ColumnsInListDisallowed](/en/reference/audit-rules/aud-nonnullconstraint4columnsinlistdisallowed) | `aud-nonnullconstraint4columnsinlistdisallowed` | warning |
| [NumOfColumnsExceedThreshold](/en/reference/audit-rules/aud-numofcolumnsexceedthreshold) | `aud-numofcolumnsexceedthreshold` | warning |
| [NumOfPKColumnsExceed](/en/reference/audit-rules/aud-numofpkcolumnsexceed) | `aud-numofpkcolumnsexceed` | warning |
| [Object Name Length Must Not Exceed Threshold](/en/reference/audit-rules/aud-object-name-length-must-not-exceed-threshold) | `aud-object-name-length-must-not-exceed-threshold` | warning |
| [Object Naming Convention](/en/reference/audit-rules/aud-object-naming-convention) | `aud-object-naming-convention` | info |
| [OneIdentityColumnAllowed](/en/reference/audit-rules/aud-oneidentitycolumnallowed) | `aud-oneidentitycolumnallowed` | warning |
| [Partition Key Length Must Not Exceed Threshold](/en/reference/audit-rules/aud-partition-key-length-must-not-exceed-threshold) | `aud-partition-key-length-must-not-exceed-threshold` | warning |
| [PartitionedTableDisallowed](/en/reference/audit-rules/aud-partitionedtabledisallowed) | `aud-partitionedtabledisallowed` | info |
| [Prefer Hash Distribution](/en/reference/audit-rules/aud-prefer-hash-distribution) | `aud-prefer-hash-distribution` | warning |
| [PrimaryKeyRequired](/en/reference/audit-rules/aud-primarykeyrequired) | `aud-primarykeyrequired` | error |
| [Schema Naming Convention](/en/reference/audit-rules/aud-schema-naming-convention) | `aud-schema-naming-convention` | info |
| [SetDataTypeDisallowed](/en/reference/audit-rules/aud-setdatatypedisallowed) | `aud-setdatatypedisallowed` | warning |
| [ShortenDataTypeLengthDisallowed](/en/reference/audit-rules/aud-shortendatatypelengthdisallowed) | `aud-shortendatatypelengthdisallowed` | warning |
| [SignedInteger4IdentityColumnDisallowed](/en/reference/audit-rules/aud-signedinteger4identitycolumndisallowed) | `aud-signedinteger4identitycolumndisallowed` | warning |
| [Specific Character Set Required for Database Creation](/en/reference/audit-rules/aud-specific-character-set-required-for-database-cre) | `aud-specific-character-set-required-for-database-cre` | warning |
| [Specific Collation Required for Database Creation](/en/reference/audit-rules/aud-specific-collation-required-for-database-creatio) | `aud-specific-collation-required-for-database-creatio` | error |
| [SpecificCharSet4TableRequired](/en/reference/audit-rules/aud-specificcharset4tablerequired) | `aud-specificcharset4tablerequired` | warning |
| [SpecificCollation4TableRequired](/en/reference/audit-rules/aud-specificcollation4tablerequired) | `aud-specificcollation4tablerequired` | warning |
| [SpecificColumnsRequired](/en/reference/audit-rules/aud-specificcolumnsrequired) | `aud-specificcolumnsrequired` | warning |
| [Specify DISABLE and NONVALIDATE for Hive Constraints](/en/reference/audit-rules/aud-specify-disable-and-nonvalidate-for-hive-constra) | `aud-specify-disable-and-nonvalidate-for-hive-constra` | warning |
| [Stored Procedure Disallowed](/en/reference/audit-rules/aud-stored-procedure-disallowed) | `aud-stored-procedure-disallowed` | warning |
| [Table naming convention](/en/reference/audit-rules/aud-table-naming-convention) | `aud-table-naming-convention` | info |
| [Table/View with this Name Already Exists](/en/reference/audit-rules/aud-tableview-with-this-name-already-exists) | `aud-tableview-with-this-name-already-exists` | error |
| [Table/View with this Name Does't Exists](/en/reference/audit-rules/aud-tableview-with-this-name-doest-exists) | `aud-tableview-with-this-name-doest-exists` | error |
| [Timestamp Data Type Disallowed](/en/reference/audit-rules/aud-timestamp-data-type-disallowed) | `aud-timestamp-data-type-disallowed` | warning |
| [TriggerDisallowed](/en/reference/audit-rules/aud-triggerdisallowed) | `aud-triggerdisallowed` | warning |
| [UpdateTimeStampColumnsRequired](/en/reference/audit-rules/aud-updatetimestampcolumnsrequired) | `aud-updatetimestampcolumnsrequired` | warning |
| [UpdatingColumnsUsedInIndexDisallowed](/en/reference/audit-rules/aud-updatingcolumnsusedinindexdisallowed) | `aud-updatingcolumnsusedinindexdisallowed` | warning |
| [Use ALTER TABLE to Set Auto Increment Start in TDSQL](/en/reference/audit-rules/aud-use-alter-table-to-set-auto-increment-start-in-t) | `aud-use-alter-table-to-set-auto-increment-start-in-t` | info |
| [Use Bucketing Strategy for Large Hive Tables](/en/reference/audit-rules/aud-use-bucketing-strategy-for-large-hive-tables) | `aud-use-bucketing-strategy-for-large-hive-tables` | warning |
| [Use High Cardinality Distribution Keys](/en/reference/audit-rules/aud-use-high-cardinality-distribution-keys) | `aud-use-high-cardinality-distribution-keys` | warning |
| [Use INT(10) or BIGINT(20) for Integer Columns](/en/reference/audit-rules/aud-use-int10-or-bigint20-for-integer-columns) | `aud-use-int10-or-bigint20-for-integer-columns` | info |
| [Use Partitioned Tables for Large Hive Tables](/en/reference/audit-rules/aud-use-partitioned-tables-for-large-hive-tables) | `aud-use-partitioned-tables-for-large-hive-tables` | warning |
| [Use Partitioned Tables for Large Tables](/en/reference/audit-rules/aud-use-partitioned-tables-for-large-tables) | `aud-use-partitioned-tables-for-large-tables` | info |
| [Use Primary Key as Distribution Key](/en/reference/audit-rules/aud-use-primary-key-as-distribution-key) | `aud-use-primary-key-as-distribution-key` | warning |
| [Use Specified Data Distribution Method](/en/reference/audit-rules/aud-use-specified-data-distribution-method) | `aud-use-specified-data-distribution-method` | warning |
| [UseDecimalForNumericColumns](/en/reference/audit-rules/aud-usedecimalfornumericcolumns) | `aud-usedecimalfornumericcolumns` | warning |
| [UserDefinedFunction(UDF) Disallowed](/en/reference/audit-rules/aud-userdefinedfunctionudf-disallowed) | `aud-userdefinedfunctionudf-disallowed` | error |
| [UserDefinedType(UDT) Disallowed](/en/reference/audit-rules/aud-userdefinedtypeudt-disallowed) | `aud-userdefinedtypeudt-disallowed` | warning |
| [UseSysdateAsDefaultDisallowed](/en/reference/audit-rules/aud-usesysdateasdefaultdisallowed) | `aud-usesysdateasdefaultdisallowed` | warning |
| [VARCHAR Column Length Exceeds Threshold](/en/reference/audit-rules/aud-varchar-column-length-exceeds-threshold) | `aud-varchar-column-length-exceeds-threshold` | warning |
| [ViewDisallowed](/en/reference/audit-rules/aud-viewdisallowed) | `aud-viewdisallowed` | warning |

## Data Manipulation (DML)

| Rule | ID | Severity |
|---|---|---|
| [Add Schema Qualifier Before Object References](/en/reference/audit-rules/aud-add-schema-qualifier-before-object-references) | `aud-add-schema-qualifier-before-object-references` | info |
| [Avoid ANTI JOIN Operations in Distributed Databases](/en/reference/audit-rules/aud-avoid-anti-join-operations-in-distributed-databa) | `aud-avoid-anti-join-operations-in-distributed-databa` | warning |
| [Avoid COUNT DISTINCT on Multiple Nullable Columns](/en/reference/audit-rules/aud-avoid-count-distinct-on-multiple-nullable-column) | `aud-avoid-count-distinct-on-multiple-nullable-column` | info |
| [Avoid CROSS JOIN](/en/reference/audit-rules/aud-avoid-cross-join) | `aud-avoid-cross-join` | warning |
| [Avoid Cross-Shard DML Operations in Distributed Databases](/en/reference/audit-rules/aud-avoid-crossshard-dml-operations-in-distributed-d) | `aud-avoid-crossshard-dml-operations-in-distributed-d` | warning |
| [Avoid Duplicate Table Aliases](/en/reference/audit-rules/aud-avoid-duplicate-table-aliases) | `aud-avoid-duplicate-table-aliases` | warning |
| [Avoid FOR UPDATE with Derived Tables](/en/reference/audit-rules/aud-avoid-for-update-with-derived-tables) | `aud-avoid-for-update-with-derived-tables` | warning |
| [Avoid GROUP BY Column Ordinal Position](/en/reference/audit-rules/aud-avoid-group-by-column-ordinal-position) | `aud-avoid-group-by-column-ordinal-position` | info |
| [Avoid GROUP BY on Long Columns](/en/reference/audit-rules/aud-avoid-group-by-on-long-columns) | `aud-avoid-group-by-on-long-columns` | warning |
| [Avoid Leading or Trailing Spaces in String Literals](/en/reference/audit-rules/aud-avoid-leading-or-trailing-spaces-in-string-liter) | `aud-avoid-leading-or-trailing-spaces-in-string-liter` | warning |
| [Avoid LIKE Without Wildcards](/en/reference/audit-rules/aud-avoid-like-without-wildcards) | `aud-avoid-like-without-wildcards` | warning |
| [Avoid LIMIT Without ORDER BY in SELECT](/en/reference/audit-rules/aud-avoid-limit-without-order-by-in-select) | `aud-avoid-limit-without-order-by-in-select` | warning |
| [Avoid LIMIT Without ORDER BY in UPDATE/DELETE](/en/reference/audit-rules/aud-avoid-limit-without-order-by-in-updatedelete) | `aud-avoid-limit-without-order-by-in-updatedelete` | warning |
| [Avoid NATURAL JOIN](/en/reference/audit-rules/aud-avoid-natural-join) | `aud-avoid-natural-join` | warning |
| [Avoid ORDER BY Column Ordinal Position](/en/reference/audit-rules/aud-avoid-order-by-column-ordinal-position) | `aud-avoid-order-by-column-ordinal-position` | info |
| [Avoid ORDER BY on Long Columns](/en/reference/audit-rules/aud-avoid-order-by-on-long-columns) | `aud-avoid-order-by-on-long-columns` | warning |
| [Avoid ORDER BY Random Function](/en/reference/audit-rules/aud-avoid-order-by-random-function) | `aud-avoid-order-by-random-function` | warning |
| [Avoid Scalar Subqueries](/en/reference/audit-rules/aud-avoid-scalar-subqueries) | `aud-avoid-scalar-subqueries` | info |
| [SELECT * Detection](/en/reference/audit-rules/aud-avoid-select) | `aud-avoid-select` | info |
| [Avoid SELECT with FOR UPDATE](/en/reference/audit-rules/aud-avoid-select-with-for-update) | `aud-avoid-select-with-for-update` | warning |
| [Avoid SELECT with LIMIT and FOR UPDATE](/en/reference/audit-rules/aud-avoid-select-with-limit-and-for-update) | `aud-avoid-select-with-limit-and-for-update` | warning |
| [Avoid SELECT Without WHERE and GROUP BY](/en/reference/audit-rules/aud-avoid-select-without-where-and-group-by) | `aud-avoid-select-without-where-and-group-by` | info |
| [Avoid STRAIGHT JOIN](/en/reference/audit-rules/aud-avoid-straight-join) | `aud-avoid-straight-join` | warning |
| [UPDATE/DELETE without WHERE](/en/reference/audit-rules/aud-avoid-unconditional-updatedelete-statements) | `aud-avoid-unconditional-updatedelete-statements` | warning |
| [Avoid Unnecessary Built-in Functions](/en/reference/audit-rules/aud-avoid-unnecessary-builtin-functions) | `aud-avoid-unnecessary-builtin-functions` | info |
| [Avoid Unnecessary DISTINCT Operations](/en/reference/audit-rules/aud-avoid-unnecessary-distinct-operations) | `aud-avoid-unnecessary-distinct-operations` | info |
| [Avoid Unnecessary UPDATE Operations](/en/reference/audit-rules/aud-avoid-unnecessary-update-operations) | `aud-avoid-unnecessary-update-operations` | info |
| [Avoid Updating Primary Key Values](/en/reference/audit-rules/aud-avoid-updating-primary-key-values) | `aud-avoid-updating-primary-key-values` | warning |
| [Avoid Updating Unique Constraint Values](/en/reference/audit-rules/aud-avoid-updating-unique-constraint-values) | `aud-avoid-updating-unique-constraint-values` | warning |
| [Bucket Count Integer Multiple for Join in Hive](/en/reference/audit-rules/aud-bucket-count-integer-multiple-for-join-in-hive) | `aud-bucket-count-integer-multiple-for-join-in-hive` | info |
| [DELETE/UPDATE Forbidden with Table Join](/en/reference/audit-rules/aud-deleteupdate-forbidden-with-table-join) | `aud-deleteupdate-forbidden-with-table-join` | warning |
| [Distribution Key Required in INSERT/REPLACE for Sharded Tables](/en/reference/audit-rules/aud-distribution-key-required-in-insertreplace-for-s) | `aud-distribution-key-required-in-insertreplace-for-s` | error |
| [DML Affected Rows Must Not Exceed Threshold](/en/reference/audit-rules/aud-dml-affected-rows-must-not-exceed-threshold) | `aud-dml-affected-rows-must-not-exceed-threshold` | error |
| [Filter Condition Must Use Primary Key or Index Column](/en/reference/audit-rules/aud-filter-condition-must-use-primary-key-or-index-c) | `aud-filter-condition-must-use-primary-key-or-index-c` | info |
| [Filter Invalid Values Early to Avoid Unnecessary Computation](/en/reference/audit-rules/aud-filter-invalid-values-early-to-avoid-unnecessary) | `aud-filter-invalid-values-early-to-avoid-unnecessary` | info |
| [FrequentlyUpdatedTablesShouldUseLocalTables](/en/reference/audit-rules/aud-frequentlyupdatedtablesshoulduselocaltables) | `aud-frequentlyupdatedtablesshoulduselocaltables` | info |
| [GROUP BY Fields Must Include Distribution Key](/en/reference/audit-rules/aud-group-by-fields-must-include-distribution-key) | `aud-group-by-fields-must-include-distribution-key` | warning |
| [GroupByConstExprDisallowed](/en/reference/audit-rules/aud-groupbyconstexprdisallowed) | `aud-groupbyconstexprdisallowed` | warning |
| [INSERT Must Include Primary Key Column](/en/reference/audit-rules/aud-insert-must-include-primary-key-column) | `aud-insert-must-include-primary-key-column` | warning |
| [INSERT Value Count Exceeds Threshold](/en/reference/audit-rules/aud-insert-value-count-exceeds-threshold) | `aud-insert-value-count-exceeds-threshold` | info |
| [INSERT VALUES Column and Value Count Match](/en/reference/audit-rules/aud-insert-values-column-and-value-count-match) | `aud-insert-values-column-and-value-count-match` | error |
| [INSERT VALUES Must Specify Column Names](/en/reference/audit-rules/aud-insert-values-must-specify-column-names) | `aud-insert-values-must-specify-column-names` | error |
| [JoinColumnDataTypeMismatch](/en/reference/audit-rules/aud-joincolumndatatypemismatch) | `aud-joincolumndatatypemismatch` | info |
| [MissingJoinCondition](/en/reference/audit-rules/aud-missingjoincondition) | `aud-missingjoincondition` | info |
| [ModifyingPartitionKeyValueDisallowed](/en/reference/audit-rules/aud-modifyingpartitionkeyvaluedisallowed) | `aud-modifyingpartitionkeyvaluedisallowed` | warning |
| [ModifyingShardKeyValueDisallowed](/en/reference/audit-rules/aud-modifyingshardkeyvaluedisallowed) | `aud-modifyingshardkeyvaluedisallowed` | warning |
| [No TO_DATE/TO_TIMESTAMP on Partition Key in Filter Conditions](/en/reference/audit-rules/aud-no-todatetotimestamp-on-partition-key-in-filter-) | `aud-no-todatetotimestamp-on-partition-key-in-filter-` | error |
| [Non-Bucket Column Table Join in Hive](/en/reference/audit-rules/aud-nonbucket-column-table-join-in-hive) | `aud-nonbucket-column-table-join-in-hive` | info |
| [Nullable IN Subquery May Produce Unexpected Results](/en/reference/audit-rules/aud-nullable-in-subquery-may-produce-unexpected-resu) | `aud-nullable-in-subquery-may-produce-unexpected-resu` | error |
| [NullValueComparisonDisallowed](/en/reference/audit-rules/aud-nullvaluecomparisondisallowed) | `aud-nullvaluecomparisondisallowed` | warning |
| [Number of Joined Tables Exceeds Threshold](/en/reference/audit-rules/aud-number-of-joined-tables-exceeds-threshold) | `aud-number-of-joined-tables-exceeds-threshold` | warning |
| [NumberOfJoinedTablesExceedCriticalThreshold](/en/reference/audit-rules/aud-numberofjoinedtablesexceedcriticalthreshold) | `aud-numberofjoinedtablesexceedcriticalthreshold` | error |
| [Optimize Outer Join Between Replicated and Sharded Tables](/en/reference/audit-rules/aud-optimize-outer-join-between-replicated-and-shard) | `aud-optimize-outer-join-between-replicated-and-shard` | info |
| [ORDER BY Forbidden in UPDATE/DELETE](/en/reference/audit-rules/aud-order-by-forbidden-in-updatedelete) | `aud-order-by-forbidden-in-updatedelete` | warning |
| [OrderByConstExprDisallowed](/en/reference/audit-rules/aud-orderbyconstexprdisallowed) | `aud-orderbyconstexprdisallowed` | warning |
| [Outer Join to Inner Join Conversion](/en/reference/audit-rules/aud-outer-join-to-inner-join-conversion) | `aud-outer-join-to-inner-join-conversion` | info |
| [Partition Column Operation Prevents Partition Pruning](/en/reference/audit-rules/aud-partition-column-operation-prevents-partition-pr) | `aud-partition-column-operation-prevents-partition-pr` | warning |
| [Partition Table Queried Without Partition Key Filter](/en/reference/audit-rules/aud-partition-table-queried-without-partition-key-fi) | `aud-partition-table-queried-without-partition-key-fi` | info |
| [Same Table Same Column Comparison](/en/reference/audit-rules/aud-same-table-same-column-comparison) | `aud-same-table-same-column-comparison` | warning |
| [SELECT Statement Must Have LIMIT](/en/reference/audit-rules/aud-select-statement-must-have-limit) | `aud-select-statement-must-have-limit` | info |
| [Sharded Table UPDATE Does Not Support Subquery Values](/en/reference/audit-rules/aud-sharded-table-update-does-not-support-subquery-v) | `aud-sharded-table-update-does-not-support-subquery-v` | error |
| [SQL Length Exceeds Threshold](/en/reference/audit-rules/aud-sql-length-exceeds-threshold) | `aud-sql-length-exceeds-threshold` | info |
| [SQLInjectionFuncsDisallowed](/en/reference/audit-rules/aud-sqlinjectionfuncsdisallowed) | `aud-sqlinjectionfuncsdisallowed` | warning |
| [Subquery Nesting Depth Exceeds Threshold](/en/reference/audit-rules/aud-subquery-nesting-depth-exceeds-threshold) | `aud-subquery-nesting-depth-exceeds-threshold` | warning |
| [SYSDATE Function Forbidden in INSERT](/en/reference/audit-rules/aud-sysdate-function-forbidden-in-insert) | `aud-sysdate-function-forbidden-in-insert` | warning |
| [UPDATE/DELETE With LIMIT Warning](/en/reference/audit-rules/aud-updatedelete-with-limit-warning) | `aud-updatedelete-with-limit-warning` | warning |
| [Use DROP PARTITION Instead of Batch DELETE](/en/reference/audit-rules/aud-use-drop-partition-instead-of-batch-delete) | `aud-use-drop-partition-instead-of-batch-delete` | info |
| [Use DROP PARTITION Instead of DELETE for Date-Based Cleanup](/en/reference/audit-rules/aud-use-drop-partition-instead-of-delete-for-datebas) | `aud-use-drop-partition-instead-of-delete-for-datebas` | warning |
| [Use '<>' Instead of '!='](/en/reference/audit-rules/aud-use-instead-of) | `aud-use-instead-of` | warning |
| [Use Table Aliases in Multi-Table Queries](/en/reference/audit-rules/aud-use-table-aliases-in-multitable-queries) | `aud-use-table-aliases-in-multitable-queries` | info |
| [Use Unique Index for Data Update Operations](/en/reference/audit-rules/aud-use-unique-index-for-data-update-operations) | `aud-use-unique-index-for-data-update-operations` | info |
| [Use Variable Binding for Parameters](/en/reference/audit-rules/aud-use-variable-binding-for-parameters) | `aud-use-variable-binding-for-parameters` | warning |
| [ViewExpansion](/en/reference/audit-rules/aud-viewexpansion) | `aud-viewexpansion` | info |

## Index

| Rule | ID | Severity |
|---|---|---|
| [Avoid LIKE Pattern Starting with Wildcard](/en/reference/audit-rules/aud-avoid-like-pattern-starting-with-wildcard) | `aud-avoid-like-pattern-starting-with-wildcard` | warning |
| [Avoid Negative Queries on Filter Columns](/en/reference/audit-rules/aud-avoid-negative-queries-on-filter-columns) | `aud-avoid-negative-queries-on-filter-columns` | warning |
| [Avoid OR Conditions on Different Columns](/en/reference/audit-rules/aud-avoid-or-conditions-on-different-columns) | `aud-avoid-or-conditions-on-different-columns` | warning |
| [Avoid ORDER BY Columns from Different Tables](/en/reference/audit-rules/aud-avoid-order-by-columns-from-different-tables) | `aud-avoid-order-by-columns-from-different-tables` | info |
| [Avoid Specifying COLLATION in ORDER BY](/en/reference/audit-rules/aud-avoid-specifying-collation-in-order-by) | `aud-avoid-specifying-collation-in-order-by` | warning |
| [AvoidUsingNullableColumnsInIndex](/en/reference/audit-rules/aud-avoidusingnullablecolumnsinindex) | `aud-avoidusingnullablecolumnsinindex` | warning |
| [Collation4IndexDisallowed](/en/reference/audit-rules/aud-collation4indexdisallowed) | `aud-collation4indexdisallowed` | warning |
| [DuplicateColumnsInIndex](/en/reference/audit-rules/aud-duplicatecolumnsinindex) | `aud-duplicatecolumnsinindex` | warning |
| [Expression in GROUP BY Causes Index Invalidation](/en/reference/audit-rules/aud-expression-in-group-by-causes-index-invalidation) | `aud-expression-in-group-by-causes-index-invalidation` | info |
| [Expression in ORDER BY Causes Index Invalidation](/en/reference/audit-rules/aud-expression-in-order-by-causes-index-invalidation) | `aud-expression-in-order-by-causes-index-invalidation` | info |
| [Foreign Key Naming Convention](/en/reference/audit-rules/aud-foreign-key-naming-convention) | `aud-foreign-key-naming-convention` | info |
| [FulltextIndexDisallowed](/en/reference/audit-rules/aud-fulltextindexdisallowed) | `aud-fulltextindexdisallowed` | warning |
| [FunctionalIndexDisallowed](/en/reference/audit-rules/aud-functionalindexdisallowed) | `aud-functionalindexdisallowed` | warning |
| [GlobalIndexOnDistributedTableDisallowed](/en/reference/audit-rules/aud-globalindexondistributedtabledisallowed) | `aud-globalindexondistributedtabledisallowed` | warning |
| [GlobalIndexOnPartitionedTableDisallowed](/en/reference/audit-rules/aud-globalindexonpartitionedtabledisallowed) | `aud-globalindexonpartitionedtabledisallowed` | warning |
| [GROUP BY Columns from Multiple Tables](/en/reference/audit-rules/aud-group-by-columns-from-multiple-tables) | `aud-group-by-columns-from-multiple-tables` | info |
| [Implicit Type Conversion Causes Index Invalidation](/en/reference/audit-rules/aud-implicit-type-conversion-causes-index-invalidati) | `aud-implicit-type-conversion-causes-index-invalidati` | warning |
| [Index Column Selectivity Should Exceed Threshold](/en/reference/audit-rules/aud-index-column-selectivity-should-exceed-threshold) | `aud-index-column-selectivity-should-exceed-threshold` | info |
| [Index Invalid or Invisible](/en/reference/audit-rules/aud-index-invalid-or-invisible) | `aud-index-invalid-or-invisible` | warning |
| [Index naming convention](/en/reference/audit-rules/aud-index-naming-convention) | `aud-index-naming-convention` | info |
| [IndexNameRequired](/en/reference/audit-rules/aud-indexnamerequired) | `aud-indexnamerequired` | info |
| [Join Column Type Mismatch Causes Index Invalidation](/en/reference/audit-rules/aud-join-column-type-mismatch-causes-index-invalidat) | `aud-join-column-type-mismatch-causes-index-invalidat` | warning |
| [LongLengthColumns4IndexDisallowed](/en/reference/audit-rules/aud-longlengthcolumns4indexdisallowed) | `aud-longlengthcolumns4indexdisallowed` | warning |
| [Mixed Sort Directions Cause Index Inefficiency](/en/reference/audit-rules/aud-mixed-sort-directions-cause-index-inefficiency) | `aud-mixed-sort-directions-cause-index-inefficiency` | info |
| [Number of Indexes Exceeds Threshold](/en/reference/audit-rules/aud-number-of-indexes-exceeds-threshold) | `aud-number-of-indexes-exceeds-threshold` | warning |
| [NumberOfColumnsInIndexExceedThreshold](/en/reference/audit-rules/aud-numberofcolumnsinindexexceedthreshold) | `aud-numberofcolumnsinindexexceedthreshold` | warning |
| [Primary Key Naming Convention](/en/reference/audit-rules/aud-primary-key-naming-convention) | `aud-primary-key-naming-convention` | info |
| [Redundant Index Detection](/en/reference/audit-rules/aud-redundantindexdisallowed) | `aud-redundantindexdisallowed` | warning |
| [RuleFuncWithColumnInPredicate](/en/reference/audit-rules/aud-rulefuncwithcolumninpredicate) | `aud-rulefuncwithcolumninpredicate` | info |
| [Text&LobColumnsInIndexDisallowed](/en/reference/audit-rules/aud-textlobcolumnsinindexdisallowed) | `aud-textlobcolumnsinindexdisallowed` | warning |
| [TotalIndexLengthExceedThreshold](/en/reference/audit-rules/aud-totalindexlengthexceedthreshold) | `aud-totalindexlengthexceedthreshold` | info |
| [Unique Key Naming Convention](/en/reference/audit-rules/aud-unique-key-naming-convention) | `aud-unique-key-naming-convention` | info |
| [Use Prefix Index for Long VARCHAR Columns](/en/reference/audit-rules/aud-use-prefix-index-for-long-varchar-columns) | `aud-use-prefix-index-for-long-varchar-columns` | warning |

## Unclassified

| Rule | ID | Severity |
|---|---|---|
| [Column with this Name Does Not Exist](/en/reference/audit-rules/aud-column-with-this-name-does-not-exist) | `aud-column-with-this-name-does-not-exist` | error |
