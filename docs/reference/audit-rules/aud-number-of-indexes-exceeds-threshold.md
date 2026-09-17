---
id: audit-rule-aud-number-of-indexes-exceeds-threshold
title: 单表的索引个数超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-number-of-indexes-exceeds-threshold
tags:
- audit-rule
- index
description: 限制单个表的索引数量是为了避免索引过多带来的性能下降和复杂的索引维护开销。每个额外的索引都会增加 `INSERT`、`UPDATE`、`DELETE`
  操作的写入成本，因为数据库需要在每次数据变更时同时维护所有相关索引。
localeOf: en-audit-rule-aud-number-of-indexes-exceeds-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-number-of-indexes-exceeds-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-number-of-indexes-exceeds-threshold |
| 规则名称 | 单表的索引个数超过阈值 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

限制单个表的索引数量是为了避免索引过多带来的性能下降和复杂的索引维护开销。每个额外的索引都会增加 `INSERT`、`UPDATE`、`DELETE` 操作的写入成本，因为数据库需要在每次数据变更时同时维护所有相关索引。
过多的索引还会占用大量磁盘空间，增加优化器选择执行计划时的复杂度，反而可能导致查询性能下降。建议将单表索引数量控制在合理范围内（默认 5 个），仅为核心查询路径创建必要的索引。

## 反例

```sql
-- ❌ 不推荐：单表索引过多（超过 5 个），影响写入性能
CREATE INDEX idx_1 ON t_order (col1);
CREATE INDEX idx_2 ON t_order (col2);
CREATE INDEX idx_3 ON t_order (col3);
CREATE INDEX idx_4 ON t_order (col4);
CREATE INDEX idx_5 ON t_order (col5);
CREATE INDEX idx_6 ON t_order (col6);  -- 超过阈值
```

## 正例

```sql
-- ✅ 推荐：控制索引数量，评估后合并冗余索引
-- 例如将 (col1) 和 (col1, col2) 合并为 (col1, col2)
```
