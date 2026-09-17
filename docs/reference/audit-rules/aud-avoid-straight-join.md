---
id: audit-rule-aud-avoid-straight-join
title: 避免使用STRAIGHT JOIN
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-straight-join
tags:
- audit-rule
- dml
description: STRAIGHT JOIN 是 MySQL 特有的一种表连接方式，它会强制优化器按照 FROM 子句中表的书写顺序来进行表连接，在结果上等价于内连接。它给予了开发人员对数据库执行计划的一定的控制能力，但也因此剥夺了优化器进行表连接顺序优化的机会。
localeOf: en-audit-rule-aud-avoid-straight-join
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-straight-join
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-straight-join |
| 规则名称 | 避免使用STRAIGHT JOIN |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

STRAIGHT JOIN 是 MySQL 特有的一种表连接方式，它会强制优化器按照 FROM 子句中表的书写顺序来进行表连接，在结果上等价于内连接。它给予了开发人员对数据库执行计划的一定的控制能力，但也因此剥夺了优化器进行表连接顺序优化的机会。
MySQL 优化器的连接顺序优化是提升多表 JOIN 性能的关键手段之一。使用 STRAIGHT JOIN 意味着绕过了这一优化，极易导致选择非最优的连接顺序，引发严重的性能问题。除非你对其影响有充分把握，否则不应使用。PawSQL 对使用 STRAIGHT_JOIN 的语句进行风险提示。

## 反例

```sql
-- ❌ 不推荐：STRAIGHT JOIN 强制连接顺序，绕过优化器
SELECT * FROM large_table STRAIGHT_JOIN small_table ON large_table.id = small_table.id;
```

## 正例

```sql
-- ✅ 推荐：使用普通的 JOIN，让优化器选择最优连接顺序
SELECT * FROM large_table JOIN small_table ON large_table.id = small_table.id;
```
