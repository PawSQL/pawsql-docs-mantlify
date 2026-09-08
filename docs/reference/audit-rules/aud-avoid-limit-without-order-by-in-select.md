---
id: audit-rule-aud-avoid-limit-without-order-by-in-select
title: 避免在SELECT语句中使用LIMIT而没有ORDER BY
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-limit-without-order-by-in-select
tags:
- audit-rule
- dml
description: SELECT 用 LIMIT 无 ORDER BY 时返回行不确定；加 ORDER BY 明确取哪前 N 行。
localeOf: en-audit-rule-aud-avoid-limit-without-order-by-in-select
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-limit-without-order-by-in-select
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-limit-without-order-by-in-select |
| 规则名称 | 避免在SELECT语句中使用LIMIT而没有ORDER BY |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 `SELECT` 语句中使用 `LIMIT` 而没有 `ORDER BY` 子句，会导致每次执行的结果不确定。数据库在没有排序指令的情况下，返回行的顺序是不保证的——它取决于存储引擎的物理存储顺序、查询执行计划的细节等因素，而这些因素在不同时间、不同版本下可能发生变化。
如果业务逻辑依赖 `LIMIT` 返回"前 N 条"记录，必须同时指定 `ORDER BY` 来明确定义"前"的排序规则，确保结果的可重复性和正确性。PawSQL 会检查此类写法并进行提醒。

## 反例

```sql
-- ❌ 不推荐：LIMIT 没有 ORDER BY，每次返回的行可能不同
SELECT * FROM user LIMIT 10;
```

## 正例

```sql
-- ✅ 推荐：明确指定 ORDER BY，确保结果稳定可重复
SELECT * FROM user ORDER BY id LIMIT 10;
```
