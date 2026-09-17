---
id: audit-rule-aud-longlengthcolumns4indexdisallowed
title: 索引的字段长度不应超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-longlengthcolumns4indexdisallowed
tags:
- audit-rule
- index
description: 限制索引中单个字段的字节长度，以避免索引过大导致的维护开销和性能问题。MySQL 建立索引时默认采用字段的完整长度，而 VARCHAR 类型定义长度越长，索引占用的存储空间越大，扫描效率越低。
localeOf: en-audit-rule-aud-longlengthcolumns4indexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-longlengthcolumns4indexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-longlengthcolumns4indexdisallowed |
| 规则名称 | 索引的字段长度不应超过阈值 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

限制索引中单个字段的字节长度，以避免索引过大导致的维护开销和性能问题。MySQL 建立索引时默认采用字段的完整长度，而 VARCHAR 类型定义长度越长，索引占用的存储空间越大，扫描效率越低。
对于长字段，建议使用前缀索引（指定前缀长度）来减小索引体积，或将该字段从索引中移除。默认阈值为 32 个字符（或 1024 字节），可根据业务需求调整。

## 反例

```sql
-- ❌ 不推荐：索引字段长度过长（如 VARCHAR(1024) 全部作为索引）
CREATE INDEX idx_long ON article(content VARCHAR(1024));
```

## 正例

```sql
-- ✅ 推荐：使用前缀索引限制索引字段长度
CREATE INDEX idx_prefix ON article(content(100));
```
