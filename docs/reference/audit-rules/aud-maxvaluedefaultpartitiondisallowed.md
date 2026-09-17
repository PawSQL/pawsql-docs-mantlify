---
id: audit-rule-aud-maxvaluedefaultpartitiondisallowed
title: 禁止设置MAXVALUE默认分区
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-maxvaluedefaultpartitiondisallowed
tags:
- audit-rule
- ddl
description: 使用 MAXVALUE 作为默认分区虽然可以避免数据无法落入分区的错误，但也会使得所有未预见的新数据全部涌入同一个分区，导致该分区数据量失控、查询性能恶化，并失去分区修剪的优势。
localeOf: en-audit-rule-aud-maxvaluedefaultpartitiondisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-maxvaluedefaultpartitiondisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-maxvaluedefaultpartitiondisallowed |
| 规则名称 | 禁止设置MAXVALUE默认分区 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

使用 MAXVALUE 作为默认分区虽然可以避免数据无法落入分区的错误，但也会使得所有未预见的新数据全部涌入同一个分区，导致该分区数据量失控、查询性能恶化，并失去分区修剪的优势。
合理做法是预先规划好完整的分区键值范围，或者使用定期维护脚本自动创建新分区，而非依赖 MAXVALUE 兜底。此规则适用于 RANGE 分区表的定义。

## 反例

```sql
-- ❌ 不推荐：使用 MAXVALUE 默认分区
CREATE TABLE orders (
    order_id BIGINT,
    order_date DATE
) PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p_max VALUES LESS THAN (MAXVALUE)
);
```

## 正例

```sql
-- ✅ 推荐：明确所有分区范围，不依赖 MAXVALUE
CREATE TABLE orders (
    order_id BIGINT,
    order_date DATE
) PARTITION BY RANGE (YEAR(order_date)) (
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)
);
```
