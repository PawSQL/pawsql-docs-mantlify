---
id: audit-rule-aud-distribution-key-must-use-specified-collation
title: 分布键的需使用指定的排序规则
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-distribution-key-must-use-specified-collation
tags:
- audit-rule
- ddl
description: 分布键字段应使用大小写敏感的排序规则（如 `utf8mb4_bin`），以确保大小写不同的值能被正确路由到不同的分片，避免因排序规则不一致导致的数据混淆。如果分布键使用大小写不敏感的排序规则（如
  `utf8mb4_general_ci`），两个大小写不同但语义相同的值（如 'ABC' 和 'abc'）会被视为相等，可能导致路由结果不符合预期。
localeOf: en-audit-rule-aud-distribution-key-must-use-specified-collation
subtype: rule
language: zh
translationKey: audit-rule-aud-distribution-key-must-use-specified-collation
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-distribution-key-must-use-specified-collation |
| 规则名称 | 分布键的需使用指定的排序规则 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

分布键字段应使用大小写敏感的排序规则（如 `utf8mb4_bin`），以确保大小写不同的值能被正确路由到不同的分片，避免因排序规则不一致导致的数据混淆。如果分布键使用大小写不敏感的排序规则（如 `utf8mb4_general_ci`），两个大小写不同但语义相同的值（如 'ABC' 和 'abc'）会被视为相等，可能导致路由结果不符合预期。
为保证分布键路由的一致性和可预测性，字符类型的分布键字段应指定大小写敏感的二进制排序规则。

## 反例

```sql
-- ❌ 不推荐：分布键使用大小写不敏感的排序规则
CREATE TABLE t_product (
    code VARCHAR(50) COLLATE utf8mb4_general_ci,
    name VARCHAR(100)
) shardkey = code;
```

## 正例

```sql
-- ✅ 推荐：分布键使用大小写敏感的排序规则
CREATE TABLE t_product (
    code VARCHAR(50) COLLATE utf8mb4_bin,
    name VARCHAR(100)
) shardkey = code;
```
