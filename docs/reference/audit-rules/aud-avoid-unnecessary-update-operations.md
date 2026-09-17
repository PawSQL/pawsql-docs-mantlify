---
id: audit-rule-aud-avoid-unnecessary-update-operations
title: 避免不必要的更新操作
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-unnecessary-update-operations
tags:
- audit-rule
- dml
description: '`UPDATE` 语句即使将字段值更新为与原值完全相同，也会产生写入日志（redo/undo log）并触发相应的行锁、索引维护等开销。在高并发或批量更新的场景下，这些"无效更新"会白白消耗
  IO 带宽、日志空间和锁资源，影响整体系统性能。'
localeOf: en-audit-rule-aud-avoid-unnecessary-update-operations
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-unnecessary-update-operations
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-unnecessary-update-operations |
| 规则名称 | 避免不必要的更新操作 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`UPDATE` 语句即使将字段值更新为与原值完全相同，也会产生写入日志（redo/undo log）并触发相应的行锁、索引维护等开销。在高并发或批量更新的场景下，这些"无效更新"会白白消耗 IO 带宽、日志空间和锁资源，影响整体系统性能。
通过在 WHERE 条件中加入 `AND col != new_value`，可以过滤掉那些值已为目标值的行，避免无效更新，从而大幅减少 IO 和日志量，提升更新操作的执行效率。

## 反例

```sql
-- ❌ 不推荐：不检查当前值，可能执行无效更新
UPDATE user SET status = 'ACTIVE' WHERE id = 100;
```

## 正例

```sql
-- ✅ 推荐：WHERE 条件中排除已为目标值的行，避免无效更新
UPDATE user SET status = 'ACTIVE' WHERE id = 100 AND status != 'ACTIVE';
```
