---
id: audit-rule-aud-distribution-key-must-have-not-null-constraint
title: 分片表的分布键应设置非空约束
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-distribution-key-must-have-not-null-constraint
tags:
- audit-rule
- ddl
description: 分布键的值用于计算数据所在的分片，其值不能为 `NULL`。如果分布键允许 `NULL` 值，插入 `NULL` 分布键的数据时会直接报错，导致业务中断。因此，应在表设计时为分布键字段明确添加
  `NOT NULL` 约束，从数据库层面杜绝 `NULL` 值的产生。
localeOf: en-audit-rule-aud-distribution-key-must-have-not-null-constraint
subtype: rule
language: zh
translationKey: audit-rule-aud-distribution-key-must-have-not-null-constraint
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-distribution-key-must-have-not-null-constraint |
| 规则名称 | 分片表的分布键应设置非空约束 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

分布键的值用于计算数据所在的分片，其值不能为 `NULL`。如果分布键允许 `NULL` 值，插入 `NULL` 分布键的数据时会直接报错，导致业务中断。因此，应在表设计时为分布键字段明确添加 `NOT NULL` 约束，从数据库层面杜绝 `NULL` 值的产生。
设置非空约束不仅是技术层面的防护，也是业务语义的明确表达——分布键字段作为数据路由的锚点，其值必须是有意义的。

## 反例

```sql
-- ❌ 不推荐：分布键字段未设置非空约束，NULL 值会导致插入报错
CREATE TABLE t_order (
    id   INT,
    name VARCHAR(50)
) shardkey = id;
```

## 正例

```sql
-- ✅ 推荐：分布键字段设置 NOT NULL 约束
CREATE TABLE t_order (
    id   INT NOT NULL,
    name VARCHAR(50)
) shardkey = id;
```
