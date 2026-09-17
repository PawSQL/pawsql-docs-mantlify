---
id: audit-rule-aud-index-with-this-name-already-exists
title: 索引名已存在
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-index-with-this-name-already-exists
tags:
- audit-rule
- ddl
description: 此规则确保在创建新索引时，索引名称在数据库中是唯一的，避免与现有索引发生命名冲突。重复的索引名称会导致 SQL 执行失败，可能中断部署流程或造成预期之外的错误。
localeOf: en-audit-rule-aud-index-with-this-name-already-exists
subtype: rule
language: zh
translationKey: audit-rule-aud-index-with-this-name-already-exists
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-index-with-this-name-already-exists |
| 规则名称 | 索引名已存在 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则确保在创建新索引时，索引名称在数据库中是唯一的，避免与现有索引发生命名冲突。重复的索引名称会导致 SQL 执行失败，可能中断部署流程或造成预期之外的错误。
如果 SQL 语句添加了 `IF NOT EXISTS` 子句，则不会触发此规则告警。在生产环境中，建议始终显式管理索引名称。

## 反例

```sql
-- ❌ 不推荐：创建索引时名称与已存在的索引冲突
CREATE INDEX idx_orders_status ON orders(status);
```

## 正例

```sql
-- ✅ 推荐：添加 IF NOT EXISTS 避免冲突
CREATE INDEX IF NOT EXISTS idx_orders_status_new ON orders(status);
```
