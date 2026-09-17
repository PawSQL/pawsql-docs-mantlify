---
id: audit-rule-aud-if-not-exists-required-for-creating-objects
title: 创建表/视图/索引时需指定 IF NOT EXISTS
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-if-not-exists-required-for-creating-objects
tags:
- audit-rule
- ddl
description: 创建表、视图或索引时要求使用 `IF NOT EXISTS` 子句，以避免在重复执行部署脚本或多环境回放时因对象已存在而报错中断变更流程。这是提升
  DDL 脚本幂等性和自动化发布稳定性的重要实践。
localeOf: en-audit-rule-aud-if-not-exists-required-for-creating-objects
subtype: rule
language: zh
translationKey: audit-rule-aud-if-not-exists-required-for-creating-objects
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-if-not-exists-required-for-creating-objects |
| 规则名称 | 创建表/视图/索引时需指定 IF NOT EXISTS |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

创建表、视图或索引时要求使用 `IF NOT EXISTS` 子句，以避免在重复执行部署脚本或多环境回放时因对象已存在而报错中断变更流程。这是提升 DDL 脚本幂等性和自动化发布稳定性的重要实践。
如果不添加 `IF NOT EXISTS`，当对象已存在时 `CREATE` 语句会直接报错，导致整个部署流程失败。启用此规则可以确保脚本在多次执行时的行为一致，同时仍需配合结构一致性校验防止"存在但定义不一致"的隐性问题。

## 反例

```sql
-- ❌ 不推荐：未使用 IF NOT EXISTS，重复执行会报错
CREATE TABLE t_user (
    id   BIGINT,
    name VARCHAR(50)
);
```

## 正例

```sql
-- ✅ 推荐：使用 IF NOT EXISTS，确保幂等性
CREATE TABLE IF NOT EXISTS t_user (
    id   BIGINT,
    name VARCHAR(50)
);
```
