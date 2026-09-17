---
id: audit-rule-aud-avoid-unnecessary-distinct-operations
title: 避免不必要的去重操作
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-unnecessary-distinct-operations
tags:
- audit-rule
- dml
description: '`SELECT DISTINCT` 会引入昂贵的去重操作（通常需要排序或哈希聚合），消耗额外的 CPU 和内存资源。如果查询逻辑本身能保证结果的唯一性--例如
  SELECT 列表中已包含主键或唯一索引的所有列，或者外层查询已执行去重--那么内部的 DISTINCT 就是多余的，应当予以去除。'
localeOf: en-audit-rule-aud-avoid-unnecessary-distinct-operations
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-unnecessary-distinct-operations
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-unnecessary-distinct-operations |
| 规则名称 | 避免不必要的去重操作 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`SELECT DISTINCT` 会引入昂贵的去重操作（通常需要排序或哈希聚合），消耗额外的 CPU 和内存资源。如果查询逻辑本身能保证结果的唯一性--例如 SELECT 列表中已包含主键或唯一索引的所有列，或者外层查询已执行去重--那么内部的 DISTINCT 就是多余的，应当予以去除。
移除不必要的去重操作可以避免数据库执行无意义的排序或哈希聚合，直接降低查询的资源消耗和执行时间。

## 反例

```sql
-- ❌ 不推荐：id 是主键，结果本身唯一，DISTINCT 是多余的
SELECT DISTINCT id, name FROM user;
```

## 正例

```sql
-- ✅ 推荐：去除多余的 DISTINCT
SELECT id, name FROM user;
```
