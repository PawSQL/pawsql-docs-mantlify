---
id: audit-rule-aud-use-instead-of
title: 建议使用'<>'代替'!='
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-instead-of
tags:
- audit-rule
- dml
description: '`!=` 是非标准的SQL运算符，`<>` 才是SQL标准中定义的不等于运算符。虽然大多数数据库同时支持两种写法，但为了提升SQL代码的可移植性和规范程度，建议统一使用`<>`代替`!=`。'
localeOf: en-audit-rule-aud-use-instead-of
subtype: rule
language: zh
translationKey: audit-rule-aud-use-instead-of
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-instead-of |
| 规则名称 | 建议使用'<>'代替'!=' |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`!=` 是非标准的SQL运算符，`<>` 才是SQL标准中定义的不等于运算符。虽然大多数数据库同时支持两种写法，但为了提升SQL代码的可移植性和规范程度，建议统一使用`<>`代替`!=`。
在某些数据库系统或特定的SQL模式中，`!=`可能不被支持或具有不同的语义。统一使用标准运算符可以避免在不同数据库之间迁移时出现兼容性问题。

## 反例

```sql
-- ❌ 不推荐：使用非标准的 != 运算符
SELECT * FROM t WHERE col != 1;
```

## 正例

```sql
-- ✅ 推荐：使用标准的 <> 不等于运算符
SELECT * FROM t WHERE col <> 1;
```
