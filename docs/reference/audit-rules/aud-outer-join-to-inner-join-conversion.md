---
id: audit-rule-aud-outer-join-to-inner-join-conversion
title: 外连接优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-outer-join-to-inner-join-conversion
tags:
- audit-rule
- dml
description: 外连接优化指的是当外表（OUTER JOIN中可为NULL的一侧）的WHERE条件中包含NULL拒绝条件（Null-Rejecting Condition）时，该外连接可以安全地转化为内连接。这一转化使得数据库优化器在选择执行计划时拥有更大的自由度：优化器可以更灵活地选择驱动表，并可以先应用过滤条件获取较小的结果集，再进行表关联，从而显著提升SQL查询的性能。
localeOf: en-audit-rule-aud-outer-join-to-inner-join-conversion
subtype: rule
language: zh
translationKey: audit-rule-aud-outer-join-to-inner-join-conversion
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-outer-join-to-inner-join-conversion |
| 规则名称 | 外连接优化 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

外连接优化指的是当外表（OUTER JOIN中可为NULL的一侧）的WHERE条件中包含NULL拒绝条件（Null-Rejecting Condition）时，该外连接可以安全地转化为内连接。这一转化使得数据库优化器在选择执行计划时拥有更大的自由度：优化器可以更灵活地选择驱动表，并可以先应用过滤条件获取较小的结果集，再进行表关联，从而显著提升SQL查询的性能。
例如，当LEFT JOIN的右表上存在`WHERE`过滤条件（如`col < 20`、`col IS NOT NULL`等）时，该条件隐含地拒绝了NULL行，因此外连接退化为内连接，优化器可以利用这一特性生成更优的执行计划。

## 正例

```sql
-- ✅ 优化前：LEFT JOIN 的右表 WHERE 条件隐含非空约束
SELECT c_custkey
FROM orders
LEFT JOIN customer ON c_custkey = o_custkey
WHERE C_NATIONKEY < 20;

-- ✅ 优化后：外连接退化为内连接，优化器可选择更优连接顺序
SELECT c_custkey
FROM orders
INNER JOIN customer ON c_custkey = o_custkey
WHERE C_NATIONKEY < 20;
```
