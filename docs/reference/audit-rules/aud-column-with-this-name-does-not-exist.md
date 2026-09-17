---
id: audit-rule-aud-column-with-this-name-does-not-exist
title: 使用不存在的列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-column-with-this-name-does-not-exist
tags:
- audit-rule
- unknown
description: 引用表中不存在的列是一个严重的语法错误，会导致 SQL 语句执行失败。此类问题通常由字段名拼写错误、数据库结构变更后未同步更新代码、或表结构与预期不一致等原因引起。
localeOf: en-audit-rule-aud-column-with-this-name-does-not-exist
subtype: rule
language: zh
translationKey: audit-rule-aud-column-with-this-name-does-not-exist
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-column-with-this-name-does-not-exist |
| 规则名称 | 使用不存在的列 |
| 类别 | unknown（待归类（产品核对中）） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

引用表中不存在的列是一个严重的语法错误，会导致 SQL 语句执行失败。此类问题通常由字段名拼写错误、数据库结构变更后未同步更新代码、或表结构与预期不一致等原因引起。
在开发阶段尽早发现并修正此类问题，可以避免在运行时出现不必要的错误中断，减少排查成本。该规则对所有类型的 SQL 语句生效，确保任何引用的列名在目标表中确实存在。

## 反例

```sql
-- ❌ 不推荐：引用了表中不存在的列
SELECT user_namme FROM t_user;
```

## 正例

```sql
-- ✅ 推荐：确保列名拼写正确且存在
SELECT user_name FROM t_user;
```
