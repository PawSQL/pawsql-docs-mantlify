---
id: audit-rule-sql-index-023
title: 禁止创建重复索引/冗余索引
type: reference
status: draft
tags:
- audit-rule
- index
- mysql
- postgresql
description: 检测重复/冗余索引：其前缀列已被其它索引覆盖，只会增加写入与存储成本，应删除。
localeOf: en-audit-rule-sql-index-023
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | SQL-INDEX-023 |
| 规则名称 | 禁止创建重复索引/冗余索引 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | mysql, postgresql |
| 引入版本 | 8.4.0 |
| 实现 | `RedundantIndexRule` |

## 说明

禁止创建重复或冗余的索引。重复索引（完全相同的列组合）和冗余索引（新索引的前缀列已被现有索引覆盖）不会带来任何查询性能提升，反而会浪费存储空间并降低写入性能——每次 INSERT/UPDATE/DELETE 都需要维护所有这些多余的索引结构。在数据量大的表上，冗余索引的额外维护开销可能十分显著。

## 为什么重要

重复/冗余索引对查询没有任何帮助，却持续占用磁盘空间，并在每次写入时被额外维护，拖慢 DML 却不提升任何查询。

## 如何修复

创建索引前应仔细分析现有索引的列组合，确保新索引确实覆盖了现有索引未能覆盖的查询模式；如现有索引已能满足需求，则不应重复创建，并删除前缀列已被现有索引完全覆盖的多余索引。

## 反例

```sql
-- 不推荐：冗余索引，idx_name_dup 已被 idx_full 的前缀覆盖
CREATE INDEX idx_full ON user(name, age, email);
CREATE INDEX idx_name_dup ON user(name);
```

## 正例

```sql
-- 推荐：仅创建必要的、非冗余的索引
CREATE INDEX idx_full ON user(name, age, email);
-- idx_full 已经可以满足 name 列的等值/范围查询，无需额外索引
```

## 关联规则

`SQL-INDEX-UNUSED`, `SQL-INDEX-DUPLICATE`
