---
id: audit-rule-aud-avoid-updating-primary-key-values
title: 避免更新主键的值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-updating-primary-key-values
tags:
- audit-rule
- dml
description: 在 MySQL InnoDB 引擎或 SQL Server 数据库中，数据以主键为聚簇索引的方式进行物理存储——主键值决定了数据行在磁盘上的物理位置。对主键值的更新不仅仅是一次简单的数据修改，而是涉及到数据在磁盘上物理组织的调整（行搬迁），同时还需要进行主键唯一性的校验。
localeOf: en-audit-rule-aud-avoid-updating-primary-key-values
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-updating-primary-key-values
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-updating-primary-key-values |
| 规则名称 | 避免更新主键的值 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 MySQL InnoDB 引擎或 SQL Server 数据库中，数据以主键为聚簇索引的方式进行物理存储——主键值决定了数据行在磁盘上的物理位置。对主键值的更新不仅仅是一次简单的数据修改，而是涉及到数据在磁盘上物理组织的调整（行搬迁），同时还需要进行主键唯一性的校验。
在表数据量非常大的情况下，更新主键的代价可能极高：不仅要修改聚簇索引本身，还要同步更新所有指向该行的二级索引中的主键引用。此外，如果存在外键关联，级联更新的代价更是难以估量。因此，主键应当在设计之初就选为不可变的业务标识。

## 反例

```sql
-- ❌ 不推荐：更新主键值，导致磁盘物理重排和索引重建
UPDATE orders SET order_id = 99999 WHERE order_id = 100;
```

## 正例

```sql
-- ✅ 推荐：主键不应更新；如需变更标识，考虑逻辑删除+重新插入
-- 或使用不变的自然键/雪花ID作为主键
```
