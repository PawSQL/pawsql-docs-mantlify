---
id: audit-rule-aud-nonnullconstraint4columnsinlistdisallowed
title: 禁止为列表中的列设置非空约束
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-nonnullconstraint4columnsinlistdisallowed
tags:
- audit-rule
- ddl
description: 禁止为 BLOB、CLOB、TEXT 等大对象类型的列设置非空约束。大对象类型的列通常存储体积较大的数据，强制要求非空意味着每次插入都必须提供完整的大对象值，这不仅增加了存储和网络开销，还可能在批量导入或数据迁移场景中导致插入失败。此外，大对象类型的列在部分数据库中无法高效地进行
  NULL 检查和索引优化，强制非空约束还可能引发锁竞争和性能退化。
localeOf: en-audit-rule-aud-nonnullconstraint4columnsinlistdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-nonnullconstraint4columnsinlistdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-nonnullconstraint4columnsinlistdisallowed |
| 规则名称 | 禁止为列表中的列设置非空约束 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止为 BLOB、CLOB、TEXT 等大对象类型的列设置非空约束。大对象类型的列通常存储体积较大的数据，强制要求非空意味着每次插入都必须提供完整的大对象值，这不仅增加了存储和网络开销，还可能在批量导入或数据迁移场景中导致插入失败。此外，大对象类型的列在部分数据库中无法高效地进行 NULL 检查和索引优化，强制非空约束还可能引发锁竞争和性能退化。
合理的做法是在应用层通过业务逻辑保证大对象字段的有值校验，而非依赖数据库层的非空约束。

## 反例

```sql
-- ❌ 不推荐：为大对象类型列设置非空约束
CREATE TABLE t (
    id INT NOT NULL,
    content TEXT NOT NULL
);
```

## 正例

```sql
-- ✅ 推荐：大对象列允许 NULL，通过应用层校验
CREATE TABLE t (
    id INT NOT NULL,
    content TEXT
);
```
