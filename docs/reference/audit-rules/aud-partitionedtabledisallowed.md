---
id: audit-rule-aud-partitionedtabledisallowed
title: 禁止使用分区表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-partitionedtabledisallowed
tags:
- audit-rule
- ddl
description: 禁止在 MySQL 中创建分区表。MySQL 分区表虽然可以按范围、列表等维度组织数据，但在实际生产环境中会增加表管理的复杂性——分区裁剪并非总能如预期生效，分区键选择不当会导致查询退化。此外，分区表的
  DDL 操作（如增删分区、重组分区）通常持有元数据锁，在高并发场景下容易引发大面积阻塞，部分操作还可能触发全表数据拷贝。
localeOf: en-audit-rule-aud-partitionedtabledisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-partitionedtabledisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-partitionedtabledisallowed |
| 规则名称 | 禁止使用分区表 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止在 MySQL 中创建分区表。MySQL 分区表虽然可以按范围、列表等维度组织数据，但在实际生产环境中会增加表管理的复杂性——分区裁剪并非总能如预期生效，分区键选择不当会导致查询退化。此外，分区表的 DDL 操作（如增删分区、重组分区）通常持有元数据锁，在高并发场景下容易引发大面积阻塞，部分操作还可能触发全表数据拷贝。
对于大多数应用场景，通过合理的索引设计和数据归档策略即可满足性能和数据管理需求，无需引入分区表的额外复杂度。

## 反例

```sql
-- ❌ 不推荐：MySQL 分区表，增加管理复杂度
CREATE TABLE orders (
    id INT,
    order_date DATE
) PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024)
);
```

## 正例

```sql
-- ✅ 推荐：通过日期索引 + 定期归档满足需求
CREATE TABLE orders (
    id INT,
    order_date DATE,
    INDEX idx_order_date (order_date)
);
```
