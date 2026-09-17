---
id: audit-rule-aud-specificcolumnsrequired
title: 表必须包含的列名及数据类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-specificcolumnsrequired
tags:
- audit-rule
- ddl
description: 要求表必须包含特定的列及其数据类型，如 `id`（主键）、`created_ts`（创建时间戳）和 `updated_ts`（更新时间戳），以满足应用程序的标准需求和数据治理规范。统一的表结构有助于
  ORM 框架集成、日志审计和数据生命周期管理。
localeOf: en-audit-rule-aud-specificcolumnsrequired
subtype: rule
language: zh
translationKey: audit-rule-aud-specificcolumnsrequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-specificcolumnsrequired |
| 规则名称 | 表必须包含的列名及数据类型 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求表必须包含特定的列及其数据类型，如 `id`（主键）、`created_ts`（创建时间戳）和 `updated_ts`（更新时间戳），以满足应用程序的标准需求和数据治理规范。统一的表结构有助于 ORM 框架集成、日志审计和数据生命周期管理。
此规则可配置，默认要求包含 `id:unsigned int, created_ts:timestamp, updated_ts:timestamp`，团队可根据业务规范调整必选列的列表。

## 反例

```sql
-- ❌ 不推荐：缺少必要的标准列（如创建时间和更新时间戳列）
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    amount DECIMAL(10,2)
);
```

## 正例

```sql
-- ✅ 推荐：包含完整的必选列
CREATE TABLE orders (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    order_id BIGINT,
    amount DECIMAL(10,2),
    created_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```
