---
id: en-audit-rule-aud-column-and-table-character-set-mismatch
title: Column and Table Character Set Mismatch
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 当列级别的字符集与表级别的字符集不一致时，可能导致隐式字符集转换、数据截断或乱码问题。在多语言环境下，字符集不一致还可能引发索引失效（MySQL
  中字符集不一致的字段进行 JOIN 时无法使用索引）和查询结果不符合预期等隐蔽性故障。
localeOf: audit-rule-aud-column-and-table-character-set-mismatch
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-column-and-table-character-set-mismatch |
| Name | Column and Table Character Set Mismatch |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

当列级别的字符集与表级别的字符集不一致时，可能导致隐式字符集转换、数据截断或乱码问题。在多语言环境下，字符集不一致还可能引发索引失效（MySQL 中字符集不一致的字段进行 JOIN 时无法使用索引）和查询结果不符合预期等隐蔽性故障。
建议在表级别统一指定字符集，各列继承表的字符集配置，避免个别列使用不同的字符集。保持一致的字符集策略是数据库设计的基本规范。

## Bad Example

```sql
-- ❌ 不推荐：列级别字符集与表级别不一致
CREATE TABLE t_user (
    name VARCHAR(50) CHARSET latin1
) DEFAULT CHARSET utf8mb4;
```

## Good Example

```sql
-- ✅ 推荐：列继承表的字符集，保持一致
CREATE TABLE t_user (
    name VARCHAR(50)
) DEFAULT CHARSET utf8mb4;
```
