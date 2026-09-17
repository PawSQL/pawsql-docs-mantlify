---
id: audit-rule-aud-rulefuncwithcolumninpredicate
title: 索引列上的运算导致索引失效
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-rulefuncwithcolumninpredicate
tags:
- audit-rule
- index
description: 在索引列上进行运算（包括函数调用和 `+`、`-`、`*`、`/` 等算术运算符）将导致索引失效，数据库优化器无法使用该索引，容易退化为全表扫描，产生严重的性能问题。
localeOf: en-audit-rule-aud-rulefuncwithcolumninpredicate
subtype: rule
language: zh
translationKey: audit-rule-aud-rulefuncwithcolumninpredicate
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-rulefuncwithcolumninpredicate |
| 规则名称 | 索引列上的运算导致索引失效 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在索引列上进行运算（包括函数调用和 `+`、`-`、`*`、`/` 等算术运算符）将导致索引失效，数据库优化器无法使用该索引，容易退化为全表扫描，产生严重的性能问题。
正确做法是将运算转换到常量端进行，使索引列保持"裸列"状态。PawSQL 可以帮助自动转换大量函数及运算符相关的操作，将索引列上的运算等价移动到常量侧，从而恢复索引可用性。

## 反例

```sql
-- ❌ 不推荐：索引列参与函数运算，导致索引失效
SELECT * FROM tpch.orders
WHERE ADDDATE(o_orderdate, INTERVAL 31 DAY) = DATE '2019-10-10';
```

## 正例

```sql
-- ✅ 推荐：将运算移至常量端，恢复索引使用
SELECT * FROM tpch.orders
WHERE o_orderdate = SUBDATE(DATE '2019-10-10', INTERVAL 31 DAY);
```
