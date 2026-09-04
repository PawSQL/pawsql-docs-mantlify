---
id: audit-rule-aud-char-column-length
title: CHAR 字段长度超过阈值
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 检查声明长度超过阈值（默认 64）的 CHAR 字段：定长存储会让过大的 CHAR 膨胀行与索引、增加 I/O，建议改用 VARCHAR。
localeOf: en-audit-rule-aud-char-column-length
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-char-column-length |
| 规则名称 | CHAR 字段长度超过阈值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 所有支持数据库 |

## 说明

当 CHAR 类型字段的长度超过一定阈值时，应考虑修改为 VARCHAR 类型。CHAR 类型采用定长存储，即使实际数据较短也会占用固定长度的存储空间；对于长度波动较大的数据，过长的 CHAR 字段会导致行与索引膨胀、增加 I/O 与内存占用、降低缓存效率。将长度超过阈值的 CHAR 字段改为 VARCHAR 类型可以实现动态存储，节省空间并提升查询性能。

## 为什么重要

Fixed-width CHAR is only a good fit for values that are nearly always the same width. Switching over-long CHAR columns to VARCHAR enables dynamic storage, saves space, and improves query performance.

## 如何修复

将声明长度超过阈值（默认 64）的 CHAR 字段修改为 VARCHAR 类型。该规则可配置。

## 反例

```sql
-- 不推荐：CHAR 字段长度过大（>64），应改为 VARCHAR
CREATE TABLE t (
    content CHAR(10000)
);
```

## 正例

```sql
-- 推荐：将超长 CHAR 字段改为 VARCHAR 类型
CREATE TABLE t (
    content VARCHAR(10000)
);
```
