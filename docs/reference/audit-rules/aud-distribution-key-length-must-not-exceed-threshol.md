---
id: audit-rule-aud-distribution-key-length-must-not-exceed-threshol
title: 分布键的长度不得超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-distribution-key-length-must-not-exceed-threshol
tags:
- audit-rule
- ddl
description: 如果分布键为字符类型（`CHAR` / `VARCHAR`），其字段长度不宜超过 255 个字符。过长的分布键值会增加哈希计算和路由判定的
  CPU 开销，同时也会增大分布相关的元数据占用。
localeOf: en-audit-rule-aud-distribution-key-length-must-not-exceed-threshol
subtype: rule
language: zh
translationKey: audit-rule-aud-distribution-key-length-must-not-exceed-threshol
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-distribution-key-length-must-not-exceed-threshol |
| 规则名称 | 分布键的长度不得超过阈值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

如果分布键为字符类型（`CHAR` / `VARCHAR`），其字段长度不宜超过 255 个字符。过长的分布键值会增加哈希计算和路由判定的 CPU 开销，同时也会增大分布相关的元数据占用。
建议将字符类型分布键的长度控制在合理范围内，对于需要更长字符串的业务场景，可考虑使用字符串的哈希摘要值或更短的业务标识作为分布键。

## 反例

```sql
-- ❌ 不推荐：分布键字段长度超过 255 字符
CREATE TABLE t_log (
    long_code VARCHAR(1000),
    log_data  TEXT
) shardkey = long_code;
```

## 正例

```sql
-- ✅ 推荐：分布键字段长度在阈值以内
CREATE TABLE t_log (
    short_code VARCHAR(100),
    log_data   TEXT
) shardkey = short_code;
```
