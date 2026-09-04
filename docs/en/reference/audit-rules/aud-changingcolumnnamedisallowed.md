---
id: en-audit-rule-aud-changingcolumnnamedisallowed
title: ChangingColumnNameDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止修改字段名（`RENAME COLUMN` / `CHANGE COLUMN`）。重命名字段会对所有依赖该字段的应用程序、报表、ETL
  脚本和视图造成影响，导致线上业务瞬间中断。在不支持不停机发布的架构中，这种修改需要在维护窗口内协调大量上下游系统，风险极高。
localeOf: audit-rule-aud-changingcolumnnamedisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-changingcolumnnamedisallowed |
| Name | ChangingColumnNameDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

禁止修改字段名（`RENAME COLUMN` / `CHANGE COLUMN`）。重命名字段会对所有依赖该字段的应用程序、报表、ETL 脚本和视图造成影响，导致线上业务瞬间中断。在不支持不停机发布的架构中，这种修改需要在维护窗口内协调大量上下游系统，风险极高。
如果确实需要重命名字段，应由 DBA 在充分评估依赖关系后手工干预，通过灰度方案（如新增列 + 双写 + 切换 + 下线旧列）实现平滑过渡，而不是直接执行 `RENAME` 操作。

## Bad Example

```sql
-- ❌ 不推荐：直接重命名列，破坏上下游依赖
ALTER TABLE t CHANGE old_name new_name VARCHAR(50);
```

## Good Example

```sql
-- ✅ 推荐：灰度方案
-- 1. ALTER TABLE t ADD COLUMN new_name VARCHAR(50);
-- 2. 双写 + 历史数据回填
-- 3. 切换所有消费方使用 new_name
-- 4. ALTER TABLE t DROP COLUMN old_name;
```
