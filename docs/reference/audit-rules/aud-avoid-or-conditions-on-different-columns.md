---
id: audit-rule-aud-avoid-or-conditions-on-different-columns
title: 避免不同字段的OR条件
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-or-conditions-on-different-columns
tags:
- audit-rule
- index
description: 对于同一字段上的多个 OR 条件（如 `WHERE col = 1 OR col = 2`），数据库优化器可以将其统一视为一个索引范围扫描的候选项，从而利用索引进行高效的数据定位。然而，当
  OR 条件涉及不同字段时（如 `WHERE col_a = 1 OR col_b = 2`），优化器通常无法在单次索引扫描中同时覆盖两个不同的列，可能被迫选择全表扫描来评估条件。
localeOf: en-audit-rule-aud-avoid-or-conditions-on-different-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-or-conditions-on-different-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-or-conditions-on-different-columns |
| 规则名称 | 避免不同字段的OR条件 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于同一字段上的多个 OR 条件（如 `WHERE col = 1 OR col = 2`），数据库优化器可以将其统一视为一个索引范围扫描的候选项，从而利用索引进行高效的数据定位。然而，当 OR 条件涉及不同字段时（如 `WHERE col_a = 1 OR col_b = 2`），优化器通常无法在单次索引扫描中同时覆盖两个不同的列，可能被迫选择全表扫描来评估条件。
如果确实需要在不同字段间使用 OR 条件，可以考虑将其重写为 UNION ALL 的形式，使每个分支都能独立利用各自的索引；或者在两个字段上建立复合索引来覆盖该查询模式。

## 反例

```sql
-- ❌ 不推荐：OR 条件跨不同字段，难以利用索引
SELECT * FROM t WHERE col_a = 1 OR col_b = 2;
```

## 正例

```sql
-- ✅ 推荐：重写为 UNION ALL，每个分支各自利用索引
SELECT * FROM t WHERE col_a = 1
UNION ALL
SELECT * FROM t WHERE col_b = 2;
```
