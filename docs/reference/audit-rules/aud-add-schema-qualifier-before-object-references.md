---
id: audit-rule-aud-add-schema-qualifier-before-object-references
title: 对象前需添加属主
type: reference
status: draft
tags:
- audit-rule
- dml
description: SQL 引用对象前加 Schema/属主限定（schema.object），避免跨 Schema/多租户下同名对象歧义与误引用。
localeOf: en-audit-rule-aud-add-schema-qualifier-before-object-references
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-add-schema-qualifier-before-object-references |
| 规则名称 | 对象前需添加属主 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 所有支持数据库 |

## 说明

在进行SQL开发时，为每一个引用的数据库对象添加其所属的Schema/Owner标识（即使用`schema.object`的完整限定名），可以提升SQL语句的可读性以及后期的可维护性。这种做法使代码审查者能够快速确定每个对象的来源，避免因不同的Schema中存在同名对象而导致的歧义或错误引用。
缺少属主前缀的SQL语句，在跨Schema访问或多租户环境下特别容易出现问题——查询可能意外访问到错误的Schema中的同名表或视图。

## 反例

```sql
-- ❌ 不推荐：未指定Schema，在跨Schema环境中可能引用错误表
SELECT * FROM my_table;
```

## 正例

```sql
-- ✅ 推荐：使用 schema.table 完整限定名，明确对象来源
SELECT * FROM mydb.my_table;
```
