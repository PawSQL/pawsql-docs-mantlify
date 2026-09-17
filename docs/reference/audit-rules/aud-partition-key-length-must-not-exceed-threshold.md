---
id: audit-rule-aud-partition-key-length-must-not-exceed-threshold
title: 分区键的长度不得超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-partition-key-length-must-not-exceed-threshold
tags:
- audit-rule
- ddl
description: 如果使用 `CHAR` 或 `VARCHAR` 类型的字段作为分区键，过长的字段值会增加分区计算和哈希路由的成本，并可能导致分区元数据和索引过大，影响分区管理的效率。
localeOf: en-audit-rule-aud-partition-key-length-must-not-exceed-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-partition-key-length-must-not-exceed-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-partition-key-length-must-not-exceed-threshold |
| 规则名称 | 分区键的长度不得超过阈值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

如果使用 `CHAR` 或 `VARCHAR` 类型的字段作为分区键，过长的字段值会增加分区计算和哈希路由的成本，并可能导致分区元数据和索引过大，影响分区管理的效率。
建议分区键的字符串长度不超过 255 个字符。对于更长的字符串值，可以考虑使用其哈希值或更短的业务标识作为分区键。

## 反例

```sql
-- ❌ 不推荐：分区键字段长度超过 255 字符
CREATE TABLE customers (
    id        BIGINT,
    city_name VARCHAR(500),
    PRIMARY KEY (id, city_name)
) PARTITION BY LIST COLUMNS (city_name) (
    PARTITION p_beijing VALUES IN ('Beijing'),
    PARTITION p_shanghai VALUES IN ('Shanghai')
);
```

## 正例

```sql
-- ✅ 推荐：分区键字段长度不超过阈值
CREATE TABLE customers (
    id        BIGINT,
    city_name VARCHAR(100),
    PRIMARY KEY (id, city_name)
) PARTITION BY LIST COLUMNS (city_name) (
    PARTITION p_beijing VALUES IN ('Beijing'),
    PARTITION p_shanghai VALUES IN ('Shanghai')
);
```
