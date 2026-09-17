---
id: audit-rule-aud-insert-value-count-exceeds-threshold
title: INSERT语句中值的数量超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-insert-value-count-exceeds-threshold
tags:
- audit-rule
- dml
description: 批量插入值可以有效地提升数据插入的效率，但如果单条 INSERT 语句中插入的数据量过多，可能让数据库优化器选择低效的执行计划，导致性能问题。甚至可能超过数据库的内部限制（如
  MySQL 的 `max_allowed_packet`），导致数据库端直接报错。
localeOf: en-audit-rule-aud-insert-value-count-exceeds-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-insert-value-count-exceeds-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-insert-value-count-exceeds-threshold |
| 规则名称 | INSERT语句中值的数量超过阈值 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

批量插入值可以有效地提升数据插入的效率，但如果单条 INSERT 语句中插入的数据量过多，可能让数据库优化器选择低效的执行计划，导致性能问题。甚至可能超过数据库的内部限制（如 MySQL 的 `max_allowed_packet`），导致数据库端直接报错。
PawSQL 检测 INSERT 语句中 VALUES 列表的行数，对超过阈值（默认 500）的批量插入语句进行预警，引导开发者合理控制单次插入的数据量。

## 反例

```sql
-- ❌ 不推荐：单次插入值数量超过阈值（默认 500）
INSERT INTO customer(c_custkey, lastname, firstName)
VALUES (1, 'Dan', 'Mike'),
       (2, 'Chaw', 'Tomas'),
       (3, 'Wang', 'Nancy');
-- ...（超过阈值行数）
```
