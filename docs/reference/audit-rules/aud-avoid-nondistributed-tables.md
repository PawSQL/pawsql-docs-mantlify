---
id: audit-rule-aud-avoid-nondistributed-tables
title: 分布式数据库不建议创建非分布表
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-nondistributed-tables
tags:
- audit-rule
- ddl
description: 分布式数据库应避免非分布表（单点瓶颈、关联需重分布）；业务表用 HASH 分布。
localeOf: en-audit-rule-aud-avoid-nondistributed-tables
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-nondistributed-tables
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-nondistributed-tables |
| 规则名称 | 分布式数据库不建议创建非分布表 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在分布式数据库中，非分布表（如 `DISTRIBUTED BY LOCAL`）的数据仅存储在单个节点上，容易成为性能瓶颈和单点故障。当多个查询同时访问该表时，所有请求都会集中到一个节点，无法充分利用分布式架构的并行计算能力。
此外，非分布表与分布表进行关联操作时，通常需要将分布表的数据重分布到非分布表所在的节点，产生大量的网络传输开销。建议所有业务表均使用合理的分布策略，充分利用分布式数据库的水平扩展优势。

## 反例

```sql
-- ❌ 不推荐：在分布式环境中创建本地表/非分布表
CREATE TABLE large_table (
    id   BIGINT,
    data TEXT
) DISTRIBUTED BY LOCAL;
```

## 正例

```sql
-- ✅ 推荐：使用 HASH 分布，数据均匀分散到各节点
CREATE TABLE large_table (
    id   BIGINT,
    data TEXT
) DISTRIBUTED BY HASH (id);
```
