---
id: zh-audit-rule-aud-pk-naming
title: 主键命名规范
type: reference
status: draft
tags:
- audit-rule
- zh
- ddl
description: 主键命名规范要求数据库对象名称遵循统一规范，便于团队协作和代码维护。统一的主键命名格式（如 pk_表名_列名）可以让开发人员和 DBA 快速识别约束类型和归属关系，降低沟通成本，在跨团队协作时尤其重要。不规范的命名会增加理解难度，降低代码可读性，在数据库结构变更和故障排查时容易引发误解。
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-pk-naming |
| 规则名称 | 主键命名规范 |
| 类别 | ddl |
| 预警级别 | 提示 |
| 适用数据库 | 所有支持数据库 |

## 说明

主键命名规范要求数据库对象名称遵循统一规范，便于团队协作和代码维护。统一的主键命名格式（如 pk_表名_列名）可以让开发人员和 DBA 快速识别约束类型和归属关系，降低沟通成本，在跨团队协作时尤其重要。不规范的命名会增加理解难度，降低代码可读性，在数据库结构变更和故障排查时容易引发误解。

## 为什么重要

Constraint naming is a readability and maintainability concern: a primary key whose name does not reveal its table adds cognitive cost in cross-team work and during database structure changes.

## 如何修复

按配置的命名正则（^pk_{table}_{columns}$）为主键约束命名。例如 t_user 表的主键命名为 pk_t_user_id。该规则可配置。

## 反例

```sql
-- 不推荐：主键名称不符合命名规范
CREATE TABLE t_user (
    id BIGINT,
    name VARCHAR(50),
    CONSTRAINT pri_user PRIMARY KEY (id)
);
```

## 正例

```sql
-- 推荐：主键名称符合规范（格式: pk_{table}_{columns}）
CREATE TABLE t_user (
    id BIGINT,
    name VARCHAR(50),
    CONSTRAINT pk_t_user_id PRIMARY KEY (id)
);
```
