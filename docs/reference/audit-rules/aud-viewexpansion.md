---
id: audit-rule-aud-viewexpansion
title: 视图展开
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-viewexpansion
tags:
- audit-rule
- dml
description: 视图展开是指将查询中引用的视图替换为其定义体（子查询）的过程。这种优化技术可以让查询优化器（包括 PawSQL 优化引擎和数据库优化器）获得更多的优化机会，例如谓词下推、连接消除和索引选择，从而可能产生更高效的执行计划。
localeOf: en-audit-rule-aud-viewexpansion
subtype: rule
language: zh
translationKey: audit-rule-aud-viewexpansion
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-viewexpansion |
| 规则名称 | 视图展开 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

视图展开是指将查询中引用的视图替换为其定义体（子查询）的过程。这种优化技术可以让查询优化器（包括 PawSQL 优化引擎和数据库优化器）获得更多的优化机会，例如谓词下推、连接消除和索引选择，从而可能产生更高效的执行计划。
当查询直接引用视图时，优化器的优化范围受限于视图的边界；将视图展开后，外层 WHERE 条件可以直接穿透到基表，利用基表上的索引和统计信息，显著提升执行效率。

## 反例

```sql
-- ❌ 可优化：视图引用阻碍了谓词下推等优化
SELECT h.name, d.department_name
FROM high_salary_employees h
JOIN departments d ON h.department_id = d.department_id
WHERE h.employee_id < 1000;
```

## 正例

```sql
-- ✅ 优化后：视图展开为子查询，外层条件可与内层合并优化
SELECT h.name, d.department_name
FROM (
    SELECT employee_id, name, department_id
    FROM employees
    WHERE salary > 50000
) h
JOIN departments d ON h.department_id = d.department_id
WHERE h.employee_id < 1000;
```
