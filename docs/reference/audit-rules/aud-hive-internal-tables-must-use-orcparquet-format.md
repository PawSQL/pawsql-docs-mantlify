---
id: audit-rule-aud-hive-internal-tables-must-use-orcparquet-format
title: Hive内部表需使用orc/parquet存储格式
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-hive-internal-tables-must-use-orcparquet-format
tags:
- audit-rule
- ddl
description: ORC（Optimized Row Columnar）和 Parquet 是专为大数据分析优化的列式存储格式，相比传统的 TextFile
  格式具有显著更高的压缩比和更好的查询性能。列式存储支持谓词下推、投影裁剪等优化技术，可以大幅减少 I/O 读取的数据量。内部表使用行式存储格式（如 TextFile、SequenceFile）会导致查询性能低下和存储空间浪费。
localeOf: en-audit-rule-aud-hive-internal-tables-must-use-orcparquet-format
subtype: rule
language: zh
translationKey: audit-rule-aud-hive-internal-tables-must-use-orcparquet-format
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-hive-internal-tables-must-use-orcparquet-format |
| 规则名称 | Hive内部表需使用orc/parquet存储格式 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

ORC（Optimized Row Columnar）和 Parquet 是专为大数据分析优化的列式存储格式，相比传统的 TextFile 格式具有显著更高的压缩比和更好的查询性能。列式存储支持谓词下推、投影裁剪等优化技术，可以大幅减少 I/O 读取的数据量。内部表使用行式存储格式（如 TextFile、SequenceFile）会导致查询性能低下和存储空间浪费。
此规则检测 Hive 内部表的存储格式定义，对未使用 ORC/Parquet 等列式存储格式的内部表进行预警。
> 此规则适用于 Hive 数据仓库环境。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。

## 反例

```sql
-- ❌ 不推荐：内部表使用 TEXTFILE 格式，查询性能低下
CREATE TABLE t (...) STORED AS TEXTFILE;
```

## 正例

```sql
-- ✅ 推荐：内部表使用 ORC 列式存储格式
CREATE TABLE t (...) STORED AS ORC;

-- ✅ 推荐：内部表使用 Parquet 列式存储格式
CREATE TABLE t (...) STORED AS PARQUET;
```
