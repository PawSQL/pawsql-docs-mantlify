---
id: audit-rule-aud-avoid-negative-queries-on-filter-columns
title: 避免对条件字段使用负向查询
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-negative-queries-on-filter-columns
tags:
- audit-rule
- index
description: 负向查询指的是使用否定条件的查询，包括 `<>`（不等于）、`!=`、`NOT IN`、`NOT EXISTS`、`NOT LIKE`、`IS
  NOT NULL` 等否定谓词。此类查询通常无法利用索引进行快速数据定位，因为索引擅长的是"找到符合某值的行"，而非"排除不符合某值的行"。数据库往往需要对大量数据进行全索引扫描甚至全表扫描才能完成负向条件的评估。
localeOf: en-audit-rule-aud-avoid-negative-queries-on-filter-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-negative-queries-on-filter-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-negative-queries-on-filter-columns |
| 规则名称 | 避免对条件字段使用负向查询 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

负向查询指的是使用否定条件的查询，包括 `<>`（不等于）、`!=`、`NOT IN`、`NOT EXISTS`、`NOT LIKE`、`IS NOT NULL` 等否定谓词。此类查询通常无法利用索引进行快速数据定位，因为索引擅长的是"找到符合某值的行"，而非"排除不符合某值的行"。数据库往往需要对大量数据进行全索引扫描甚至全表扫描才能完成负向条件的评估。
在业务允许的情况下，建议将负向查询改写为正向查询，或通过其他方式（如将 NULL 替换为默认值来避免 `IS NOT NULL`）来提升查询性能。

## 反例

```sql
-- ❌ 不推荐：负向查询 <> 无法有效利用索引
SELECT * FROM t WHERE status <> 1;
```

## 正例

```sql
-- ✅ 推荐：改写为正向查询，可利用索引
SELECT * FROM t WHERE status IN (0, 2, 3);
```
