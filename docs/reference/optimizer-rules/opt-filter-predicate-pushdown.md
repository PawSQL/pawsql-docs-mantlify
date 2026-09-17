---
id: optimizer-rule-opt-filter-predicate-pushdown
title: 过滤谓词下推
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-filter-predicate-pushdown
tags:
- optimizer-rule
- rewrite
description: 过滤条件下推（Filter Predicate Pushdown，FPPD）是一种 SQL 重写优化技术，通过尽可能地将外层查询的过滤条件"下压"到内部查询块（如派生表、子查询、UNION
  分支等）中，提前过滤掉不符合条件的数据，从而减少中间结果集的大小，降低后续计算需要处理的数据量，最终提升 SQL 整体执行性能。
localeOf: en-optimizer-rule-opt-filter-predicate-pushdown
subtype: rule
language: zh
translationKey: optimizer-rule-opt-filter-predicate-pushdown
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-filter-predicate-pushdown |
| 规则名称 | 过滤谓词下推 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

过滤条件下推（Filter Predicate Pushdown，FPPD）是一种 SQL 重写优化技术，通过尽可能地将外层查询的过滤条件"下压"到内部查询块（如派生表、子查询、UNION 分支等）中，提前过滤掉不符合条件的数据，从而减少中间结果集的大小，降低后续计算需要处理的数据量，最终提升 SQL 整体执行性能。
如果过滤条件未能下推到内部查询块，数据库需要在生成完整的中间结果集后，再在外层应用过滤条件，这意味着大量本可提前排除的数据参与了中间计算，浪费了 CPU、内存和 IO 资源。

## 反例

```sql
-- ❌ 不推荐：过滤条件在外层，无法提前削减内部查询的数据量
select *
from (select c_nationkey nation, 'C' as type, count(1) num
      from customer
      group by nation
      union
      select s_nationkey nation, 'S', count(1) num
      from supplier
      group by nation) as person
where nation = 100;
```

## 正例

```sql
-- ✅ 推荐：过滤条件下推到派生表内部，提前过滤各分支数据
select *
from (select c_nationkey nation, 'C' as type, count(1) num
      from customer
      where c_nationkey = 100
      group by nation
      union
      select s_nationkey nation, 'S', count(1) num
      from supplier
      where s_nationkey = 100
      group by nation) as person;
```
