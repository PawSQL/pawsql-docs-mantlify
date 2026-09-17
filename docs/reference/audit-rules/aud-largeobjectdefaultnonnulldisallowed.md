---
id: audit-rule-aud-largeobjectdefaultnonnulldisallowed
title: 禁止为列表中的列设置非空默认值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-largeobjectdefaultnonnulldisallowed
tags:
- audit-rule
- ddl
description: 禁止为 BLOB、CLOB、TEXT 等大对象类型的列设置非空默认值。大对象类型的数据通常体积庞大，为这类列设置非空默认值意味着即使业务未显式提供该字段的值，数据库也会为每一行填充默认的大对象数据，这会导致存储空间的严重浪费和写入性能的显著下降。在批量操作场景下，这种隐式的数据膨胀尤其危险，可能导致磁盘空间快速耗尽。
localeOf: en-audit-rule-aud-largeobjectdefaultnonnulldisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-largeobjectdefaultnonnulldisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-largeobjectdefaultnonnulldisallowed |
| 规则名称 | 禁止为列表中的列设置非空默认值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止为 BLOB、CLOB、TEXT 等大对象类型的列设置非空默认值。大对象类型的数据通常体积庞大，为这类列设置非空默认值意味着即使业务未显式提供该字段的值，数据库也会为每一行填充默认的大对象数据，这会导致存储空间的严重浪费和写入性能的显著下降。在批量操作场景下，这种隐式的数据膨胀尤其危险，可能导致磁盘空间快速耗尽。
正确做法是让大对象列允许 NULL（或设置合理的应用层默认值），由应用层在确实需要时显式写入数据。

## 反例

```sql
-- ❌ 不推荐：为大对象列设置非空默认值，导致存储膨胀
CREATE TABLE t (
    id INT NOT NULL,
    content TEXT NOT NULL DEFAULT 'placeholder content...'
);
```

## 正例

```sql
-- ✅ 推荐：大对象列允许 NULL，业务需要时再写入
CREATE TABLE t (
    id INT NOT NULL,
    content TEXT
);
```
