---
id: audit-rule-aud-commentsontablerequired
title: 表必须有注释
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-commentsontablerequired
tags:
- audit-rule
- ddl
description: 建表时应写表注释（业务用途/数据来源/生命周期），适用于 MySQL 等支持表注释的库。
localeOf: en-audit-rule-aud-commentsontablerequired
subtype: rule
language: zh
translationKey: audit-rule-aud-commentsontablerequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-commentsontablerequired |
| 规则名称 | 表必须有注释 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求在创建表时必须为表添加注释（COMMENT），详细的表注释可以帮助开发者和维护者快速理解表的用途、字段含义和业务逻辑，提高代码可读性和团队协作效率。在生产环境中，缺少注释的表在交接和维护时会显著增加沟通成本。
此规则适用于 MySQL 等支持表注释的数据库。建议在表注释中说明表的业务用途、数据来源和生命周期。

## 反例

```sql
-- ❌ 不推荐：表缺少注释
CREATE TABLE t (id INT);
```

## 正例

```sql
-- ✅ 推荐：创建表时添加注释
CREATE TABLE t (id INT) COMMENT = '用户信息表，记录系统注册用户的基本资料';
```
