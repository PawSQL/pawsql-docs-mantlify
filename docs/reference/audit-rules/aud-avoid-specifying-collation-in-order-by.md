---
id: audit-rule-aud-avoid-specifying-collation-in-order-by
title: 避免查询排序时指定COLLATION
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-specifying-collation-in-order-by
tags:
- audit-rule
- index
description: 在 SQL 中可以显式指定排序字段所使用的 `COLLATION`（字符序），例如 `ORDER BY c_name COLLATE utf8mb4_0900_bin`。当查询中指定了与索引定义不同的
  COLLATION 时，数据库将无法利用该列上索引的有序性来直接返回排序结果，而必须执行一次额外的排序操作（filesort），消耗额外的 CPU 和内存资源。
localeOf: en-audit-rule-aud-avoid-specifying-collation-in-order-by
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-specifying-collation-in-order-by
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-specifying-collation-in-order-by |
| 规则名称 | 避免查询排序时指定COLLATION |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 SQL 中可以显式指定排序字段所使用的 `COLLATION`（字符序），例如 `ORDER BY c_name COLLATE utf8mb4_0900_bin`。当查询中指定了与索引定义不同的 COLLATION 时，数据库将无法利用该列上索引的有序性来直接返回排序结果，而必须执行一次额外的排序操作（filesort），消耗额外的 CPU 和内存资源。
如果确实需要使用特定排序规则，建议在创建索引时就将该 COLLATION 纳入索引定义，或通过调整列的默认 COLLATION 来避免查询时临时指定。

## 反例

```sql
-- ❌ 不推荐：ORDER BY 中指定 COLLATION，无法利用索引排序
select * from customer c order by c_name COLLATE utf8mb4_0900_bin;
```

## 正例

```sql
-- ✅ 推荐：使用列的默认 COLLATION，可利用索引排序
select * from customer c order by c_name;
```
