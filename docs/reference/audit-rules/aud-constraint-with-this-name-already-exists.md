---
id: audit-rule-aud-constraint-with-this-name-already-exists
title: 约束名已存在
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-constraint-with-this-name-already-exists
tags:
- audit-rule
- ddl
description: 约束名须唯一，重名会使 DDL 失败并中断部署/迁移；可用 IF NOT EXISTS 或唯一命名。
localeOf: en-audit-rule-aud-constraint-with-this-name-already-exists
subtype: rule
language: zh
translationKey: audit-rule-aud-constraint-with-this-name-already-exists
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-constraint-with-this-name-already-exists |
| 规则名称 | 约束名已存在 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则确保在添加新约束时，约束名称在数据库中（或表内）是唯一的，避免与现有约束冲突。重复的约束名称会导致 SQL 执行失败，可能中断部署脚本或数据迁移流程。
如果 SQL 语句添加了 `IF NOT EXISTS` 子句，则不会触发此规则告警。规范的约束命名和唯一性检查是数据库变更管理的基本要求。

## 反例

```sql
-- ❌ 不推荐：添加约束时名称与已存在的约束冲突
ALTER TABLE orders ADD CONSTRAINT pk_orders PRIMARY KEY (order_id);
```

## 正例

```sql
-- ✅ 推荐：添加 IF NOT EXISTS 或使用唯一约束名称
ALTER TABLE orders ADD CONSTRAINT pk_orders_new PRIMARY KEY (order_id);
```
