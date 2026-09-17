---
id: audit-rule-aud-timestamp-data-type-disallowed
title: 不允许使用时间戳类型
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-timestamp-data-type-disallowed
tags:
- audit-rule
- ddl
description: TIMESTAMP 类型存在两大致命缺陷：第一，范围限制问题 -- TIMESTAMP 的最大值为 `'2038-01-19 03:14:07'`
  UTC，超过此时间点的数据将无法存储（即"2038 年问题"）；第二，时区转换问题 -- TIMESTAMP 在存储和读取时会自动进行时区转换，在不同时区环境或数据库迁移时可能导致数据不一致。
localeOf: en-audit-rule-aud-timestamp-data-type-disallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-timestamp-data-type-disallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-timestamp-data-type-disallowed |
| 规则名称 | 不允许使用时间戳类型 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

TIMESTAMP 类型存在两大致命缺陷：第一，范围限制问题 -- TIMESTAMP 的最大值为 `'2038-01-19 03:14:07'` UTC，超过此时间点的数据将无法存储（即"2038 年问题"）；第二，时区转换问题 -- TIMESTAMP 在存储和读取时会自动进行时区转换，在不同时区环境或数据库迁移时可能导致数据不一致。
建议使用 DATETIME 类型替代 TIMESTAMP。DATETIME 的范围更大（`'1000-01-01'` 至 `'9999-12-31'`），且不受时区影响，存储和读取的值完全一致，更加可靠。

## 反例

```sql
-- ❌ 不推荐：TIMESTAMP 有 2038 年限制和时区转换问题
CREATE TABLE t (
    ts TIMESTAMP
);
```

## 正例

```sql
-- ✅ 推荐：使用 DATETIME 类型替代
CREATE TABLE t (
    dt DATETIME
);
```
