---
id: optimizer-rule-opt-npe-rewrite
title: NPE 重写（空指针异常预防）
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-npe-rewrite
tags:
- optimizer-rule
- rewrite
description: 当聚合输入全为 NULL 时 SUM/AVG 返回 NULL 可能引发程序 NPE；自动用空值处理函数包装聚合，保证返回数值。
localeOf: en-optimizer-rule-opt-npe-rewrite
subtype: rule
language: zh
translationKey: optimizer-rule-opt-npe-rewrite
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-npe-rewrite |
| 规则名称 | NPE 重写（空指针异常预防） |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

SQL 中的 NPE（Null Pointer Exception）问题是指当聚合列全为 NULL 时，SUM、AVG 等聚合函数会返回 NULL 而非数字零。如果后续应用程序（如 Java、Python）直接将 SQL 返回的 NULL 值用于数值运算，就可能触发空指针异常。PawSQL 自动检测此类场景，将聚合函数包装在空值处理函数中（如 IFNULL(SUM(col), 0)），确保聚合结果始终返回数值型结果，避免应用程序端的 NPE 问题。

## 如何修复

把聚合函数包进数据库的空值处理函数，使全 NULL 时返回 0 而非 NULL：Oracle 使用 NVL()，SQL Server 使用 ISNULL()，MySQL 使用 IFNULL() 或 COALESCE()；COALESCE() 在各数据库通用。

## 反例

```sql
-- 不推荐：聚合列全为 NULL 时，SUM 返回 NULL，可能导致程序 NPE
SELECT SUM(t.b) FROM (VALUES ROW(1, NULL)) AS t(a, b);
```

## 正例

```sql
-- 推荐：使用空值处理函数，确保返回 0 而非 NULL
SELECT IFNULL(SUM(t.b), 0) FROM (VALUES ROW(1, NULL)) AS t(a, b);
-- Oracle 写法：SELECT NVL(SUM(t.b), 0) FROM ...;
-- SQL Server 写法：SELECT ISNULL(SUM(t.b), 0) FROM ...;
-- 通用写法（所有数据库适用）：SELECT COALESCE(SUM(t.b), 0) FROM ...;
```
