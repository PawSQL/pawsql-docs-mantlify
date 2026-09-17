---
id: audit-rule-aud-distribution-key-data-type-restriction
title: 分布键的数据类型限制
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-distribution-key-data-type-restriction
tags:
- audit-rule
- ddl
description: 分布键（Shardkey）的数据类型有明确的限制，只能为 `int`、`bigint`、`smallint`、`char`、`varchar`
  这五种类型。使用不兼容的数据类型（如 `DATE`、`FLOAT`、`TEXT`、`BLOB` 等）作为分布键会导致建表失败或路由异常。
localeOf: en-audit-rule-aud-distribution-key-data-type-restriction
subtype: rule
language: zh
translationKey: audit-rule-aud-distribution-key-data-type-restriction
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-distribution-key-data-type-restriction |
| 规则名称 | 分布键的数据类型限制 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

分布键（Shardkey）的数据类型有明确的限制，只能为 `int`、`bigint`、`smallint`、`char`、`varchar` 这五种类型。使用不兼容的数据类型（如 `DATE`、`FLOAT`、`TEXT`、`BLOB` 等）作为分布键会导致建表失败或路由异常。
选择正确且简洁的分布键数据类型，可以减少哈希计算和路由判定的开销，确保分布式数据库的高效运行。

## 反例

```sql
-- ❌ 不推荐：使用不兼容的数据类型（如 DATE）作为分布键
CREATE TABLE t_order (
    date_col DATE,
    amount   DECIMAL(10, 2)
) shardkey = date_col;
```

## 正例

```sql
-- ✅ 推荐：使用兼容的数据类型（如 BIGINT）作为分布键
CREATE TABLE t_order (
    id       BIGINT,
    date_col DATE,
    amount   DECIMAL(10, 2)
) shardkey = id;
```
