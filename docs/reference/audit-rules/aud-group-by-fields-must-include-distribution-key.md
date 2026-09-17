---
id: audit-rule-aud-group-by-fields-must-include-distribution-key
title: 分组字段不包含分布键
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-group-by-fields-must-include-distribution-key
tags:
- audit-rule
- dml
description: 当对分片表进行 `GROUP BY` 分组操作时，如果分组字段不包含分布键，则需要在各个分片上分别完成分组计算，然后将各分片的结果集拉取到协调节点再进行一轮全局分组和聚合。这个"数据重分布"过程会产生大量的网络传输开销和额外的
  CPU 计算，严重影响查询性能。
localeOf: en-audit-rule-aud-group-by-fields-must-include-distribution-key
subtype: rule
language: zh
translationKey: audit-rule-aud-group-by-fields-must-include-distribution-key
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-group-by-fields-must-include-distribution-key |
| 规则名称 | 分组字段不包含分布键 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当对分片表进行 `GROUP BY` 分组操作时，如果分组字段不包含分布键，则需要在各个分片上分别完成分组计算，然后将各分片的结果集拉取到协调节点再进行一轮全局分组和聚合。这个"数据重分布"过程会产生大量的网络传输开销和额外的 CPU 计算，严重影响查询性能。
应尽量使 `GROUP BY` 的字段包含分布键，这样每个分片可以独立完成分组聚合而无需跨节点传输中间结果，实现分片本地化的高效聚合计算。

## 反例

```sql
-- ❌ 不推荐：GROUP BY 字段不包含分布键，需要全局聚合
SELECT status, COUNT(*)
FROM t_order
GROUP BY status;
```

## 正例

```sql
-- ✅ 推荐：GROUP BY 字段包含分布键，分片本地化聚合
SELECT id, status, COUNT(*)
FROM t_order
GROUP BY id, status;
```
