---
id: audit-rule-aud-compressedattributedisallowed
title: 禁止通过COMPRESSED打开字段压缩功能
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-compressedattributedisallowed
tags:
- audit-rule
- ddl
description: 禁止用 COMPRESSED 做列级压缩（utf8/utf8mb4 易乱码、增 CPU 开销）；压缩放到存储/引擎层。
localeOf: en-audit-rule-aud-compressedattributedisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-compressedattributedisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-compressedattributedisallowed |
| 规则名称 | 禁止通过COMPRESSED打开字段压缩功能 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 `utf8` 及 `utf8mb4` 字符集下，通过 `COMPRESSED` 属性打开字段压缩功能容易出现乱码问题。此外，压缩和解压缩操作会消耗额外的 CPU 资源，在高并发场景下可能成为性能瓶颈。
数据压缩应在存储层或应用层解决（如 InnoDB 页压缩、操作系统级压缩），而非在列级别逐个字段开启。应避免在表定义中使用此功能。

## 反例

```sql
-- ❌ 不推荐：使用 COMPRESSED 属性
CREATE TABLE t1 (
    id INT,
    long_text TEXT COMPRESSED
);
```

## 正例

```sql
-- ✅ 推荐：不使用列级压缩，依赖存储引擎或应用层压缩方案
CREATE TABLE t1 (
    id INT,
    long_text TEXT
);
```
