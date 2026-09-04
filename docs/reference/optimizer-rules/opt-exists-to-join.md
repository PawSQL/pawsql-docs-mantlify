---
id: optimizer-rule-opt-exists-to-join
title: EXISTS 查询转换为表连接
type: reference
status: draft
tags:
- optimizer-rule
- rewrite
description: 将可转换的 EXISTS 子查询重写为等价内连接，让优化器可自由选择驱动表。
localeOf: en-optimizer-rule-opt-exists-to-join
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-exists-to-join |
| 规则名称 | EXISTS 查询转换为表连接 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 所有支持数据库 |

## 说明

EXISTS 子查询向外层查询返回一个布尔值，表示是否存在满足条件的行。当满足一定条件时（等值关联、子查询结果唯一、无分组无 LIMIT），EXISTS 子查询可以转换为 JOIN 表连接。转换为 JOIN 后，数据库优化器可以灵活选择驱动表，生成更优的查询计划，从而提升查询性能。

## 如何修复

无需人工处理：PawSQL 自动识别可转换的 EXISTS 子查询模式，将其重写为等价的内连接形式，为优化器提供更丰富的执行计划选择空间。

## 反例

```sql
-- 不推荐：EXISTS 子查询限制了优化器对驱动表的选择
SELECT * FROM lineitem l
WHERE EXISTS (SELECT * FROM part p WHERE p.p_partkey = l.l_partkey AND p.p_name = 'a');
```

## 正例

```sql
-- 推荐：转换为 JOIN，优化器可灵活选择驱动表
SELECT l.* FROM lineitem AS l, part AS p
WHERE p.p_partkey = l.l_partkey AND p.p_name = 'a';
```
