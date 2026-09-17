---
id: audit-rule-aud-insert-values-must-specify-column-names
title: INSERT...VALUES应该指定列名
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-insert-values-must-specify-column-names
tags:
- audit-rule
- dml
description: '`INSERT INTO ... VALUES` 语句应当显式指定列名列表。如果不指定列名，则值的顺序必须与表中列的物理顺序完全一致。当表结构发生变更（如添加、删除或重排列）时，未指定列名的
  INSERT 语句可能将数据写入错误的列，造成严重的数据错误且难以排查。'
localeOf: en-audit-rule-aud-insert-values-must-specify-column-names
subtype: rule
language: zh
translationKey: audit-rule-aud-insert-values-must-specify-column-names
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-insert-values-must-specify-column-names |
| 规则名称 | INSERT...VALUES应该指定列名 |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`INSERT INTO ... VALUES` 语句应当显式指定列名列表。如果不指定列名，则值的顺序必须与表中列的物理顺序完全一致。当表结构发生变更（如添加、删除或重排列）时，未指定列名的 INSERT 语句可能将数据写入错误的列，造成严重的数据错误且难以排查。
显式指定列名可以提高代码的可维护性和健壮性，使插入语句不依赖于表结构的列顺序，即使表结构发生变化，只要列名不变，插入逻辑就不会出错。

## 反例

```sql
-- ❌ 不推荐：未指定列名，依赖表中列的顺序
INSERT INTO customer VALUES (1, 'Dan', 'Mike');
```

## 正例

```sql
-- ✅ 推荐：显式指定列名，不依赖列的顺序
INSERT INTO customer (c_custkey, lastname, firstName) VALUES (1, 'Dan', 'Mike');
```
