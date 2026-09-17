---
id: audit-rule-aud-userdefinedtypeudt-disallowed
title: 禁止创建自定义类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-userdefinedtypeudt-disallowed
tags:
- audit-rule
- ddl
description: 禁止创建自定义数据类型（UDT）。自定义类型维护性较差，依赖关系复杂且不透明，会导致 SQL 无法跨数据库无缝迁移，增加了数据库操作的复杂性和潜在的安全风险。自定义类型一旦被多个表引用，后续修改或删除将涉及大量下游对象的级联变更，风险极高。
localeOf: en-audit-rule-aud-userdefinedtypeudt-disallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-userdefinedtypeudt-disallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-userdefinedtypeudt-disallowed |
| 规则名称 | 禁止创建自定义类型 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止创建自定义数据类型（UDT）。自定义类型维护性较差，依赖关系复杂且不透明，会导致 SQL 无法跨数据库无缝迁移，增加了数据库操作的复杂性和潜在的安全风险。自定义类型一旦被多个表引用，后续修改或删除将涉及大量下游对象的级联变更，风险极高。
应使用 SQL 标准支持的内置数据类型来建模业务数据，将复杂类型抽象封装在应用层而非数据库层，以确保系统的可移植性和可维护性。

## 反例

```sql
-- ❌ 不推荐：自定义类型，迁移和维护困难
CREATE TYPE my_type AS ENUM ('a', 'b');
```

## 正例

```sql
-- ✅ 推荐：使用标准内置类型
CREATE TABLE t (
    category VARCHAR(20) NOT NULL
);
-- 枚举校验在应用层实现
```
