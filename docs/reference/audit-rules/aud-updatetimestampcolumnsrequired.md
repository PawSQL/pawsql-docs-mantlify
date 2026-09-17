---
id: audit-rule-aud-updatetimestampcolumnsrequired
title: 表需定义更新时间戳列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-updatetimestampcolumnsrequired
tags:
- audit-rule
- ddl
description: 要求表中包含更新时间戳列（如 `updated_at`、`modified_time`），以记录数据的最后更新时间，有助于数据变更追踪和问题排查。缺乏更新时间戳的表在数据审计、增量同步和数据生命周期管理中会增加额外的复杂度和开销。
localeOf: en-audit-rule-aud-updatetimestampcolumnsrequired
subtype: rule
language: zh
translationKey: audit-rule-aud-updatetimestampcolumnsrequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-updatetimestampcolumnsrequired |
| 规则名称 | 表需定义更新时间戳列 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求表中包含更新时间戳列（如 `updated_at`、`modified_time`），以记录数据的最后更新时间，有助于数据变更追踪和问题排查。缺乏更新时间戳的表在数据审计、增量同步和数据生命周期管理中会增加额外的复杂度和开销。
建议使用 `TIMESTAMP` 或 `DATETIME` 类型，并配合 `ON UPDATE CURRENT_TIMESTAMP`（MySQL）或触发器（PostgreSQL）实现自动更新，确保时间戳的准确性和一致性。

## 反例

```sql
-- ❌ 不推荐：表缺少更新时间戳列
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    amount DECIMAL(10,2)
);
```

## 正例

```sql
-- ✅ 推荐：包含更新时间戳列，并设置自动更新
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    amount DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```
