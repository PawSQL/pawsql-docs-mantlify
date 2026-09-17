---
id: audit-rule-aud-use-int10-or-bigint20-for-integer-columns
title: 整型建议采用 INT(10) 或 BIGINT(20)
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-int10-or-bigint20-for-integer-columns
tags:
- audit-rule
- ddl
description: 在MySQL等数据库中，整型列定义时建议显式指定显示宽度。使用`INT(10)`和`BIGINT(20)`是推荐的标准写法，能够确保整数类型的显示宽度一致，避免在不同客户端或应用程序中出现格式化差异。虽然显示宽度不影响存储范围，但它影响某些客户端（如MySQL命令行）的数据展示效果，统一规范有助于减少视觉歧义。
localeOf: en-audit-rule-aud-use-int10-or-bigint20-for-integer-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-use-int10-or-bigint20-for-integer-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-int10-or-bigint20-for-integer-columns |
| 规则名称 | 整型建议采用 INT(10) 或 BIGINT(20) |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在MySQL等数据库中，整型列定义时建议显式指定显示宽度。使用`INT(10)`和`BIGINT(20)`是推荐的标准写法，能够确保整数类型的显示宽度一致，避免在不同客户端或应用程序中出现格式化差异。虽然显示宽度不影响存储范围，但它影响某些客户端（如MySQL命令行）的数据展示效果，统一规范有助于减少视觉歧义。
该规则检查CREATE TABLE和ALTER TABLE中整型列的定义，要求使用`INT(10)`或`BIGINT(20)`格式，而不是无显示宽度的`INT`或`BIGINT`。

## 反例

```sql
-- ❌ 不推荐：整数列定义缺少显示宽度
CREATE TABLE t (count INTEGER);
```

## 正例

```sql
-- ✅ 推荐：显式指定显示宽度，格式统一规范
CREATE TABLE t (count INT(10));
```
