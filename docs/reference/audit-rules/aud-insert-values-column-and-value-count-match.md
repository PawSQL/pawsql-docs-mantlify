---
id: audit-rule-aud-insert-values-column-and-value-count-match
title: INSERT...VALUES列和值数量一致
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-insert-values-column-and-value-count-match
tags:
- audit-rule
- dml
description: '`INSERT INTO ... VALUES` 语句根据列的声明顺序与值的排列顺序建立对应关系。如果显式指定的列数量与 VALUES
  中提供的值的数量不一致，说明 SQL 语句存在语法错误或逻辑错误，将无法正确执行。这是一种基本的 SQL 正确性约束。'
localeOf: en-audit-rule-aud-insert-values-column-and-value-count-match
subtype: rule
language: zh
translationKey: audit-rule-aud-insert-values-column-and-value-count-match
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-insert-values-column-and-value-count-match |
| 规则名称 | INSERT...VALUES列和值数量一致 |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`INSERT INTO ... VALUES` 语句根据列的声明顺序与值的排列顺序建立对应关系。如果显式指定的列数量与 VALUES 中提供的值的数量不一致，说明 SQL 语句存在语法错误或逻辑错误，将无法正确执行。这是一种基本的 SQL 正确性约束。
此规则在 PawSQL 中被归类为禁止级别规则，检测到列值数量不匹配时直接拦截，防止错误 SQL 进入生产环境。

## 反例

```sql
-- ❌ 禁止：列数（2）与值数（1）不匹配
INSERT INTO t (a, b) VALUES (1);
```

## 正例

```sql
-- ✅ 推荐：列数与值数一致
INSERT INTO t (a, b) VALUES (1, 2);
```
