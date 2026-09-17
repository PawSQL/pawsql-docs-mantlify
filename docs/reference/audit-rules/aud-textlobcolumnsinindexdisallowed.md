---
id: audit-rule-aud-textlobcolumnsinindexdisallowed
title: 索引中的字段不可以为TEXT和LOB类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-textlobcolumnsinindexdisallowed
tags:
- audit-rule
- index
description: 索引中不应包含 TEXT 和 LOB（如 BLOB、CLOB）类型的字段，因为这些类型的字段通常存储大体积数据，会导致索引节点膨胀、索引扫描效率低下，且部分数据库引擎对这些大对象类型根本不支持索引。
localeOf: en-audit-rule-aud-textlobcolumnsinindexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-textlobcolumnsinindexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-textlobcolumnsinindexdisallowed |
| 规则名称 | 索引中的字段不可以为TEXT和LOB类型 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

索引中不应包含 TEXT 和 LOB（如 BLOB、CLOB）类型的字段，因为这些类型的字段通常存储大体积数据，会导致索引节点膨胀、索引扫描效率低下，且部分数据库引擎对这些大对象类型根本不支持索引。
如果确实需要对大文本字段进行搜索，应考虑使用前缀索引（指定前缀长度）、全文索引（FULLTEXT），或将数据拆分至单独的表进行关联查询。

## 反例

```sql
-- ❌ 不推荐：TEXT/LOB 列不能用于普通索引
CREATE INDEX idx_content ON article(content TEXT);
```

## 正例

```sql
-- ✅ 推荐：使用前缀索引或全文索引
CREATE INDEX idx_content ON article(content(100));
-- 或
CREATE FULLTEXT INDEX idx_content_ft ON article(content);
```
