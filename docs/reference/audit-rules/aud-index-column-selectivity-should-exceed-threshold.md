---
id: audit-rule-aud-index-column-selectivity-should-exceed-threshold
title: 建议索引字段对区分度大于阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-index-column-selectivity-should-exceed-threshold
tags:
- audit-rule
- index
description: 选择区分度高的字段作为索引，可以利用索引快速定位数据，提升查询效率。区分度（Selectivity）指索引字段中不同值的数量占总行数的比例——区分度越接近1，索引越有效。如果字段区分度过低（如性别字段仅包含男/女两种值），索引无法有效过滤数据，数据库优化器可能放弃使用索引而转向全表扫描，索引不仅浪费了存储空间，还增加了写入时的维护负担。
localeOf: en-audit-rule-aud-index-column-selectivity-should-exceed-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-index-column-selectivity-should-exceed-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-index-column-selectivity-should-exceed-threshold |
| 规则名称 | 建议索引字段对区分度大于阈值 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

选择区分度高的字段作为索引，可以利用索引快速定位数据，提升查询效率。区分度（Selectivity）指索引字段中不同值的数量占总行数的比例——区分度越接近1，索引越有效。如果字段区分度过低（如性别字段仅包含男/女两种值），索引无法有效过滤数据，数据库优化器可能放弃使用索引而转向全表扫描，索引不仅浪费了存储空间，还增加了写入时的维护负担。
该规则检查索引字段的区分度（基数/总行数）是否低于预设阈值（默认0.1，即10%）。建议选择区分度大于10%的字段创建索引，以确保索引发挥实际效用。

## 反例

```sql
-- ❌ 不推荐：gender字段只有M/F两种值，区分度极低，索引几乎无效
CREATE INDEX idx_gender ON user(gender);
```

## 正例

```sql
-- ✅ 推荐：在区分度高的字段上创建索引，有效过滤数据
CREATE INDEX idx_user_id ON user(user_id);
```
