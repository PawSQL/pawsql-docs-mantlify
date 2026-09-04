---
id: audit-rule-aud-avoid-crossshard-dml-operations-in-distributed-d
title: 分布式数据库应避免跨分片的 DML 操作
type: reference
status: draft
tags:
- audit-rule
- dml
description: UPDATE/DELETE 的 WHERE 未含分布键等值会跨分片触发分布式事务（慢且易死锁）；应加分布键等值条件。
localeOf: en-audit-rule-aud-avoid-crossshard-dml-operations-in-distributed-d
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-crossshard-dml-operations-in-distributed-d |
| 规则名称 | 分布式数据库应避免跨分片的 DML 操作 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

一个 DML 操作（如 `UPDATE` 或 `DELETE`）如果涉及多个分片（即其 `WHERE` 条件未指定分布键），就需要在多个节点上开启分布式事务。分布式事务的性能远低于单节点事务，并且在高并发场景下极易产生分布式死锁。
为保障分布式数据库的写入性能和事务成功率，应尽量保证每个 DML 事务的影响范围限定在同一个分片内，即 `WHERE` 条件中必须包含分布键的等值条件。

## 反例

```sql
-- ❌ 不推荐：WHERE 条件中不包含分布键，可能跨分片执行
UPDATE t_user SET status = 1 WHERE user_id = 100;
```

## 正例

```sql
-- ✅ 推荐：WHERE 条件包含分布键，事务限定在单个分片
UPDATE t_user SET status = 1 WHERE id = 1000;
```
