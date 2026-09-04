---
id: en-audit-rule-aud-comments-on-column-required
title: Comments on Column Required
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 表中的每一列都必须有注释（`COMMENT`），以便于后续的维护和团队协作。列注释提供了对字段含义、用途、取值范围等信息的说明，帮助开发人员和
  DBA 快速理解表结构和业务逻辑。
localeOf: audit-rule-aud-comments-on-column-required
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-comments-on-column-required |
| Name | Comments on Column Required |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

表中的每一列都必须有注释（`COMMENT`），以便于后续的维护和团队协作。列注释提供了对字段含义、用途、取值范围等信息的说明，帮助开发人员和 DBA 快速理解表结构和业务逻辑。
缺少注释的列在数据库结构变更、故障排查、新人交接等场景下会增加沟通成本和理解难度。养成良好的注释习惯是数据库设计的基本素养。

## Bad Example

```sql
-- ❌ 不推荐：列缺少注释，字段含义不明确
CREATE TABLE t_user (
    name VARCHAR(50)
);
```

## Good Example

```sql
-- ✅ 推荐：每列都添加清晰的注释
CREATE TABLE t_user (
    name VARCHAR(50) COMMENT '用户姓名'
);
```
