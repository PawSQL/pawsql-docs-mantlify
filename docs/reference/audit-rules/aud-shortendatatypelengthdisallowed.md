---
id: audit-rule-aud-shortendatatypelengthdisallowed
title: 禁止修改降低字段长度
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-shortendatatypelengthdisallowed
tags:
- audit-rule
- ddl
description: 禁止直接缩短字段长度（如 `VARCHAR(50)` 缩短为 `VARCHAR(10)`）。缩短长度会带来数据截断或写入失败的风险——如果表中已存在超过新长度的数据，`ALTER
  TABLE` 可能直接失败（严格模式），或在非严格模式下静默截断数据。此外，缩短长度可能触发表重写与锁表，并可能导致依赖该列的索引和执行计划发生变化。
localeOf: en-audit-rule-aud-shortendatatypelengthdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-shortendatatypelengthdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-shortendatatypelengthdisallowed |
| 规则名称 | 禁止修改降低字段长度 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止直接缩短字段长度（如 `VARCHAR(50)` 缩短为 `VARCHAR(10)`）。缩短长度会带来数据截断或写入失败的风险——如果表中已存在超过新长度的数据，`ALTER TABLE` 可能直接失败（严格模式），或在非严格模式下静默截断数据。此外，缩短长度可能触发表重写与锁表，并可能导致依赖该列的索引和执行计划发生变化。
正确做法是先评估并清理超长数据，在应用层收紧校验后，通过新增新长度列并灰度迁移回填的方式安全收缩长度。

## 反例

```sql
-- ❌ 不推荐：缩短字段长度，可能截断已有数据
ALTER TABLE t MODIFY col VARCHAR(10);  -- 原长度 50
```

## 正例

```sql
-- ✅ 推荐：先清理超长数据，再灰度迁移
-- 1. SELECT MAX(LENGTH(col)) FROM t;  -- 评估现有数据
-- 2. UPDATE t SET col = LEFT(col, 10) WHERE LENGTH(col) > 10;  -- 清理
-- 3. ALTER TABLE t ALTER COLUMN col TYPE VARCHAR(10);  -- 在线 DDL
```
