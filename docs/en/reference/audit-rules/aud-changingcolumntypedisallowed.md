---
id: en-audit-rule-aud-changingcolumntypedisallowed
title: ChangingColumnTypeDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止直接修改列的数据类型。修改列的数据类型通常触发表重写与长时间锁表——数据库需要将全表数据按新类型转换后重新写入磁盘。在高并发生产环境中，这会导致索引失效、执行计划突变，并可能因隐式类型转换导致数据截断或语义改变，带来难以恢复的数据损毁风险。
localeOf: audit-rule-aud-changingcolumntypedisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-changingcolumntypedisallowed |
| Name | ChangingColumnTypeDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

禁止直接修改列的数据类型。修改列的数据类型通常触发表重写与长时间锁表——数据库需要将全表数据按新类型转换后重新写入磁盘。在高并发生产环境中，这会导致索引失效、执行计划突变，并可能因隐式类型转换导致数据截断或语义改变，带来难以恢复的数据损毁风险。
正确做法是通过新增新类型列、双写或触发器同步、分批回填校验、切换应用、最终下线旧列的灰度迁移方案完成变更，确保每个步骤可验证、可回滚。

## Bad Example

```sql
-- ❌ 不推荐：直接修改列类型，触发表重写，可能截断数据
ALTER TABLE t MODIFY col VARCHAR(100);
```

## Good Example

```sql
-- ✅ 推荐：灰度迁移方案
-- 1. ALTER TABLE t ADD COLUMN col_new VARCHAR(100);
-- 2. 双写新旧列（应用层 / 触发器）
-- 3. UPDATE t SET col_new = col WHERE col_new IS NULL;  -- 分批回填
-- 4. 切换应用使用 col_new
-- 5. ALTER TABLE t DROP COLUMN col;
```
