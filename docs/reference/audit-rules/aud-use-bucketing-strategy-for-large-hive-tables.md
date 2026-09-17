---
id: audit-rule-aud-use-bucketing-strategy-for-large-hive-tables
title: 大的Hive表应该使用分桶策略
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-bucketing-strategy-for-large-hive-tables
tags:
- audit-rule
- ddl
description: 对于数据量较大的Hive表，分桶（Bucketing）能够将数据按照指定字段的哈希值分散到多个文件中，避免产生过大的单个文件。分桶策略有助于提升查询并行度：在进行抽样查询、Map端JOIN等操作时，分桶可以使数据分布更加均匀，充分利用集群的并行计算能力。
localeOf: en-audit-rule-aud-use-bucketing-strategy-for-large-hive-tables
subtype: rule
language: zh
translationKey: audit-rule-aud-use-bucketing-strategy-for-large-hive-tables
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-bucketing-strategy-for-large-hive-tables |
| 规则名称 | 大的Hive表应该使用分桶策略 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于数据量较大的Hive表，分桶（Bucketing）能够将数据按照指定字段的哈希值分散到多个文件中，避免产生过大的单个文件。分桶策略有助于提升查询并行度：在进行抽样查询、Map端JOIN等操作时，分桶可以使数据分布更加均匀，充分利用集群的并行计算能力。
分桶与分区可以配合使用——分区用于粗粒度的数据隔离，分桶用于细粒度的数据分布。对于频繁进行JOIN操作的大型表，合理的分桶策略能够显著减少Shuffle开销，提升查询效率。

## 反例

```sql
-- ❌ 不推荐：大表未分桶，可能产生过大文件，JOIN性能差
CREATE TABLE big_table (
    id BIGINT,
    name STRING
) STORED AS ORC;
```

## 正例

```sql
-- ✅ 推荐：按customer_id分桶为32个文件，提升并行度与JOIN效率
CREATE TABLE big_table (
    id BIGINT,
    name STRING
) CLUSTERED BY (customer_id) INTO 32 BUCKETS STORED AS ORC;
```
