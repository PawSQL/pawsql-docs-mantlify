---
id: en-audit-rule-aud-constraint-with-this-name-already-exists
title: Constraint with this Name Already Exists
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 此规则确保在添加新约束时，约束名称在数据库中（或表内）是唯一的，避免与现有约束冲突。重复的约束名称会导致 SQL 执行失败，可能中断部署脚本或数据迁移流程。
localeOf: audit-rule-aud-constraint-with-this-name-already-exists
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-constraint-with-this-name-already-exists |
| Name | Constraint with this Name Already Exists |
| Category | ddl — DDL / object design |
| Severity | error |
| Databases | All supported databases |

## Description

此规则确保在添加新约束时，约束名称在数据库中（或表内）是唯一的，避免与现有约束冲突。重复的约束名称会导致 SQL 执行失败，可能中断部署脚本或数据迁移流程。
如果 SQL 语句添加了 `IF NOT EXISTS` 子句，则不会触发此规则告警。规范的约束命名和唯一性检查是数据库变更管理的基本要求。

## Bad Example

```sql
-- ❌ 不推荐：添加约束时名称与已存在的约束冲突
ALTER TABLE orders ADD CONSTRAINT pk_orders PRIMARY KEY (order_id);
```

## Good Example

```sql
-- ✅ 推荐：添加 IF NOT EXISTS 或使用唯一约束名称
ALTER TABLE orders ADD CONSTRAINT pk_orders_new PRIMARY KEY (order_id);
```
