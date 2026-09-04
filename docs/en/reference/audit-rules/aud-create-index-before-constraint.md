---
id: en-audit-rule-aud-create-index-before-constraint
title: Create Index Before Constraint
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 在创建约束（如唯一约束、外键约束、CHECK 约束）之前，应先创建相关的索引。约束的执行依赖于底层索引来进行数据校验，如果事先没有相关索引，数据库在验证约束时将不得不进行全表扫描，严重影响
  DDL 操作的执行效率，甚至在大表上导致长时间的锁等待。
localeOf: audit-rule-aud-create-index-before-constraint
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-create-index-before-constraint |
| Name | Create Index Before Constraint |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

在创建约束（如唯一约束、外键约束、CHECK 约束）之前，应先创建相关的索引。约束的执行依赖于底层索引来进行数据校验，如果事先没有相关索引，数据库在验证约束时将不得不进行全表扫描，严重影响 DDL 操作的执行效率，甚至在大表上导致长时间的锁等待。
提前手动创建索引可以让数据库直接复用已有索引进行约束校验，避免全表扫描，确保 DDL 变更平稳执行。同时这也有助于对索引进行更精细的命名和结构控制。

## Bad Example

```sql
-- ❌ 不推荐：创建唯一约束前未创建对应索引，导致全表扫描校验
ALTER TABLE t_order ADD CONSTRAINT uk_order_no UNIQUE (order_no);
```

## Good Example

```sql
-- ✅ 推荐：先创建索引，再添加约束，复用已有索引
CREATE UNIQUE INDEX uk_order_no ON t_order (order_no);
ALTER TABLE t_order ADD CONSTRAINT uk_order_no UNIQUE USING INDEX uk_order_no;
```
