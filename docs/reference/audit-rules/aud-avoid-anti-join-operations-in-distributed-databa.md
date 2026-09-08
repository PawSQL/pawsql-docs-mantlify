---
id: audit-rule-aud-avoid-anti-join-operations-in-distributed-databa
title: 分布式数据库应避免出现 ANTI JOIN 操作
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-anti-join-operations-in-distributed-databa
tags:
- audit-rule
- dml
description: 分布式库应避免 NOT IN/NOT EXISTS 反连接（拉取全量到协调端、内存/网络开销巨大）；用物化/拆分或 LEFT JOIN+IS
  NULL。
localeOf: en-audit-rule-aud-avoid-anti-join-operations-in-distributed-databa
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-anti-join-operations-in-distributed-databa
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-anti-join-operations-in-distributed-databa |
| 规则名称 | 分布式数据库应避免出现 ANTI JOIN 操作 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`NOT IN` 或 `NOT EXISTS` 反关联（ANTI JOIN）查询在分布式环境中极难优化。它们通常会导致需要将两张表的所有数据拉取到 Proxy 端或协调节点进行笛卡尔积式的全量比较，内存和网络开销极其巨大，可能引发 OOM 或查询超时。
在分布式数据库中应尽量避免 ANTI JOIN 操作。可以通过创建临时表将增量数据预先物化、拆分 SQL 在应用层分步实现、或使用 LEFT JOIN + IS NULL 等替代方案来降低对分布式算力的消耗。

## 反例

```sql
-- ❌ 不推荐：NOT IN 子查询在分布式环境中性能极差
DELETE FROM t1 WHERE t1.id NOT IN (SELECT t2.id FROM t2);
```

## 正例

```sql
-- ✅ 推荐：拆分为应用层分步操作，或使用 LEFT JOIN + IS NULL
DELETE t1
FROM t1
LEFT JOIN t2 ON t1.id = t2.id
WHERE t2.id IS NULL;
```
