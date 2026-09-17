---
id: audit-rule-aud-if-exists-required-for-dropping-objects
title: 删除表/视图/索引时需指定 IF EXISTS
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-if-exists-required-for-dropping-objects
tags:
- audit-rule
- ddl
description: 删除表、视图或索引时要求使用 `IF EXISTS` 子句，以避免在对象不存在时 DDL 报错中断发布流程。这是提升 DDL 脚本幂等性和跨环境执行稳定性的重要实践。
localeOf: en-audit-rule-aud-if-exists-required-for-dropping-objects
subtype: rule
language: zh
translationKey: audit-rule-aud-if-exists-required-for-dropping-objects
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-if-exists-required-for-dropping-objects |
| 规则名称 | 删除表/视图/索引时需指定 IF EXISTS |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

删除表、视图或索引时要求使用 `IF EXISTS` 子句，以避免在对象不存在时 DDL 报错中断发布流程。这是提升 DDL 脚本幂等性和跨环境执行稳定性的重要实践。
如果不添加 `IF EXISTS`，当对象不存在时 `DROP` 语句会直接报错，导致发布流水线中断。使用 `IF EXISTS` 可以确保脚本在任何环境状态下都能安全执行，同时应配合依赖分析和变更审计防止误删仍被使用的对象。

## 反例

```sql
-- ❌ 不推荐：未使用 IF EXISTS，对象不存在时会报错
DROP TABLE important_table;
```

## 正例

```sql
-- ✅ 推荐：使用 IF EXISTS，确保安全删除
DROP TABLE IF EXISTS important_table;
```
