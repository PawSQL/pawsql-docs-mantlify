---
id: audit-rule-aud-duplicatedobjectnameswithkeywords
title: 禁止对象名称与关键字重名
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-duplicatedobjectnameswithkeywords
tags:
- audit-rule
- ddl
description: 禁止使用数据库关键字作为对象名称（如表名、列名、索引名、存储过程名、函数名、视图名等）。使用保留关键字作为对象名会导致潜在的 SQL 语法冲突和解析歧义——即使当前数据库版本允许通过反引号或双引号转义使用这些名称，后续数据库版本升级、迁移到其他数据库、或在新开发者编写
  SQL 时忽略转义，都可能引发难以排查的语法错误或逻辑意外。
localeOf: en-audit-rule-aud-duplicatedobjectnameswithkeywords
subtype: rule
language: zh
translationKey: audit-rule-aud-duplicatedobjectnameswithkeywords
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-duplicatedobjectnameswithkeywords |
| 规则名称 | 禁止对象名称与关键字重名 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用数据库关键字作为对象名称（如表名、列名、索引名、存储过程名、函数名、视图名等）。使用保留关键字作为对象名会导致潜在的 SQL 语法冲突和解析歧义——即使当前数据库版本允许通过反引号或双引号转义使用这些名称，后续数据库版本升级、迁移到其他数据库、或在新开发者编写 SQL 时忽略转义，都可能引发难以排查的语法错误或逻辑意外。
此外，关键字命名的对象在 ORM 框架和代码生成工具中通常需要额外的转义处理，增加了开发和维护的复杂度。应选择有业务语义且不与 SQL 关键字冲突的名称。

## 反例

```sql
-- ❌ 不推荐：使用保留关键字作为对象名，语法冲突风险
CREATE TABLE `order` (id INT);
CREATE TABLE `group` (id INT);
```

## 正例

```sql
-- ✅ 推荐：使用有业务语义且非关键字的名称
CREATE TABLE orders (id INT);
CREATE TABLE user_groups (id INT);
```
