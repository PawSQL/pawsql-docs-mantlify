---
id: audit-rule-aud-character-set-required-for-database-creation
title: 创建库必须指定数据库字符集
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 创建库必须显式指定字符集，避免默认配置随环境变化导致乱码与排序不一致。
localeOf: en-audit-rule-aud-character-set-required-for-database-creation
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-character-set-required-for-database-creation |
| 规则名称 | 创建库必须指定数据库字符集 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

在创建数据库时必须显式指定字符集，以确保数据的一致性和兼容性。如果未指定字符集，数据库会使用默认配置，而默认配置可能因环境、版本或安装方式不同而有所差异，导致跨环境部署时出现乱码或排序不一致等问题。
显式指定字符集（如 `utf8mb4`）可以避免数据存储时的字符编码问题，在多语言业务场景下尤为重要。

## 反例

```sql
-- ❌ 不推荐：创建数据库时未指定字符集
CREATE DATABASE mydb;
```

## 正例

```sql
-- ✅ 推荐：创建数据库时显式指定字符集
CREATE DATABASE mydb DEFAULT CHARACTER SET utf8mb4;
```
