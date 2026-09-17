---
id: audit-rule-aud-object-naming-convention
title: 对象命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-object-naming-convention
tags:
- audit-rule
- ddl
description: 对象命名规范定义了数据库对象（包括表、列、索引、约束）的命名规则，通常要求对象名称使用小写字母和下划线（snake_case），以保持团队内部的一致性和代码可读性。不规范的命名会增加沟通成本，降低代码可读性，在跨团队协作时尤其容易引发误解。
localeOf: en-audit-rule-aud-object-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-object-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-object-naming-convention |
| 规则名称 | 对象命名规范 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对象命名规范定义了数据库对象（包括表、列、索引、约束）的命名规则，通常要求对象名称使用小写字母和下划线（snake_case），以保持团队内部的一致性和代码可读性。不规范的命名会增加沟通成本，降低代码可读性，在跨团队协作时尤其容易引发误解。
该规则通过正则表达式来验证对象命名是否符合团队约定的规范。默认的正则模式要求对象名称全部使用小写字母，单词之间以下划线分隔，不包含特殊字符。

## 反例

```sql
-- ❌ 不推荐：使用了大写字母，命名不规范
CREATE TABLE MyDatabase (id INT);
```

## 正例

```sql
-- ✅ 推荐：全部小写+下划线，符合命名规范
CREATE TABLE my_database (id INT);
```
