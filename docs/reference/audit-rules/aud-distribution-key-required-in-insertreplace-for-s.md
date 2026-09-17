---
id: audit-rule-aud-distribution-key-required-in-insertreplace-for-s
title: 对分片表的INSERT/REPLACE时字段必须包含分布键
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-distribution-key-required-in-insertreplace-for-s
tags:
- audit-rule
- dml
description: 对于分片表（Sharding Table），执行`INSERT`或`REPLACE`操作时，插入的数据必须显式包含分布键（Shardkey）列及其值。这是因为数据库的Proxy层需要根据分布键的值计算该行数据应该被路由到哪个具体的物理分片（Set）。如果未提供分布键的值，Proxy无法确定数据的目标分片，将直接拒绝执行该SQL语句。
localeOf: en-audit-rule-aud-distribution-key-required-in-insertreplace-for-s
subtype: rule
language: zh
translationKey: audit-rule-aud-distribution-key-required-in-insertreplace-for-s
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-distribution-key-required-in-insertreplace-for-s |
| 规则名称 | 对分片表的INSERT/REPLACE时字段必须包含分布键 |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于分片表（Sharding Table），执行`INSERT`或`REPLACE`操作时，插入的数据必须显式包含分布键（Shardkey）列及其值。这是因为数据库的Proxy层需要根据分布键的值计算该行数据应该被路由到哪个具体的物理分片（Set）。如果未提供分布键的值，Proxy无法确定数据的目标分片，将直接拒绝执行该SQL语句。
此规则确保所有写入分片表的数据能够被正确定位和路由到目标分片，避免因缺失分布键而导致的数据路由失败。在TDSQL等分布式数据库中，这是强制执行的基本要求。

## 反例

```sql
-- ❌ 不推荐：未指定分布键id列，Proxy无法确定目标分片
INSERT INTO t (name) VALUES ('张三');
```

## 正例

```sql
-- ✅ 推荐：显式指定分布键id及其值，Proxy可正确路由数据
INSERT INTO t (id, name) VALUES (100, '张三');
```
