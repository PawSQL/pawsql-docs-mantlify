---
id: en-audit-rule-aud-charsetontabledisallowed
title: CharsetOnTableDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止在表定义时单独指定字符集，以避免表级字符集与数据库级字符集不一致导致的数据问题。当表字符集与数据库字符集不同时，跨表操作可能触发隐式字符集转换，影响查询性能并可能导致乱码。
localeOf: audit-rule-aud-charsetontabledisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-charsetontabledisallowed |
| Name | CharsetOnTableDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

禁止在表定义时单独指定字符集，以避免表级字符集与数据库级字符集不一致导致的数据问题。当表字符集与数据库字符集不同时，跨表操作可能触发隐式字符集转换，影响查询性能并可能导致乱码。
字符集应在数据库级别（或列级别）统一管理，表应继承数据库的默认字符集，避免在表级覆盖设置。

## Bad Example

```sql
-- ❌ 不推荐：表定义时指定了字符集，可能与数据库不一致
CREATE TABLE t (id INT) DEFAULT CHARSET = utf8;
```

## Good Example

```sql
-- ✅ 推荐：表继承数据库默认字符集，不在表级单独指定
CREATE TABLE t (id INT);
```
