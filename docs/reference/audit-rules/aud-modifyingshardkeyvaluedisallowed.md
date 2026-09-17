---
id: audit-rule-aud-modifyingshardkeyvaluedisallowed
title: 禁止修改分片键的值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-modifyingshardkeyvaluedisallowed
tags:
- audit-rule
- dml
description: 分片键（Shardkey）的值决定了数据行所在的物理分片。直接更新分片键的值会导致数据需要从一个分片迁移到另一个分片，这在大多数分布式数据库中是不允许的操作，可能导致数据路由混乱、数据丢失或跨分片事务异常。
localeOf: en-audit-rule-aud-modifyingshardkeyvaluedisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-modifyingshardkeyvaluedisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-modifyingshardkeyvaluedisallowed |
| 规则名称 | 禁止修改分片键的值 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

分片键（Shardkey）的值决定了数据行所在的物理分片。直接更新分片键的值会导致数据需要从一个分片迁移到另一个分片，这在大多数分布式数据库中是不允许的操作，可能导致数据路由混乱、数据丢失或跨分片事务异常。
如果业务上确实需要修改分片键对应的值，应通过在一个事务中先删除旧记录、再插入新记录的方式显式实现，确保数据迁移的可控性和一致性。

## 反例

```sql
-- ❌ 不推荐：直接修改分片键值，导致跨分片数据迁移
UPDATE t SET id = 200 WHERE id = 100;
```

## 正例

```sql
-- ✅ 推荐：通过 DELETE + INSERT 显式处理分片变更
BEGIN;
DELETE FROM t WHERE id = 100;
INSERT INTO t (id, name, ...) VALUES (200, '...', ...);
COMMIT;
```
