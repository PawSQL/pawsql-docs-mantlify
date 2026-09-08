---
id: audit-rule-aud-avoid-duplicate-table-aliases
title: 避免表引用使用重复的别名
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-duplicate-table-aliases
tags:
- audit-rule
- dml
description: 避免表引用别名重复或与库表名冲突（可读性差）；每个表引用用唯一且有语义的别名。
localeOf: en-audit-rule-aud-avoid-duplicate-table-aliases
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-duplicate-table-aliases
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-duplicate-table-aliases |
| 规则名称 | 避免表引用使用重复的别名 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

查询语句中存在别名相同的表引用或子查询，或者表的别名与数据库中其他表名相同，会导致代码可读性急剧恶化——阅读者很难分辨每个列引用究竟来自哪张表，也不利于后续的代码维护和问题排查。
在同一个查询块中，每个表引用应始终使用唯一且语义明确的别名。这不仅是一种良好的编码习惯，也是保障 SQL 在复杂业务场景下可维护性的基本要求。

## 反例

```sql
-- ❌ 不推荐：表别名重复，无法区分列来源
SELECT * FROM t a, t a;
```

## 正例

```sql
-- ✅ 推荐：使用唯一且语义明确的别名
SELECT * FROM t t1, t t2 WHERE t1.id = t2.parent_id;
```
