---
id: audit-rule-aud-avoid-unnecessary-builtin-functions
title: 避免使用不必要的内置函数
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-unnecessary-builtin-functions
tags:
- audit-rule
- dml
description: 某些内置函数可能不满足业务或计算上的某些规范要求，或者在对索引列使用时会导致索引失效。通过配置该规则，可以指定业务中需要禁止使用的内置函数列表，当
  SQL 中出现这些函数时进行预警。
localeOf: en-audit-rule-aud-avoid-unnecessary-builtin-functions
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-unnecessary-builtin-functions
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-unnecessary-builtin-functions |
| 规则名称 | 避免使用不必要的内置函数 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

某些内置函数可能不满足业务或计算上的某些规范要求，或者在对索引列使用时会导致索引失效。通过配置该规则，可以指定业务中需要禁止使用的内置函数列表，当 SQL 中出现这些函数时进行预警。
常见的不必要函数使用场景包括：在 WHERE 条件中对索引列使用函数（如 `WHERE ABS(col) > 0`），这会导致索引失效；或者在可以简单运算替代的场景下使用了复杂的函数调用。

## 反例

```sql
-- ❌ 不推荐：在索引列上使用函数，导致索引失效
SELECT * FROM t WHERE ABS(col) > 0;
```

## 正例

```sql
-- ✅ 推荐：将函数应用于常量侧，保留索引可用性
SELECT * FROM t WHERE col > 0 OR col < 0;
```
