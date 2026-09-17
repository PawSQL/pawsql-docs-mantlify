---
id: audit-rule-aud-frequentlyupdatedtablesshoulduselocaltables
title: 经常更新的表应使用本地表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-frequentlyupdatedtablesshoulduselocaltables
tags:
- audit-rule
- dml
description: 对于高并发且包含频繁 UPDATE 或 SELECT ... FOR UPDATE 操作的表，如果使用分布式/分片表，跨分片的更新和加锁会严重拖垮性能，引发分布式事务开销、锁传播延迟和网络消耗。
localeOf: en-audit-rule-aud-frequentlyupdatedtablesshoulduselocaltables
subtype: rule
language: zh
translationKey: audit-rule-aud-frequentlyupdatedtablesshoulduselocaltables
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-frequentlyupdatedtablesshoulduselocaltables |
| 规则名称 | 经常更新的表应使用本地表 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于高并发且包含频繁 UPDATE 或 SELECT ... FOR UPDATE 操作的表，如果使用分布式/分片表，跨分片的更新和加锁会严重拖垮性能，引发分布式事务开销、锁传播延迟和网络消耗。
如果业务场景可以接受，建议将此类表设计为本地表（非分片表/LOCAL 表），以避免分布式锁的开销和跨节点事务的复杂度。如果必须使用分布式表，应仔细评估分片键的选择，确保更新操作能够路由到单分片。

## 反例

```sql
-- ❌ 不推荐：高频更新的表使用分片表，且更新操作不带分片键
UPDATE t_sharded SET status = 'completed' WHERE other_col = ?;
```

## 正例

```sql
-- ✅ 推荐：评估是否可设计为本地表
CREATE TABLE t_local (...) ENGINE=InnoDB;
-- 或确保更新查询包含分片键
UPDATE t_sharded SET status = 'completed' WHERE shard_key = ?;
```
