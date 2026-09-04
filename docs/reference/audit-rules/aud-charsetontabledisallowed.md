---
id: audit-rule-aud-charsetontabledisallowed
title: 表定义时禁止使用字符集
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止在表定义时单独指定字符集，以避免表级字符集与数据库级字符集不一致导致的数据问题。当表字符集与数据库字符集不同时，跨表操作可能触发隐式字符集转换，影响查询性能并可能导致乱码。
localeOf: en-audit-rule-aud-charsetontabledisallowed
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-charsetontabledisallowed |
| 规则名称 | 表定义时禁止使用字符集 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

禁止在表定义时单独指定字符集，以避免表级字符集与数据库级字符集不一致导致的数据问题。当表字符集与数据库字符集不同时，跨表操作可能触发隐式字符集转换，影响查询性能并可能导致乱码。
字符集应在数据库级别（或列级别）统一管理，表应继承数据库的默认字符集，避免在表级覆盖设置。

## 反例

```sql
-- ❌ 不推荐：表定义时指定了字符集，可能与数据库不一致
CREATE TABLE t (id INT) DEFAULT CHARSET = utf8;
```

## 正例

```sql
-- ✅ 推荐：表继承数据库默认字符集，不在表级单独指定
CREATE TABLE t (id INT);
```
