---
id: audit-rule-aud-consider-replicated-distribution-for-small-table
title: 小于阈值的分布表建议设计为复制表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-consider-replicated-distribution-for-small-table
tags:
- audit-rule
- ddl
description: 分布式小表（10 万行以下、读多写少）建议设计为复制表，关联避免跨节点数据交换。
localeOf: en-audit-rule-aud-consider-replicated-distribution-for-small-table
subtype: rule
language: zh
translationKey: audit-rule-aud-consider-replicated-distribution-for-small-table
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-consider-replicated-distribution-for-small-table |
| 规则名称 | 小于阈值的分布表建议设计为复制表 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式数据库环境中，表的数据分布方式（分片表或复制表）对查询性能有显著影响。当分布表（Sharding Table）的数据量较小时，若继续采用分片存储，在与其他表进行关联查询时（尤其是非等值关联），可能因跨节点数据交换而导致性能下降。相反，将这些小表设计为复制表（Replicated Table），即将完整数据复制到每个节点，可以避免跨节点数据交换，从而提升查询性能。
该规则检查查询语句中涉及多表关联的场景，通过分析关联条件和表的行数，自动识别出适合改造为复制表的小表。建议对数据量在10万行以下且读多写少的表采用复制表策略。

## 反例

```sql
-- ❌ 不推荐：小表t1采用分片分布，非等值关联导致跨节点数据传输
SELECT * FROM t1, t2 WHERE t1.amount > t2.threshold;
```

## 正例

```sql
-- ✅ 建议：将t1设计为复制表，消除跨节点数据传输
-- (t1改为：CREATE TABLE t1 (...) DISTRIBUTED BY REPLICATION;)
```
