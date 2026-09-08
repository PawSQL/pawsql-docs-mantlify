---
id: audit-rule-aud-insert-must-include-pk
title: INSERT 语句必须包含主键字段
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-insert-must-include-pk
tags:
- audit-rule
- dml
description: 对无自增主键的表，INSERT 必须显式包含主键列并提供明确的值，避免主键冲突与数据不一致。
localeOf: en-audit-rule-aud-insert-must-include-pk
subtype: rule
language: zh
translationKey: audit-rule-aud-insert-must-include-pk
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-insert-must-include-pk |
| 规则名称 | INSERT 语句必须包含主键字段 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于没有自增主键的表，插入数据时应当显式指定主键的值。即使主键字段定义了默认值，省略主键字段也可能导致默认值重复或不符合业务预期。在生产环境中，缺失主键值的 INSERT 语句可能导致主键冲突或数据不一致问题。

## 如何修复

在 INSERT 列清单中显式包含主键字段并提供明确的值。

## 反例

```sql
-- 不推荐：表有非自增主键，但 INSERT 未包含主键字段
INSERT INTO user (name) VALUES ('张三');
```

## 正例

```sql
-- 推荐：显式指定主键字段的值
INSERT INTO user (id, name) VALUES (1, '张三');
```
