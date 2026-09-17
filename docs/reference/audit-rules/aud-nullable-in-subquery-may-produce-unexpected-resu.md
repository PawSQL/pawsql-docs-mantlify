---
id: audit-rule-aud-nullable-in-subquery-may-produce-unexpected-resu
title: IN可空子查询可能导致结果集不符合预期
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-nullable-in-subquery-may-produce-unexpected-resu
tags:
- audit-rule
- dml
localeOf: en-audit-rule-aud-nullable-in-subquery-may-produce-unexpected-resu
subtype: rule
language: zh
translationKey: audit-rule-aud-nullable-in-subquery-may-produce-unexpected-resu
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-nullable-in-subquery-may-produce-unexpected-resu |
| 规则名称 | IN可空子查询可能导致结果集不符合预期 |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

使用 `NOT IN` 子查询时，如果子查询的结果集中存在 NULL 值，整个 `NOT IN` 判断将永远返回空结果集（或 UNKNOWN），这与大多数开发者的直觉预期严重不符。例如，想要查询"没有订单的用户"时，如果 `orders` 表的 `o_custkey` 列存在 NULL 值，`SELECT * FROM customer WHERE c_custkey NOT IN (SELECT o_custkey FROM orders)` 将永远返回空结果。
正确的做法是在子查询内部添加非空过滤条件（`WHERE o_custkey IS NOT NULL`），确保 NULL 值不会影响比较结果。PawSQL 检测此类 SQL 模式并给出强制预警，防止因 NULL 语义导致的隐性数据错误。

## 反例

```sql
-- ❌ 不推荐：NOT IN 子查询的源列可为 NULL，结果可能永远为空
SELECT * FROM customer
WHERE c_custkey NOT IN (SELECT o_custkey FROM orders);
```

## 正例

```sql
-- ✅ 推荐：在子查询中添加非空过滤，避免 NULL 干扰
SELECT * FROM customer
WHERE c_custkey NOT IN (SELECT o_custkey FROM orders WHERE o_custkey IS NOT NULL);
```
