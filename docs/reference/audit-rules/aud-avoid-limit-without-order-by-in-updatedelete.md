---
id: audit-rule-aud-avoid-limit-without-order-by-in-updatedelete
title: 避免在UPDELETE语句中使用LIMIT而没有ORDER
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-limit-without-order-by-in-updatedelete
tags:
- audit-rule
- dml
description: UPDATE/DELETE 用 LIMIT 无 ORDER BY 影响行不确定；应配 ORDER BY（PG/openGauss 用 WHERE
  子查询定位）。
localeOf: en-audit-rule-aud-avoid-limit-without-order-by-in-updatedelete
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-limit-without-order-by-in-updatedelete
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-limit-without-order-by-in-updatedelete |
| 规则名称 | 避免在UPDELETE语句中使用LIMIT而没有ORDER |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 `UPDATE` 或 `DELETE` 语句中使用 `LIMIT` 而没有 `ORDER BY` 子句，会导致每次执行时受影响的行不确定。数据库在没有排序指令的情况下，处理行的顺序是不保证的，这意味着每次执行 `UPDATE/DELETE ... LIMIT N` 可能更新或删除不同的 N 行记录。
这种行为在数据清理、分批处理等场景中尤其危险——开发者可能期望按某种顺序分批处理数据，但实际每次处理的行却是随机的。正确的做法是始终配合 `ORDER BY` 使用 `LIMIT`，确保操作的可预测性和数据安全性。
> 注意：PostgreSQL/OpenGauss 不支持在 `UPDATE` 或 `DELETE` 语句中使用 `ORDER BY` 子句，在这些数据库中应使用 `WHERE` 子查询的方式来精确定位目标行。

## 反例

```sql
-- ❌ 不推荐：LIMIT 但没有 ORDER BY，每次删除的行不确定
DELETE FROM t WHERE status = 0 LIMIT 10;
```

## 正例

```sql
-- ✅ 推荐：配合 ORDER BY，确保分批处理稳定可预测
DELETE FROM t WHERE status = 0 ORDER BY created_at LIMIT 10;
```
