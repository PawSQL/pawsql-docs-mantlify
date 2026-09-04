---
id: audit-rule-aud-avoid-leading-or-trailing-spaces-in-string-liter
title: 避免常量字符串开头或结尾包含空格
type: reference
status: draft
tags:
- audit-rule
- dml
description: 字符串常量首尾空格多为误输入却影响匹配结果；应清理，确需匹配空格时用 TRIM 或注释说明。
localeOf: en-audit-rule-aud-avoid-leading-or-trailing-spaces-in-string-liter
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-leading-or-trailing-spaces-in-string-liter |
| 规则名称 | 避免常量字符串开头或结尾包含空格 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

在 SQL 中，字符串常量开头或结尾的空格通常不具有实际的业务意义。这类情况往往是由于开发人员的误输入导致的（例如从文档中复制粘贴时多带了前后空格），但它可能直接影响 SQL 查询的结果——`WHERE name = ' test '` 和 `WHERE name = 'test'` 会匹配到不同的数据。
开发者应特别关注此类预警，检查字符串常量的前后空格是否为有意为之。如果是误输入，应及时清理；如果确实需要匹配带空格的数据，建议使用 `TRIM()` 函数或添加注释说明意图。

## 反例

```sql
-- ❌ 不推荐：字符串常量包含首尾空格，可能是误输入
SELECT * FROM t WHERE name = ' test ';
```

## 正例

```sql
-- ✅ 推荐：去除无意义的空格
SELECT * FROM t WHERE name = 'test';

-- 如果确实需要匹配含空格的数据，使用 TRIM 或显式注明意图
SELECT * FROM t WHERE TRIM(name) = 'test';
```
