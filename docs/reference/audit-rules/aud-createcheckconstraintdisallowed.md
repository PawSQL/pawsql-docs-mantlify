---
id: audit-rule-aud-createcheckconstraintdisallowed
title: 禁止使用CHECK约束
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-createcheckconstraintdisallowed
tags:
- audit-rule
- ddl
description: 禁止使用 CHECK 约束，因为在生产环境中 CHECK 约束增加了数据库操作的复杂性和性能开销。每次 INSERT 或 UPDATE 操作都需要对
  CHECK 约束的表达式进行求值验证，在大批量写入场景下这会显著拖慢写入性能。此外，CHECK 约束的逻辑隐藏在数据库层，业务代码和数据库之间存在隐式耦合，排查数据质量问题时不易定位。
localeOf: en-audit-rule-aud-createcheckconstraintdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-createcheckconstraintdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-createcheckconstraintdisallowed |
| 规则名称 | 禁止使用CHECK约束 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用 CHECK 约束，因为在生产环境中 CHECK 约束增加了数据库操作的复杂性和性能开销。每次 INSERT 或 UPDATE 操作都需要对 CHECK 约束的表达式进行求值验证，在大批量写入场景下这会显著拖慢写入性能。此外，CHECK 约束的逻辑隐藏在数据库层，业务代码和数据库之间存在隐式耦合，排查数据质量问题时不易定位。
推荐将数据校验逻辑上移到应用层，通过业务代码或数据校验框架显式执行检查，这样既保证了数据的合法性校验，又保持了系统的可维护性和可观测性。

## 反例

```sql
-- ❌ 不推荐：定义 CHECK 约束，增加写入开销
CREATE TABLE t (
    amount DECIMAL CHECK (amount > 0)
);
```

## 正例

```sql
-- ✅ 推荐：在应用层校验数据合法性
-- 应用层代码示例：if (amount <= 0) throw new ValidationException();
```
