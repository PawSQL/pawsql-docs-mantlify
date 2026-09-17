---
id: audit-rule-aud-use-specified-data-distribution-method
title: 应使用指定的数据分布方式
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-specified-data-distribution-method
tags:
- audit-rule
- ddl
description: 在TDSQL等分布式数据库中，应使用指定的数据分布方式（默认为`murmurhash`算法）作为分片键的哈希函数。`murmurhash`是一种非加密型哈希函数，具有高运算效率和良好的分布均匀性，能够确保数据在各个分片上尽可能均匀分布，避免数据倾斜导致的节点负载不均。
localeOf: en-audit-rule-aud-use-specified-data-distribution-method
subtype: rule
language: zh
translationKey: audit-rule-aud-use-specified-data-distribution-method
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-specified-data-distribution-method |
| 规则名称 | 应使用指定的数据分布方式 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在TDSQL等分布式数据库中，应使用指定的数据分布方式（默认为`murmurhash`算法）作为分片键的哈希函数。`murmurhash`是一种非加密型哈希函数，具有高运算效率和良好的分布均匀性，能够确保数据在各个分片上尽可能均匀分布，避免数据倾斜导致的节点负载不均。
使用其他非标准的分布方式可能导致数据分布不均，某些分片的数据量远大于其他分片，从而引发热点问题、跨节点查询性能下降，严重时甚至导致单个节点成为系统瓶颈。

## 正例

```sql
-- ✅ 推荐：使用默认的murmurhash分布算法，数据均匀分布在各个分片
CREATE TABLE t (
    id BIGINT,
    name VARCHAR(100)
) shardkey=id;
```
