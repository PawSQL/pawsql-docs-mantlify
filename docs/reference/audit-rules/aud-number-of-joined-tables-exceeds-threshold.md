---
id: audit-rule-aud-number-of-joined-tables-exceeds-threshold
title: 查询中表连接的个数超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-number-of-joined-tables-exceeds-threshold
tags:
- audit-rule
- dml
description: 在单机版数据库中，执行计划的规划涉及表连接的顺序和连接方法的选择——这是优化器最重要的决策内容。表连接数目的增加会使优化器对于最优执行计划的搜寻空间呈几何级数增长：n个表的连接有(n-1)!种可能的连接顺序，每种顺序又有多种连接方法可选。这导致生成执行计划的时间变长，且在高连接数时优化器容易因搜索空间过大而生成性能较差的执行计划。
localeOf: en-audit-rule-aud-number-of-joined-tables-exceeds-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-number-of-joined-tables-exceeds-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-number-of-joined-tables-exceeds-threshold |
| 规则名称 | 查询中表连接的个数超过阈值 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在单机版数据库中，执行计划的规划涉及表连接的顺序和连接方法的选择——这是优化器最重要的决策内容。表连接数目的增加会使优化器对于最优执行计划的搜寻空间呈几何级数增长：n个表的连接有(n-1)!种可能的连接顺序，每种顺序又有多种连接方法可选。这导致生成执行计划的时间变长，且在高连接数时优化器容易因搜索空间过大而生成性能较差的执行计划。
PawSQL检测单个查询块中表连接的数目是否超过阈值（默认为5），当超过时提醒用户可能存在性能风险。建议将多表连接拆分为多步查询，或使用临时表存储中间结果。

## 反例

```sql
-- ❌ 不推荐：单个查询块连接6张表，超过默认阈值5，优化器规划空间过大
SELECT *
FROM t1
JOIN t2 ON t1.id = t2.t1_id
JOIN t3 ON t2.id = t3.t2_id
JOIN t4 ON t3.id = t4.t3_id
JOIN t5 ON t4.id = t5.t4_id
JOIN t6 ON t5.id = t6.t5_id;
```

## 正例

```sql
-- ✅ 推荐：拆分为多步查询或使用临时表减少单查询块的连接数
-- 将前3张表的连接结果存入临时表，再与其余表关联
```
