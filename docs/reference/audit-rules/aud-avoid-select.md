---
id: audit-rule-aud-avoid-select
title: 避免在查询中使用 SELECT *
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-select
tags:
- audit-rule
- dml
- mysql
- postgresql
- oracle
description: 识别查询中的 SELECT *：无用列浪费 IO 与带宽，且阻碍覆盖索引优化；应只列出所需列。
localeOf: en-audit-rule-aud-avoid-select
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-select
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-select |
| 规则名称 | 避免在查询中使用 SELECT * |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | mysql, postgresql, oracle |
| 引入版本 | 8.0.0 |

## 说明

在查询中使用 SELECT * 存在多方面的弊端：可能包含无用的大字段（尤其 TEXT/CLOB 类型），造成不必要的磁盘 IO 与网络传输开销； 表结构增减字段后容易与 ResultMap 不一致，或在 INSERT INTO ... SELECT * 时字段映射出错； 数据库优化器无法进行覆盖索引规划，PawSQL 也无法推荐覆盖索引来优化此类查询；返回不必要的列还会增加内存占用与结果集传输时间。

## 为什么重要

SELECT * 获取了不需要的列，浪费 IO 与网络带宽，并让优化器无法规划覆盖索引。

## 如何修复

始终显式列出查询实际所需的列名。

## 反例

```sql
-- 不推荐：SELECT * 获取了不需要的列，浪费 IO 和网络带宽
SELECT * FROM user WHERE id = 1;
```

## 正例

```sql
-- 推荐：只查询需要的列
SELECT id, name, email FROM user WHERE id = 1;
```

## 关联规则

`AUD-EXPLICIT-COLUMNS`
