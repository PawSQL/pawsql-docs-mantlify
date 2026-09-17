---
id: audit-rule-aud-object-name-length-must-not-exceed-threshold
title: 对象名称长度不得超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-object-name-length-must-not-exceed-threshold
tags:
- audit-rule
- ddl
description: 限制数据库对象名称的长度是为了确保符合数据库的命名规则，同时便于代码维护和阅读。过长的对象名称（如表名、索引名、视图名等）不仅会降低代码可读性，还可能导致一些数据库系统因内部限制而截断名称，引发难以排查的问题。此外，过长的索引名和约束名在某些数据库中可能突破系统长度限制，导致DDL执行失败。
localeOf: en-audit-rule-aud-object-name-length-must-not-exceed-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-object-name-length-must-not-exceed-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-object-name-length-must-not-exceed-threshold |
| 规则名称 | 对象名称长度不得超过阈值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

限制数据库对象名称的长度是为了确保符合数据库的命名规则，同时便于代码维护和阅读。过长的对象名称（如表名、索引名、视图名等）不仅会降低代码可读性，还可能导致一些数据库系统因内部限制而截断名称，引发难以排查的问题。此外，过长的索引名和约束名在某些数据库中可能突破系统长度限制，导致DDL执行失败。
该规则检查所有DDL语句中创建或修改的对象名称长度是否超过预设阈值（默认64个字符）。

## 反例

```sql
-- ❌ 不推荐：对象名称超长，可读性差且可能突破数据库限制
CREATE TABLE this_is_a_very_long_table_name_that_exceeds_limit (id INT);
```

## 正例

```sql
-- ✅ 推荐：对象名称简洁明确，符合长度规范
CREATE TABLE user_profile (id INT);
```
