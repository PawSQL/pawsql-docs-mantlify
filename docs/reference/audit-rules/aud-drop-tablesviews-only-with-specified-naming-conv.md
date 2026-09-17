---
id: audit-rule-aud-drop-tablesviews-only-with-specified-naming-conv
title: 只能删除指定命名规范的表和视图
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-drop-tablesviews-only-with-specified-naming-conv
tags:
- audit-rule
- ddl
description: 此规则限制只能删除符合特定命名规范的表和视图，目的是将清理范围限定在临时表、备份表、中间表等可识别对象上，避免误删核心业务数据并降低依赖断裂风险。
localeOf: en-audit-rule-aud-drop-tablesviews-only-with-specified-naming-conv
subtype: rule
language: zh
translationKey: audit-rule-aud-drop-tablesviews-only-with-specified-naming-conv
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-drop-tablesviews-only-with-specified-naming-conv |
| 规则名称 | 只能删除指定命名规范的表和视图 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则限制只能删除符合特定命名规范的表和视图，目的是将清理范围限定在临时表、备份表、中间表等可识别对象上，避免误删核心业务数据并降低依赖断裂风险。
通过配置正则表达式（如 `.*_del$`），只有以特定后缀结尾的表和视图才允许被直接删除。对于需要下线的核心业务表，应通过重命名将其纳入删除白名单，待确认无影响后再进行删除操作。

## 反例

```sql
-- ❌ 不推荐：删除不符合命名规范的表（可能误删核心业务表）
DROP TABLE t_user;
```

## 正例

```sql
-- ✅ 推荐：只删除符合删除命名规范的表（如以 _del 结尾）
DROP TABLE t_user_del;
```
