---
id: audit-rule-aud-specific-character-set-required-for-database-cre
title: 创建库或模式时必须使用指定字符集
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-specific-character-set-required-for-database-cre
tags:
- audit-rule
- ddl
description: 要求在创建数据库或模式时使用指定的字符集，以确保数据的一致性和跨环境兼容性。如果未使用规定的字符集，可能导致不同环境之间的字符编码不一致，引发乱码、数据截断或索引失效等问题。
localeOf: en-audit-rule-aud-specific-character-set-required-for-database-cre
subtype: rule
language: zh
translationKey: audit-rule-aud-specific-character-set-required-for-database-cre
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-specific-character-set-required-for-database-cre |
| 规则名称 | 创建库或模式时必须使用指定字符集 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求在创建数据库或模式时使用指定的字符集，以确保数据的一致性和跨环境兼容性。如果未使用规定的字符集，可能导致不同环境之间的字符编码不一致，引发乱码、数据截断或索引失效等问题。
通过配置指定字符集（如 `utf8mb4`），可以强制所有环境使用统一的字符编码标准，从源头上杜绝字符集不一致带来的各类问题。

## 反例

```sql
-- ❌ 不推荐：未使用指定的字符集
CREATE DATABASE mydb CHARACTER SET latin1;
```

## 正例

```sql
-- ✅ 推荐：使用指定的字符集 utf8mb4
CREATE DATABASE mydb DEFAULT CHARACTER SET utf8mb4;
```
