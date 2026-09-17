---
id: audit-rule-aud-numberofcolumnsinindexexceedthreshold
title: 索引中的字段数目超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-numberofcolumnsinindexexceedthreshold
tags:
- audit-rule
- index
description: 限制索引中字段的数量，以避免索引过大导致的维护问题和性能下降。复合索引的字段越多，索引树越宽、体积越大，每次 INSERT/UPDATE/DELETE
  操作的维护成本越高，且 B+Tree 的查找效率也会随之递减。
localeOf: en-audit-rule-aud-numberofcolumnsinindexexceedthreshold
subtype: rule
language: zh
translationKey: audit-rule-aud-numberofcolumnsinindexexceedthreshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-numberofcolumnsinindexexceedthreshold |
| 规则名称 | 索引中的字段数目超过阈值 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

限制索引中字段的数量，以避免索引过大导致的维护问题和性能下降。复合索引的字段越多，索引树越宽、体积越大，每次 INSERT/UPDATE/DELETE 操作的维护成本越高，且 B+Tree 的查找效率也会随之递减。
建议将复合索引的列数控制在合理范围内（默认阈值 5），超过阈值的索引需要评估是否可以通过拆分索引或调整查询方式来优化。此阈值可根据业务需求配置。

## 反例

```sql
-- ❌ 不推荐：复合索引字段过多（超过阈值 5）
CREATE INDEX idx_complex ON orders(a, b, c, d, e, f, g);
```

## 正例

```sql
-- ✅ 推荐：将索引拆分为更聚焦的多个索引
CREATE INDEX idx_orders_a_b ON orders(a, b);
CREATE INDEX idx_orders_c_d ON orders(c, d);
```
