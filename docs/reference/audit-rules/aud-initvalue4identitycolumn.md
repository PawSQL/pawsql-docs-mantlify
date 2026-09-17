---
id: audit-rule-aud-initvalue4identitycolumn
title: 自增列的初始值应从0/1开始
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-initvalue4identitycolumn
tags:
- audit-rule
- ddl
description: 自增列的初始值应当从 0 或 1 开始，以确保生成的键值遵循统一约定。从 0 或 1 开始可以保持一致性，便于理解和管理，避免因初始值不统一导致的混淆——例如某些环境从
  1 开始、另一些从 1000 开始，数据迁移和对比时会产生不必要的差异。
localeOf: en-audit-rule-aud-initvalue4identitycolumn
subtype: rule
language: zh
translationKey: audit-rule-aud-initvalue4identitycolumn
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-initvalue4identitycolumn |
| 规则名称 | 自增列的初始值应从0/1开始 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

自增列的初始值应当从 0 或 1 开始，以确保生成的键值遵循统一约定。从 0 或 1 开始可以保持一致性，便于理解和管理，避免因初始值不统一导致的混淆——例如某些环境从 1 开始、另一些从 1000 开始，数据迁移和对比时会产生不必要的差异。
此规则适用于 `CREATE TABLE` 中自增列的定义。默认建议从 1 开始，可通过配置调整。

## 反例

```sql
-- ❌ 不推荐：自增起始值不规范，从 100 开始
CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY) AUTO_INCREMENT = 100;
```

## 正例

```sql
-- ✅ 推荐：自增从 0 或 1 开始
CREATE TABLE t (id INT AUTO_INCREMENT PRIMARY KEY) AUTO_INCREMENT = 1;
```
