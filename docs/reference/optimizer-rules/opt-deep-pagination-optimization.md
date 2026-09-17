---
id: optimizer-rule-opt-deep-pagination-optimization
title: 深分页优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-deep-pagination-optimization
tags:
- optimizer-rule
- rewrite
localeOf: en-optimizer-rule-opt-deep-pagination-optimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-deep-pagination-optimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-deep-pagination-optimization |
| 规则名称 | 深分页优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

深分页指的是翻页请求中的页码数非常大、OFFSET 数值非常大的情况。如果直接使用 `LIMIT offset, limit` 的方式进行分页，当 OFFSET 超过阈值（如 10000）时性能会明显下降。原因是数据库会先获取符合条件的 `offset + n` 行数据，然后再丢弃前 `offset` 行，返回后 `n` 行——这意味着 `LIMIT 10000, 10` 需要扫描并回表 10010 次，大量时间消耗在回表操作上。
优化的核心思路是减少回表次数：通过子查询先定位主键（利用覆盖索引避免回表），再通过主键关联回表获取完整行数据。当查询涉及的字段数较少（<=4）时，直接创建覆盖索引即可；当字段较多时，推荐采用"延迟关联"的重写策略。

## 反例

```sql
-- ❌ 不推荐：大 OFFSET 导致大量无效回表
SELECT * FROM orders WHERE O_ORDERSTATUS = '1' ORDER BY O_ORDERKEY LIMIT 10000, 10;
```

## 正例

```sql
-- ✅ 推荐：子查询 + 覆盖索引 减少回表（延迟关联）
SELECT o.*
FROM orders AS o
INNER JOIN (
    SELECT O_ORDERKEY
    FROM orders
    WHERE O_ORDERSTATUS = '1'
    ORDER BY O_ORDERKEY
    LIMIT 10 OFFSET 10000
) AS orders_dt ON o.O_ORDERKEY = orders_dt.O_ORDERKEY;
```
