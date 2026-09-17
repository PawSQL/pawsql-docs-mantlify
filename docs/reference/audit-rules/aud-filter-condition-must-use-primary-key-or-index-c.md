---
id: audit-rule-aud-filter-condition-must-use-primary-key-or-index-c
title: 过滤条件中必须使用主键或索引列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-filter-condition-must-use-primary-key-or-index-c
tags:
- audit-rule
- dml
description: 当 SQL 语句的 WHERE 或 JOIN 条件中的列缺少可利用的主键或索引时，数据库优化器只能选择全表扫描来定位数据。全表扫描会逐行读取整个表的数据，随着表数据量的增长，查询性能将线性恶化，严重影响系统吞吐量和响应时间。
localeOf: en-audit-rule-aud-filter-condition-must-use-primary-key-or-index-c
subtype: rule
language: zh
translationKey: audit-rule-aud-filter-condition-must-use-primary-key-or-index-c
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-filter-condition-must-use-primary-key-or-index-c |
| 规则名称 | 过滤条件中必须使用主键或索引列 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当 SQL 语句的 WHERE 或 JOIN 条件中的列缺少可利用的主键或索引时，数据库优化器只能选择全表扫描来定位数据。全表扫描会逐行读取整个表的数据，随着表数据量的增长，查询性能将线性恶化，严重影响系统吞吐量和响应时间。
确保过滤条件命中索引或主键，是数据库查询优化的基本准则。如果某个查询没有合适的索引可用，应及时考虑创建匹配的索引来支撑该查询。

## 反例

```sql
-- ❌ 不推荐：过滤条件未命中任何索引，导致全表扫描
SELECT * FROM t WHERE unindexed_col = 1;
```

## 正例

```sql
-- ✅ 推荐：过滤条件使用了索引列，可利用索引快速定位
SELECT * FROM t WHERE indexed_col = 1;
```
