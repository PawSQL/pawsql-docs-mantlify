---
id: audit-rule-aud-nullvaluecomparisondisallowed
title: 禁止使用=NULL判断空值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-nullvaluecomparisondisallowed
tags:
- audit-rule
- dml
description: 在 SQL 中，`= NULL` 并不能正确判断表达式是否为空——`= NULL` 的比较结果始终为 `UNKNOWN`（等价于假），因此永远无法匹配到
  NULL 行。正确的空值判断应使用 `IS NULL` 或 `IS NOT NULL`。同样，`CASE expr WHEN NULL` 也无法正确判断空值，应改为
  `CASE WHEN expr IS NULL`。
localeOf: en-audit-rule-aud-nullvaluecomparisondisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-nullvaluecomparisondisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-nullvaluecomparisondisallowed |
| 规则名称 | 禁止使用=NULL判断空值 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 SQL 中，`= NULL` 并不能正确判断表达式是否为空——`= NULL` 的比较结果始终为 `UNKNOWN`（等价于假），因此永远无法匹配到 NULL 行。正确的空值判断应使用 `IS NULL` 或 `IS NOT NULL`。同样，`CASE expr WHEN NULL` 也无法正确判断空值，应改为 `CASE WHEN expr IS NULL`。
在 `WHERE`/`HAVING` 筛选条件中的错误写法相对容易发现和纠正，而隐藏在 `CASE` 语句中的 NULL 值判断错误则更为隐蔽，可能导致业务逻辑静默出错，排查成本极高。该规则是 SQL 正确性的基础保障。

## 反例

```sql
-- ❌ 不推荐：= NULL 永远为假，无法匹配空值行
SELECT * FROM t WHERE nullable_col = NULL;

-- ❌ 不推荐：CASE WHEN NULL 判断不可靠
SELECT CASE col WHEN NULL THEN 'empty' ELSE 'has value' END FROM t;
```

## 正例

```sql
-- ✅ 推荐：使用 IS NULL 正确判断空值
SELECT * FROM t WHERE nullable_col IS NULL;

-- ✅ 推荐：CASE 中正确判断空值
SELECT CASE WHEN col IS NULL THEN 'empty' ELSE 'has value' END FROM t;
```
