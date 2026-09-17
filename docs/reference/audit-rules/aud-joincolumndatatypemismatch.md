---
id: audit-rule-aud-joincolumndatatypemismatch
title: 表关联字段数据类型长度不一致
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-joincolumndatatypemismatch
tags:
- audit-rule
- dml
description: 进行表关联（`JOIN`）时，如果关联字段的数据类型或长度不一致，数据库无法直接使用索引进行匹配，需要进行隐式数据类型转换，这会导致该字段上的索引失效，从而引发全表扫描，严重影响查询性能。
localeOf: en-audit-rule-aud-joincolumndatatypemismatch
subtype: rule
language: zh
translationKey: audit-rule-aud-joincolumndatatypemismatch
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-joincolumndatatypemismatch |
| 规则名称 | 表关联字段数据类型长度不一致 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

进行表关联（`JOIN`）时，如果关联字段的数据类型或长度不一致，数据库无法直接使用索引进行匹配，需要进行隐式数据类型转换，这会导致该字段上的索引失效，从而引发全表扫描，严重影响查询性能。
必须确保关联字段的类型定义完全一致，包括数据类型、长度、精度和字符集。此规则适用于 SELECT、UPDATE、DELETE 语句中的 JOIN ON 条件。

## 反例

```sql
-- ❌ 不推荐：关联字段数据类型不一致
-- a.id 是 INT，b.parent_id 是 VARCHAR
SELECT * FROM a JOIN b ON a.id = b.parent_id;

-- ❌ 不推荐：关联字段长度不一致
-- a.code 是 VARCHAR(10)，b.code 是 VARCHAR(20)
SELECT * FROM a JOIN b ON a.code = b.code;
```

## 正例

```sql
-- ✅ 推荐：关联字段类型和长度完全一致
-- 两表关联列均为 INT
SELECT * FROM a JOIN b ON a.id = b.parent_id;
```
