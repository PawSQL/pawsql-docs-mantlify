---
id: optimizer-rule-opt-query-folding
title: 查询折叠(QUERY FOLDING)
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-query-folding
tags:
- optimizer-rule
- rewrite
description: 查询折叠（Query Folding）指的是把视图、CTE或派生表（Derived Table）子查询展开，并与引用它的外层查询语句合并的优化技术。通过消除不必要的子查询层次，查询折叠可以减少序列化中间结果集的开销，同时为优化器提供更全面的查询上下文，从而触发更优的表连接规划和索引选择。
localeOf: en-optimizer-rule-opt-query-folding
subtype: rule
language: zh
translationKey: optimizer-rule-opt-query-folding
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-query-folding |
| 规则名称 | 查询折叠(QUERY FOLDING) |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

查询折叠（Query Folding）指的是把视图、CTE或派生表（Derived Table）子查询展开，并与引用它的外层查询语句合并的优化技术。通过消除不必要的子查询层次，查询折叠可以减少序列化中间结果集的开销，同时为优化器提供更全面的查询上下文，从而触发更优的表连接规划和索引选择。
PawSQL优化引擎支持两种查询折叠策略：类型I适用于视图本身不含DISTINCT、聚集函数、窗口函数、LIMIT和UNION的场景；类型II适用于外部查询块中视图是唯一表引用、且外部无分组和聚合的场景。MySQL 5.7及PostgreSQL 14.0以上版本已支持类型I的查询折叠，但类型II在最新的MySQL及PostgreSQL中仍未原生支持。

## 正例

```sql
-- ✅ 优化前：无意义的派生表包裹，增加不必要的查询层次
SELECT * FROM (SELECT c_custkey, c_name FROM customer) AS derived_t1;

-- ✅ 优化后：查询折叠消除派生表，直接查询基表
SELECT c_custkey, c_name FROM customer;
```
