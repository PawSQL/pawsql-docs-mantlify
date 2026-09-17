---
id: audit-rule-aud-nonnull-default-value-required-for-nonexcluded-c
title: 非列表中的列应设置非空默认值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-nonnull-default-value-required-for-nonexcluded-c
tags:
- audit-rule
- ddl
description: 对于非大对象类型的列（即不在排除列表中的列），应设置非空默认值以确保数据的完整性。排除列表中的大对象类型（如 JSON、BJSON、XML、BLOB、CLOB、TEXT
  等）通常不适合设置默认值，但普通业务字段（如 INT、VARCHAR、DATE 等）如果没有默认值且被定义为 NOT NULL，会导致 INSERT 操作在不指定该列时直接报错，增加应用程序的错误处理负担。
localeOf: en-audit-rule-aud-nonnull-default-value-required-for-nonexcluded-c
subtype: rule
language: zh
translationKey: audit-rule-aud-nonnull-default-value-required-for-nonexcluded-c
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-nonnull-default-value-required-for-nonexcluded-c |
| 规则名称 | 非列表中的列应设置非空默认值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于非大对象类型的列（即不在排除列表中的列），应设置非空默认值以确保数据的完整性。排除列表中的大对象类型（如 JSON、BJSON、XML、BLOB、CLOB、TEXT 等）通常不适合设置默认值，但普通业务字段（如 INT、VARCHAR、DATE 等）如果没有默认值且被定义为 NOT NULL，会导致 INSERT 操作在不指定该列时直接报错，增加应用程序的错误处理负担。
为这些列设置合理的默认值，可以简化 INSERT 操作、保证数据的完整性，也使得数据库 Schema 更加健壮。默认值应根据业务语义来定义（如状态字段默认 0、时间字段默认当前时间等）。

## 反例

```sql
-- ❌ 不推荐：非大对象类型的列定义为 NOT NULL 但没有默认值
CREATE TABLE t (
    id INT NOT NULL,
    status INT NOT NULL
);
```

## 正例

```sql
-- ✅ 推荐：为 NOT NULL 列设置合理的默认值
CREATE TABLE t (
    id INT NOT NULL AUTO_INCREMENT,
    status INT NOT NULL DEFAULT 0
);
```
