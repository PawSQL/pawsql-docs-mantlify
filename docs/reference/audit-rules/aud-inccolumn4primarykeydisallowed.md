---
id: audit-rule-aud-inccolumn4primarykeydisallowed
title: 主键禁止使用自增
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-inccolumn4primarykeydisallowed
tags:
- audit-rule
- ddl
description: 在分布式数据库场景下，使用自增主键可能导致全局唯一性冲突。由于数据分布在多个节点上，各节点独立生成自增值，不同节点可能产生相同的自增值，从而导致主键重复。此外，全局自增锁会成为分布式写入的性能瓶颈。
localeOf: en-audit-rule-aud-inccolumn4primarykeydisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-inccolumn4primarykeydisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-inccolumn4primarykeydisallowed |
| 规则名称 | 主键禁止使用自增 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式数据库场景下，使用自增主键可能导致全局唯一性冲突。由于数据分布在多个节点上，各节点独立生成自增值，不同节点可能产生相同的自增值，从而导致主键重复。此外，全局自增锁会成为分布式写入的性能瓶颈。
分布式数据库建议使用全局有序的唯一 ID 生成策略（如 Snowflake 算法、UUID、或数据库内置的全局序列），以确保主键在全局范围内的唯一性。

## 反例

```sql
-- ❌ 不推荐：分布式场景下使用自增主键
CREATE TABLE t_order (
    id   BIGINT AUTO_INCREMENT,
    PRIMARY KEY (id)
);
```

## 正例

```sql
-- ✅ 推荐：使用全局有序的主键生成策略（如雪花算法生成唯一ID）
CREATE TABLE t_order (
    id   BIGINT,
    PRIMARY KEY (id)
);
```
