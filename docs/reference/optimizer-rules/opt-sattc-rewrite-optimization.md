---
id: optimizer-rule-opt-sattc-rewrite-optimization
title: SATTC重写优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-sattc-rewrite-optimization
tags:
- optimizer-rule
- rewrite
description: SAT-TC（SATisfiability-Transitive Closure）重写优化是指对一组相关的查询条件进行逻辑分析，发现其中自相矛盾的条件、可简化的表达式，或推断出新的过滤条件，从而帮助数据库优化器选择更好的执行计划。
localeOf: en-optimizer-rule-opt-sattc-rewrite-optimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-sattc-rewrite-optimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-sattc-rewrite-optimization |
| 规则名称 | SATTC重写优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

SAT-TC（SATisfiability-Transitive Closure）重写优化是指对一组相关的查询条件进行逻辑分析，发现其中自相矛盾的条件、可简化的表达式，或推断出新的过滤条件，从而帮助数据库优化器选择更好的执行计划。
具体包括三种场景：第一，条件自相矛盾（如 `c_name = 'John' AND c_name = 'Jessey'`），可直接简化为 `WHERE 1=0` 避免无效扫描；第二，条件可简化（如 `c_custkey <> c_custkey OR c_name = 'b'` 简化为 `c_name = 'b'`）；第三，从谓词集中推断新条件（如 `c_custkey=1 AND c_custkey=o_custkey` 意味着 `o_custkey=1`），新增的过滤条件可进一步缩小数据范围。

## 反例

```sql
-- ❌ 不推荐：条件自相矛盾，但未优化
SELECT c.c_name FROM customer c
WHERE c.c_name = 'John' AND c.c_name = 'Jessey';

-- ❌ 不推荐：条件可简化但未简化
SELECT * FROM customer WHERE c_custkey <> c_custkey OR c_name = 'b';

-- ❌ 不推荐：缺少传递闭包推断的新条件
SELECT * FROM customer c, orders o
WHERE c_custkey = 1 AND c_custkey = o_custkey;
```

## 正例

```sql
-- ✅ 推荐：SATTC 识别矛盾后简化为 1=0，避免无效扫描
SELECT c.c_name FROM customer c WHERE 1 = 0;

-- ✅ 推荐：简化冗余条件
SELECT * FROM customer WHERE c_name = 'b';

-- ✅ 推荐：SATTC 推断出 o_custkey = 1，增加过滤条件
SELECT * FROM customer c, orders o
WHERE c_custkey = 1 AND c_custkey = o_custkey AND o_custkey = 1;
```
