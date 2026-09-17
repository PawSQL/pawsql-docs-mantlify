---
id: audit-rule-aud-sharded-table-update-does-not-support-subquery-v
title: 分片表不支持 UPDATE 更新的值为子查询
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-sharded-table-update-does-not-support-subquery-v
tags:
- audit-rule
- dml
description: 在 TDSQL 等分布式数据库中，`UPDATE` 语句的 `SET` 子句的值部分不支持使用子查询。这是分布式数据库在语法层面的实现限制，如果违反会导致
  SQL 执行直接报错。
localeOf: en-audit-rule-aud-sharded-table-update-does-not-support-subquery-v
subtype: rule
language: zh
translationKey: audit-rule-aud-sharded-table-update-does-not-support-subquery-v
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-sharded-table-update-does-not-support-subquery-v |
| 规则名称 | 分片表不支持 UPDATE 更新的值为子查询 |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 TDSQL 等分布式数据库中，`UPDATE` 语句的 `SET` 子句的值部分不支持使用子查询。这是分布式数据库在语法层面的实现限制，如果违反会导致 SQL 执行直接报错。
如果需要基于另一张表的数据来更新本表，建议通过应用程序分步查询和更新，或使用多表 `UPDATE ... JOIN` 语法（如果数据库支持）来实现。

## 反例

```sql
-- ❌ 不推荐：分片表 UPDATE 的 SET 子句使用了子查询（不支持）
UPDATE t_order
SET total = (SELECT MAX(amount) FROM t_payment)
WHERE id = 1;
```

## 正例

```sql
-- ✅ 推荐：在应用层分步执行，先查询再更新
-- 步骤一：SELECT MAX(amount) INTO @max_amount FROM t_payment;
-- 步骤二：UPDATE t_order SET total = @max_amount WHERE id = 1;
```
