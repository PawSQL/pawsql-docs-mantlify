---
id: audit-rule-aud-sysdate-function-forbidden-in-insert
title: INSERT语句禁止使用SYSDATE函数
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-sysdate-function-forbidden-in-insert
tags:
- audit-rule
- dml
description: 在基于 STATEMENT 模式的 MySQL 主从复制环境下，`SYSDATE()` 函数会返回语句实际执行时的时间点。由于主库执行语句与从库通过日志重放存在时间差，从库执行时
  `SYSDATE()` 会返回不同的时间值，导致主从数据不一致。这是一个常见的 MySQL 数据一致性陷阱。
localeOf: en-audit-rule-aud-sysdate-function-forbidden-in-insert
subtype: rule
language: zh
translationKey: audit-rule-aud-sysdate-function-forbidden-in-insert
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-sysdate-function-forbidden-in-insert |
| 规则名称 | INSERT语句禁止使用SYSDATE函数 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在基于 STATEMENT 模式的 MySQL 主从复制环境下，`SYSDATE()` 函数会返回语句实际执行时的时间点。由于主库执行语句与从库通过日志重放存在时间差，从库执行时 `SYSDATE()` 会返回不同的时间值，导致主从数据不一致。这是一个常见的 MySQL 数据一致性陷阱。
因此，在 MySQL 环境下，INSERT 语句中应避免使用 `SYSDATE()` 函数作为列的取值，改用 `NOW()` 或应用层传入固定的时间值。

## 反例

```sql
-- ❌ 不推荐：SYSDATE() 在主从复制下产生不一致的时间值
INSERT INTO t (ctime) VALUES (SYSDATE());
```

## 正例

```sql
-- ✅ 推荐：使用 NOW() 替代 SYSDATE()，或由应用层传入固定时间
INSERT INTO t (ctime) VALUES (NOW());
```
