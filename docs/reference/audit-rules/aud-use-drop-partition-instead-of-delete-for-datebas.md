---
id: audit-rule-aud-use-drop-partition-instead-of-delete-for-datebas
title: 使用日期时间字段删除建议改为分区表删除分区
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-drop-partition-instead-of-delete-for-datebas
tags:
- audit-rule
- dml
description: 对于基于日期字段进行数据清理的场景，使用 `DELETE` 语句逐行删除数据效率极低，会产生大量的事务日志和锁开销，在数据量大的情况下还可能导致事务超时或表锁定。如果目标表是按日期范围分区的分区表，使用
  `DROP PARTITION` 或 `TRUNCATE PARTITION` 是更加高效和安全的方式。
localeOf: en-audit-rule-aud-use-drop-partition-instead-of-delete-for-datebas
subtype: rule
language: zh
translationKey: audit-rule-aud-use-drop-partition-instead-of-delete-for-datebas
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-drop-partition-instead-of-delete-for-datebas |
| 规则名称 | 使用日期时间字段删除建议改为分区表删除分区 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于基于日期字段进行数据清理的场景，使用 `DELETE` 语句逐行删除数据效率极低，会产生大量的事务日志和锁开销，在数据量大的情况下还可能导致事务超时或表锁定。如果目标表是按日期范围分区的分区表，使用 `DROP PARTITION` 或 `TRUNCATE PARTITION` 是更加高效和安全的方式。
`DROP PARTITION` 是 DDL 操作，直接删除分区对应的物理存储文件，几乎瞬间完成，不会产生逐行的日志记录，对系统性能影响极小。这是日期范围数据清理的最佳实践。

## 反例

```sql
-- ❌ 不推荐：日期字段范围 DELETE，效率低且可能造成大事务
DELETE FROM order_history WHERE order_date < '2022-01-01';
```

## 正例

```sql
-- ✅ 推荐：对于按日期分区的表，直接删除分区
ALTER TABLE order_history DROP PARTITION p202112;
```
