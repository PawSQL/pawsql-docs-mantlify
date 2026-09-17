---
id: audit-rule-aud-indexnamerequired
title: 索引必须要有名字
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-indexnamerequired
tags:
- audit-rule
- index
description: 为索引指定一个有意义的名字，对于后续的数据库维护、性能分析和问题排查至关重要。通过索引名可以快速了解其所属表、包含的字段和用途（如普通索引、唯一索引等）。如果使用数据库自动生成的索引名，在日志和监控中将难以定位具体的索引，导致管理混乱。
localeOf: en-audit-rule-aud-indexnamerequired
subtype: rule
language: zh
translationKey: audit-rule-aud-indexnamerequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-indexnamerequired |
| 规则名称 | 索引必须要有名字 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

为索引指定一个有意义的名字，对于后续的数据库维护、性能分析和问题排查至关重要。通过索引名可以快速了解其所属表、包含的字段和用途（如普通索引、唯一索引等）。如果使用数据库自动生成的索引名，在日志和监控中将难以定位具体的索引，导致管理混乱。
显式命名索引也有助于团队协作——所有成员都能通过索引名称理解其设计意图。索引名应遵循统一的命名规范。

## 反例

```sql
-- ❌ 不推荐：创建索引时未指定名称
CREATE INDEX ON employee (last_name);
CREATE UNIQUE INDEX ON employee (emp_no);
```

## 正例

```sql
-- ✅ 推荐：显式指定有意义的索引名称
CREATE INDEX idx_employee_last_name ON employee (last_name);
CREATE UNIQUE INDEX idx_employee_emp_no ON employee (emp_no);
```
