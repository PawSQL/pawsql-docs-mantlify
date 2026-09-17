---
id: audit-rule-aud-database-naming-convention
title: 数据库命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-database-naming-convention
tags:
- audit-rule
- ddl
description: 数据库命名规范定义了数据库本身名称的命名规则，通常要求数据库名使用小写字母和连字符（kebab-case）或下划线（snake_case），以保持团队内部的一致性和可读性。不规范的命名会增加沟通成本，降低代码可读性，在跨团队协作和多环境部署时尤其容易引发混淆。
localeOf: en-audit-rule-aud-database-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-database-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-database-naming-convention |
| 规则名称 | 数据库命名规范 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

数据库命名规范定义了数据库本身名称的命名规则，通常要求数据库名使用小写字母和连字符（kebab-case）或下划线（snake_case），以保持团队内部的一致性和可读性。不规范的命名会增加沟通成本，降低代码可读性，在跨团队协作和多环境部署时尤其容易引发混淆。
该规则通过正则表达式来验证数据库名称是否符合团队约定的规范。默认的正则模式要求数据库名称全部使用小写字母，单词之间以连字符分隔。

## 反例

```sql
-- ❌ 不推荐：使用了大写字母，命名不规范
CREATE DATABASE MyDatabase;
```

## 正例

```sql
-- ✅ 推荐：全部小写+连字符，符合命名规范
CREATE DATABASE my_database;
```
