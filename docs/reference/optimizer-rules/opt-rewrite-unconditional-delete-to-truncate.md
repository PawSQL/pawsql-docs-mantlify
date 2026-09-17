---
id: optimizer-rule-opt-rewrite-unconditional-delete-to-truncate
title: 无条件的DELETE建议重写为Truncate
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-rewrite-unconditional-delete-to-truncate
tags:
- optimizer-rule
- rewrite
description: 没有WHERE条件或WHERE条件恒真的`DELETE`语句会删除表中的所有数据。`DELETE`作为DML语句，需要逐行记录日志以便事务回滚和主备同步——对于大表而言，这可能导致数据库长时间锁定、事务日志膨胀、主从同步延迟等问题。
localeOf: en-optimizer-rule-opt-rewrite-unconditional-delete-to-truncate
subtype: rule
language: zh
translationKey: optimizer-rule-opt-rewrite-unconditional-delete-to-truncate
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-rewrite-unconditional-delete-to-truncate |
| 规则名称 | 无条件的DELETE建议重写为Truncate |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

没有WHERE条件或WHERE条件恒真的`DELETE`语句会删除表中的所有数据。`DELETE`作为DML语句，需要逐行记录日志以便事务回滚和主备同步——对于大表而言，这可能导致数据库长时间锁定、事务日志膨胀、主从同步延迟等问题。
如果确认表中的数据不再需要，应当使用`TRUNCATE`来代替无条件的`DELETE`。`TRUNCATE`是DDL操作，不会逐行记录日志，而是直接将表清空并释放存储空间，执行速度远快于`DELETE`，且对系统资源的消耗极小。

## 反例

```sql
-- ❌ 不推荐：无条件的DELETE，逐行删除并记录日志，大表场景极其低效
DELETE FROM lineitem;
```

## 正例

```sql
-- ✅ 推荐：使用TRUNCATE直接清空表，速度快且不产生行级日志
TRUNCATE TABLE lineitem;
```
