---
id: audit-rule-aud-same-table-same-column-comparison
title: 同表同字段比较
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-same-table-same-column-comparison
tags:
- audit-rule
- dml
description: 同表同字段进行比较通常是由于编写错误导致的不合理 SQL 语句，可以从逻辑上重写为更简洁的表达式。例如 `t.c = t.c` 本质上等价于
  `t.c IS NOT NULL`，`t.c <> t.c` 则恒为假值 `1 = 0`。
localeOf: en-audit-rule-aud-same-table-same-column-comparison
subtype: rule
language: zh
translationKey: audit-rule-aud-same-table-same-column-comparison
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-same-table-same-column-comparison |
| 规则名称 | 同表同字段比较 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

同表同字段进行比较通常是由于编写错误导致的不合理 SQL 语句，可以从逻辑上重写为更简洁的表达式。例如 `t.c = t.c` 本质上等价于 `t.c IS NOT NULL`，`t.c <> t.c` 则恒为假值 `1 = 0`。
这类条件往往是开发过程中的疏忽或代码生成工具的产物，不仅增加了查询的复杂度，还可能误导优化器生成低效的执行计划。PawSQL 能够自动识别此类冗余比较并进行优化重写。

## 反例

```sql
-- ❌ 不推荐：同表同字段比较，属于冗余或错误的逻辑
-- 等价关系参考：
-- t.c = t.c       =>  t.c IS NOT NULL
-- t.c >= t.c      =>  t.c IS NOT NULL
-- t.c <= t.c      =>  t.c IS NOT NULL
-- t.c <> t.c      =>  1 = 0 (恒假)
-- t.c > t.c       =>  1 = 0 (恒假)
-- t.c < t.c       =>  1 = 0 (恒假)
SELECT * FROM t_order WHERE order_id = order_id;
```

## 正例

```sql
-- ✅ 推荐：使用正确的语义表达
SELECT * FROM t_order WHERE order_id IS NOT NULL;
```
