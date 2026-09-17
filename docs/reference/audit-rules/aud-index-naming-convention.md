---
id: audit-rule-aud-index-naming-convention
title: 索引命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-index-naming-convention
tags:
- audit-rule
- index
description: 此规则定义了索引的命名规范，要求索引名遵循统一的格式，通常包括表名和列名的组合，以便于识别和管理索引。规范的索引命名有助于 DBA 快速定位索引所属的表和功能，降低运维排查成本。
localeOf: en-audit-rule-aud-index-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-index-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-index-naming-convention |
| 规则名称 | 索引命名规范 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

此规则定义了索引的命名规范，要求索引名遵循统一的格式，通常包括表名和列名的组合，以便于识别和管理索引。规范的索引命名有助于 DBA 快速定位索引所属的表和功能，降低运维排查成本。
默认命名模式为 `idx_{table}_{columns}`，可通过正则表达式配置。不符合命名规范的索引会在审核时触发提示，但不会阻止操作。

## 反例

```sql
-- ❌ 不推荐：索引命名不符合规范
CREATE INDEX my_idx ON orders(status);
```

## 正例

```sql
-- ✅ 推荐：遵循 idx_{table}_{columns} 命名格式
CREATE INDEX idx_orders_status ON orders(status);
```
