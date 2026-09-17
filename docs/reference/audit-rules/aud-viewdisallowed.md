---
id: audit-rule-aud-viewdisallowed
title: 禁止使用视图
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-viewdisallowed
tags:
- audit-rule
- ddl
description: 禁止在 MySQL 核心业务中大量使用视图。视图难以建立有效索引，MySQL 在执行涉及视图的查询时通常会将其展开为复杂子查询，这会使得优化器失去谓词下推与索引利用的机会，带来不可控的性能退化和执行计划不稳定。此外，嵌套视图和多层视图依赖关系使得问题排查和性能调优异常困难。
localeOf: en-audit-rule-aud-viewdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-viewdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-viewdisallowed |
| 规则名称 | 禁止使用视图 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止在 MySQL 核心业务中大量使用视图。视图难以建立有效索引，MySQL 在执行涉及视图的查询时通常会将其展开为复杂子查询，这会使得优化器失去谓词下推与索引利用的机会，带来不可控的性能退化和执行计划不稳定。此外，嵌套视图和多层视图依赖关系使得问题排查和性能调优异常困难。
推荐将关键查询逻辑下沉为可控的物化结果表，或在应用侧/SQL 中显式展开查询并针对性地建立索引优化。如果仅用于封装查询权限，可通过应用层的查询接口封装替代。

## 反例

```sql
-- ❌ 不推荐：视图难以建立索引，性能不可控
CREATE VIEW v_active_orders AS
SELECT * FROM orders WHERE status = 'active';

-- ❌ 不推荐：嵌套视图导致执行计划复杂
CREATE VIEW v_summary AS
SELECT * FROM v_active_orders WHERE amount > 100;
```

## 正例

```sql
-- ✅ 推荐：直接使用基表查询，配合合理索引
SELECT * FROM orders WHERE status = 'active' AND amount > 100;
```
