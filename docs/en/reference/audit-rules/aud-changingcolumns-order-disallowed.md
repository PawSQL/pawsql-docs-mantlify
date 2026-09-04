---
id: en-audit-rule-aud-changingcolumns-order-disallowed
title: ChangingColumn's Order Disallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止修改表中列的顺序。虽然 `ALTER TABLE ... MODIFY COLUMN ... AFTER` 等语法允许调整列的位置，但这会触发表的重建操作，且可能影响依赖于列顺序的应用程序逻辑（如使用
  `SELECT *` 或按位置索引访问列的代码）。在大型表上执行列顺序调整，锁持有时间长、回滚代价大。
localeOf: audit-rule-aud-changingcolumns-order-disallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-changingcolumns-order-disallowed |
| Name | ChangingColumn's Order Disallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

禁止修改表中列的顺序。虽然 `ALTER TABLE ... MODIFY COLUMN ... AFTER` 等语法允许调整列的位置，但这会触发表的重建操作，且可能影响依赖于列顺序的应用程序逻辑（如使用 `SELECT *` 或按位置索引访问列的代码）。在大型表上执行列顺序调整，锁持有时间长、回滚代价大。
数据库表的列顺序应在初始设计时确定，后续如需调整，应通过创建新表的迁移方案实现，而非直接修改现有表结构。

## Bad Example

```sql
-- ❌ 不推荐：调整列顺序，触发表重建，影响依赖程序
ALTER TABLE t MODIFY COLUMN col2 INT AFTER col5;
```

## Good Example

```sql
-- ✅ 推荐：在新表中定义列顺序，通过迁移方案切换
-- CREATE TABLE t_new (col1 INT, col2 INT, col3 INT, ...);
-- 数据迁移 + 应用切换
```
