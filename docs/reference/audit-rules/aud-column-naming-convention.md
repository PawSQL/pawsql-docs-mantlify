---
id: audit-rule-aud-column-naming-convention
title: 列名命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-column-naming-convention
tags:
- audit-rule
- ddl
description: 列名应统一小写下划线 snake_case；大写/特殊字符/关键字/中文命名增加维护与迁移成本。
localeOf: en-audit-rule-aud-column-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-column-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-column-naming-convention |
| 规则名称 | 列名命名规范 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

列名命名规范要求数据库对象名称遵循统一规范，便于团队协作和代码维护。通常要求列名使用小写字母和下划线（snake_case），以保持一致性、可读性和跨平台兼容性。
不规范的列名（如使用大写字母、特殊字符、关键字或中文字符）会增加沟通成本，降低代码可读性，在跨团队协作和跨平台迁移时尤其容易引发问题。

## 反例

```sql
-- ❌ 不推荐：列名使用大写、中文或包含特殊字符
CREATE TABLE t_user (
    "UserID"    INT,
    "用户姓名"  VARCHAR(50)
);
```

## 正例

```sql
-- ✅ 推荐：使用小写字母和下划线
CREATE TABLE t_user (
    user_id   INT,
    user_name VARCHAR(50)
);
```
