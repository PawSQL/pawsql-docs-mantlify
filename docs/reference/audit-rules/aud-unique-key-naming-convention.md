---
id: audit-rule-aud-unique-key-naming-convention
title: 唯一性索引命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-unique-key-naming-convention
tags:
- audit-rule
- index
description: 唯一性索引命名规范要求数据库对象名称遵循统一规范，便于团队协作和代码维护。通常要求唯一索引以 `uk_` 为前缀，后跟表名和列名列表，如
  `uk_{table}_{column_list}`。
localeOf: en-audit-rule-aud-unique-key-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-unique-key-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-unique-key-naming-convention |
| 规则名称 | 唯一性索引命名规范 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

唯一性索引命名规范要求数据库对象名称遵循统一规范，便于团队协作和代码维护。通常要求唯一索引以 `uk_` 为前缀，后跟表名和列名列表，如 `uk_{table}_{column_list}`。
规范的命名可以让开发人员和 DBA 快速识别约束类型、归属表和涉及的字段，在故障排查、性能优化和数据库结构变更时大幅提升效率。

## 反例

```sql
-- ❌ 不推荐：唯一索引名称不符合命名规范
CREATE UNIQUE INDEX idx_email ON t_user (email);
```

## 正例

```sql
-- ✅ 推荐：唯一索引名称符合规范（格式: uk_{table}_{columns}）
CREATE UNIQUE INDEX uk_t_user_email ON t_user (email);
```
