---
id: optimizer-rule-opt-derived-table-to-lateral-join-conversion
title: 派生表转换为Lateral表关联
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-derived-table-to-lateral-join-conversion
tags:
- optimizer-rule
- rewrite
description: 当派生表（Derived Table）中包含窗口函数（如 `ROW_NUMBER()` + `PARTITION BY`）或分组聚合后再通过外层条件过滤时，传统写法会先生成完整的中间结果集再进行过滤，导致大量不必要的计算。例如对全表先计算窗口函数生成百万级的临时结果集，然后取前
  N 条记录——绝大多数计算都是无效的。
localeOf: en-optimizer-rule-opt-derived-table-to-lateral-join-conversion
subtype: rule
language: zh
translationKey: optimizer-rule-opt-derived-table-to-lateral-join-conversion
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-derived-table-to-lateral-join-conversion |
| 规则名称 | 派生表转换为Lateral表关联 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当派生表（Derived Table）中包含窗口函数（如 `ROW_NUMBER()` + `PARTITION BY`）或分组聚合后再通过外层条件过滤时，传统写法会先生成完整的中间结果集再进行过滤，导致大量不必要的计算。例如对全表先计算窗口函数生成百万级的临时结果集，然后取前 N 条记录——绝大多数计算都是无效的。
通过 `LATERAL JOIN` 改写，可以将外层过滤条件"下压"到派生表内部按需逐行计算，数据库仅处理与当前驱动行相关的数据。在 Top-N 查询场景中，LATERAL JOIN 配合 `ORDER BY + LIMIT` 可实现 10-60 倍的性能提升。

## 反例

```sql
-- ❌ 不推荐：窗口函数 + 派生表全量计算，再过滤 Top-N
SELECT *
FROM (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rn
    FROM employee
) t
WHERE t.rn <= 3;
```

## 正例

```sql
-- ✅ 推荐：LATERAL JOIN 按需计算，仅处理每个部门的前 3 条
SELECT d.dept_name, t.*
FROM department d,
     LATERAL (
         SELECT *
         FROM employee
         WHERE dept_id = d.id
         ORDER BY salary DESC
         LIMIT 3
     ) t;
```
