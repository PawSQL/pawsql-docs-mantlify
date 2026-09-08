---
id: audit-rule-aud-dml-where
title: 避免无条件的 UPDATE/DELETE 语句
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: AUD-DML-WHERE
tags:
- audit-rule
- dml
- mysql
- postgresql
- oracle
description: 无条件（无 WHERE）的 UPDATE/DELETE 会作用于整张表，是数据丢失的常见根源；应加条件，确需清空时用 TRUNCATE。
localeOf: en-audit-rule-aud-dml-where
subtype: rule
language: zh
translationKey: audit-rule-aud-dml-where
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | AUD-DML-WHERE |
| 规则名称 | 避免无条件的 UPDATE/DELETE 语句 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | mysql, postgresql, oracle |
| 引入版本 | 8.0.0 |

## 说明

没有 WHERE 条件（或条件恒真）的 UPDATE 或 DELETE 语句，会更新或删除表中的所有数据记录。这是一个极其危险的操作—— 在生产环境中，一次无条件的 DELETE 可能在瞬间清空整张核心业务表，造成灾难性后果且难以恢复。

## 为什么重要

缺少 WHERE 的 DML 会作用于整张表，是数据丢失事故的常见根源；在执行前识别它可以为高风险变更加一道安全闸。

## 如何修复

如果确实需要清空全表数据，建议使用 TRUNCATE 语句替代 DELETE——TRUNCATE 是 DDL 操作，速度更快（不逐行记录日志）， 且更能清晰地表达“清空整表”的意图。如果业务逻辑确实需要更新所有行，也应在 WHERE 条件中显式写出恒真条件（如 WHERE 1=1）， 以表明这是有意为之而非遗漏。

## 反例

```sql
-- 不推荐：无条件 DELETE，会清空整张表
DELETE FROM t;
```

## 正例

```sql
-- 推荐：使用 TRUNCATE 清空表（更快且意图清晰）
TRUNCATE TABLE t;

-- 推荐：带 WHERE 条件的 DELETE，仅删除目标行
DELETE FROM t WHERE created_at < '2024-01-01';
```

## 关联规则

`AUD-DML-LIMIT`
