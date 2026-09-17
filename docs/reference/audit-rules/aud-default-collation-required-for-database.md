---
id: audit-rule-aud-default-collation-required-for-database
title: 数据库需指定默认排序规则（Collate）
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-default-collation-required-for-database
tags:
- audit-rule
- ddl
description: 要求在创建数据库时显式指定默认的排序规则（Collation），以确保数据的字符串比较和排序行为符合业务预期。排序规则决定了字符集中的字符如何进行比较和排序，不同的排序规则可能导致相同的查询返回不同的结果顺序，这在多语言环境、跨平台迁移和分布式部署中尤其需要注意。
localeOf: en-audit-rule-aud-default-collation-required-for-database
subtype: rule
language: zh
translationKey: audit-rule-aud-default-collation-required-for-database
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-default-collation-required-for-database |
| 规则名称 | 数据库需指定默认排序规则（Collate） |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求在创建数据库时显式指定默认的排序规则（Collation），以确保数据的字符串比较和排序行为符合业务预期。排序规则决定了字符集中的字符如何进行比较和排序，不同的排序规则可能导致相同的查询返回不同的结果顺序，这在多语言环境、跨平台迁移和分布式部署中尤其需要注意。
未指定排序规则时，数据库会使用系统默认值。当应用层期望特定的排序行为（如大小写不敏感比较`utf8mb4_general_ci`）而数据库使用了不同的默认排序规则时，可能导致业务逻辑错误或查询结果不符合预期。

## 反例

```sql
-- ❌ 不推荐：创建数据库时未指定排序规则，依赖系统默认值
CREATE DATABASE mydb;
```

## 正例

```sql
-- ✅ 推荐：显式指定排序规则，确保字符串比较行为符合预期
CREATE DATABASE mydb DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
```
