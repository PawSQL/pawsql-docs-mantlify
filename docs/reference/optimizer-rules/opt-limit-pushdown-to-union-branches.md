---
id: optimizer-rule-opt-limit-pushdown-to-union-branches
title: LIMIT下推至UNION分支
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-limit-pushdown-to-union-branches
tags:
- optimizer-rule
- rewrite
description: LIMIT 子句下推优化通过将外查询的 LIMIT 子句尽可能"下压"至 UNION 内部查询块，提前过滤掉部分数据，减少中间结果集的大小，从而降低后续计算（如排序、合并）需要处理的数据量，显著提升查询性能。
localeOf: en-optimizer-rule-opt-limit-pushdown-to-union-branches
subtype: rule
language: zh
translationKey: optimizer-rule-opt-limit-pushdown-to-union-branches
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-limit-pushdown-to-union-branches |
| 规则名称 | LIMIT下推至UNION分支 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

LIMIT 子句下推优化通过将外查询的 LIMIT 子句尽可能"下压"至 UNION 内部查询块，提前过滤掉部分数据，减少中间结果集的大小，从而降低后续计算（如排序、合并）需要处理的数据量，显著提升查询性能。
例如，外查询 `ORDER BY ... LIMIT 20, 10` 通过 UNION 连接两个子查询，可将 LIMIT 下推至每个分支内部执行，避免先生成所有数据再排序截取。PawSQL 自动计算合理的内层 LIMIT 值并完成下推重写。

## 反例

```sql
-- ❌ 不推荐：LIMIT 在外层执行，UNION 后数据量大
SELECT *
FROM (
    SELECT c_nationkey nation, 'C' AS type, COUNT(1) num
    FROM customer
    GROUP BY c_nationkey
    UNION
    SELECT s_nationkey nation, 'S' AS type, COUNT(1) num
    FROM supplier
    GROUP BY nation
) AS nation_s
ORDER BY nation LIMIT 20, 10;
```

## 正例

```sql
-- ✅ 推荐：LIMIT 下推至各 UNION 分支，减少中间数据量
SELECT *
FROM (
    (SELECT customer.c_nationkey AS nation, 'C' AS `type`, COUNT(1) AS num
     FROM customer
     GROUP BY customer.c_nationkey
     ORDER BY customer.c_nationkey LIMIT 30)
    UNION
    (SELECT supplier.s_nationkey AS nation, 'S' AS `type`, COUNT(1) AS num
     FROM supplier
     GROUP BY supplier.s_nationkey
     ORDER BY supplier.s_nationkey LIMIT 30)
) AS nation_s
ORDER BY nation_s.nation LIMIT 20, 10;
```
