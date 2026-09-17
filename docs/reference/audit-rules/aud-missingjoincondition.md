---
id: audit-rule-aud-missingjoincondition
title: 表连接缺少连接条件
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-missingjoincondition
tags:
- audit-rule
- dml
description: 表连接缺少连接条件会导致结果集变成两个表的笛卡尔积，数据量随两表行数乘积增长，极易造成结果集膨胀失控，且极大概率不符合开发者的预期。
localeOf: en-audit-rule-aud-missingjoincondition
subtype: rule
language: zh
translationKey: audit-rule-aud-missingjoincondition
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-missingjoincondition |
| 规则名称 | 表连接缺少连接条件 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

表连接缺少连接条件会导致结果集变成两个表的笛卡尔积，数据量随两表行数乘积增长，极易造成结果集膨胀失控，且极大概率不符合开发者的预期。
PawSQL 会检查此类写法并发出告警提醒。建议在所有 JOIN 语句中明确写出 ON 条件，或使用 INNER JOIN / LEFT JOIN 语法替代逗号分隔的隐式连接。

## 反例

```sql
-- ❌ 不推荐：表连接缺少连接条件，产生笛卡尔积
SELECT *
FROM orders o
JOIN customer c;

-- ❌ 不推荐：隐式连接缺少 WHERE 条件
SELECT * FROM orders, customer;
```

## 正例

```sql
-- ✅ 推荐：明确指定连接条件
SELECT *
FROM orders o
JOIN customer c ON o.customer_id = c.id;
```
