---
id: audit-rule-aud-avoid-select-with-limit-and-for-update
title: 避免limit子句的查询语句使用for update
type: reference
status: draft
tags:
- audit-rule
- dml
description: 避免 ORDER BY+LIMIT+FOR UPDATE（锁定行数远超返回、竞争严重）；分两步：先取主键再精确加锁。
localeOf: en-audit-rule-aud-avoid-select-with-limit-and-for-update
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-select-with-limit-and-for-update |
| 规则名称 | 避免limit子句的查询语句使用for update |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

`SELECT ... ORDER BY ... LIMIT ... FOR UPDATE` 这种写法在 MySQL 中会带来严重的锁竞争问题。由于 `ORDER BY` 的存在，执行器会先扫描所有符合 WHERE 条件的记录并对其加锁，然后再进行排序并返回满足 LIMIT 数量的行。这意味着实际需要加锁的行数远大于最终返回的行数，导致大量不必要的锁阻塞，降低并发性能。
正确的做法是分两步完成：首先通过普通 SELECT 查询获取目标行的主键，然后再通过主键进行精确的 `SELECT ... FOR UPDATE` 加锁，使锁的范围精确控制在真正需要的行上。

## 反例

```sql
-- ❌ 不推荐：ORDER BY + LIMIT + FOR UPDATE，锁定范围远超实际需要
SELECT msg_id FROM t_msg WHERE msg_type = 'type' ORDER BY send_time LIMIT 1 FOR UPDATE;
```

## 正例

```sql
-- ✅ 推荐：分两步操作，先获取主键，再精确加锁
-- 步骤1：获取主键（不加锁）
SELECT msg_id FROM t_msg WHERE msg_type = 'type' ORDER BY send_time LIMIT 1;
-- 步骤2：通过主键精确加锁
SELECT * FROM t_msg WHERE msg_id = ? FOR UPDATE;
```
