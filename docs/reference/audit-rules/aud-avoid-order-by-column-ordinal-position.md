---
id: audit-rule-aud-avoid-order-by-column-ordinal-position
title: 避免ORDER BY选择列的序号
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-order-by-column-ordinal-position
tags:
- audit-rule
- dml
description: 避免 ORDER BY 用列序号（SELECT 顺序变化会悄然改变语义）；直接用列名或表达式。
localeOf: en-audit-rule-aud-avoid-order-by-column-ordinal-position
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-order-by-column-ordinal-position
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-order-by-column-ordinal-position |
| 规则名称 | 避免ORDER BY选择列的序号 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在进行 SQL 开发时，可以使用 SELECT 列表中列的序号（如 `ORDER BY 1, 2`）来代替具体的列名或表达式。这种写法虽然给开发人员带来了一定的书写便利，但会严重降低代码的可读性和可维护性——当 SELECT 列表中的列顺序发生变化时，ORDER BY 的语义会随之改变，而这种改变对代码审阅者来说极难察觉，容易引入隐蔽的 bug。
建议始终在 ORDER BY 中使用明确的列名或表达式，使 SQL 意图清晰可见，也便于后续的代码维护和重构。

## 反例

```sql
-- ❌ 不推荐：使用列序号进行 ORDER BY，可读性差
SELECT id, name FROM t ORDER BY 2;
```

## 正例

```sql
-- ✅ 推荐：使用明确的列名进行 ORDER BY
SELECT id, name FROM t ORDER BY name;
```
