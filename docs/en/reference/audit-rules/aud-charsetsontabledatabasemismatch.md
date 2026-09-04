---
id: en-audit-rule-aud-charsetsontabledatabasemismatch
title: CharsetsOnTable&DatabaseMismatch
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 要求表的字符集必须与数据库的字符集保持一致，以避免字符集不一致导致的数据问题。当表的字符集与数据库字符集不同时，跨表查询或数据迁移可能触发隐式字符集转换，增加
  CPU 开销、影响索引使用效率，严重时还可能导致乱码和数据丢失。
localeOf: audit-rule-aud-charsetsontabledatabasemismatch
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-charsetsontabledatabasemismatch |
| Name | CharsetsOnTable&DatabaseMismatch |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

要求表的字符集必须与数据库的字符集保持一致，以避免字符集不一致导致的数据问题。当表的字符集与数据库字符集不同时，跨表查询或数据迁移可能触发隐式字符集转换，增加 CPU 开销、影响索引使用效率，严重时还可能导致乱码和数据丢失。
建议在创建表时不指定字符集，使其自动继承数据库的默认字符集。如果必须指定，应确保与数据库完全一致。

## Bad Example

```sql
-- ❌ 不推荐：表的字符集与数据库不一致
-- 假设数据库字符集为 utf8mb4
CREATE TABLE t (id INT) DEFAULT CHARSET = latin1;
```

## Good Example

```sql
-- ✅ 推荐：表继承数据库默认字符集，保持一致
CREATE TABLE t (id INT);
```
