---
id: audit-rule-aud-setdatatypedisallowed
title: 禁止使用SET数据类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-setdatatypedisallowed
tags:
- audit-rule
- ddl
description: 禁止使用 SET 数据类型。SET 类型允许在一个列中存储多个集合成员值，看似方便，但其后期修改代价极大——修改集合定义需要重建列，且查询和索引支持有限，容易导致数据维护和查询复杂性增加。SET
  类型同样不是 SQL 标准类型，在不同数据库间的移植性差。
localeOf: en-audit-rule-aud-setdatatypedisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-setdatatypedisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-setdatatypedisallowed |
| 规则名称 | 禁止使用SET数据类型 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用 SET 数据类型。SET 类型允许在一个列中存储多个集合成员值，看似方便，但其后期修改代价极大——修改集合定义需要重建列，且查询和索引支持有限，容易导致数据维护和查询复杂性增加。SET 类型同样不是 SQL 标准类型，在不同数据库间的移植性差。
推荐在业务层通过关联表或位运算实现多选值的存储和管理，将集合逻辑保留在应用层，避免与特定数据库实现耦合。

## 反例

```sql
-- ❌ 不推荐：SET 类型，后期修改需重建列
CREATE TABLE t (
    flags SET('a', 'b', 'c')
);
```

## 正例

```sql
-- ✅ 推荐：使用关联表替代 SET 类型
CREATE TABLE t_flags (
    t_id INT NOT NULL,
    flag VARCHAR(10) NOT NULL,
    PRIMARY KEY (t_id, flag)
);
```
