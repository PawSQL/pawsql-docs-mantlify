---
id: audit-rule-aud-order-by-forbidden-in-dml
title: UPDATE/DELETE 禁止使用 ORDER 子句
type: reference
status: draft
tags:
- audit-rule
- dml
description: UPDATE/DELETE 中 ORDER BY 无意义且增加开销，某些数据库甚至是语法错误；应移除或将排序放进子查询。
localeOf: en-audit-rule-aud-order-by-forbidden-in-dml
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-order-by-forbidden-in-dml |
| 规则名称 | UPDATE/DELETE 禁止使用 ORDER 子句 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

在 UPDATE 或 DELETE 语句中使用 ORDER BY 子句通常没有实际意义。DML 操作的目标是变更数据，而非返回有序结果集。ORDER BY 在 DML 中不仅增加了不必要的排序开销，还可能导致执行计划变差。在 PostgreSQL 等数据库中，DELETE ... ORDER BY 甚至是语法错误（除非配合 LIMIT），直接使用将导致执行失败。

## 如何修复

移除 DML 语句中无意义的 ORDER BY。若确实需要按某种顺序取出部分行执行 DML（如取前 N 条），把排序放进子查询，再用 WHERE IN (...) 驱动更新或删除。

## 反例

```sql
-- 不推荐：DELETE/UPDATE 中使用 ORDER BY 无意义
DELETE FROM t ORDER BY id LIMIT 10;
UPDATE t SET status = 1 ORDER BY created_at;
```

## 正例

```sql
-- 推荐：在子查询中排序选取目标行，再执行 DML
DELETE FROM t WHERE id IN (SELECT id FROM t ORDER BY id LIMIT 10);
UPDATE t SET status = 1 WHERE id IN (
    SELECT id FROM t WHERE status = 0 ORDER BY created_at LIMIT 100
);
```
