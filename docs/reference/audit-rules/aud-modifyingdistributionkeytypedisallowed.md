---
id: audit-rule-aud-modifyingdistributionkeytypedisallowed
title: 禁止修改分布键字段类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-modifyingdistributionkeytypedisallowed
tags:
- audit-rule
- ddl
description: 分布键（Shardkey / Distribution Key）是分布式表中数据路由的核心依据，其值决定了数据行所在的物理分片。修改分布键的字段类型或长度将导致现有数据的哈希路由规则失效，数据无法被正确路由到目标分片，造成查询不到数据或数据分布异常。因此，该操作在分布式数据库中应被严格禁止。
localeOf: en-audit-rule-aud-modifyingdistributionkeytypedisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-modifyingdistributionkeytypedisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-modifyingdistributionkeytypedisallowed |
| 规则名称 | 禁止修改分布键字段类型 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

分布键（Shardkey / Distribution Key）是分布式表中数据路由的核心依据，其值决定了数据行所在的物理分片。修改分布键的字段类型或长度将导致现有数据的哈希路由规则失效，数据无法被正确路由到目标分片，造成查询不到数据或数据分布异常。因此，该操作在分布式数据库中应被严格禁止。
如果确实需要修改分布键的字段类型，只能通过重建表（创建新结构表→数据迁移→切换应用→下线旧表）的方式实现。

## 反例

```sql
-- ❌ 不推荐：修改分布键字段类型，破坏数据路由
ALTER TABLE t MODIFY shardkey_col VARCHAR(50);
```

## 正例

```sql
-- ✅ 推荐：如需变更，通过重建表实现
-- 1. CREATE TABLE t_new (...) shardkey=new_col;
-- 2. INSERT INTO t_new SELECT * FROM t;
-- 3. 切换应用读写指向 t_new
-- 4. DROP TABLE t;
```
