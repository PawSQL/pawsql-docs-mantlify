---
id: audit-rule-aud-avoidusingnullablecolumnsinindex
title: 索引中避免使用可空列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoidusingnullablecolumnsinindex
tags:
- audit-rule
- index
description: 索引中应尽量避免使用可空列。可空列上的 NULL 值在多数数据库中不会进入 B+Tree 索引，导致索引不完整——查询 `WHERE col
  IS NULL` 无法利用索引，且包含可空列的复合索引在某些场景下可能出现部分扫描问题，影响查询性能。
localeOf: en-audit-rule-aud-avoidusingnullablecolumnsinindex
subtype: rule
language: zh
translationKey: audit-rule-aud-avoidusingnullablecolumnsinindex
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoidusingnullablecolumnsinindex |
| 规则名称 | 索引中避免使用可空列 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

索引中应尽量避免使用可空列。可空列上的 NULL 值在多数数据库中不会进入 B+Tree 索引，导致索引不完整——查询 `WHERE col IS NULL` 无法利用索引，且包含可空列的复合索引在某些场景下可能出现部分扫描问题，影响查询性能。
如果业务允许，建议为索引列添加 `NOT NULL` 约束，或者为 NULL 值设计默认值替代方案。这有助于提升索引的覆盖率和查询效率。

## 反例

```sql
-- ❌ 不推荐：索引字段未设置非空约束，NULL 值无法被索引
CREATE INDEX idx_user_email ON user(email);
```

## 正例

```sql
-- ✅ 推荐：为索引列添加 NOT NULL 约束
CREATE TABLE user (
    id INT PRIMARY KEY,
    email VARCHAR(255) NOT NULL
);
CREATE INDEX idx_user_email ON user(email);
```
