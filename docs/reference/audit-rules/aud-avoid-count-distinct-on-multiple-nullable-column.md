---
id: audit-rule-aud-avoid-count-distinct-on-multiple-nullable-column
title: 避免COUNT DISTINCT多个可空列
type: reference
status: draft
tags:
- audit-rule
- dml
description: COUNT(DISTINCT 多列) 会排除任一列为 NULL 的行，结果与单列去重不同；用 COALESCE 换默认值再计数。
localeOf: en-audit-rule-aud-avoid-count-distinct-on-multiple-nullable-column
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-count-distinct-on-multiple-nullable-column |
| 规则名称 | 避免COUNT DISTINCT多个可空列 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 所有支持数据库 |

## 说明

当你使用 `COUNT(DISTINCT)` 进行多列的计算时，它的计算结果可能和你预想的不同。`COUNT(DISTINCT col)` 计算该列除 NULL 之外的不重复行数，而 `COUNT(DISTINCT col1, col2)` 则会排除掉任意一列为 NULL 的行。这种行为的差异在包含可空列时尤其容易造成统计结果与业务预期不符。
例如，对列 a 和列组合 (a, b) 分别统计不同值的个数，如果 b 列存在 NULL 值，则 `COUNT(DISTINCT a, b)` 的结果会小于或等于 `COUNT(DISTINCT a)`，这可能不符合开发者的预期，需要特别关注。

## 反例

```sql
-- ❌ 不推荐：COUNT(DISTINCT) 多列且列可空，结果可能不符合预期
select count(distinct t.a) a_cnt, count(distinct t.a, t.b) a_b_cnt
from (values
      row(1, 2),
      row(3, null)) as t(a, b);
-- 结果: a_cnt=2, a_b_cnt=1 — 列b为NULL的行被排除
```

## 正例

```sql
-- ✅ 推荐：使用 COALESCE 将 NULL 替换为默认值后再参与去重
select count(distinct t.a) a_cnt, count(distinct t.a, coalesce(t.b, -1)) a_b_cnt
from (values
      row(1, 2),
      row(3, null)) as t(a, b);
```
