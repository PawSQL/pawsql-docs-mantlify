---
id: audit-rule-aud-specify-disable-and-nonvalidate-for-hive-constra
title: 定义约束时需指定DISABLE和NONVALIDATE
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-specify-disable-and-nonvalidate-for-hive-constra
tags:
- audit-rule
- ddl
description: 在Hive中定义表约束（如PRIMARY KEY、FOREIGN KEY、UNIQUE等）时，应该显式指定`DISABLE`和`NONVALIDATE`选项。这样做的目的是：让Hive仅将约束信息作为元数据提供给查询优化器（用于生成更优的执行计划），而不实际执行约束检查，从而避免约束验证带来的性能开销。
localeOf: en-audit-rule-aud-specify-disable-and-nonvalidate-for-hive-constra
subtype: rule
language: zh
translationKey: audit-rule-aud-specify-disable-and-nonvalidate-for-hive-constra
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-specify-disable-and-nonvalidate-for-hive-constra |
| 规则名称 | 定义约束时需指定DISABLE和NONVALIDATE |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在Hive中定义表约束（如PRIMARY KEY、FOREIGN KEY、UNIQUE等）时，应该显式指定`DISABLE`和`NONVALIDATE`选项。这样做的目的是：让Hive仅将约束信息作为元数据提供给查询优化器（用于生成更优的执行计划），而不实际执行约束检查，从而避免约束验证带来的性能开销。
如果未指定`DISABLE NOVALIDATE`，Hive会在数据写入时验证约束，这对于大数据量场景会造成严重的性能影响。因此，在Hive中定义约束时应始终携带这两个选项，在保证优化器可用的前提下避免运行时负担。

## 反例

```sql
-- ❌ 不推荐：未指定DISABLE NOVALIDATE，Hive将进行约束验证，严重影响写入性能
ALTER TABLE customer_table
ADD CONSTRAINT pk_customer PRIMARY KEY(customer_id);
```

## 正例

```sql
-- ✅ 推荐：显式指定DISABLE NOVALIDATE，提供元信息但不验证
ALTER TABLE customer_table
ADD CONSTRAINT pk_customer PRIMARY KEY(customer_id)
DISABLE NOVALIDATE;
```
