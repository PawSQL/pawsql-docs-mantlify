---
id: audit-rule-aud-modifyingcolumnchangedefaultdisallowed
title: 禁止为列修改默认值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-modifyingcolumnchangedefaultdisallowed
tags:
- audit-rule
- ddl
description: 禁止随意修改列的默认值，因为这会在无感知情况下改变后续写入数据的语义，导致多版本应用行为不一致，并可能引发数据质量与审计问题。例如，旧版本应用可能依赖原有默认值逻辑生成数据，一旦默认值被修改，新旧应用写入的数据将产生分歧，追溯和修复成本极高。
localeOf: en-audit-rule-aud-modifyingcolumnchangedefaultdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-modifyingcolumnchangedefaultdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-modifyingcolumnchangedefaultdisallowed |
| 规则名称 | 禁止为列修改默认值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止随意修改列的默认值，因为这会在无感知情况下改变后续写入数据的语义，导致多版本应用行为不一致，并可能引发数据质量与审计问题。例如，旧版本应用可能依赖原有默认值逻辑生成数据，一旦默认值被修改，新旧应用写入的数据将产生分歧，追溯和修复成本极高。
正确做法是通过版本化字段或应用层显式赋值灰度过渡，完成数据校验后再统一调整默认策略。

## 反例

```sql
-- ❌ 不推荐：直接修改列的默认值，影响后续写入语义
ALTER TABLE t ALTER COLUMN col SET DEFAULT 'new_default';
```

## 正例

```sql
-- ✅ 推荐：通过应用层显式赋值过渡，确认后再统一调整
-- 1. 应用层代码显式设置新默认值
-- 2. 灰度验证数据一致性
-- 3. 统一修改列默认值
```
