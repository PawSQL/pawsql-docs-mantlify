---
id: en-audit-rule-aud-autoincrement-column-naming-convention
title: Auto-increment column naming convention
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 此规则定义了自增列的命名规范，要求自增列有一个明确的命名模式，通常为 `id`，以便于团队快速识别自增列。统一的自增列命名在 ORM 框架集成、自动化代码生成和数据库维护中能显著提升效率。
localeOf: audit-rule-aud-autoincrement-column-naming-convention
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-autoincrement-column-naming-convention |
| Name | Auto-increment column naming convention |
| Category | ddl — DDL / object design |
| Severity | info |
| Databases | All supported databases |

## Description

此规则定义了自增列的命名规范，要求自增列有一个明确的命名模式，通常为 `id`，以便于团队快速识别自增列。统一的自增列命名在 ORM 框架集成、自动化代码生成和数据库维护中能显著提升效率。
默认命名模式为 `id`（或正则 `^id$`），可通过配置调整为其他模式。不符合命名规范的自增列会在审核时触发提示，但不会阻止 DDL 执行。

## Bad Example

```sql
-- ❌ 不推荐：自增列命名不符合规范
CREATE TABLE orders (order_auto_id INT AUTO_INCREMENT PRIMARY KEY);
```

## Good Example

```sql
-- ✅ 推荐：遵循 id 命名规范
CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY);
```
