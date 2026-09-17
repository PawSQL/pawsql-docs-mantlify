---
id: audit-rule-aud-drop-columns-only-with-specified-naming-conventi
title: 只能删除指定命名规范的列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-drop-columns-only-with-specified-naming-conventi
tags:
- audit-rule
- ddl
description: 此规则限制只能删除符合特定命名规范的列，目的是将变更范围限定在明确标识为临时、冗余或过渡用途的字段上，避免误删核心业务数据并降低依赖断裂与历史任务失败的风险。
localeOf: en-audit-rule-aud-drop-columns-only-with-specified-naming-conventi
subtype: rule
language: zh
translationKey: audit-rule-aud-drop-columns-only-with-specified-naming-conventi
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-drop-columns-only-with-specified-naming-conventi |
| 规则名称 | 只能删除指定命名规范的列 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则限制只能删除符合特定命名规范的列，目的是将变更范围限定在明确标识为临时、冗余或过渡用途的字段上，避免误删核心业务数据并降低依赖断裂与历史任务失败的风险。
通过配置正则表达式（如 `.*_del$`），只有以特定后缀结尾的列才允许被删除，从流程上杜绝了误操作的可能性。在需要清理历史字段时，应先通过重命名将其纳入删除白名单，再进行删除操作。

## 反例

```sql
-- ❌ 不推荐：删除不符合命名规范的列（可能误删核心字段）
ALTER TABLE t_user DROP COLUMN user_name;
```

## 正例

```sql
-- ✅ 推荐：只删除符合删除命名规范的列（如以 _del 结尾）
ALTER TABLE t_user DROP COLUMN user_name_del;
```
