---
id: optimizer-rule-opt-eliminate-unnecessary-distinct-in-subqueries
title: 子查询中的DISTINCT消除
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-eliminate-unnecessary-distinct-in-subqueries
tags:
- optimizer-rule
- rewrite
description: 对于仅进行存在性测试的子查询（如`IN`、`EXISTS`子查询），如果子查询中使用了`DISTINCT`关键字，那么这个去重操作通常是多余的——因为`IN`/`EXISTS`只关心值是否存在，而不关心值出现的次数。消除不必要的`DISTINCT`可以避免一次代价高昂的去重操作（排序或哈希聚合），从而提升查询性能。
localeOf: en-optimizer-rule-opt-eliminate-unnecessary-distinct-in-subqueries
subtype: rule
language: zh
translationKey: optimizer-rule-opt-eliminate-unnecessary-distinct-in-subqueries
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-eliminate-unnecessary-distinct-in-subqueries |
| 规则名称 | 子查询中的DISTINCT消除 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于仅进行存在性测试的子查询（如`IN`、`EXISTS`子查询），如果子查询中使用了`DISTINCT`关键字，那么这个去重操作通常是多余的——因为`IN`/`EXISTS`只关心值是否存在，而不关心值出现的次数。消除不必要的`DISTINCT`可以避免一次代价高昂的去重操作（排序或哈希聚合），从而提升查询性能。
该优化适用于所有使用`IN`或`EXISTS`子查询进行存在性判断的场景。PawSQL优化引擎会自动检测并建议消除此类冗余的`DISTINCT`关键字。

## 反例

```sql
-- ❌ 不推荐：IN子查询中的DISTINCT多余，仅存在性判断无需去重
SELECT * FROM customer WHERE c_custkey IN (SELECT DISTINCT o_custkey FROM orders);
```

## 正例

```sql
-- ✅ 推荐：消除DISTINCT，避免不必要的去重操作
SELECT * FROM customer WHERE c_custkey IN (SELECT o_custkey FROM orders);
```
