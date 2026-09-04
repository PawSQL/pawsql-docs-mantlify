---
id: en-audit-rule-aud-compressedattributedisallowed
title: CompressedAttributeDisallowed
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 在 `utf8` 及 `utf8mb4` 字符集下，通过 `COMPRESSED` 属性打开字段压缩功能容易出现乱码问题。此外，压缩和解压缩操作会消耗额外的
  CPU 资源，在高并发场景下可能成为性能瓶颈。
localeOf: audit-rule-aud-compressedattributedisallowed
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-compressedattributedisallowed |
| Name | CompressedAttributeDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

在 `utf8` 及 `utf8mb4` 字符集下，通过 `COMPRESSED` 属性打开字段压缩功能容易出现乱码问题。此外，压缩和解压缩操作会消耗额外的 CPU 资源，在高并发场景下可能成为性能瓶颈。
数据压缩应在存储层或应用层解决（如 InnoDB 页压缩、操作系统级压缩），而非在列级别逐个字段开启。应避免在表定义中使用此功能。

## Bad Example

```sql
-- ❌ 不推荐：使用 COMPRESSED 属性
CREATE TABLE t1 (
    id INT,
    long_text TEXT COMPRESSED
);
```

## Good Example

```sql
-- ✅ 推荐：不使用列级压缩，依赖存储引擎或应用层压缩方案
CREATE TABLE t1 (
    id INT,
    long_text TEXT
);
```
