---
id: audit-rule-aud-dml-affected-rows-must-not-exceed-threshold
title: 数据操作语句影响的行数不得超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-dml-affected-rows-must-not-exceed-threshold
tags:
- audit-rule
- dml
description: 单个事务中INSERT、UPDATE、DELETE等DML操作影响的行数过多（即"大事务"）会带来一系列严重问题：锁定大量记录，阻塞其他会话的正常操作；产生海量Binlog/WAL日志，导致主从同步延迟；事务回滚耗时极长，可能造成系统长时间不可用。应当通过将大事务拆分为小批次操作来控制每批影响的行数。
localeOf: en-audit-rule-aud-dml-affected-rows-must-not-exceed-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-dml-affected-rows-must-not-exceed-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-dml-affected-rows-must-not-exceed-threshold |
| 规则名称 | 数据操作语句影响的行数不得超过阈值 |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

单个事务中INSERT、UPDATE、DELETE等DML操作影响的行数过多（即"大事务"）会带来一系列严重问题：锁定大量记录，阻塞其他会话的正常操作；产生海量Binlog/WAL日志，导致主从同步延迟；事务回滚耗时极长，可能造成系统长时间不可用。应当通过将大事务拆分为小批次操作来控制每批影响的行数。
该规则对DML语句的影响行数进行预估，当预估影响行数超过预设阈值时触发告警。建议联机交易场景设置阈值5,000行，夜间批量作业可适当放宽至100,000行。

## 反例

```sql
-- ❌ 不推荐：一次性删除100万行，大事务可能锁表并产生海量日志
DELETE FROM log_table WHERE create_date < '2023-01-01';
```

## 正例

```sql
-- ✅ 推荐：分批删除，控制每批影响行数在阈值内
DELETE FROM log_table WHERE create_date < '2023-01-01' LIMIT 5000;
-- 反复执行上述语句，直到受影响行数为0
```
