---
id: optimizer-rule-opt-or-union
title: OR 条件 SELECT 重写
type: reference
status: draft
tags:
- optimizer-rule
- rewrite
- mysql
- postgresql
- oracle
description: 将连接不同字段的 OR 条件重写为 UNION（分支互斥用 UNION ALL），让各分支独立利用索引，避免单一计划退化为全表扫描。
localeOf: en-optimizer-rule-opt-or-union
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | OPT-OR-UNION |
| 规则名称 | OR 条件 SELECT 重写 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | mysql, postgresql, oracle |
| 引入版本 | 8.5.0 |
| 实现 | `OrToUnionRule` |

## 说明

当 SELECT 查询的 WHERE 条件使用 OR 连接不同字段时，数据库优化器可能无法有效利用索引来完成查询。即使两个字段上分别存在索引，OR 条件也可能迫使优化器选择全表扫描而非索引扫描。PawSQL 自动检测此类模式，将 OR 条件拆分为 UNION 或 UNION ALL 查询（如果各 OR 分支条件是互斥的），使每个分支可以独立利用对应字段上的索引，显著提升查询性能。如果数据库支持 INDEX MERGING 优化策略，也可以作为替代方案。

## 为什么重要

OR 连接不同字段时，即便各字段上都有索引，数据库也可能无法同时利用，被迫退化为全表扫描；把分支拆开后，每个分支可独立走各自的索引。

## 如何修复

无需人工处理：PawSQL 自动将 OR 分支拆分为 UNION（分支互斥时用 UNION ALL），使各分支独立利用索引；数据库支持 INDEX MERGING 时也可作为替代。

## 反例

```sql
-- 不推荐：OR 连接不同字段，可能导致全表扫描
SELECT * FROM lineitem
WHERE l_shipdate = DATE '2010-12-01' OR l_partkey < 100;
```

## 正例

```sql
-- 推荐：重写为 UNION，各分支可独立利用索引
SELECT * FROM lineitem WHERE l_shipdate = DATE '2010-12-01'
UNION
SELECT * FROM lineitem WHERE l_partkey < 100;

-- 推荐：若 OR 分支条件互斥，使用 UNION ALL 更高效
SELECT * FROM lineitem WHERE l_shipdate = DATE '2010-12-01'
UNION ALL
SELECT * FROM lineitem WHERE l_partkey < 100 AND l_shipdate <> DATE '2010-12-01';
```
