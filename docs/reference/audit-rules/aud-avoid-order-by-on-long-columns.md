---
id: audit-rule-aud-avoid-order-by-on-long-columns
title: 避免对长字段进行排序
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-order-by-on-long-columns
tags:
- audit-rule
- dml
description: 避免对超长字段直接排序（比较代价与临时空间大）；用前缀（LEFT）或哈希排序替代。
localeOf: en-audit-rule-aud-avoid-order-by-on-long-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-order-by-on-long-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-order-by-on-long-columns |
| 规则名称 | 避免对长字段进行排序 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

排序是一个 O(n log n) 时间复杂度的操作，如果需要排序的行数较多，单字段的长度会显著影响排序效率——字段越长，每次比较的代价越高，排序所需的临时空间也越大。此规则通过比较排序字段的长度是否超过用户设定的阈值来判断风险。
默认阈值为 128 字符。如果排序字段的类型为 CHAR/VARCHAR 且长度超过阈值，或类型为 CLOB/TEXT 等大对象类型，则会触发预警。建议对长字段使用前缀排序或哈希排序来替代全字段排序。

## 反例

```sql
-- ❌ 不推荐：对超过阈值的 VARCHAR 字段进行排序，效率低下
SELECT * FROM articles ORDER BY content;
```

## 正例

```sql
-- ✅ 推荐：使用前缀排序或哈希排序
SELECT * FROM articles ORDER BY LEFT(content, 64);
```
