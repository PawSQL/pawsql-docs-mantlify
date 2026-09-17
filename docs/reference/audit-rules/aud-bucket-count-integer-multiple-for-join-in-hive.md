---
id: audit-rule-aud-bucket-count-integer-multiple-for-join-in-hive
title: HIVE中关联字段分桶数应保持整数倍
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-bucket-count-integer-multiple-for-join-in-hive
tags:
- audit-rule
- dml
description: 当两个分桶表进行 JOIN 时，如果 JOIN 字段就是分桶字段且两表的分桶数存在整数倍关系，Hive 在进行 Bucket Map Join
  时可以通过桶映射优化直接进行本地关联，完全避免数据的 Shuffle 操作，大大提升 JOIN 性能。
localeOf: en-audit-rule-aud-bucket-count-integer-multiple-for-join-in-hive
subtype: rule
language: zh
translationKey: audit-rule-aud-bucket-count-integer-multiple-for-join-in-hive
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-bucket-count-integer-multiple-for-join-in-hive |
| 规则名称 | HIVE中关联字段分桶数应保持整数倍 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当两个分桶表进行 JOIN 时，如果 JOIN 字段就是分桶字段且两表的分桶数存在整数倍关系，Hive 在进行 Bucket Map Join 时可以通过桶映射优化直接进行本地关联，完全避免数据的 Shuffle 操作，大大提升 JOIN 性能。
如果两个分桶表的分桶数之间不存在整数倍关系，Hive 无法进行桶映射，数据仍需要 Shuffle 重分布，失去了分桶策略带来的优化效果。此规则检测 JOIN 操作中关联分桶表的分桶数关系，对不满足整数倍关系的表结构进行预警。
> 此规则适用于 Hive 数据仓库环境。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。

## 反例

```sql
-- ❌ 不推荐：分桶数 7 和 3 不存在整数倍关系，无法利用桶映射
CREATE TABLE table_a (...) CLUSTERED BY (id) INTO 7 BUCKETS;
CREATE TABLE table_b (...) CLUSTERED BY (id) INTO 3 BUCKETS;
```

## 正例

```sql
-- ✅ 推荐：分桶数 64 和 32 满足整数倍关系，可利用桶映射优化
CREATE TABLE table_a (...) CLUSTERED BY (id) INTO 64 BUCKETS;
CREATE TABLE table_b (...) CLUSTERED BY (id) INTO 32 BUCKETS;
```
