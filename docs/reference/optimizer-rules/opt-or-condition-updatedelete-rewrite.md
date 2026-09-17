---
id: optimizer-rule-opt-or-condition-updatedelete-rewrite
title: OR条件的UPDELETE重写
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-or-condition-updatedelete-rewrite
tags:
- optimizer-rule
- rewrite
description: 当 UPDATE 或 DELETE 语句的 WHERE 条件使用 `OR` 连接不同字段时，数据库优化器可能无法有效利用索引来完成数据定位。OR
  条件可能导致全表扫描执行 UPDATE/DELETE，在大数据量下锁表时间极长，严重影响并发性能。
localeOf: en-optimizer-rule-opt-or-condition-updatedelete-rewrite
subtype: rule
language: zh
translationKey: optimizer-rule-opt-or-condition-updatedelete-rewrite
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-or-condition-updatedelete-rewrite |
| 规则名称 | OR条件的UPDELETE重写 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当 UPDATE 或 DELETE 语句的 WHERE 条件使用 `OR` 连接不同字段时，数据库优化器可能无法有效利用索引来完成数据定位。OR 条件可能导致全表扫描执行 UPDATE/DELETE，在大数据量下锁表时间极长，严重影响并发性能。
PawSQL 自动检测此类模式，将包含 OR 条件的 UPDATE/DELETE 语句拆分为多条独立的语句，使每条语句可以独立利用对应字段上的索引，缩小锁范围并提升执行效率。

## 反例

```sql
-- ❌ 不推荐：OR 连接不同字段，UPDATE 可能全表扫描
DELETE FROM lineitem
WHERE l_shipdate = DATE '2010-12-01' OR l_partkey < 100;
```

## 正例

```sql
-- ✅ 推荐：拆分为多条语句，各分支可独立利用索引
DELETE FROM lineitem WHERE l_shipdate = DATE '2010-12-01';
DELETE FROM lineitem WHERE l_partkey < 100;
```
