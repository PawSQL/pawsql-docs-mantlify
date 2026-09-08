---
id: audit-rule-aud-create-index-before-constraint
title: 创建约束前提前创建相关的索引
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-create-index-before-constraint
tags:
- audit-rule
- ddl
description: 加唯一/外键/CHECK 约束前先建对应索引，约束校验可复用索引、避免全表扫描。
localeOf: en-audit-rule-aud-create-index-before-constraint
subtype: rule
language: zh
translationKey: audit-rule-aud-create-index-before-constraint
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-create-index-before-constraint |
| 规则名称 | 创建约束前提前创建相关的索引 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在创建约束（如唯一约束、外键约束、CHECK 约束）之前，应先创建相关的索引。约束的执行依赖于底层索引来进行数据校验，如果事先没有相关索引，数据库在验证约束时将不得不进行全表扫描，严重影响 DDL 操作的执行效率，甚至在大表上导致长时间的锁等待。
提前手动创建索引可以让数据库直接复用已有索引进行约束校验，避免全表扫描，确保 DDL 变更平稳执行。同时这也有助于对索引进行更精细的命名和结构控制。

## 反例

```sql
-- ❌ 不推荐：创建唯一约束前未创建对应索引，导致全表扫描校验
ALTER TABLE t_order ADD CONSTRAINT uk_order_no UNIQUE (order_no);
```

## 正例

```sql
-- ✅ 推荐：先创建索引，再添加约束，复用已有索引
CREATE UNIQUE INDEX uk_order_no ON t_order (order_no);
ALTER TABLE t_order ADD CONSTRAINT uk_order_no UNIQUE USING INDEX uk_order_no;
```
