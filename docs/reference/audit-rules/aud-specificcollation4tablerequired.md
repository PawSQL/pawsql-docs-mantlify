---
id: audit-rule-aud-specificcollation4tablerequired
title: 表上应使用指定的排序规则
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-specificcollation4tablerequired
tags:
- audit-rule
- ddl
description: 要求表必须使用指定的排序规则（如 `utf8mb4_0900_ai_ci`），以确保数据的比较和排序行为符合预期。排序规则不一致会导致查询结果在不同环境中出现差异，例如大小写敏感/不敏感的排序差异可能影响业务逻辑。
localeOf: en-audit-rule-aud-specificcollation4tablerequired
subtype: rule
language: zh
translationKey: audit-rule-aud-specificcollation4tablerequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-specificcollation4tablerequired |
| 规则名称 | 表上应使用指定的排序规则 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求表必须使用指定的排序规则（如 `utf8mb4_0900_ai_ci`），以确保数据的比较和排序行为符合预期。排序规则不一致会导致查询结果在不同环境中出现差异，例如大小写敏感/不敏感的排序差异可能影响业务逻辑。
默认配置为 `utf8mb4_0900_ai_ci`（MySQL 推荐的 Unicode 排序规则），可通过配置调整。

## 反例

```sql
-- ❌ 不推荐：表排序规则不符合规范
CREATE TABLE t (id INT) COLLATE = utf8mb4_general_ci;
```

## 正例

```sql
-- ✅ 推荐：使用指定的标准排序规则
CREATE TABLE t (id INT) COLLATE = utf8mb4_0900_ai_ci;
```
