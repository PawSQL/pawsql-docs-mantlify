---
id: audit-rule-aud-diffdatatypesofricolumns
title: 主外键的数据类型不一致
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-diffdatatypesofricolumns
tags:
- audit-rule
- ddl
description: 主外键的数据类型必须保持一致，这是保障数据完整性和查询性能的重要约束。当主键和外键的数据类型不一致时，数据库在表关联（JOIN）操作中可能无法使用索引，导致全表扫描，严重降低查询性能。此外，类型不一致还可能导致隐式类型转换，引发数据截断、精度丢失或错误的比较结果。
localeOf: en-audit-rule-aud-diffdatatypesofricolumns
subtype: rule
language: zh
translationKey: audit-rule-aud-diffdatatypesofricolumns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-diffdatatypesofricolumns |
| 规则名称 | 主外键的数据类型不一致 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

主外键的数据类型必须保持一致，这是保障数据完整性和查询性能的重要约束。当主键和外键的数据类型不一致时，数据库在表关联（JOIN）操作中可能无法使用索引，导致全表扫描，严重降低查询性能。此外，类型不一致还可能导致隐式类型转换，引发数据截断、精度丢失或错误的比较结果。
合理的字段定义可以保证数据一致性、节省存储空间、避免隐式转换导致的性能问题。违反此规则的表结构可能在数据插入、更新或查询时出现意外行为。

## 反例

```sql
-- ❌ 不推荐：主外键数据类型不一致，可能导致索引失效
CREATE TABLE parent (
    id BIGINT PRIMARY KEY
);
CREATE TABLE child (
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES parent(id)
);
```

## 正例

```sql
-- ✅ 推荐：主外键数据类型保持一致
CREATE TABLE parent (
    id BIGINT PRIMARY KEY
);
CREATE TABLE child (
    parent_id BIGINT,
    FOREIGN KEY (parent_id) REFERENCES parent(id)
);
```
