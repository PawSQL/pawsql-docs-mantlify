---
id: audit-rule-aud-comments-on-column-required
title: 列必须有注释
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 表中的每一列都必须有注释（`COMMENT`），以便于后续的维护和团队协作。列注释提供了对字段含义、用途、取值范围等信息的说明，帮助开发人员和
  DBA 快速理解表结构和业务逻辑。
localeOf: en-audit-rule-aud-comments-on-column-required
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-comments-on-column-required |
| 规则名称 | 列必须有注释 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

表中的每一列都必须有注释（`COMMENT`），以便于后续的维护和团队协作。列注释提供了对字段含义、用途、取值范围等信息的说明，帮助开发人员和 DBA 快速理解表结构和业务逻辑。
缺少注释的列在数据库结构变更、故障排查、新人交接等场景下会增加沟通成本和理解难度。养成良好的注释习惯是数据库设计的基本素养。

## 反例

```sql
-- ❌ 不推荐：列缺少注释，字段含义不明确
CREATE TABLE t_user (
    name VARCHAR(50)
);
```

## 正例

```sql
-- ✅ 推荐：每列都添加清晰的注释
CREATE TABLE t_user (
    name VARCHAR(50) COMMENT '用户姓名'
);
```
