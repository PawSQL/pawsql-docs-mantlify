---
id: audit-rule-aud-modifyingcolumnaddnotnulldisallowed
title: 禁止为列新增非空约束
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-modifyingcolumnaddnotnulldisallowed
tags:
- audit-rule
- ddl
description: 禁止直接为已有数据的列新增 `NOT NULL` 约束，因为这会触发表数据全量校验甚至重写，导致长时间锁表与阻塞。此外，如果历史数据中存在
  NULL 值，变更将直接失败。即使当前数据满足约束，在高并发环境下，全表扫描期间的锁竞争也可能引发雪崩式的性能退化。
localeOf: en-audit-rule-aud-modifyingcolumnaddnotnulldisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-modifyingcolumnaddnotnulldisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-modifyingcolumnaddnotnulldisallowed |
| 规则名称 | 禁止为列新增非空约束 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止直接为已有数据的列新增 `NOT NULL` 约束，因为这会触发表数据全量校验甚至重写，导致长时间锁表与阻塞。此外，如果历史数据中存在 NULL 值，变更将直接失败。即使当前数据满足约束，在高并发环境下，全表扫描期间的锁竞争也可能引发雪崩式的性能退化。
正确做法是先补齐可能存在的空值数据，通过默认值与应用校验灰度收敛，确保所有路径写入的数据均非空后，再在低峰期以在线 DDL 方式添加约束。

## 反例

```sql
-- ❌ 不推荐：直接为已有数据的列新增 NOT NULL，触发全表扫描
ALTER TABLE t MODIFY col INT NOT NULL;
```

## 正例

```sql
-- ✅ 推荐：先补齐空值，再以在线 DDL 方式添加约束
-- 1. UPDATE t SET col = 0 WHERE col IS NULL;
-- 2. ALTER TABLE t ALTER COLUMN col SET NOT NULL;  -- 在线 DDL
```
