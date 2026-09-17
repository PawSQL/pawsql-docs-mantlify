---
id: audit-rule-aud-enumdatatypedisallowed
title: 禁止使用ENUM数据类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-enumdatatypedisallowed
tags:
- audit-rule
- ddl
description: 禁止使用 ENUM 数据类型。ENUM 不是 SQL 标准类型，在不同数据库间的移植性极差。后期如需修改或新增枚举值，通常需要重建整张表（`ALTER
  TABLE ... MODIFY` 可能触发全表复制），代价巨大。此外，ENUM 的排序基于内部枚举索引而非字面量值，可能导致非预期的排序结果，带来隐蔽的业务逻辑错误。
localeOf: en-audit-rule-aud-enumdatatypedisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-enumdatatypedisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-enumdatatypedisallowed |
| 规则名称 | 禁止使用ENUM数据类型 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用 ENUM 数据类型。ENUM 不是 SQL 标准类型，在不同数据库间的移植性极差。后期如需修改或新增枚举值，通常需要重建整张表（`ALTER TABLE ... MODIFY` 可能触发全表复制），代价巨大。此外，ENUM 的排序基于内部枚举索引而非字面量值，可能导致非预期的排序结果，带来隐蔽的业务逻辑错误。
推荐使用 `VARCHAR` 配合应用层枚举校验，或使用 `TINYINT` 配合字典表来管理枚举值。这样既保持了数据约束能力，又避免了数据库层面的耦合和移植风险。

## 反例

```sql
-- ❌ 不推荐：ENUM 类型，扩展性差，非 SQL 标准
CREATE TABLE t (
    status ENUM('active', 'inactive')
);
```

## 正例

```sql
-- ✅ 推荐：使用 VARCHAR 配合应用层校验
CREATE TABLE t (
    status VARCHAR(20)
);

-- ✅ 推荐：使用 TINYINT 配合字典表
CREATE TABLE t (
    status TINYINT NOT NULL
);
```
