---
id: audit-rule-aud-globalindexonpartitionedtabledisallowed
title: 禁止在分区表上创建全局索引
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-globalindexonpartitionedtabledisallowed
tags:
- audit-rule
- index
description: 禁止在分区表上创建全局索引。全局索引打破分区与索引的局部性，会导致分区裁剪失效——即使查询只涉及单个分区的数据，数据库也需要维护和查询一个横跨所有分区的全局索引结构。这显著增加了分区增删或重建时的维护成本与锁冲突风险，带来长时间的维护窗口和不可控的性能影响。
localeOf: en-audit-rule-aud-globalindexonpartitionedtabledisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-globalindexonpartitionedtabledisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-globalindexonpartitionedtabledisallowed |
| 规则名称 | 禁止在分区表上创建全局索引 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止在分区表上创建全局索引。全局索引打破分区与索引的局部性，会导致分区裁剪失效——即使查询只涉及单个分区的数据，数据库也需要维护和查询一个横跨所有分区的全局索引结构。这显著增加了分区增删或重建时的维护成本与锁冲突风险，带来长时间的维护窗口和不可控的性能影响。
合理做法是优先使用本地（分区对齐）索引。本地索引与分区一一对应，增删分区时只需维护对应分区的索引，不影响其他分区的查询性能。

## 反例

```sql
-- ❌ 不推荐：分区表上创建全局索引，破坏分区局部性
CREATE GLOBAL INDEX idx_g ON partitioned_table(id);
```

## 正例

```sql
-- ✅ 推荐：使用本地索引，与分区对齐
CREATE LOCAL INDEX idx_local ON partitioned_table(id);
-- 或
CREATE INDEX idx_local ON partitioned_table(id) LOCAL;
```
