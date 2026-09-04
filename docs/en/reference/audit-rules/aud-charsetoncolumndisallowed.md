---
id: en-audit-rule-aud-charsetoncolumndisallowed
title: CharsetOnColumnDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止为列单独指定字符集。当列的字符集与表或数据库的默认字符集不一致时，`JOIN` 操作中需要进行隐式字符集转换，这会导致索引失效并引发全表扫描——此类性能问题隐蔽且影响范围大。此外，字符集不一致还可能造成数据比较结果不符合预期，产生难以排查的业务逻辑错误。
localeOf: audit-rule-aud-charsetoncolumndisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-charsetoncolumndisallowed |
| Name | CharsetOnColumnDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

禁止为列单独指定字符集。当列的字符集与表或数据库的默认字符集不一致时，`JOIN` 操作中需要进行隐式字符集转换，这会导致索引失效并引发全表扫描——此类性能问题隐蔽且影响范围大。此外，字符集不一致还可能造成数据比较结果不符合预期，产生难以排查的业务逻辑错误。
推荐在表级别统一指定字符集，让所有列继承一致的字符集设置，避免列级别的特殊化配置。

## Bad Example

```sql
-- ❌ 不推荐：列级别单独指定字符集，可能导致 JOIN 索引失效
CREATE TABLE t (
    id INT,
    name VARCHAR(100) CHARACTER SET latin1
);
```

## Good Example

```sql
-- ✅ 推荐：在表级别统一指定字符集
CREATE TABLE t (
    id INT,
    name VARCHAR(100)
) DEFAULT CHARSET=utf8mb4;
```
