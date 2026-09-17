---
id: audit-rule-aud-datatypesdisallowed
title: 禁止使用的数据类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-datatypesdisallowed
tags:
- audit-rule
- ddl
description: 禁止使用某些存在潜在正确性、安全性或性能问题的数据类型。某些数据类型（如 JSON、XML、BJSON）虽然在某些场景下提供了便利的存储方式，但它们的查询优化能力有限，索引支持不完善，且在不同数据库间的兼容性和移植性差。使用这些类型可能导致查询性能退化、数据一致性问题以及数据库迁移困难。
localeOf: en-audit-rule-aud-datatypesdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-datatypesdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-datatypesdisallowed |
| 规则名称 | 禁止使用的数据类型 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用某些存在潜在正确性、安全性或性能问题的数据类型。某些数据类型（如 JSON、XML、BJSON）虽然在某些场景下提供了便利的存储方式，但它们的查询优化能力有限，索引支持不完善，且在不同数据库间的兼容性和移植性差。使用这些类型可能导致查询性能退化、数据一致性问题以及数据库迁移困难。
推荐使用标准的关系型数据类型（如 `VARCHAR`、`INT`、`DECIMAL` 等）存储结构化数据，将复杂嵌套数据的处理逻辑保留在应用层。

## 反例

```sql
-- ❌ 不推荐：使用 JSON/XML 等非标准数据类型
CREATE TABLE t (
    id INT,
    data JSON
);
```

## 正例

```sql
-- ✅ 推荐：使用标准关系型数据类型
CREATE TABLE t (
    id INT,
    data TEXT,
    data_type VARCHAR(20)
);
```
