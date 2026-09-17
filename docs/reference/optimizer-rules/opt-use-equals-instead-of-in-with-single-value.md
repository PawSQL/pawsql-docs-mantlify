---
id: optimizer-rule-opt-use-equals-instead-of-in-with-single-value
title: 使用 = 替代 IN（单值）
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-use-equals-instead-of-in-with-single-value
tags:
- optimizer-rule
- rewrite
description: 当 `IN` 列表中只包含单个值时，使用 `IN` 和 `=` 在语义上完全等价。但使用 `=` 语义更清晰，代码可读性更强，同时可以避免某些数据库优化器对
  `IN` 操作符的特殊处理带来的潜在性能差异。
localeOf: en-optimizer-rule-opt-use-equals-instead-of-in-with-single-value
subtype: rule
language: zh
translationKey: optimizer-rule-opt-use-equals-instead-of-in-with-single-value
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-use-equals-instead-of-in-with-single-value |
| 规则名称 | 使用 = 替代 IN（单值） |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当 `IN` 列表中只包含单个值时，使用 `IN` 和 `=` 在语义上完全等价。但使用 `=` 语义更清晰，代码可读性更强，同时可以避免某些数据库优化器对 `IN` 操作符的特殊处理带来的潜在性能差异。
在索引利用方面，`=` 是等值比较，优化器能够更精确地估算选择率并选择最优的索引访问路径。养成使用 `=` 替代单值 `IN` 的编码习惯，有助于编写更清晰、更高效的 SQL 语句。

## 反例

```sql
-- ❌ 不推荐：IN 列表只有单个值
SELECT * FROM t_user WHERE id IN (100);
```

## 正例

```sql
-- ✅ 推荐：使用 = 替代单值 IN
SELECT * FROM t_user WHERE id = 100;
```
