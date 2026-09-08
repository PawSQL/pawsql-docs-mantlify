---
id: audit-rule-aud-avoid-multiple-distribution-keys
title: 分布键不建议使用多个字段
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-multiple-distribution-keys
tags:
- audit-rule
- ddl
description: 多列分布键限制水平扩展、增加哈希与本地化关联难度；建议用单一高频关联字段作分布键。
localeOf: en-audit-rule-aud-avoid-multiple-distribution-keys
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-multiple-distribution-keys
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-multiple-distribution-keys |
| 规则名称 | 分布键不建议使用多个字段 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

使用多个字段作为分布键会限制表的水平扩展能力，影响分片（Sharding）的灵活性和路由效率。多列分布键会导致哈希计算复杂度增加，同时在表关联（JOIN）时需要所有分布键字段都匹配才能本地化执行，增加了优化器生成高效执行计划的难度。
多列分布键还会增加跨节点数据移动的成本，因为数据重分布需要基于所有分布键列进行计算。建议尽可能使用单一字段作为分布键，优先选择查询关联中最频繁使用的连接字段。

## 反例

```sql
-- ❌ 不推荐：使用多字段作为分布键
CREATE TABLE t_sales (
    region    VARCHAR(50),
    product   VARCHAR(50),
    amount    DECIMAL(10, 2)
) DISTRIBUTED BY HASH (region, product);
```

## 正例

```sql
-- ✅ 推荐：使用单一字段作为分布键
CREATE TABLE t_sales (
    region    VARCHAR(50),
    product   VARCHAR(50),
    amount    DECIMAL(10, 2)
) DISTRIBUTED BY HASH (region);
```
