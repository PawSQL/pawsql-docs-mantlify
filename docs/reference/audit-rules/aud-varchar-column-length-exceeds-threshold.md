---
id: audit-rule-aud-varchar-column-length-exceeds-threshold
title: VARCHAR字段长度超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-varchar-column-length-exceeds-threshold
tags:
- audit-rule
- ddl
description: VARCHAR 字段长度设置过大（如 `VARCHAR(65535)`）会造成行与索引膨胀，增加 I/O 与内存占用，降低缓存命中率，并削弱排序和连接操作的效率。过大的长度声明还会降低统计信息的估算精度，影响数据库优化器做出正确的执行计划选择。
localeOf: en-audit-rule-aud-varchar-column-length-exceeds-threshold
subtype: rule
language: zh
translationKey: audit-rule-aud-varchar-column-length-exceeds-threshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-varchar-column-length-exceeds-threshold |
| 规则名称 | VARCHAR字段长度超过阈值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

VARCHAR 字段长度设置过大（如 `VARCHAR(65535)`）会造成行与索引膨胀，增加 I/O 与内存占用，降低缓存命中率，并削弱排序和连接操作的效率。过大的长度声明还会降低统计信息的估算精度，影响数据库优化器做出正确的执行计划选择。
合理做法是依据真实数据分布设定接近上限的长度，对确实可能超长的内容改用 TEXT 类型（配合前缀索引或哈希列索引），在应用层或数据库层加长度约束来控制数据尺寸。PawSQL 检测 VARCHAR 字段长度是否超过配置的阈值（默认 10000）并进行预警。

## 反例

```sql
-- ❌ 不推荐：VARCHAR 字段长度过大（>10000），导致行与索引膨胀
CREATE TABLE t (
    content VARCHAR(65535)
);
```

## 正例

```sql
-- ✅ 推荐：根据实际数据分布设定合理长度
CREATE TABLE t (
    content VARCHAR(500)
);

-- ✅ 推荐：对超长内容使用 TEXT 类型
CREATE TABLE t (
    content TEXT
);
```
