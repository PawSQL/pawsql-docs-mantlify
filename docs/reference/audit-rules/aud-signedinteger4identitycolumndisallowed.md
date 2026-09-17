---
id: audit-rule-aud-signedinteger4identitycolumndisallowed
title: 自增列不得使用有符号整数
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-signedinteger4identitycolumndisallowed
tags:
- audit-rule
- ddl
description: 禁止在自增列中使用有符号整数类型（如 `INT`、`BIGINT` 未加 `UNSIGNED` 修饰），自增列的值永远是正数，使用有符号类型会浪费一半的取值空间。例如有符号
  `INT` 的取值范围约为正负 21 亿，而 `INT UNSIGNED` 可提供约 42 亿的正数范围。
localeOf: en-audit-rule-aud-signedinteger4identitycolumndisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-signedinteger4identitycolumndisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-signedinteger4identitycolumndisallowed |
| 规则名称 | 自增列不得使用有符号整数 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止在自增列中使用有符号整数类型（如 `INT`、`BIGINT` 未加 `UNSIGNED` 修饰），自增列的值永远是正数，使用有符号类型会浪费一半的取值空间。例如有符号 `INT` 的取值范围约为正负 21 亿，而 `INT UNSIGNED` 可提供约 42 亿的正数范围。
对于作为主键的自增列，更大的取值范围意味着更晚触发序列耗尽，有助于系统的长期稳定运行。建议自增列统一使用 `UNSIGNED` 修饰。

## 反例

```sql
-- ❌ 不推荐：自增列使用有符号整数，浪费一半取值范围
CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY);
```

## 正例

```sql
-- ✅ 推荐：自增列使用无符号整数
CREATE TABLE t (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY);
```
