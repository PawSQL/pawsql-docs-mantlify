---
id: audit-rule-aud-sql-length-exceeds-threshold
title: SQL长度超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-sql-length-exceeds-threshold
tags:
- audit-rule
- dml
description: 过长的 SQL 语句可读性较差，难以维护和调试；同时，过长的 SQL 可能包含过多的表连接或子查询嵌套，容易引发性能问题。在团队协作和代码审查中，冗长的
  SQL 增加了理解成本和出错概率。
localeOf: en-audit-rule-aud-sql-length-exceeds-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-sql-length-exceeds-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-sql-length-exceeds-threshold |
| 规则名称 | SQL长度超过阈值 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

过长的 SQL 语句可读性较差，难以维护和调试；同时，过长的 SQL 可能包含过多的表连接或子查询嵌套，容易引发性能问题。在团队协作和代码审查中，冗长的 SQL 增加了理解成本和出错概率。
PawSQL 检测 SQL 文本的总长度是否超过用户指定的阈值（默认 1024），对超过阈值的 SQL 进行预警，引导开发者将复杂查询拆分为更小、更可维护的单元。

## 反例

```sql
-- ❌ 不推荐：SQL 语句过长，可读性和维护性差
SELECT /* 一段非常长的 SQL 包含多个子查询和复杂逻辑，超过阈值... */;
```

## 正例

```sql
-- ✅ 推荐：将复杂 SQL 拆分为多个步骤或使用 CTE
WITH step1 AS (...), step2 AS (...) SELECT ...;
```
