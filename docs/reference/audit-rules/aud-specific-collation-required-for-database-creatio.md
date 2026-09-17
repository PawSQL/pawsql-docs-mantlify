---
id: audit-rule-aud-specific-collation-required-for-database-creatio
title: 创建库或模式时使用规定的排序规则
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-specific-collation-required-for-database-creatio
tags:
- audit-rule
- ddl
description: 要求在创建数据库或模式时使用规定的排序规则（Collation），以确保数据的比较和排序行为与业务预期一致。排序规则决定字符比较时的大小写敏感性、重音符号处理等行为，不一致的排序规则会导致查询结果不符合预期，特别是在多语言环境或分布式部署中需要特别注意。
localeOf: en-audit-rule-aud-specific-collation-required-for-database-creatio
subtype: rule
language: zh
translationKey: audit-rule-aud-specific-collation-required-for-database-creatio
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-specific-collation-required-for-database-creatio |
| 规则名称 | 创建库或模式时使用规定的排序规则 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求在创建数据库或模式时使用规定的排序规则（Collation），以确保数据的比较和排序行为与业务预期一致。排序规则决定字符比较时的大小写敏感性、重音符号处理等行为，不一致的排序规则会导致查询结果不符合预期，特别是在多语言环境或分布式部署中需要特别注意。
统一使用规定的排序规则（如 `utf8mb4_0900_ai_ci`）可以确保跨环境查询结果的一致性，避免因排序规则差异造成的索引失效和隐式转换问题。

## 反例

```sql
-- ❌ 不推荐：未使用规定的排序规则
CREATE DATABASE mydb COLLATE utf8mb4_general_ci;
```

## 正例

```sql
-- ✅ 推荐：使用规定的排序规则
CREATE DATABASE mydb DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```
