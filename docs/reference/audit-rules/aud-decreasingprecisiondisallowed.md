---
id: audit-rule-aud-decreasingprecisiondisallowed
title: 禁止修改降低字段精度
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-decreasingprecisiondisallowed
tags:
- audit-rule
- ddl
description: 禁止降低字段的精度（如 `DECIMAL(18,6)` 降为 `DECIMAL(10,2)`）。降低精度会造成不可逆的数据舍入或截断，引发财务与统计口径错误。例如，金额数据从小数点后
  6 位降到 2 位，后续的计算和汇总将产生累积误差。此外，精度变更可能触发表重写与索引失效，在高并发环境下带来严重的性能冲击。
localeOf: en-audit-rule-aud-decreasingprecisiondisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-decreasingprecisiondisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-decreasingprecisiondisallowed |
| 规则名称 | 禁止修改降低字段精度 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止降低字段的精度（如 `DECIMAL(18,6)` 降为 `DECIMAL(10,2)`）。降低精度会造成不可逆的数据舍入或截断，引发财务与统计口径错误。例如，金额数据从小数点后 6 位降到 2 位，后续的计算和汇总将产生累积误差。此外，精度变更可能触发表重写与索引失效，在高并发环境下带来严重的性能冲击。
正确做法是先评估影响范围并在应用侧与报表口径完成切换后，通过新增新精度列、分批回填校验、灰度迁移的方式完成调整。

## 反例

```sql
-- ❌ 不推荐：降低精度导致数据截断，财务数据不可逆损毁
ALTER TABLE t MODIFY amount DECIMAL(10,2);  -- 原 DECIMAL(18,6)
```

## 正例

```sql
-- ✅ 推荐：新增列 + 灰度迁移
-- 1. ALTER TABLE t ADD COLUMN amount_new DECIMAL(10,2);
-- 2. UPDATE t SET amount_new = ROUND(amount, 2);
-- 3. 验证切换
```
