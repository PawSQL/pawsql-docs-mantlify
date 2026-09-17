---
id: audit-rule-aud-datatypelimitofprimarykey
title: 主键列的数据类型限制
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-datatypelimitofprimarykey
tags:
- audit-rule
- ddl
description: 主键列的数据类型应当受到限制，通常推荐使用整数类型（如 `unsigned int` 或 `unsigned bigint`），以优化索引效率和查询性能。过大的数据类型（如字符串或复合类型）会增加主键索引的存储空间，降低索引扫描速度，并影响基于主键的关联操作性能。
localeOf: en-audit-rule-aud-datatypelimitofprimarykey
subtype: rule
language: zh
translationKey: audit-rule-aud-datatypelimitofprimarykey
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-datatypelimitofprimarykey |
| 规则名称 | 主键列的数据类型限制 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

主键列的数据类型应当受到限制，通常推荐使用整数类型（如 `unsigned int` 或 `unsigned bigint`），以优化索引效率和查询性能。过大的数据类型（如字符串或复合类型）会增加主键索引的存储空间，降低索引扫描速度，并影响基于主键的关联操作性能。
选择合适的主键数据类型可以减少存储空间，提高索引效率，避免不必要的类型转换和性能开销。

## 反例

```sql
-- ❌ 不推荐：主键使用非推荐的数据类型
CREATE TABLE orders (
    order_id VARCHAR(64) PRIMARY KEY,
    details  TEXT
);
```

## 正例

```sql
-- ✅ 推荐：主键使用无符号整数类型
CREATE TABLE orders (
    order_id BIGINT UNSIGNED PRIMARY KEY,
    details  TEXT
);
```
