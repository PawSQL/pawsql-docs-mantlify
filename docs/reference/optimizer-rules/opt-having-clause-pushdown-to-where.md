---
id: optimizer-rule-opt-having-clause-pushdown-to-where
title: HAVING条件下推
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-having-clause-pushdown-to-where
tags:
- optimizer-rule
- rewrite
description: 从逻辑上看，HAVING 条件是在分组之后执行的，而 WHERE 子句上的条件可以在表访问时（索引访问）或表访问之后、分组之前执行。在分组之前过滤数据的代价远小于分组之后。因此，当
  HAVING 子句中不包含聚集函数的条件时，应将其"下推"到 WHERE 子句中提前过滤，减少参与分组计算的数据量，从而提升 SQL 性能。
localeOf: en-optimizer-rule-opt-having-clause-pushdown-to-where
subtype: rule
language: zh
translationKey: optimizer-rule-opt-having-clause-pushdown-to-where
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-having-clause-pushdown-to-where |
| 规则名称 | HAVING条件下推 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

从逻辑上看，HAVING 条件是在分组之后执行的，而 WHERE 子句上的条件可以在表访问时（索引访问）或表访问之后、分组之前执行。在分组之前过滤数据的代价远小于分组之后。因此，当 HAVING 子句中不包含聚集函数的条件时，应将其"下推"到 WHERE 子句中提前过滤，减少参与分组计算的数据量，从而提升 SQL 性能。
PawSQL 自动识别此类模式，将 HAVING 中不含聚集函数的过滤条件下推到 WHERE 子句，在数据到达 GROUP BY 之前就完成过滤。

## 反例

```sql
-- ❌ 不推荐：HAVING 中不含聚集函数的条件，在分组后才过滤
SELECT c_custkey, COUNT(*) FROM customer GROUP BY c_custkey HAVING c_custkey < 100;
```

## 正例

```sql
-- ✅ 推荐：条件下推到 WHERE，在分组前过滤，减少分组数据量
SELECT c_custkey, COUNT(*) FROM customer WHERE c_custkey < 100 GROUP BY c_custkey;
```
