---
id: zh-optimizer-rule-opt-count-to-exists
title: COUNT 标量子查询重写
type: reference
status: draft
tags:
- optimizer-rule
- zh
- rewrite
description: 对于使用 COUNT 标量子查询来判断记录是否存在的场景（如 (SELECT COUNT(*) FROM ...) > 0），可以重写为
  EXISTS 子查询。COUNT(*) > 0 需要扫描所有匹配行完成聚集运算后才能得出结果，而 EXISTS 在找到第一条匹配记录后即可短路停止扫描，避免不必要的全量计数，从而显著降低
  I/O 和计算开销。
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-count-to-exists |
| 规则名称 | COUNT 标量子查询重写 |
| 类别 | rewrite |
| 预警级别 | 提示 |
| 适用数据库 | 所有支持数据库 |

## 说明

对于使用 COUNT 标量子查询来判断记录是否存在的场景（如 (SELECT COUNT(*) FROM ...) > 0），可以重写为 EXISTS 子查询。COUNT(*) > 0 需要扫描所有匹配行完成聚集运算后才能得出结果，而 EXISTS 在找到第一条匹配记录后即可短路停止扫描，避免不必要的全量计数，从而显著降低 I/O 和计算开销。

## 如何修复

无需人工处理：PawSQL 自动识别此类 SQL 模式，将 COUNT(*) > 0 的相关子查询改写为 EXISTS，让数据库优化器可以在语义等价的前提下选择更高效的执行策略。

## 反例

```sql
-- 不推荐：COUNT 标量子查询需要完成全量聚集运算
SELECT * FROM customer
WHERE (SELECT COUNT(*) FROM orders WHERE c_custkey = o_custkey) > 0;
```

## 正例

```sql
-- 推荐：重写为 EXISTS，找到第一条匹配记录即可短路
SELECT * FROM customer
WHERE EXISTS (SELECT 1 FROM orders WHERE c_custkey = o_custkey);
```
