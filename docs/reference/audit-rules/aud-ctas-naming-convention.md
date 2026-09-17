---
id: audit-rule-aud-ctas-naming-convention
title: CTAS 命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-ctas-naming-convention
tags:
- audit-rule
- ddl
description: '`CREATE TABLE AS SELECT`（CTAS）语句创建的数据库对象名称应遵循统一的命名规范。规范的命名有助于团队协作和代码维护，不规范的命名会增加沟通成本、降低代码可读性，在跨团队协作时尤其容易引发误解。此规则要求
  CTAS 创建的表名符合配置的正则表达式模式，确保数据库对象命名的一致性与可追溯性。'
localeOf: en-audit-rule-aud-ctas-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-ctas-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-ctas-naming-convention |
| 规则名称 | CTAS 命名规范 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`CREATE TABLE AS SELECT`（CTAS）语句创建的数据库对象名称应遵循统一的命名规范。规范的命名有助于团队协作和代码维护，不规范的命名会增加沟通成本、降低代码可读性，在跨团队协作时尤其容易引发误解。此规则要求 CTAS 创建的表名符合配置的正则表达式模式，确保数据库对象命名的一致性与可追溯性。

## 反例

```sql
-- ❌ 不推荐：CTAS 创建的表名不符合命名规范
CREATE TABLE MyDatabase (id INT) AS SELECT * FROM t;
```

## 正例

```sql
-- ✅ 推荐：表名符合命名规范（如模式 ^{table}_ts$）
CREATE TABLE t_ts (id INT) AS SELECT * FROM t;
```
