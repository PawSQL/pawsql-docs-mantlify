---
id: audit-rule-aud-avoid-select-with-for-update
title: 避免在SELECT语句添加FOR UPDATE
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-select-with-for-update
tags:
- audit-rule
- dml
description: 避免随意 SELECT ... FOR UPDATE（行锁致等待/阻塞/死锁）；仅确需悲观锁时使用，并尽量缩小锁定范围。
localeOf: en-audit-rule-aud-avoid-select-with-for-update
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-select-with-for-update
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-select-with-for-update |
| 规则名称 | 避免在SELECT语句添加FOR UPDATE |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`SELECT ... FOR UPDATE` 会对查询命中的行加排他锁，在事务提交或回滚之前阻止其他事务对这些行进行修改或加锁读取。这种行级锁定在并发场景下可能导致锁等待、阻塞甚至死锁，严重影响数据库的并发处理能力和整体性能。
因此 `FOR UPDATE` 应谨慎使用，仅在确实需要悲观锁保证数据一致性的场景下使用，并尽可能缩小锁定范围（如通过精确的主键查询来限制锁定行数）。对于不需要加锁的查询，绝不应随意添加 `FOR UPDATE`。PawSQL 会检查此类写法并进行提醒。

## 反例

```sql
-- ❌ 不推荐：无必要地使用 FOR UPDATE，导致锁竞争
SELECT * FROM user WHERE status = 'active' FOR UPDATE;
```

## 正例

```sql
-- ✅ 推荐：仅在需要悲观锁时使用，且通过主键精确锁定
SELECT * FROM user WHERE id = 100 FOR UPDATE;
```
