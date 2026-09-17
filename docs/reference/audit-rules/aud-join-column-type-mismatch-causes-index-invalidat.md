---
id: audit-rule-aud-join-column-type-mismatch-causes-index-invalidat
title: 连接字段类型不匹配导致索引失效
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-join-column-type-mismatch-causes-index-invalidat
tags:
- audit-rule
- index
description: 当 JOIN 连接条件中两个字段的数据类型不同时，在查询执行过程中数据库会进行隐式的数据类型转换。当类型转换被应用到列上（而非常量上）时，该列上的索引将无法被使用，可能导致原本高效的索引连接退化为全表扫描或全索引扫描，引发严重的性能问题。
localeOf: en-audit-rule-aud-join-column-type-mismatch-causes-index-invalidat
subtype: rule
language: zh
translationKey: audit-rule-aud-join-column-type-mismatch-causes-index-invalidat
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-join-column-type-mismatch-causes-index-invalidat |
| 规则名称 | 连接字段类型不匹配导致索引失效 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当 JOIN 连接条件中两个字段的数据类型不同时，在查询执行过程中数据库会进行隐式的数据类型转换。当类型转换被应用到列上（而非常量上）时，该列上的索引将无法被使用，可能导致原本高效的索引连接退化为全表扫描或全索引扫描，引发严重的性能问题。
PawSQL 会检查类型不匹配的连接条件并进行提醒，帮助开发者及时发现并修复此类隐匿的性能隐患。修复方式通常包括统一字段的数据类型，或在常量侧进行显式类型转换以避免转换落在列上。

## 反例

```sql
-- ❌ 不推荐：连接字段类型不匹配，隐式转换导致索引失效
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.id;
-- 假设 o.customer_id 为 VARCHAR，c.id 为 INT，转换落在 o.customer_id 列上，索引失效
```

## 正例

```sql
-- ✅ 推荐：统一字段类型，或显式转换常量侧
SELECT * FROM orders o JOIN customers c ON o.customer_id = CAST(c.id AS VARCHAR);
```
