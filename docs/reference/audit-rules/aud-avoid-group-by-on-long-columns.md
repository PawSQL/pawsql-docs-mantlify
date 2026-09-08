---
id: audit-rule-aud-avoid-group-by-on-long-columns
title: 避免对长字段进行分组
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-group-by-on-long-columns
tags:
- audit-rule
- dml
description: 避免对超长字段分组（CHAR/VARCHAR>128 或 CLOB/TEXT，排序/哈希开销大）；用前缀或哈希分组。
localeOf: en-audit-rule-aud-avoid-group-by-on-long-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-group-by-on-long-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-group-by-on-long-columns |
| 规则名称 | 避免对长字段进行分组 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在数据库中，GROUP BY 分组操作通常通过排序或哈希来实现，其时间复杂度和内存开销与参与分组的数据量及字段长度密切相关。如果需要分组的行数较多，单个字段的长度会显著影响分组效率——字段越长，排序比较或哈希计算的成本越高，临时空间占用也越大。
此规则通过比较分组字段的长度是否超过用户设定的阈值来判断是否存在风险。默认阈值为 128 字符。如果分组字段的类型为 CHAR/VARCHAR 且长度超过阈值，或类型为 CLOB/TEXT 等大对象类型，则会触发预警。

## 反例

```sql
-- ❌ 不推荐：对长度超过阈值的 VARCHAR 字段进行分组，效率低下
SELECT long_description, COUNT(*) FROM products GROUP BY long_description;
```

## 正例

```sql
-- ✅ 推荐：使用字段的哈希值或前缀来分组
SELECT LEFT(long_description, 64), COUNT(*) FROM products GROUP BY LEFT(long_description, 64);
```
