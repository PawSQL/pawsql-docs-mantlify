---
id: audit-rule-aud-numberofjoinedtablesexceedcriticalthreshold
title: 禁止表关联数目超过阈值（严重）
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-numberofjoinedtablesexceedcriticalthreshold
tags:
- audit-rule
- dml
description: 在数据库执行计划的规划中，表连接的顺序和连接方法是优化器最重要的规划内容。表连接数目的增加将几何级数地增加数据库优化器对于最优执行计划的搜寻空间，导致生成执行计划的时间变长，且容易生成性能较差的执行计划。
localeOf: en-audit-rule-aud-numberofjoinedtablesexceedcriticalthreshold
subtype: rule
language: zh
translationKey: audit-rule-aud-numberofjoinedtablesexceedcriticalthreshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-numberofjoinedtablesexceedcriticalthreshold |
| 规则名称 | 禁止表关联数目超过阈值（严重） |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在数据库执行计划的规划中，表连接的顺序和连接方法是优化器最重要的规划内容。表连接数目的增加将几何级数地增加数据库优化器对于最优执行计划的搜寻空间，导致生成执行计划的时间变长，且容易生成性能较差的执行计划。
多表 JOIN 在分布式数据库中更是性能的头号杀手，跨节点的数据重分布会消耗大量网络和计算资源。PawSQL 检测查询中表连接的数目是否超过阈值，并对严重超限的情况发出严重级别告警。阈值的默认值是 5，用户可以在创建优化任务时修改此阈值。

## 反例

```sql
-- ❌ 不推荐：关联表数目超过阈值（严重级别，默认阈值 5）
SELECT ...
FROM t1
JOIN t2 ON t1.id = t2.id
JOIN t3 ON t2.id = t3.id
JOIN t4 ON t3.id = t4.id
JOIN t5 ON t4.id = t5.id
JOIN t6 ON t5.id = t6.id
WHERE ...;
```

## 正例

```sql
-- ✅ 推荐：拆分为多个简单查询，或通过临时表/物化视图减少单次关联数
```
