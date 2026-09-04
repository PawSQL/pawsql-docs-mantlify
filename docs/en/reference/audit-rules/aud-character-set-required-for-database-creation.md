---
id: en-audit-rule-aud-character-set-required-for-database-creation
title: Character Set Required for Database Creation
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 在创建数据库时必须显式指定字符集，以确保数据的一致性和兼容性。如果未指定字符集，数据库会使用默认配置，而默认配置可能因环境、版本或安装方式不同而有所差异，导致跨环境部署时出现乱码或排序不一致等问题。
localeOf: audit-rule-aud-character-set-required-for-database-creation
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-character-set-required-for-database-creation |
| Name | Character Set Required for Database Creation |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

在创建数据库时必须显式指定字符集，以确保数据的一致性和兼容性。如果未指定字符集，数据库会使用默认配置，而默认配置可能因环境、版本或安装方式不同而有所差异，导致跨环境部署时出现乱码或排序不一致等问题。
显式指定字符集（如 `utf8mb4`）可以避免数据存储时的字符编码问题，在多语言业务场景下尤为重要。

## Bad Example

```sql
-- ❌ 不推荐：创建数据库时未指定字符集
CREATE DATABASE mydb;
```

## Good Example

```sql
-- ✅ 推荐：创建数据库时显式指定字符集
CREATE DATABASE mydb DEFAULT CHARACTER SET utf8mb4;
```
