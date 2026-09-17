---
id: audit-rule-aud-partition-column-operation-prevents-partition-pr
title: 分区字段上有运算导致无法进行分区裁剪
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-partition-column-operation-prevents-partition-pr
tags:
- audit-rule
- dml
description: 当 `WHERE` 子句中的分区字段参与算术运算、函数调用或类型转换时，查询优化器无法识别分区过滤条件，导致分区裁剪功能失效。这意味着查询将扫描所有分区而非仅扫描目标分区，严重降低查询性能。
localeOf: en-audit-rule-aud-partition-column-operation-prevents-partition-pr
subtype: rule
language: zh
translationKey: audit-rule-aud-partition-column-operation-prevents-partition-pr
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-partition-column-operation-prevents-partition-pr |
| 规则名称 | 分区字段上有运算导致无法进行分区裁剪 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当 `WHERE` 子句中的分区字段参与算术运算、函数调用或类型转换时，查询优化器无法识别分区过滤条件，导致分区裁剪功能失效。这意味着查询将扫描所有分区而非仅扫描目标分区，严重降低查询性能。
分区裁剪是大数据查询优化的核心手段之一。确保分区字段在过滤条件中"干净"地参与比较——不包裹任何函数或运算——是保障分区裁剪生效的基本前提。常见的问题模式包括对日期分区字段使用 `YEAR()`、`TO_DATE()` 等函数。

## 反例

```sql
-- ❌ 不推荐：分区字段上使用了函数，无法进行分区裁剪
SELECT * FROM sales_table
WHERE YEAR(dt) >= 2024;
```

## 正例

```sql
-- ✅ 推荐：直接对分区字段进行比较，分区裁剪生效
SELECT * FROM sales_table
WHERE dt >= '2024-01-01';
```
