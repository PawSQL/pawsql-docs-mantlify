---
id: audit-rule-aud-use-partitioned-tables-for-large-tables
title: 大表建议使用分区表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-partitioned-tables-for-large-tables
tags:
- audit-rule
- ddl
description: 单表行数超过500万行或容量超过10GB的表，在查询、维护（如数据清理、备份）等方面会遇到性能瓶颈。使用分区表可以将一个大表分解为多个更小、更易于管理的物理片段。通过分区裁剪（Partition
  Pruning），查询只需扫描相关分区，显著减少I/O开销；同时，通过`DROP PARTITION`可以高效地清理历史数据，避免高成本的逐行DELETE操作。
localeOf: en-audit-rule-aud-use-partitioned-tables-for-large-tables
subtype: rule
language: zh
translationKey: audit-rule-aud-use-partitioned-tables-for-large-tables
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-partitioned-tables-for-large-tables |
| 规则名称 | 大表建议使用分区表 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

单表行数超过500万行或容量超过10GB的表，在查询、维护（如数据清理、备份）等方面会遇到性能瓶颈。使用分区表可以将一个大表分解为多个更小、更易于管理的物理片段。通过分区裁剪（Partition Pruning），查询只需扫描相关分区，显著减少I/O开销；同时，通过`DROP PARTITION`可以高效地清理历史数据，避免高成本的逐行DELETE操作。
该规则在表巡检时检测行数或大小超过阈值的非分区表，建议将其转换为分区表。常见的分区策略包括按时间范围（RANGE）、列表（LIST）或哈希（HASH）分区。

## 反例

```sql
-- ❌ 不推荐：大表未分区，查询和维护效率低下
CREATE TABLE t_log (
    id INT,
    log_time DATETIME
);
```

## 正例

```sql
-- ✅ 推荐：按月范围分区，支持分区裁剪和快速删除历史数据
CREATE TABLE t_log (
    id INT,
    log_time DATETIME
) PARTITION BY RANGE COLUMNS(log_time) (
    PARTITION p202401 VALUES LESS THAN ('2024-02-01'),
    PARTITION p202402 VALUES LESS THAN ('2024-03-01')
);
```
