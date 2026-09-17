---
id: audit-rule-aud-use-primary-key-as-distribution-key
title: 应使用主键作为分布键
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-primary-key-as-distribution-key
tags:
- audit-rule
- ddl
description: 在分布式数据库中，使用主键作为分布键是最佳实践之一。主键作分布键可以保证数据在各节点间均匀分布，同时依靠主键的唯一性避免数据倾斜。此外，将主键设为分布键还能减少涉及主键操作的跨节点通信——当查询通过主键等值条件定位数据时，可以精确路由到目标节点，避免全节点广播。
localeOf: en-audit-rule-aud-use-primary-key-as-distribution-key
subtype: rule
language: zh
translationKey: audit-rule-aud-use-primary-key-as-distribution-key
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-primary-key-as-distribution-key |
| 规则名称 | 应使用主键作为分布键 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式数据库中，使用主键作为分布键是最佳实践之一。主键作分布键可以保证数据在各节点间均匀分布，同时依靠主键的唯一性避免数据倾斜。此外，将主键设为分布键还能减少涉及主键操作的跨节点通信——当查询通过主键等值条件定位数据时，可以精确路由到目标节点，避免全节点广播。
当主键字段未被同时设为分布键时，主键的唯一性只能在各节点内保证，跨节点的全局唯一性需要额外的协调机制，这将增加系统的复杂度和性能开销。

## 反例

```sql
-- ❌ 不推荐：主键为id，但分布键使用其他列，数据分布可能不均
CREATE TABLE t (
    id BIGINT PRIMARY KEY,
    name VARCHAR(100)
) DISTRIBUTED BY HASH(name);
```

## 正例

```sql
-- ✅ 推荐：使用主键作为分布键，保证数据均匀分布与全局唯一性
CREATE TABLE t (
    id BIGINT PRIMARY KEY,
    name VARCHAR(100)
) DISTRIBUTED BY HASH(id);
```
