---
id: audit-rule-aud-avoid-order-by-random-function
title: 避免使用随机函数排序
type: reference
status: draft
tags:
- audit-rule
- dml
description: 避免 ORDER BY RAND()/RANDOM() 取随机样本（需对全行生成随机值并排序）；用随机主键范围或 TABLESAMPLE。
localeOf: en-audit-rule-aud-avoid-order-by-random-function
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-order-by-random-function |
| 规则名称 | 避免使用随机函数排序 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

MySQL 的函数 `RAND()` 或 PostgreSQL 的函数 `RANDOM()` 会返回一个在范围 0 到 1.0 之间的随机浮点数。有些开发者会使用 `ORDER BY RAND() LIMIT N` 来获取数据集的随机样本。当表少于 10,000 行时，这种方法效果尚可；但当表达到百万级别时，排序的开销将变得不可接受——因为数据库必须先生成每一行的随机值，然后对所有行进行排序，最终却只保留其中极少数行。
获取随机样本有远更高效的方法，例如通过随机主键范围筛选或使用表采样（TABLESAMPLE）特性。点击获取该优化的[详细信息](https://app.pawsql.com/docs/rule/RuleOrderByRandomWarning)。

## 反例

```sql
-- ❌ 不推荐：对所有行计算随机值并排序，性能极差
select * from orders order by rand() limit 1;
```

## 正例

```sql
-- ✅ 推荐：使用更高效的方式获取随机样本，例如基于主键范围
-- 假设 id 范围为 1~1000000
select * from orders where id >= (select floor(rand() * max(id)) from orders) limit 1;
```
