---
id: audit-rule-aud-no-todatetotimestamp-on-partition-key-in-filter-
title: 分区键上的过滤条件禁止使用 TO_DATE/TO_TIMESTAMP 函数
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-no-todatetotimestamp-on-partition-key-in-filter-
tags:
- audit-rule
- dml
description: 在 TDSQL 分布式实例或其他支持分区的数据库中，如果对分区键使用 `TO_DATE` 或 `TO_TIMESTAMP` 等日期转换函数，可能导致分区裁剪失效，使得查询扫描所有分区子表，而非仅扫描目标分区，严重影响查询性能。
localeOf: en-audit-rule-aud-no-todatetotimestamp-on-partition-key-in-filter-
subtype: rule
language: zh
translationKey: audit-rule-aud-no-todatetotimestamp-on-partition-key-in-filter-
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-no-todatetotimestamp-on-partition-key-in-filter- |
| 规则名称 | 分区键上的过滤条件禁止使用 TO_DATE/TO_TIMESTAMP 函数 |
| 类别 | dml（数据操作） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 TDSQL 分布式实例或其他支持分区的数据库中，如果对分区键使用 `TO_DATE` 或 `TO_TIMESTAMP` 等日期转换函数，可能导致分区裁剪失效，使得查询扫描所有分区子表，而非仅扫描目标分区，严重影响查询性能。
正确的做法是避免对分区键字段应用任何函数，将函数应用于常量一侧，或使用数据库支持的隐式类型转换，以确保优化器能够准确定位目标分区。

## 反例

```sql
-- ❌ 不推荐：对分区键使用日期转换函数，分区裁剪失效
SELECT * FROM t_log
WHERE TO_DATE(log_date, 'YYYY-MM-DD') = '2024-01-01';
```

## 正例

```sql
-- ✅ 推荐：直接比较或常量侧函数，分区裁剪生效
SELECT * FROM t_log
WHERE log_date = '2024-01-01';
```
