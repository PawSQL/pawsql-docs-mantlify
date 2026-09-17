---
id: audit-rule-aud-duplicatecolumnsinindex
title: 索引中不应该有重复列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-duplicatecolumnsinindex
tags:
- audit-rule
- index
description: 索引中包含重复的列是不必要的，它不会提高查询性能，反而会浪费存储空间、增加索引维护开销，并可能导致索引效率降低。每个索引列在查找和排序中只起一次作用，重复列不会提供额外的优化帮助。
localeOf: en-audit-rule-aud-duplicatecolumnsinindex
subtype: rule
language: zh
translationKey: audit-rule-aud-duplicatecolumnsinindex
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-duplicatecolumnsinindex |
| 规则名称 | 索引中不应该有重复列 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

索引中包含重复的列是不必要的，它不会提高查询性能，反而会浪费存储空间、增加索引维护开销，并可能导致索引效率降低。每个索引列在查找和排序中只起一次作用，重复列不会提供额外的优化帮助。
在创建复合索引时，应确保每一列在该索引中只出现一次，避免无意中重复添加相同字段。

## 反例

```sql
-- ❌ 不推荐：索引中有重复的字段名
CREATE INDEX idx_dup ON user(name, age, name);
```

## 正例

```sql
-- ✅ 推荐：索引中每列只出现一次
CREATE INDEX idx_user ON user(name, age, email);
```
