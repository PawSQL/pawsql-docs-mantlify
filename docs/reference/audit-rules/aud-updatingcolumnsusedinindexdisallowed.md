---
id: audit-rule-aud-updatingcolumnsusedinindexdisallowed
title: 禁止更新索引中的列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-updatingcolumnsusedinindexdisallowed
tags:
- audit-rule
- ddl
description: 应避免频繁更新索引列，因为这会触发索引项删除与重建导致随机 I/O、页分裂与锁竞争显著增加，从而放大写放大与性能抖动。对索引列的每次更新都意味着数据库不仅要修改数据页，还要同步维护所有包含该列的索引结构，在高并发场景下可能造成严重的性能瓶颈。
localeOf: en-audit-rule-aud-updatingcolumnsusedinindexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-updatingcolumnsusedinindexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-updatingcolumnsusedinindexdisallowed |
| 规则名称 | 禁止更新索引中的列 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

应避免频繁更新索引列，因为这会触发索引项删除与重建导致随机 I/O、页分裂与锁竞争显著增加，从而放大写放大与性能抖动。对索引列的每次更新都意味着数据库不仅要修改数据页，还要同步维护所有包含该列的索引结构，在高并发场景下可能造成严重的性能瓶颈。
合理做法是将高变更字段从索引中拆出，或改为对低频更新字段建索引，必要时用覆盖查询或冗余列替代。此规则适用于 ALTER TABLE MODIFY COLUMN 操作。

## 反例

```sql
-- ❌ 不推荐：被索引包含的列不应被更新
ALTER TABLE orders MODIFY COLUMN order_date DATE NOT NULL;
-- 假设 order_date 已被某个索引包含，此操作可能影响索引结构
```

## 正例

```sql
-- ✅ 推荐：评估是否可以先删除索引再修改，或新建列进行迁移
```
