---
id: audit-rule-aud-default-value-required-for-time-columns
title: 时间列未设置默认值或默认值为空
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-default-value-required-for-time-columns
tags:
- audit-rule
- ddl
description: 时间列（DATE、DATETIME、TIMESTAMP类型）应当设置合理的默认值（如`CURRENT_TIMESTAMP`），以避免出现全为0的日期格式（如`0000-00-00
  00:00:00`）与业务预期不符。未设置默认值的时间列，在INSERT语句未显式提供该列值时，会被填入`NULL`或数据库系统默认的零值，这在业务逻辑中可能导致判断错误或显示异常。
localeOf: en-audit-rule-aud-default-value-required-for-time-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-default-value-required-for-time-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-default-value-required-for-time-columns |
| 规则名称 | 时间列未设置默认值或默认值为空 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

时间列（DATE、DATETIME、TIMESTAMP类型）应当设置合理的默认值（如`CURRENT_TIMESTAMP`），以避免出现全为0的日期格式（如`0000-00-00 00:00:00`）与业务预期不符。未设置默认值的时间列，在INSERT语句未显式提供该列值时，会被填入`NULL`或数据库系统默认的零值，这在业务逻辑中可能导致判断错误或显示异常。
该规则检查CREATE TABLE和ALTER TABLE ADD COLUMN语句中时间类型列的定义，确保时间列配置了非空的默认值。

## 反例

```sql
-- ❌ 不推荐：时间列未设置默认值，插入时可能产生零日期或NULL
CREATE TABLE event_log (
    id INT,
    event_time DATETIME
);
```

## 正例

```sql
-- ✅ 推荐：为时间列设置合理的默认值
CREATE TABLE event_log (
    id INT,
    event_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
