---
id: audit-rule-aud-avoid-joining-on-nondistribution-key-columns
title: 避免表关联字段不是分布键
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 分布式库中 JOIN 关联字段非分布键会触发跨节点数据重分布、网络开销大；应让高频关联字段与分布键对齐。
localeOf: en-audit-rule-aud-avoid-joining-on-nondistribution-key-columns
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-joining-on-nondistribution-key-columns |
| 规则名称 | 避免表关联字段不是分布键 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

在分布式数据库中，如果 JOIN 操作的关联字段不是分布键（Shard Key），关联操作可能需要在多个节点之间移动数据（数据重分布 / Data Redistribution），即将一张表的数据广播或重分布到另一张表所在的节点上才能完成关联计算。这种跨节点的数据传输会产生大量的网络开销，成为查询性能的瓶颈。
在真实业务环境中，所有关联字段都使用分布键可能不现实，因此需要在表分布策略和查询性能之间进行权衡。应优先确保高频 JOIN 查询的关联字段与分布键对齐，使关联操作能够在本地节点完成，从而充分利用分布式数据库的并行计算能力。

## 反例

```sql
-- ❌ 不推荐：关联字段不是分布键，可能触发跨节点数据重分布
SELECT * FROM t1 JOIN t2 ON t1.non_shard_key = t2.col;
```

## 正例

```sql
-- ✅ 推荐：关联字段使用分布键，关联可在本地节点完成
SELECT * FROM t1 JOIN t2 ON t1.shard_key = t2.shard_key;
```
