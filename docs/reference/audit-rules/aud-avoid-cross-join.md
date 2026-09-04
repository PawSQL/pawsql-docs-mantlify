---
id: audit-rule-aud-avoid-cross-join
title: 避免使用CROSS JOIN
type: reference
status: draft
tags:
- audit-rule
- dml
description: 避免 CROSS JOIN 产生的笛卡尔积（性能陷阱）；应改用带 ON 条件的关联，确需笛卡尔积时加注释说明。
localeOf: en-audit-rule-aud-avoid-cross-join
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-cross-join |
| 规则名称 | 避免使用CROSS JOIN |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

CROSS JOIN 会将左表的每一行与右表的每一行进行笛卡尔乘积，生成 `左表行数 x 右表行数` 条记录。理论上它等价于条件为 `1=1` 的内连接。虽然 CROSS JOIN 在特定场景下（如生成测试数据、行列转换）有合理的用途，但在绝大多数情况下，它会产生大量无实际意义的记录，导致查询效率极低，同时对系统资源造成巨大压力。
PawSQL 对使用 CROSS JOIN 的语句进行风险提示，以避免其引发的性能问题。如果确实需要使用笛卡尔积，建议添加明确的注释说明业务意图。

## 反例

```sql
-- ❌ 不推荐：CROSS JOIN 产生笛卡尔积，数据量暴增
SELECT *
FROM lineitem
CROSS JOIN orders;
```

## 正例

```sql
-- ✅ 推荐：使用明确的 JOIN 条件进行关联
SELECT *
FROM lineitem l
JOIN orders o ON l.order_id = o.order_id;
```
