---
id: audit-rule-aud-expression-in-group-by-causes-index-invalidation
title: GROUP 字段中有表达式导致索引失效
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-expression-in-group-by-causes-index-invalidation
tags:
- audit-rule
- index
description: GROUP BY 使用表达式或函数（如 LEFT、YEAR）会令列索引失效，退化为额外排序或哈希分组；应直接按列分组。
localeOf: en-audit-rule-aud-expression-in-group-by-causes-index-invalidation
subtype: rule
language: zh
translationKey: audit-rule-aud-expression-in-group-by-causes-index-invalidation
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-expression-in-group-by-causes-index-invalidation |
| 规则名称 | GROUP 字段中有表达式导致索引失效 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

数据库可以利用索引的有序性来避免 GROUP BY 子句中列的排序，从而提升 SQL 性能。然而，当 GROUP BY 字段是一个表达式或函数（如 LEFT(column, 5)、YEAR(date_column)）时，数据库无法直接使用该列上的索引来完成分组排序，只能执行额外的排序或哈希分组操作，导致性能下降。

## 如何修复

尽量按原始列或物化后的派生列进行分组，避免直接对表达式分组以利用索引。若业务上必须按表达式分组，可考虑函数索引或新增存储派生列。

## 反例

```sql
-- 不推荐：GROUP BY 使用表达式，导致 c_phone 列索引失效
SELECT LEFT(c_phone, 5), COUNT(1) FROM orders GROUP BY LEFT(c_phone, 5);
```

## 正例

```sql
-- 推荐：避免在 GROUP BY 中使用函数或表达式（根据业务场景优化）
SELECT c_phone_prefix, COUNT(1) FROM orders GROUP BY c_phone_prefix;
```
