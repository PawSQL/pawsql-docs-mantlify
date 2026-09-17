---
id: audit-rule-aud-optimize-outer-join-between-replicated-and-shard
title: 复制表与分片表外关联的查询优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-optimize-outer-join-between-replicated-and-shard
tags:
- audit-rule
- dml
localeOf: en-audit-rule-aud-optimize-outer-join-between-replicated-and-shard
subtype: rule
language: zh
translationKey: audit-rule-aud-optimize-outer-join-between-replicated-and-shard
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-optimize-outer-join-between-replicated-and-shard |
| 规则名称 | 复制表与分片表外关联的查询优化 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式数据库中，复制表（Replicated Table）在所有节点上都有完整副本，而分片表（Sharded Table）的数据分散在不同节点上。当复制表与分片表进行LEFT JOIN时，如果复制表作为被驱动的右表，JOIN操作可以被下推至每个分片本地执行，性能良好。但如果复制表作为主表（左表），优化器可能无法将关联完全下推，导致需要将分片表的数据全量传输到复制表所在的节点，产生严重的跨节点网络开销。
此规则旨在提醒开发者注意JOIN的方向和表类型对下推能力的影响，合理规划分布式查询中的表关联顺序。

## 反例

```sql
-- ❌ 不推荐：复制表作为主表，可能导致分片表数据全量传输
SELECT * FROM replicated_table a LEFT JOIN sharded_table b ON a.key = b.key;
```

## 正例

```sql
-- ✅ 推荐：复制表作为被驱动的右表，JOIN可下推至各分片本地执行
SELECT * FROM sharded_table a LEFT JOIN replicated_table b ON a.key = b.key;
```
