---
id: audit-rule-aud-schema-naming-convention
title: 模式命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-schema-naming-convention
tags:
- audit-rule
- ddl
description: 此规则定义了数据库模式（schema）的命名规范。统一、一致的命名规范可以显著提升数据库对象的可读性和可维护性，降低团队成员之间的沟通成本。在大型项目或多团队协作环境中，不规范的命名会导致理解困难、脚本冲突和运维失误。
localeOf: en-audit-rule-aud-schema-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-schema-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-schema-naming-convention |
| 规则名称 | 模式命名规范 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则定义了数据库模式（schema）的命名规范。统一、一致的命名规范可以显著提升数据库对象的可读性和可维护性，降低团队成员之间的沟通成本。在大型项目或多团队协作环境中，不规范的命名会导致理解困难、脚本冲突和运维失误。
例如，模式名使用小写字母和连字符（kebab-case），使名称简洁且跨平台兼容。违反此规则的创建操作应进行调整。

## 反例

```sql
-- ❌ 不推荐：模式名不符合命名规范
CREATE SCHEMA "MySchema";
```

## 正例

```sql
-- ✅ 推荐：使用小写字母和连字符，符合 kebab-case 规范
CREATE SCHEMA my_schema;
```
