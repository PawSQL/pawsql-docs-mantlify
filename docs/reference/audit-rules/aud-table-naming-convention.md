---
id: audit-rule-aud-table-naming-convention
title: 表名命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-table-naming-convention
tags:
- audit-rule
- ddl
description: 此规则定义了表名的命名规范，通常要求表名使用小写字母和下划线（snake_case），以保持一致性和可读性。统一的表名规范便于团队协作、代码维护和自动化工具的集成。
localeOf: en-audit-rule-aud-table-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-table-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-table-naming-convention |
| 规则名称 | 表名命名规范 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则定义了表名的命名规范，通常要求表名使用小写字母和下划线（snake_case），以保持一致性和可读性。统一的表名规范便于团队协作、代码维护和自动化工具的集成。
默认命名模式为 `^[a-z]+(_[a-z]+)*$`（全小写，字母和下划线组成），可通过正则表达式配置。不符合规范的表名会在审核时触发提示。

## 反例

```sql
-- ❌ 不推荐：表名使用了大写字母（不符合 snake_case 规范）
CREATE TABLE MyTable (id INT);
CREATE TABLE OrderItems (id INT);
```

## 正例

```sql
-- ✅ 推荐：全小写 + 下划线命名
CREATE TABLE my_table (id INT);
CREATE TABLE order_items (id INT);
```
