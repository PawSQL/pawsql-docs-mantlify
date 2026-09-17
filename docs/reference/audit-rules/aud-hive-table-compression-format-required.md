---
id: audit-rule-aud-hive-table-compression-format-required
title: Hive表需使用指定的压缩格式
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-hive-table-compression-format-required
tags:
- audit-rule
- ddl
description: 为了优化存储空间和 I/O 性能，Hive 表应该使用企业标准的压缩格式。未使用压缩或使用非标准压缩格式的表会增加存储开销、网络传输成本和磁盘
  I/O。在大数据环境中，合理的压缩设置可以显著降低存储成本并提升查询效率。
localeOf: en-audit-rule-aud-hive-table-compression-format-required
subtype: rule
language: zh
translationKey: audit-rule-aud-hive-table-compression-format-required
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-hive-table-compression-format-required |
| 规则名称 | Hive表需使用指定的压缩格式 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

为了优化存储空间和 I/O 性能，Hive 表应该使用企业标准的压缩格式。未使用压缩或使用非标准压缩格式的表会增加存储开销、网络传输成本和磁盘 I/O。在大数据环境中，合理的压缩设置可以显著降低存储成本并提升查询效率。
此规则检测 Hive 表在创建或修改时是否指定了符合规范的压缩格式配置，对未指定或使用非标准压缩算法的表进行预警。
> 此规则适用于 Hive 数据仓库环境。Hive 基于 MapReduce/Spark 计算引擎，其执行机制与传统关系型数据库有本质区别。

## 反例

```sql
-- ❌ 不推荐：未指定压缩格式
CREATE TABLE t (...) STORED AS ORC;
```

## 正例

```sql
-- ✅ 推荐：使用 SNAPPY 压缩格式
CREATE TABLE t (...) STORED AS ORC TBLPROPERTIES ("orc.compress"="SNAPPY");

-- ✅ 推荐：使用 GZIP 压缩格式（适用于 TEXTFILE）
CREATE TABLE t (...) STORED AS TEXTFILE TBLPROPERTIES ("compression.codec"="gzip");
```
