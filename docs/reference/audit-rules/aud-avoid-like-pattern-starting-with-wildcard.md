---
id: audit-rule-aud-avoid-like-pattern-starting-with-wildcard
title: 避免%开头的LIKE查询
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-like-pattern-starting-with-wildcard
tags:
- audit-rule
- index
description: 在 SQL 查询中，LIKE 操作符用于字符串的模式匹配。如果模式字符串以 `%` 或 `_` 开头（例如 `LIKE '%ABC'`），数据库优化器无法利用
  B-Tree 索引来快速定位数据，因为索引的有序性依赖于前缀匹配。此时数据库只能进行全表扫描或全索引扫描，在数据量大的情况下查询性能会受到严重影响。
localeOf: en-audit-rule-aud-avoid-like-pattern-starting-with-wildcard
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-like-pattern-starting-with-wildcard
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-like-pattern-starting-with-wildcard |
| 规则名称 | 避免%开头的LIKE查询 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 SQL 查询中，LIKE 操作符用于字符串的模式匹配。如果模式字符串以 `%` 或 `_` 开头（例如 `LIKE '%ABC'`），数据库优化器无法利用 B-Tree 索引来快速定位数据，因为索引的有序性依赖于前缀匹配。此时数据库只能进行全表扫描或全索引扫描，在数据量大的情况下查询性能会受到严重影响。
因此应尽量避免以 `%` 开头的 LIKE 查询。如果业务确实需要后缀匹配或全文搜索能力，建议考虑使用全文索引（Full-Text Index）来替代普通的 LIKE 查询，以获得更好的性能表现。

## 反例

```sql
-- ❌ 不推荐：LIKE 以 % 开头，无法利用索引，导致全表扫描
SELECT * FROM t WHERE name LIKE '%test';
```

## 正例

```sql
-- ✅ 推荐：LIKE 不以通配符开头，可利用索引
SELECT * FROM t WHERE name LIKE 'test%';

-- ✅ 推荐：如需后缀匹配，考虑使用全文索引
-- ALTER TABLE t ADD FULLTEXT INDEX ft_name (name);
-- SELECT * FROM t WHERE MATCH(name) AGAINST('test');
```
