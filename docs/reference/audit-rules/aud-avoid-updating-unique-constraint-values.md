---
id: audit-rule-aud-avoid-updating-unique-constraint-values
title: 避免更新唯一约束的值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-updating-unique-constraint-values
tags:
- audit-rule
- dml
description: 对具有唯一性约束的列进行值更新时，数据库需要对新的值进行全表唯一性检查，以确保更新后的值不与已有数据冲突。在表数据量非常大的情况下，这一唯一性校验操作可能非常昂贵——尤其是在唯一约束列上没有索引或索引效率不高时，可能需要扫描大量数据。
localeOf: en-audit-rule-aud-avoid-updating-unique-constraint-values
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-updating-unique-constraint-values
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-updating-unique-constraint-values |
| 规则名称 | 避免更新唯一约束的值 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对具有唯一性约束的列进行值更新时，数据库需要对新的值进行全表唯一性检查，以确保更新后的值不与已有数据冲突。在表数据量非常大的情况下，这一唯一性校验操作可能非常昂贵——尤其是在唯一约束列上没有索引或索引效率不高时，可能需要扫描大量数据。
此外，如果该唯一约束列被其他表作为外键引用，更新操作还会触发级联检查或级联更新，进一步放大性能影响。因此，具有唯一约束的列在业务设计中应尽量保持稳定不变。

## 反例

```sql
-- ❌ 不推荐：更新唯一约束列的值，触发全表唯一性校验
UPDATE user SET email = 'new_email@example.com' WHERE id = 100;
```

## 正例

```sql
-- ✅ 推荐：唯一约束列尽量不更新；如必须变更，确保在低峰期执行
```
