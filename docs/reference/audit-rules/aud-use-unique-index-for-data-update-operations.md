---
id: audit-rule-aud-use-unique-index-for-data-update-operations
title: 应通过唯一性索引来进行数据更新操作
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-unique-index-for-data-update-operations
tags:
- audit-rule
- dml
description: '`UPDATE`语句应通过主键或唯一索引的等值条件来精确定位要修改的记录。使用唯一性索引进行定位可以最大限度地减少锁定范围——数据库只需锁定目标行，而无需锁住范围或扫描大量无关行。这能够避免阻塞其他事务，从而降低死锁发生的概率，提升并发性能。'
localeOf: en-audit-rule-aud-use-unique-index-for-data-update-operations
subtype: rule
language: zh
translationKey: audit-rule-aud-use-unique-index-for-data-update-operations
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-unique-index-for-data-update-operations |
| 规则名称 | 应通过唯一性索引来进行数据更新操作 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`UPDATE`语句应通过主键或唯一索引的等值条件来精确定位要修改的记录。使用唯一性索引进行定位可以最大限度地减少锁定范围——数据库只需锁定目标行，而无需锁住范围或扫描大量无关行。这能够避免阻塞其他事务，从而降低死锁发生的概率，提升并发性能。
如果`UPDATE`语句的WHERE条件仅使用非唯一索引的普通列，数据库可能需要锁定更多的行（甚至全表锁定），在高并发场景下容易引发锁等待和死锁问题。

## 反例

```sql
-- ❌ 不推荐：使用非唯一列定位，可能锁定多行，引发阻塞和死锁
UPDATE user SET email = 'test@example.com' WHERE user_id = 12345 AND name = '张三';
```

## 正例

```sql
-- ✅ 推荐：通过主键等值条件精确定位，仅锁住目标行
UPDATE user SET email = 'test@example.com' WHERE id = 100;
```
