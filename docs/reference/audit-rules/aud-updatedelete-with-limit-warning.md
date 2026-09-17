---
id: audit-rule-aud-updatedelete-with-limit-warning
title: UPDATE/DELETE操作使用 LIMIT 子句
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-updatedelete-with-limit-warning
tags:
- audit-rule
- dml
description: 在 `UPDATE` 或 `DELETE` 语句中使用 `LIMIT` 子句会导致不可预测的结果。由于缺少 `ORDER BY` 确定处理顺序，`LIMIT`
  更新的具体行是随机的（取决于数据库内部的物理存储顺序），每次执行可能影响不同的行。这种行为使得数据库状态不可预测，难以调试和回滚。
localeOf: en-audit-rule-aud-updatedelete-with-limit-warning
subtype: rule
language: zh
translationKey: audit-rule-aud-updatedelete-with-limit-warning
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-updatedelete-with-limit-warning |
| 规则名称 | UPDATE/DELETE操作使用 LIMIT 子句 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 `UPDATE` 或 `DELETE` 语句中使用 `LIMIT` 子句会导致不可预测的结果。由于缺少 `ORDER BY` 确定处理顺序，`LIMIT` 更新的具体行是随机的（取决于数据库内部的物理存储顺序），每次执行可能影响不同的行。这种行为使得数据库状态不可预测，难以调试和回滚。
PawSQL 检测此类写法并进行预警，引导开发者使用明确的 WHERE 条件来精确控制需要变更的数据行。

## 反例

```sql
-- ❌ 不推荐：LIMIT 导致不确定哪些行被更新/删除
UPDATE t SET status = 1 WHERE created_at < '2024-01-01' LIMIT 100;

-- ❌ 不推荐：DELETE + LIMIT 同样不确定
DELETE FROM t WHERE status = 0 LIMIT 50;
```

## 正例

```sql
-- ✅ 推荐：使用明确的 WHERE 条件精确控制变更范围
UPDATE t SET status = 1 WHERE created_at < '2024-01-01' AND id IN (
    SELECT id FROM t WHERE created_at < '2024-01-01' ORDER BY id LIMIT 100
);
```
