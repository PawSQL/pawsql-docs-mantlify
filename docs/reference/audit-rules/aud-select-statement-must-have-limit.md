---
id: audit-rule-aud-select-statement-must-have-limit
title: SELECT 语句必须带LIMIT
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-select-statement-must-have-limit
tags:
- audit-rule
- dml
description: SELECT 语句如果不带 LIMIT 子句，在遇到异常输入参数或表数据量较大时，可能返回海量结果集。服务端对于查询结果的处理能力通常有一定限制，过大的结果集不仅消耗大量网络带宽和内存资源，极端情况下可能导致服务端完全宕机。
localeOf: en-audit-rule-aud-select-statement-must-have-limit
subtype: rule
language: zh
translationKey: audit-rule-aud-select-statement-must-have-limit
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-select-statement-must-have-limit |
| 规则名称 | SELECT 语句必须带LIMIT |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

SELECT 语句如果不带 LIMIT 子句，在遇到异常输入参数或表数据量较大时，可能返回海量结果集。服务端对于查询结果的处理能力通常有一定限制，过大的结果集不仅消耗大量网络带宽和内存资源，极端情况下可能导致服务端完全宕机。
建议为所有生产环境的 SELECT 查询添加 LIMIT 子句，限制单次查询返回的最大行数。PawSQL 检测未添加 LIMIT 的 SELECT 语句并给出预警，帮助开发者建立安全查询的编码习惯。

## 反例

```sql
-- ❌ 不推荐：SELECT 缺少 LIMIT，有全表扫描返回海量数据的风险
SELECT * FROM user WHERE status = 1;
```

## 正例

```sql
-- ✅ 推荐：添加 LIMIT 限制返回行数
SELECT * FROM user WHERE status = 1 LIMIT 1000;
```
