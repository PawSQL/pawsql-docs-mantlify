---
id: audit-rule-aud-avoid-select-without-where-and-group-by
title: 避免无条件且无分组的SELECT语句
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-select-without-where-and-group-by
tags:
- audit-rule
- dml
description: 没有 WHERE 条件（或条件恒真）且没有 GROUP BY 聚合的 SELECT 语句，会触发全表扫描并返回表中的所有数据行。这种查询在小型表中可能无害，但在大型表中会导致巨大的结果集和
  IO 开销，严重影响数据库性能和网络带宽。
localeOf: en-audit-rule-aud-avoid-select-without-where-and-group-by
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-select-without-where-and-group-by
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-select-without-where-and-group-by |
| 规则名称 | 避免无条件且无分组的SELECT语句 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

没有 WHERE 条件（或条件恒真）且没有 GROUP BY 聚合的 SELECT 语句，会触发全表扫描并返回表中的所有数据行。这种查询在小型表中可能无害，但在大型表中会导致巨大的结果集和 IO 开销，严重影响数据库性能和网络带宽。
如果业务的确实需要导出全表数据，建议使用分页查询（LIMIT + OFFSET）或数据导出工具来分批处理。对于常规的业务查询，应始终添加合理的过滤条件和聚合逻辑来限制返回的数据量。

## 反例

```sql
-- ❌ 不推荐：无条件无聚合，全表扫描返回所有数据
SELECT * FROM t;
```

## 正例

```sql
-- ✅ 推荐：添加 WHERE 条件限制数据范围
SELECT * FROM t WHERE created_at >= '2025-01-01';

-- 或使用 GROUP BY 进行数据聚合
SELECT dept_id, COUNT(*) FROM t GROUP BY dept_id;
```
