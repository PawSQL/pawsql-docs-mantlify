---
id: optimizer-rule-opt-union-all-count-query-optimization
title: UNION ALL统计查询优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-union-all-count-query-optimization
tags:
- optimizer-rule
- rewrite
description: 对于 `SELECT COUNT(*) FROM (SELECT ... UNION ALL SELECT ...) tmp` 形式的查询，数据库会先将
  UNION ALL 的所有子查询结果集物化为一个临时表，再对临时表执行计数。如果子查询中包含复杂表达式或大字段，临时表可能会非常庞大，导致性能严重下降。
localeOf: en-optimizer-rule-opt-union-all-count-query-optimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-union-all-count-query-optimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-union-all-count-query-optimization |
| 规则名称 | UNION ALL统计查询优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于 `SELECT COUNT(*) FROM (SELECT ... UNION ALL SELECT ...) tmp` 形式的查询，数据库会先将 UNION ALL 的所有子查询结果集物化为一个临时表，再对临时表执行计数。如果子查询中包含复杂表达式或大字段，临时表可能会非常庞大，导致性能严重下降。
PawSQL 自动检测此类模式，将子查询中的所有列替换为常量 `1`（因为 `COUNT(*)` 只关心行数，不关心列值），再将整体 COUNT 重写为各分支 COUNT 之和：`SELECT (SELECT COUNT(*) FROM ...) + (SELECT COUNT(*) FROM ...)`，避免物化大临时表。

## 反例

```sql
-- ❌ 不推荐：UNION ALL 后 COUNT，需物化包含大字段的临时表
SELECT COUNT(*) FROM (
    SELECT col1, col2, col3 FROM t1 WHERE ...
    UNION ALL
    SELECT col1, col2, col3 FROM t2 WHERE ...
) tmp;
```

## 正例

```sql
-- ✅ 推荐：替换为常量 1，减少临时表大小
SELECT COUNT(*) FROM (
    SELECT 1 FROM t1 WHERE ...
    UNION ALL
    SELECT 1 FROM t2 WHERE ...
) tmp;

-- ✅ 更佳：拆分 COUNT 求和，完全避免物化派生表
SELECT (SELECT COUNT(*) FROM t1 WHERE ...)
     + (SELECT COUNT(*) FROM t2 WHERE ...);
```
