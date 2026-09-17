---
id: audit-rule-aud-use-partitioned-tables-for-large-hive-tables
title: 大的Hive应该使用分区表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-partitioned-tables-for-large-hive-tables
tags:
- audit-rule
- ddl
description: 对于数据量较大的Hive表，分区是最基本的性能优化手段。合理的分区策略能够实现数据的物理隔离，使查询只需要扫描相关分区的数据，大幅减少I/O开销。不进行分区意味着每次查询都需要全表扫描，当表数据增长到TB级别时，查询性能将严重恶化，同时数据管理和清理也会变得困难。
localeOf: en-audit-rule-aud-use-partitioned-tables-for-large-hive-tables
subtype: rule
language: zh
translationKey: audit-rule-aud-use-partitioned-tables-for-large-hive-tables
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-partitioned-tables-for-large-hive-tables |
| 规则名称 | 大的Hive应该使用分区表 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于数据量较大的Hive表，分区是最基本的性能优化手段。合理的分区策略能够实现数据的物理隔离，使查询只需要扫描相关分区的数据，大幅减少I/O开销。不进行分区意味着每次查询都需要全表扫描，当表数据增长到TB级别时，查询性能将严重恶化，同时数据管理和清理也会变得困难。
该规则适用于Hive数据仓库环境，要求数据量超过阈值（默认100,000行）的表必须采用分区策略。常见的分区字段包括日期（dt）、小时（hr）等具有明显时间维度的字段。

## 反例

```sql
-- ❌ 不推荐：大数据量表未分区，查询需全表扫描
CREATE TABLE transaction_log (
    transaction_id BIGINT,
    user_id BIGINT,
    transaction_time TIMESTAMP
) STORED AS ORC;
```

## 正例

```sql
-- ✅ 推荐：按日期分区，查询仅扫描相关分区
CREATE TABLE transaction_log (
    transaction_id BIGINT,
    user_id BIGINT,
    transaction_time TIMESTAMP
) PARTITIONED BY (dt STRING) STORED AS ORC;
```
