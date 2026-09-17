---
id: audit-rule-aud-largetableshouldbesharded
title: 行数超过阈值的单表建议设计为分片表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-largetableshouldbesharded
tags:
- audit-rule
- ddl
description: 对于分布式数据库实例（如 TDSQL），单表数据量过大（如超过千万级行数或数十 GB）时，应将表设计为分片表（Sharded Table），将数据水平拆分到多个数据节点上。这样可以突破单节点的性能瓶颈，利用多节点的计算和存储能力，实现高并发和大数据量的处理。
localeOf: en-audit-rule-aud-largetableshouldbesharded
subtype: rule
language: zh
translationKey: audit-rule-aud-largetableshouldbesharded
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-largetableshouldbesharded |
| 规则名称 | 行数超过阈值的单表建议设计为分片表 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于分布式数据库实例（如 TDSQL），单表数据量过大（如超过千万级行数或数十 GB）时，应将表设计为分片表（Sharded Table），将数据水平拆分到多个数据节点上。这样可以突破单节点的性能瓶颈，利用多节点的计算和存储能力，实现高并发和大数据量的处理。
未分片的大表会导致单点成为性能瓶颈和故障风险点，且无法利用分布式并行计算能力。PawSQL 通过巡检评估表行数，对超过阈值的单表给出分片建议。

## 反例

```sql
-- ❌ 不推荐：大表使用单片表（行数远超阈值）
CREATE TABLE t_huge_log (
    id BIGINT,
    log_date DATE
) shardkey=noshardkey_allset;
```

## 正例

```sql
-- ✅ 推荐：大表设计为分片表
CREATE TABLE t_huge_log (
    id BIGINT,
    log_date DATE,
    PRIMARY KEY (id)
) shardkey=id;
```
