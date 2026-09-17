---
id: optimizer-rule-opt-use-in-instead-of-or-in-distributed-databases
title: 分布式数据库中使用 IN 替代 OR
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-use-in-instead-of-or-in-distributed-databases
tags:
- optimizer-rule
- rewrite
description: 在分布式数据库中，如果 `OR` 条件包含多个不同的分片键值，优化器可能无法准确定位到具体的分片，导致查询被广播到所有节点（SET）执行，造成严重的资源浪费和性能下降。使用
  `IN` 列表可以将多个等值条件合并，有助于优化器进行更精确的分片裁剪。
localeOf: en-optimizer-rule-opt-use-in-instead-of-or-in-distributed-databases
subtype: rule
language: zh
translationKey: optimizer-rule-opt-use-in-instead-of-or-in-distributed-databases
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-use-in-instead-of-or-in-distributed-databases |
| 规则名称 | 分布式数据库中使用 IN 替代 OR |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式数据库中，如果 `OR` 条件包含多个不同的分片键值，优化器可能无法准确定位到具体的分片，导致查询被广播到所有节点（SET）执行，造成严重的资源浪费和性能下降。使用 `IN` 列表可以将多个等值条件合并，有助于优化器进行更精确的分片裁剪。
特别是当 WHERE 条件中包含多列联合分片键的 `OR` 组合时，使用多列 `IN` 语法（如 `(col1, col2) IN ((v1, v2), (v3, v4))`）可以让数据库准确计算每个分片键值对应的目标分片，大幅减少不必要的网络传输。

## 反例

```sql
-- ❌ 不推荐：OR 条件导致查询广播到所有分片
SELECT * FROM t_bond
WHERE (bond_acct = 'A1' AND bond_code = 'B1' AND bond_subj_code = 'S1')
   OR (bond_acct = 'A2' AND bond_code = 'B2' AND bond_subj_code = 'S2');
```

## 正例

```sql
-- ✅ 推荐：使用 IN 让优化器精确路由到目标分片
SELECT * FROM t_bond
WHERE (bond_acct, bond_code, bond_subj_code) IN (
    ('A1', 'B1', 'S1'),
    ('A2', 'B2', 'S2')
);
```
