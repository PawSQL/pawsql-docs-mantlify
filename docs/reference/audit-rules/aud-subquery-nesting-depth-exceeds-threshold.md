---
id: audit-rule-aud-subquery-nesting-depth-exceeds-threshold
title: 子查询的嵌套层次超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-subquery-nesting-depth-exceeds-threshold
tags:
- audit-rule
- dml
description: 子查询的嵌套会让SQL逻辑变得复杂，而过于复杂的SQL会导致数据库优化器在生成执行计划时需要搜索更大的解空间，使得计划生成时间变长，且容易生成性能较差的执行计划。在PawSQL中，子查询嵌套层次的默认阈值为2，用户可以在创建优化任务时修改此阈值。
localeOf: en-audit-rule-aud-subquery-nesting-depth-exceeds-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-subquery-nesting-depth-exceeds-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-subquery-nesting-depth-exceeds-threshold |
| 规则名称 | 子查询的嵌套层次超过阈值 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

子查询的嵌套会让SQL逻辑变得复杂，而过于复杂的SQL会导致数据库优化器在生成执行计划时需要搜索更大的解空间，使得计划生成时间变长，且容易生成性能较差的执行计划。在PawSQL中，子查询嵌套层次的默认阈值为2，用户可以在创建优化任务时修改此阈值。
当子查询嵌套层次超过阈值时，建议将部分子查询抽取为临时表、CTE（公共表表达式）或视图，以简化SQL结构，使优化器能够更高效地生成执行计划。

## 反例

```sql
-- ❌ 不推荐：子查询嵌套层次过深（3层），优化器难以生成最优计划
SELECT * FROM (SELECT * FROM (SELECT * FROM t) a) b;
```

## 正例

```sql
-- ✅ 推荐：将子查询抽取为CTE，降低嵌套深度
WITH a AS (SELECT * FROM t)
SELECT * FROM a;
```
