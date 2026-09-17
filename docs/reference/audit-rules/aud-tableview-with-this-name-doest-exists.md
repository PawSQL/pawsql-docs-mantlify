---
id: audit-rule-aud-tableview-with-this-name-doest-exists
title: 表/视图名不存在
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-tableview-with-this-name-doest-exists
tags:
- audit-rule
- ddl
description: 此规则确保在删除或操作表/视图时，指定的对象确实存在于数据库中。尝试删除不存在的对象会导致 SQL 执行失败，可能中断批处理脚本或自动化部署流程。
localeOf: en-audit-rule-aud-tableview-with-this-name-doest-exists
subtype: rule
language: zh
translationKey: audit-rule-aud-tableview-with-this-name-doest-exists
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-tableview-with-this-name-doest-exists |
| 规则名称 | 表/视图名不存在 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则确保在删除或操作表/视图时，指定的对象确实存在于数据库中。尝试删除不存在的对象会导致 SQL 执行失败，可能中断批处理脚本或自动化部署流程。
如果 SQL 语句添加了 `IF EXISTS` 子句，则不会触发此规则告警。建议在 DDL 脚本中始终添加 `IF EXISTS` 以提高脚本的健壮性。

## 反例

```sql
-- ❌ 不推荐：删除不存在的表/视图，且未加 IF EXISTS
DROP TABLE nonexistent_table;
```

## 正例

```sql
-- ✅ 推荐：添加 IF EXISTS 避免报错
DROP TABLE IF EXISTS nonexistent_table;
```
