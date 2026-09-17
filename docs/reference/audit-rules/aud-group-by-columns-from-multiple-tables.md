---
id: audit-rule-aud-group-by-columns-from-multiple-tables
title: GROUPBY字段来自不同表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-group-by-columns-from-multiple-tables
tags:
- audit-rule
- index
description: 如果分组字段来自不同的表，数据库优化器将无法利用索引的有序性来避免一次排序操作。当 WHERE 或 HAVING 子句中存在等值条件时，PawSQL
  可以通过等值条件将分组字段替换为来自同一张表的字段，使其能够利用索引来避免排序，提升查询性能。
localeOf: en-audit-rule-aud-group-by-columns-from-multiple-tables
subtype: rule
language: zh
translationKey: audit-rule-aud-group-by-columns-from-multiple-tables
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-group-by-columns-from-multiple-tables |
| 规则名称 | GROUPBY字段来自不同表 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

如果分组字段来自不同的表，数据库优化器将无法利用索引的有序性来避免一次排序操作。当 WHERE 或 HAVING 子句中存在等值条件时，PawSQL 可以通过等值条件将分组字段替换为来自同一张表的字段，使其能够利用索引来避免排序，提升查询性能。
例如，分组字段 `o_custkey, c_name` 来自两个不同的表，但存在过滤条件 `o_custkey = c_custkey`，可将 `o_custkey` 替换为 `c_custkey`，使分组字段全部来自同一张表，从而利用该表上的索引。

## 反例

```sql
-- ❌ 不推荐：分组字段来自不同表，无法利用索引排序
SELECT o_custkey, c_name, SUM(o.O_TOTALPRICE)
FROM customer c, orders o
WHERE o_custkey = c_custkey
GROUP BY o_custkey, c_name;
```

## 正例

```sql
-- ✅ 推荐：通过等值条件替换，使分组字段来自同一表
SELECT c_custkey, c_name, SUM(o.O_TOTALPRICE)
FROM customer c, orders o
WHERE o_custkey = c_custkey
GROUP BY c_custkey, c_name;
```
