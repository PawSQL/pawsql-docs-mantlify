---
id: audit-rule-aud-use-high-cardinality-distribution-keys
title: 分布键应使用区分度大的字段
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-high-cardinality-distribution-keys
tags:
- audit-rule
- ddl
description: 分布键的区分度（Cardinality）直接影响数据的分布均匀性。低区分度的字段（如性别、状态码、布尔值等）作为分布键时，数据将高度集中在少数几个节点上，引发严重的数据倾斜。数据倾斜会导致部分节点负载过高、存储不均、查询性能下降，甚至造成集群资源浪费。
localeOf: en-audit-rule-aud-use-high-cardinality-distribution-keys
subtype: rule
language: zh
translationKey: audit-rule-aud-use-high-cardinality-distribution-keys
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-high-cardinality-distribution-keys |
| 规则名称 | 分布键应使用区分度大的字段 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

分布键的区分度（Cardinality）直接影响数据的分布均匀性。低区分度的字段（如性别、状态码、布尔值等）作为分布键时，数据将高度集中在少数几个节点上，引发严重的数据倾斜。数据倾斜会导致部分节点负载过高、存储不均、查询性能下降，甚至造成集群资源浪费。
选择高区分度字段（如订单ID、用户ID等业务主键）作为分布键，可以实现更均匀的数据分布，确保各节点负载均衡，充分发挥分布式数据库的并行计算优势。

## 反例

```sql
-- ❌ 不推荐：使用低区分度字段（如性别）作为分布键，数据严重倾斜
CREATE TABLE t_user (
    gender CHAR(1),
    name   VARCHAR(50)
) DISTRIBUTED BY HASH (gender);
```

## 正例

```sql
-- ✅ 推荐：使用高区分度字段（如唯一ID）作为分布键
CREATE TABLE t_user (
    id     BIGINT,
    gender CHAR(1),
    name   VARCHAR(50)
) DISTRIBUTED BY HASH (id);
```
