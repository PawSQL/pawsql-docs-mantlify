---
id: audit-rule-aud-implicit-type-conversion-causes-index-invalidati
title: 隐式类型转换导致索引失效
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-implicit-type-conversion-causes-index-invalidati
tags:
- audit-rule
- index
description: 当 WHERE 条件表达式中字段和常量的数据类型不同时，数据库在查询执行过程中会进行隐式的数据类型转换。类型转换的规则取决于数据库的实现：有时转换会应用于常量侧（对性能无影响），有时转换会应用于字段列侧。当类型转换落在列上时，该列上的索引将无法被使用，查询退化为全表扫描，可能导致严重的性能问题。
localeOf: en-audit-rule-aud-implicit-type-conversion-causes-index-invalidati
subtype: rule
language: zh
translationKey: audit-rule-aud-implicit-type-conversion-causes-index-invalidati
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-implicit-type-conversion-causes-index-invalidati |
| 规则名称 | 隐式类型转换导致索引失效 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当 WHERE 条件表达式中字段和常量的数据类型不同时，数据库在查询执行过程中会进行隐式的数据类型转换。类型转换的规则取决于数据库的实现：有时转换会应用于常量侧（对性能无影响），有时转换会应用于字段列侧。当类型转换落在列上时，该列上的索引将无法被使用，查询退化为全表扫描，可能导致严重的性能问题。
例如，如果 `O_ORDERDATE` 列的数据类型是 `CHAR(16)`，查询条件 `WHERE O_ORDERDATE = current_date()` 会导致对 `O_ORDERDATE` 列进行隐式转换，使其索引失效。解决方案通常有两个：一是通过 `ALTER TABLE` 修改列的数据类型以匹配查询模式；二是在查询中对常量进行显式类型转换（`WHERE O_ORDERDATE = CAST(current_date() AS CHAR(16))`），使转换落在常量侧而非列侧。PawSQL 可提供此类重写建议。

## 反例

```sql
-- ❌ 不推荐：字段与常量类型不匹配，隐式转换落在列上导致索引失效
SELECT count(*) FROM ORDERS WHERE O_ORDERDATE = current_date();
-- 假设 O_ORDERDATE 为 CHAR(16)，列上的索引无法使用
```

## 正例

```sql
-- ✅ 推荐方案1：对常量进行显式类型转换，保留索引可用性
SELECT count(*) FROM ORDERS WHERE O_ORDERDATE = CAST(current_date() AS CHAR(16));

-- ✅ 推荐方案2：修改列数据类型以匹配查询模式
-- ALTER TABLE ORDERS MODIFY O_ORDERDATE DATE;
```
