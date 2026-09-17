---
id: audit-rule-aud-index-with-this-name-doest-exists
title: 索引名不存在
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-index-with-this-name-doest-exists
tags:
- audit-rule
- ddl
description: 此规则确保在引用索引时（如 `DROP INDEX`、`ALTER TABLE DROP INDEX` 等操作），该索引确实存在于数据库中。引用不存在的索引会导致
  SQL 执行失败，可能中断批处理任务或部署脚本。
localeOf: en-audit-rule-aud-index-with-this-name-doest-exists
subtype: rule
language: zh
translationKey: audit-rule-aud-index-with-this-name-doest-exists
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-index-with-this-name-doest-exists |
| 规则名称 | 索引名不存在 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则确保在引用索引时（如 `DROP INDEX`、`ALTER TABLE DROP INDEX` 等操作），该索引确实存在于数据库中。引用不存在的索引会导致 SQL 执行失败，可能中断批处理任务或部署脚本。
如果 SQL 语句添加了 `IF EXISTS` 子句，则不会触发此规则告警。建议在执行 DDL 操作前先确认索引状态。

## 反例

```sql
-- ❌ 不推荐：删除不存在的索引，且未加 IF EXISTS
ALTER TABLE orders DROP INDEX idx_nonexistent;
```

## 正例

```sql
-- ✅ 推荐：添加 IF EXISTS 避免报错
ALTER TABLE orders DROP INDEX IF EXISTS idx_nonexistent;
```
