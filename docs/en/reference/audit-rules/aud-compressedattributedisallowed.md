---
id: en-audit-rule-aud-compressedattributedisallowed
title: CompressedAttributeDisallowed
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-compressedattributedisallowed
tags:
- audit-rule
- ddl
description: Do not enable column-level COMPRESSED (mojibake risk on utf8/utf8mb4,
  extra CPU); compress at the storage/engine or application layer instead.
localeOf: audit-rule-aud-compressedattributedisallowed
subtype: rule
language: en
translationKey: audit-rule-aud-compressedattributedisallowed
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-compressedattributedisallowed |
| Name | CompressedAttributeDisallowed |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | Unverified (database scope not declared) |

## Description

Turning on column-level compression through the `COMPRESSED` attribute is prone to mojibake under the `utf8` and `utf8mb4` character sets. Compression and decompression also consume extra CPU, which can become a bottleneck under high concurrency.

Data compression should be handled at the storage or application layer (for example InnoDB page compression, or OS-level compression), not enabled column by column. Avoid this feature in table definitions.

## Bad Example

```sql
-- bad: using the COMPRESSED attribute
CREATE TABLE t1 (
    id INT,
    long_text TEXT COMPRESSED
);
```

## Good Example

```sql
-- good: no column-level compression; rely on storage-engine or application-layer compression
CREATE TABLE t1 (
    id INT,
    long_text TEXT
);
```
