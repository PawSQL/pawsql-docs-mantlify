---
id: audit-rule-aud-partition-table-queried-without-partition-key-fi
title: 访问分区表没有使用分区字段过滤
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-partition-table-queried-without-partition-key-fi
tags:
- audit-rule
- dml
description: 在访问分区表时，如果查询条件中没有使用分区字段进行过滤，数据库将不得不扫描所有分区来定位数据，即发生"全分区扫描"。这不仅无法发挥分区表的"分区裁剪"优势，还会导致查询性能显著下降、IO
  开销大幅增加，尤其是在分区数量较多或单分区数据量较大的场景下。
localeOf: en-audit-rule-aud-partition-table-queried-without-partition-key-fi
subtype: rule
language: zh
translationKey: audit-rule-aud-partition-table-queried-without-partition-key-fi
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-partition-table-queried-without-partition-key-fi |
| 规则名称 | 访问分区表没有使用分区字段过滤 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在访问分区表时，如果查询条件中没有使用分区字段进行过滤，数据库将不得不扫描所有分区来定位数据，即发生"全分区扫描"。这不仅无法发挥分区表的"分区裁剪"优势，还会导致查询性能显著下降、IO 开销大幅增加，尤其是在分区数量较多或单分区数据量较大的场景下。
正确使用分区字段过滤，可以让优化器精准定位到仅需访问的目标分区，大幅减少扫描范围，显著提升查询效率。该规则是分区表查询优化的核心规范之一。

## 反例

```sql
-- ❌ 不推荐：访问分区表未使用分区键过滤，导致全分区扫描
SELECT * FROM partitioned_table WHERE non_partition_col = 1;
```

## 正例

```sql
-- ✅ 推荐：使用分区键作为过滤条件，实现分区裁剪
SELECT * FROM partitioned_table WHERE partition_key = '2025-01-01';
```
