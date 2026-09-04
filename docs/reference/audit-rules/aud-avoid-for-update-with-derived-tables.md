---
id: audit-rule-aud-avoid-for-update-with-derived-tables
title: 避免有派生表的查询语句使用for update
type: reference
status: draft
tags:
- audit-rule
- dml
description: 派生表上的 SELECT ... FOR UPDATE 锁可能落在内部临时表而非基表；应直接对基表加锁。
localeOf: en-audit-rule-aud-avoid-for-update-with-derived-tables
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-for-update-with-derived-tables |
| 规则名称 | 避免有派生表的查询语句使用for update |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

`SELECT ... FROM (子查询) ... FOR UPDATE` 这类语句存在严重的锁失效风险。在 MySQL 中，当 FROM 子句包含派生表（子查询）时，数据库会先将子查询物化为临时表，而 `FOR UPDATE` 的锁可能被加在这个内部临时表上，而非真正的基表数据行。这意味着锁实际上并未保护你期望保护的基表数据，无法满足业务的数据一致性需求。
正确的做法是直接对基表进行 `SELECT ... FOR UPDATE`。如果需要通过子查询筛选后再加锁，应通过 `EXPLAIN` 确认执行计划，确保没有产生 `DERIVED` 临时表，或使用 JOIN 替代子查询。

## 反例

```sql
-- ❌ 不推荐：派生表上的 FOR UPDATE，锁可能加在临时表上而非基表
SELECT * FROM (SELECT * FROM t WHERE id_seq = ?) a FOR UPDATE;
```

## 正例

```sql
-- ✅ 推荐：直接对基表加锁
SELECT * FROM t WHERE id_seq = ? FOR UPDATE;
```
