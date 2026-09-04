---
id: en-audit-rule-aud-column-naming-convention
title: Column Naming Convention
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 列名命名规范要求数据库对象名称遵循统一规范，便于团队协作和代码维护。通常要求列名使用小写字母和下划线（snake_case），以保持一致性、可读性和跨平台兼容性。
localeOf: audit-rule-aud-column-naming-convention
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-column-naming-convention |
| Name | Column Naming Convention |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | All supported databases |

## Description

列名命名规范要求数据库对象名称遵循统一规范，便于团队协作和代码维护。通常要求列名使用小写字母和下划线（snake_case），以保持一致性、可读性和跨平台兼容性。
不规范的列名（如使用大写字母、特殊字符、关键字或中文字符）会增加沟通成本，降低代码可读性，在跨团队协作和跨平台迁移时尤其容易引发问题。

## Bad Example

```sql
-- ❌ 不推荐：列名使用大写、中文或包含特殊字符
CREATE TABLE t_user (
    "UserID"    INT,
    "用户姓名"  VARCHAR(50)
);
```

## Good Example

```sql
-- ✅ 推荐：使用小写字母和下划线
CREATE TABLE t_user (
    user_id   INT,
    user_name VARCHAR(50)
);
```
