---
id: audit-rule-aud-nonbucket-column-table-join-in-hive
title: HIVE中使用非分桶字段进行表关联
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-nonbucket-column-table-join-in-hive
tags:
- audit-rule
- dml
description: 当 Hive 分桶表之间使用非分桶字段进行 JOIN 时，无法利用 Bucket Map Join 带来的性能优势。数据需要额外的 Shuffle
  操作进行重新分布，增加了网络传输和磁盘 I/O 开销，严重影响查询性能。
localeOf: en-audit-rule-aud-nonbucket-column-table-join-in-hive
subtype: rule
language: zh
translationKey: audit-rule-aud-nonbucket-column-table-join-in-hive
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-nonbucket-column-table-join-in-hive |
| 规则名称 | HIVE中使用非分桶字段进行表关联 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当 Hive 分桶表之间使用非分桶字段进行 JOIN 时，无法利用 Bucket Map Join 带来的性能优势。数据需要额外的 Shuffle 操作进行重新分布，增加了网络传输和磁盘 I/O 开销，严重影响查询性能。
此规则检测 JOIN 操作中关联字段是否与表的分桶字段匹配，对于使用非分桶字段关联的场景进行预警，引导开发者优化表设计和查询逻辑。
> 此规则适用于 Hive 数据仓库环境。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。

## 反例

```sql
-- ❌ 不推荐：大表未分桶，无法利用 Bucket Map Join
CREATE TABLE big_table (...) CLUSTERED BY (id) INTO 32 BUCKETS;

-- ❌ 不推荐：JOIN 关联字段与分桶字段不匹配
SELECT * FROM bucket_table_a a
JOIN bucket_table_b b ON a.non_bucket_col = b.non_bucket_col;
```

## 正例

```sql
-- ✅ 推荐：JOIN 关联字段与分桶字段一致
SELECT * FROM bucket_table_a a
JOIN bucket_table_b b ON a.bucket_col = b.bucket_col;
```
