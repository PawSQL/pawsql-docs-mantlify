---
id: audit-rule-aud-functionalindexdisallowed
title: 禁止使用函数索引
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-functionalindexdisallowed
tags:
- audit-rule
- index
description: 禁止使用函数索引。函数索引虽然可以解决对字段使用函数时无法走索引的问题，但本质上是对业务 SQL 写法不规范的一种妥协。函数索引的维护成本高，数据变更时需要重新计算函数结果并更新索引，增加写入开销。更重要的是，函数索引的语义与列定义强绑定，在不同数据库间的兼容性差，增加了数据库迁移的难度。
localeOf: en-audit-rule-aud-functionalindexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-functionalindexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-functionalindexdisallowed |
| 规则名称 | 禁止使用函数索引 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用函数索引。函数索引虽然可以解决对字段使用函数时无法走索引的问题，但本质上是对业务 SQL 写法不规范的一种妥协。函数索引的维护成本高，数据变更时需要重新计算函数结果并更新索引，增加写入开销。更重要的是，函数索引的语义与列定义强绑定，在不同数据库间的兼容性差，增加了数据库迁移的难度。
更好的做法是规范 SQL 写法，避免在查询条件中对字段使用函数。如果业务确实需要频繁地对多列计算结果进行查询和过滤，应考虑在表中新增一个冗余列，通过应用层或触发器实时维护该列的值，并为其创建普通索引。

## 反例

```sql
-- ❌ 不推荐：函数索引，维护成本高，兼容性差
CREATE INDEX idx_month ON order_table (MONTH(order_date));
```

## 正例

```sql
-- ✅ 推荐：新增冗余列 + 普通索引
-- ALTER TABLE order_table ADD COLUMN order_month TINYINT;
-- 在插入或更新时维护该字段的值
CREATE INDEX idx_order_month ON order_table(order_month);
```
