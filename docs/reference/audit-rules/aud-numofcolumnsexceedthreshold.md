---
id: audit-rule-aud-numofcolumnsexceedthreshold
title: 表的列数不建议超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-numofcolumnsexceedthreshold
tags:
- audit-rule
- ddl
description: 建议表的列数不要超过特定的阈值，以优化性能和简化管理。避免在 OLTP 系统上做宽表设计——列数过多的表会导致单行数据量过大，影响缓存效率、增大
  I/O 开销，并使得表结构的维护和理解变得困难。
localeOf: en-audit-rule-aud-numofcolumnsexceedthreshold
subtype: rule
language: zh
translationKey: audit-rule-aud-numofcolumnsexceedthreshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-numofcolumnsexceedthreshold |
| 规则名称 | 表的列数不建议超过阈值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

建议表的列数不要超过特定的阈值，以优化性能和简化管理。避免在 OLTP 系统上做宽表设计——列数过多的表会导致单行数据量过大，影响缓存效率、增大 I/O 开销，并使得表结构的维护和理解变得困难。
默认阈值为 32 列，可根据业务需求调整。对于列数超限的表，建议考虑垂直拆分（将不常用的大字段或独立业务属性拆分到扩展表）。

## 反例

```sql
-- ❌ 不推荐：表的列数过多（超过阈值 32）
CREATE TABLE orders (
    col1 VARCHAR(100), col2 VARCHAR(100),
    -- ... 共 33+ 列
    col33 VARCHAR(100)
);
```

## 正例

```sql
-- ✅ 推荐：将表垂直拆分
CREATE TABLE orders (
    id INT PRIMARY KEY,
    status VARCHAR(20)
    -- 核心字段控制在 32 列以内
);
CREATE TABLE orders_detail (
    order_id INT,
    -- 扩展字段
);
```
