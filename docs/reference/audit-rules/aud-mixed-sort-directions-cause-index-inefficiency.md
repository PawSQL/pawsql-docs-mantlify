---
id: audit-rule-aud-mixed-sort-directions-cause-index-inefficiency
title: 排序字段方向不同导致索引失效
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-mixed-sort-directions-cause-index-inefficiency
tags:
- audit-rule
- index
description: ORDER BY 子句中的所有表达式需要按统一的ASC或DESC方向排序，才能利用索引来避免显式排序操作。如果ORDER BY语句对多个字段使用了不同方向的排序（如`ORDER
  BY col1 ASC, col2 DESC`），数据库无法直接使用单方向的B-Tree索引来满足排序需求，必须执行额外的排序操作（FileSort），这在大数据量场景下会导致严重的性能问题。
localeOf: en-audit-rule-aud-mixed-sort-directions-cause-index-inefficiency
subtype: rule
language: zh
translationKey: audit-rule-aud-mixed-sort-directions-cause-index-inefficiency
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-mixed-sort-directions-cause-index-inefficiency |
| 规则名称 | 排序字段方向不同导致索引失效 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

ORDER BY 子句中的所有表达式需要按统一的ASC或DESC方向排序，才能利用索引来避免显式排序操作。如果ORDER BY语句对多个字段使用了不同方向的排序（如`ORDER BY col1 ASC, col2 DESC`），数据库无法直接使用单方向的B-Tree索引来满足排序需求，必须执行额外的排序操作（FileSort），这在大数据量场景下会导致严重的性能问题。
当索引的排序方向与ORDER BY一致时，数据库可以沿索引顺序直接读取数据，完全跳过排序步骤，显著提升查询效率。

## 反例

```sql
-- ❌ 不推荐：col1升序、col2降序，方向不一致，导致索引(col1, col2)无法利用
SELECT * FROM t ORDER BY col1 ASC, col2 DESC;
```

## 正例

```sql
-- ✅ 推荐：排序方向与索引一致，可直接利用索引避免额外排序
SELECT * FROM t ORDER BY col1 ASC, col2 ASC;
```
