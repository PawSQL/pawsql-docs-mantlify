---
id: audit-rule-aud-oneidentitycolumnallowed
title: 每个表只能有一个自增列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-oneidentitycolumnallowed
tags:
- audit-rule
- ddl
description: 每个表只能包含一个自增列（`AUTO_INCREMENT` / `IDENTITY` / `SERIAL`），这是大多数关系数据库的硬性限制。自增列用于生成唯一、递增的数值型标识，如果在同一张表中定义多个自增列，会导致表创建失败或运行时数据异常——例如
  MySQL InnoDB/MyISAM 引擎不允许存在多个自增字段，PostgreSQL 中一张表也只能有一个 `SERIAL` 类型列。
localeOf: en-audit-rule-aud-oneidentitycolumnallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-oneidentitycolumnallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-oneidentitycolumnallowed |
| 规则名称 | 每个表只能有一个自增列 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

每个表只能包含一个自增列（`AUTO_INCREMENT` / `IDENTITY` / `SERIAL`），这是大多数关系数据库的硬性限制。自增列用于生成唯一、递增的数值型标识，如果在同一张表中定义多个自增列，会导致表创建失败或运行时数据异常——例如 MySQL InnoDB/MyISAM 引擎不允许存在多个自增字段，PostgreSQL 中一张表也只能有一个 `SERIAL` 类型列。
合理的自增列设计应当结合主键规范：每一张表只保留一个自增列作为物理行标识，其他需要递增编号的场景应通过序列（Sequence）或应用层逻辑实现。

## 反例

```sql
-- ❌ 不推荐：同一张表定义多个自增列，MySQL 会直接拒绝
CREATE TABLE t (
    id1 INT AUTO_INCREMENT,
    id2 INT AUTO_INCREMENT
);
```

## 正例

```sql
-- ✅ 推荐：只保留一个自增列作为主键
CREATE TABLE t (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(32) NOT NULL
);
```
