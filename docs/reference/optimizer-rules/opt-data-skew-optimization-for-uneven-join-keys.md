---
id: optimizer-rule-opt-data-skew-optimization-for-uneven-join-keys
title: 关联字段不均匀导致数据倾斜优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-data-skew-optimization-for-uneven-join-keys
tags:
- optimizer-rule
- rewrite
description: 在分布式计算或大规模数据处理（如 Hive、Spark SQL）场景中，表关联（JOIN）操作的关联字段如果数据分布严重不均匀（即存在"热点值"），会导致大量数据集中到少数计算节点，造成数据倾斜。数据倾斜不仅使个别节点负载过高、处理时间过长，还会导致整体查询性能严重下降，甚至引发任务失败。
localeOf: en-optimizer-rule-opt-data-skew-optimization-for-uneven-join-keys
subtype: rule
language: zh
translationKey: optimizer-rule-opt-data-skew-optimization-for-uneven-join-keys
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-data-skew-optimization-for-uneven-join-keys |
| 规则名称 | 关联字段不均匀导致数据倾斜优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式计算或大规模数据处理（如 Hive、Spark SQL）场景中，表关联（JOIN）操作的关联字段如果数据分布严重不均匀（即存在"热点值"），会导致大量数据集中到少数计算节点，造成数据倾斜。数据倾斜不仅使个别节点负载过高、处理时间过长，还会导致整体查询性能严重下降，甚至引发任务失败。
当检测到关联字段的数据分布不均匀时，应当采取分桶、加盐（salting）、Map 端 JOIN、或调整关联策略等措施来缓解数据倾斜问题。PawSQL 可自动识别此类场景并提供优化建议。
