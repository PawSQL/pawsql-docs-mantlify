---
id: audit-rule-aud-droppingindexdisallowed
title: 禁止删除索引
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-droppingindexdisallowed
tags:
- audit-rule
- ddl
description: 禁止直接删除索引。删除索引可能使关键查询退化为全表扫描、引发执行计划突变与性能雪崩，且影响难以紧急回滚——索引被删除后如需重新创建，可能需要数小时甚至数天的时间（取决于表大小），期间业务性能将持续恶化。
localeOf: en-audit-rule-aud-droppingindexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-droppingindexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-droppingindexdisallowed |
| 规则名称 | 禁止删除索引 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止直接删除索引。删除索引可能使关键查询退化为全表扫描、引发执行计划突变与性能雪崩，且影响难以紧急回滚——索引被删除后如需重新创建，可能需要数小时甚至数天的时间（取决于表大小），期间业务性能将持续恶化。
正确做法是先通过监控与执行计划分析验证索引确实无用，然后灰度下线（如先在支持该功能的数据库中设为不可见索引），观察一段时期确认无性能退化后再正式删除。

## 反例

```sql
-- ❌ 不推荐：直接删除索引，可能导致性能雪崩
DROP INDEX idx_name ON t;
```

## 正例

```sql
-- ✅ 推荐：灰度下线方案
-- 1. ALTER TABLE t ALTER INDEX idx_name INVISIBLE;  -- MySQL 8.0+
-- 2. 监控查询性能一段时间
-- 3. 确认无退化后，正式删除：DROP INDEX idx_name ON t;
```
