---
id: audit-rule-aud-collation4indexdisallowed
title: 禁止索引创建时指定collation
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-collation4indexdisallowed
tags:
- audit-rule
- index
description: 禁止在创建索引时指定排序规则（collation），因为这会导致索引排序规则与列或数据库默认规则不一致，从而引发比较语义变化、索引无法被等值/范围查询正确利用及跨环境执行计划不稳定。
localeOf: en-audit-rule-aud-collation4indexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-collation4indexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-collation4indexdisallowed |
| 规则名称 | 禁止索引创建时指定collation |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止在创建索引时指定排序规则（collation），因为这会导致索引排序规则与列或数据库默认规则不一致，从而引发比较语义变化、索引无法被等值/范围查询正确利用及跨环境执行计划不稳定。
合理做法是统一在列定义层确定字符集与排序规则，并保持索引继承一致。当索引的 collation 与列定义不一致时，数据库可能会放弃使用索引而退化为全表扫描。

## 反例

```sql
-- ❌ 不推荐：索引创建时指定 COLLATION
CREATE INDEX idx ON t(name COLLATE utf8mb4_general_ci);
```

## 正例

```sql
-- ✅ 推荐：索引继承列定义的默认排序规则
CREATE INDEX idx ON t(name);
```
