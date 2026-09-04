---
id: en-audit-rule-aud-commentsontablerequired
title: CommentsOnTableRequired
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 要求在创建表时必须为表添加注释（COMMENT），详细的表注释可以帮助开发者和维护者快速理解表的用途、字段含义和业务逻辑，提高代码可读性和团队协作效率。在生产环境中，缺少注释的表在交接和维护时会显著增加沟通成本。
localeOf: audit-rule-aud-commentsontablerequired
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-commentsontablerequired |
| Name | CommentsOnTableRequired |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

要求在创建表时必须为表添加注释（COMMENT），详细的表注释可以帮助开发者和维护者快速理解表的用途、字段含义和业务逻辑，提高代码可读性和团队协作效率。在生产环境中，缺少注释的表在交接和维护时会显著增加沟通成本。
此规则适用于 MySQL 等支持表注释的数据库。建议在表注释中说明表的业务用途、数据来源和生命周期。

## Bad Example

```sql
-- ❌ 不推荐：表缺少注释
CREATE TABLE t (id INT);
```

## Good Example

```sql
-- ✅ 推荐：创建表时添加注释
CREATE TABLE t (id INT) COMMENT = '用户信息表，记录系统注册用户的基本资料';
```
