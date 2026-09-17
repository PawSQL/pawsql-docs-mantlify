---
id: audit-rule-aud-globalindexondistributedtabledisallowed
title: 禁止在分布式表上创建全局索引
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-globalindexondistributedtabledisallowed
tags:
- audit-rule
- index
description: TDSQL 等分布式实例目前对全局索引的支持尚不成熟，且存在较多限制——如索引列不能有默认值、不能有 `TIMESTAMP` 类型、创建和维护全局索引需要在所有分片节点上协调元数据等。全局索引在分布式环境中会引入跨节点的数据一致性问题，且索引维护的复杂度随分片数线性增长。
localeOf: en-audit-rule-aud-globalindexondistributedtabledisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-globalindexondistributedtabledisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-globalindexondistributedtabledisallowed |
| 规则名称 | 禁止在分布式表上创建全局索引 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

TDSQL 等分布式实例目前对全局索引的支持尚不成熟，且存在较多限制——如索引列不能有默认值、不能有 `TIMESTAMP` 类型、创建和维护全局索引需要在所有分片节点上协调元数据等。全局索引在分布式环境中会引入跨节点的数据一致性问题，且索引维护的复杂度随分片数线性增长。
在未与 DBA 充分确认前，禁止在分布式表上创建全局索引。推荐使用本地索引覆盖查询需求，并通过优化分片键选择来满足跨分片查询的性能要求。

## 反例

```sql
-- ❌ 不推荐：分布式表上创建全局索引，支持不成熟，限制多
CREATE UNIQUE GLOBAL INDEX idx_global ON t(col);
```

## 正例

```sql
-- ✅ 推荐：使用本地索引 + 优化分片键选择
CREATE INDEX idx_local ON t(col);
-- 或调整分片键使查询落在单个分片
```
