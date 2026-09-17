---
id: audit-rule-aud-use-prefix-index-for-long-varchar-columns
title: 长度大于阈值的字段建立索引时使用前缀
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-prefix-index-for-long-varchar-columns
tags:
- audit-rule
- index
description: 对于长度较长的 VARCHAR 字段（默认阈值 50 字符），如果对其整个字段建立索引，会导致索引体积庞大、索引维护成本高、索引扫描效率低下。使用前缀索引（仅索引字段的前
  N 个字符）可以在保证较好区分度的前提下，大幅减小索引体积，提高索引的创建速度和扫描效率。
localeOf: en-audit-rule-aud-use-prefix-index-for-long-varchar-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-use-prefix-index-for-long-varchar-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-prefix-index-for-long-varchar-columns |
| 规则名称 | 长度大于阈值的字段建立索引时使用前缀 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于长度较长的 VARCHAR 字段（默认阈值 50 字符），如果对其整个字段建立索引，会导致索引体积庞大、索引维护成本高、索引扫描效率低下。使用前缀索引（仅索引字段的前 N 个字符）可以在保证较好区分度的前提下，大幅减小索引体积，提高索引的创建速度和扫描效率。
在创建前缀索引时，需要根据数据的实际分布选择合适的索引长度。索引长度过短可能导致区分度不足，索引长度过长则失去前缀索引的意义。可以通过 `SELECT COUNT(DISTINCT LEFT(col, N)) / COUNT(*)` 来评估不同前缀长度的区分度。

## 反例

```sql
-- ❌ 不推荐：对长 VARCHAR 字段建立全字段索引，索引体积大、效率低
CREATE INDEX idx_article_content ON article(content);
```

## 正例

```sql
-- ✅ 推荐：使用前缀索引，在区分度和索引体积之间取得平衡
CREATE INDEX idx_article_content ON article(content(20));
```
