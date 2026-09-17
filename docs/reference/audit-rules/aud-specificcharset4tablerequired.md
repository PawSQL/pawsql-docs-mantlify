---
id: audit-rule-aud-specificcharset4tablerequired
title: 表上应使用指定的字符集
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-specificcharset4tablerequired
tags:
- audit-rule
- ddl
description: 要求表必须使用指定的字符集（如 `utf8mb4`），以确保数据存储的一致性和国际化支持。字符集不一致会导致数据在各表之间迁移、关联或展示时出现乱码问题，特别是在多语言环境和分布式部署中需要特别关注。
localeOf: en-audit-rule-aud-specificcharset4tablerequired
subtype: rule
language: zh
translationKey: audit-rule-aud-specificcharset4tablerequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-specificcharset4tablerequired |
| 规则名称 | 表上应使用指定的字符集 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求表必须使用指定的字符集（如 `utf8mb4`），以确保数据存储的一致性和国际化支持。字符集不一致会导致数据在各表之间迁移、关联或展示时出现乱码问题，特别是在多语言环境和分布式部署中需要特别关注。
默认配置为 `utf8mb4`（MySQL）或 `UTF8`（PostgreSQL），可通过配置调整为符合企业规范的其他字符集。

## 反例

```sql
-- ❌ 不推荐：表字符集不符合规范
CREATE TABLE t (id INT) CHARSET = latin1;
```

## 正例

```sql
-- ✅ 推荐：使用指定的标准字符集
CREATE TABLE t (id INT) CHARSET = utf8mb4;
```
