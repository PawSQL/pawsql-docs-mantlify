---
id: audit-rule-aud-droppingcolumnsusedinindexdisallowed
title: 禁止删除索引中的列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-droppingcolumnsusedinindexdisallowed
tags:
- audit-rule
- ddl
description: 禁止删除被索引使用的列。如果某个列是索引定义的一部分，直接删除该列会导致索引失效或被数据库自动重建，引发执行计划变化和性能问题。此外，部分数据库在列被索引引用时可能直接拒绝删除操作，但也有一些数据库会静默删除索引，导致开发者在不知情的情况下丢失重要的性能结构。
localeOf: en-audit-rule-aud-droppingcolumnsusedinindexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-droppingcolumnsusedinindexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-droppingcolumnsusedinindexdisallowed |
| 规则名称 | 禁止删除索引中的列 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止删除被索引使用的列。如果某个列是索引定义的一部分，直接删除该列会导致索引失效或被数据库自动重建，引发执行计划变化和性能问题。此外，部分数据库在列被索引引用时可能直接拒绝删除操作，但也有一些数据库会静默删除索引，导致开发者在不知情的情况下丢失重要的性能结构。
在删除列之前，必须先检查该列是否被索引引用。如果是，应先行删除或重建索引，再安全删除列。

## 反例

```sql
-- ❌ 不推荐：直接删除索引引用的列，导致索引失效
ALTER TABLE t DROP COLUMN some_col;  -- some_col 被现有索引引用
```

## 正例

```sql
-- ✅ 推荐：先处理索引，再删除列
-- 1. DROP INDEX idx_on_col ON t;  -- 删除依赖索引
-- 2. ALTER TABLE t DROP COLUMN some_col;
-- 3. 如有需要，CREATE INDEX 创建替代索引
```
