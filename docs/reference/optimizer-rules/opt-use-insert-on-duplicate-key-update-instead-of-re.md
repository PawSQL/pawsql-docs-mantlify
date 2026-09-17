---
id: optimizer-rule-opt-use-insert-on-duplicate-key-update-instead-of-re
title: 使用 INSERT...ON DUPLICATE KEY UPDATE 替代 REPLACE 语句
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-use-insert-on-duplicate-key-update-instead-of-re
tags:
- optimizer-rule
- rewrite
description: '`REPLACE INTO` 的语义是：当发生主键或唯一键冲突时，先删除旧记录，再插入新记录。这个过程除了执行 `INSERT` 之外，还会先执行一个
  `DELETE` 操作，产生双倍的写入日志。更为严重的是，`DELETE` 操作会产生间隙锁（gap lock），容易引发死锁，在高并发场景下风险极高。'
localeOf: en-optimizer-rule-opt-use-insert-on-duplicate-key-update-instead-of-re
subtype: rule
language: zh
translationKey: optimizer-rule-opt-use-insert-on-duplicate-key-update-instead-of-re
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-use-insert-on-duplicate-key-update-instead-of-re |
| 规则名称 | 使用 INSERT...ON DUPLICATE KEY UPDATE 替代 REPLACE 语句 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`REPLACE INTO` 的语义是：当发生主键或唯一键冲突时，先删除旧记录，再插入新记录。这个过程除了执行 `INSERT` 之外，还会先执行一个 `DELETE` 操作，产生双倍的写入日志。更为严重的是，`DELETE` 操作会产生间隙锁（gap lock），容易引发死锁，在高并发场景下风险极高。
建议使用 `INSERT ... ON DUPLICATE KEY UPDATE` 替代 `REPLACE INTO`。后者在发生冲突时直接在原记录上执行更新操作，避免了先删后插的额外开销，更加高效和安全。

## 反例

```sql
-- ❌ 不推荐：REPLACE 先删后插，产生双倍日志和间隙锁
REPLACE INTO t_user (id, name, email)
VALUES (1, '张三', 'zhangsan@example.com');
```

## 正例

```sql
-- ✅ 推荐：ON DUPLICATE KEY UPDATE 直接更新，高效安全
INSERT INTO t_user (id, name, email)
VALUES (1, '张三', 'zhangsan@example.com')
ON DUPLICATE KEY UPDATE name = VALUES(name), email = VALUES(email);
```
