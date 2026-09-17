---
id: optimizer-rule-opt-group-by-with-order-by-null-optimization
title: 为分组显式添加空排序(MySQL 5.7)
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-group-by-with-order-by-null-optimization
tags:
- optimizer-rule
- rewrite
description: 在 MySQL 5.7 及更早版本中，即使没有明确指定 `ORDER BY` 子句，`GROUP BY` 默认也会按分组字段进行隐式排序。这种隐式排序行为会触发额外的文件排序（filesort）操作，消耗不必要的计算资源，影响
  SQL 查询的执行性能。
localeOf: en-optimizer-rule-opt-group-by-with-order-by-null-optimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-group-by-with-order-by-null-optimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-group-by-with-order-by-null-optimization |
| 规则名称 | 为分组显式添加空排序(MySQL 5.7) |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 MySQL 5.7 及更早版本中，即使没有明确指定 `ORDER BY` 子句，`GROUP BY` 默认也会按分组字段进行隐式排序。这种隐式排序行为会触发额外的文件排序（filesort）操作，消耗不必要的计算资源，影响 SQL 查询的执行性能。
通过显式添加 `ORDER BY NULL` 可以强制取消 `GROUP BY` 的隐式排序，从而避免不必要的排序开销。PawSQL 能够自动识别此类场景并进行重写优化。
