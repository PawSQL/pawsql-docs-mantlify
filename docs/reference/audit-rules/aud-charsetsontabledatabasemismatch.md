---
id: audit-rule-aud-charsetsontabledatabasemismatch
title: 表的字符集和数据库不一致
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 要求表的字符集必须与数据库的字符集保持一致，以避免字符集不一致导致的数据问题。当表的字符集与数据库字符集不同时，跨表查询或数据迁移可能触发隐式字符集转换，增加
  CPU 开销、影响索引使用效率，严重时还可能导致乱码和数据丢失。
localeOf: en-audit-rule-aud-charsetsontabledatabasemismatch
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-charsetsontabledatabasemismatch |
| 规则名称 | 表的字符集和数据库不一致 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

要求表的字符集必须与数据库的字符集保持一致，以避免字符集不一致导致的数据问题。当表的字符集与数据库字符集不同时，跨表查询或数据迁移可能触发隐式字符集转换，增加 CPU 开销、影响索引使用效率，严重时还可能导致乱码和数据丢失。
建议在创建表时不指定字符集，使其自动继承数据库的默认字符集。如果必须指定，应确保与数据库完全一致。

## 反例

```sql
-- ❌ 不推荐：表的字符集与数据库不一致
-- 假设数据库字符集为 utf8mb4
CREATE TABLE t (id INT) DEFAULT CHARSET = latin1;
```

## 正例

```sql
-- ✅ 推荐：表继承数据库默认字符集，保持一致
CREATE TABLE t (id INT);
```
