---
id: audit-rule-aud-autoincrement-column-naming-convention
title: 自增列命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-autoincrement-column-naming-convention
tags:
- audit-rule
- ddl
description: 自增列命名应遵循统一模式（默认 `id`，正则 `^id$`）；不合规仅提示，不阻断 DDL。
localeOf: en-audit-rule-aud-autoincrement-column-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-autoincrement-column-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-autoincrement-column-naming-convention |
| 规则名称 | 自增列命名规范 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则定义了自增列的命名规范，要求自增列有一个明确的命名模式，通常为 `id`，以便于团队快速识别自增列。统一的自增列命名在 ORM 框架集成、自动化代码生成和数据库维护中能显著提升效率。
默认命名模式为 `id`（或正则 `^id$`），可通过配置调整为其他模式。不符合命名规范的自增列会在审核时触发提示，但不会阻止 DDL 执行。

## 反例

```sql
-- ❌ 不推荐：自增列命名不符合规范
CREATE TABLE orders (order_auto_id INT AUTO_INCREMENT PRIMARY KEY);
```

## 正例

```sql
-- ✅ 推荐：遵循 id 命名规范
CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY);
```
