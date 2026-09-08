---
id: audit-rule-aud-avoid-scalar-subqueries
title: 避免使用标量子查询
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-scalar-subqueries
tags:
- audit-rule
- dml
description: 避免标量子查询（外层每行执行一次、大表性能差、可能运行时多行报错）；用 JOIN/派生表替代。
localeOf: en-audit-rule-aud-avoid-scalar-subqueries
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-scalar-subqueries
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-scalar-subqueries |
| 规则名称 | 避免使用标量子查询 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

标量子查询返回单行单列的值，它可以出现在 SQL 中任何单值出现的地方。标量子查询通常与外部查询相关联（相关子查询），数据库在运行时需要为每一行外查询的结果执行一次子查询，这种"逐行执行"的模式在大数据量场景下性能极差。此外，标量子查询在运行时才能确定是否只返回单行值，如果意外返回多行，还会导致运行时错误。
建议尽可能使用 JOIN 或派生表来替代标量子查询，使优化器能够在一次批量操作中完成计算。PawSQL 会对标量子查询进行识别并在可行时自动提供重写建议。

## 反例

```sql
-- ❌ 不推荐：选择列表中的标量子查询，外层每行执行一次子查询
SELECT id, (SELECT COUNT(*) FROM orders o WHERE o.user_id = u.id) AS cnt FROM user u;
```

## 正例

```sql
-- ✅ 推荐：使用 LEFT JOIN + GROUP BY 替代标量子查询
SELECT u.id, COUNT(o.id) AS cnt
FROM user u
LEFT JOIN orders o ON o.user_id = u.id
GROUP BY u.id;
```
