---
id: audit-rule-aud-default-value-required-for-timestamp-columns
title: 时间戳列需指定默认值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-default-value-required-for-timestamp-columns
tags:
- audit-rule
- ddl
description: 时间戳列（TIMESTAMP类型）必须指定默认值，以确保在没有显式插入时间戳值时，能够自动生成合理的默认时间（如`CURRENT_TIMESTAMP`）。未指定默认值的时间戳列在数据插入时可能被填入`NULL`或无效的零日期，导致后续的时间比较、排序和范围查询出现意外行为。
localeOf: en-audit-rule-aud-default-value-required-for-timestamp-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-default-value-required-for-timestamp-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-default-value-required-for-timestamp-columns |
| 规则名称 | 时间戳列需指定默认值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

时间戳列（TIMESTAMP类型）必须指定默认值，以确保在没有显式插入时间戳值时，能够自动生成合理的默认时间（如`CURRENT_TIMESTAMP`）。未指定默认值的时间戳列在数据插入时可能被填入`NULL`或无效的零日期，导致后续的时间比较、排序和范围查询出现意外行为。
在MySQL中，TIMESTAMP类型的列还具有自动更新特性（`ON UPDATE CURRENT_TIMESTAMP`），合理利用这一特性可以减少应用层的代码复杂度。该规则要求所有TIMESTAMP列在定义时必须指定非空的默认值。

## 反例

```sql
-- ❌ 不推荐：时间戳列缺少默认值，插入时可能产生异常数据
CREATE TABLE t (created_at TIMESTAMP);
```

## 正例

```sql
-- ✅ 推荐：显式指定时间戳默认值，自动填充当前时间
CREATE TABLE t (created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
```
