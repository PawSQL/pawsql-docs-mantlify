---
id: audit-rule-aud-fulltextindexdisallowed
title: 禁止使用全文索引
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-fulltextindexdisallowed
tags:
- audit-rule
- index
description: 禁止使用全文索引（`FULLTEXT INDEX`）。MySQL 的全文索引稳定性较差，容易出现 `FTS query exceeds result
  cache limit` 等运行时报错，且对中文分词的支持普遍不佳，查询结果往往不符合预期。在分布式数据库中，全文索引的跨节点协调更为复杂，性能和稳定性难以保障。
localeOf: en-audit-rule-aud-fulltextindexdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-fulltextindexdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-fulltextindexdisallowed |
| 规则名称 | 禁止使用全文索引 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用全文索引（`FULLTEXT INDEX`）。MySQL 的全文索引稳定性较差，容易出现 `FTS query exceeds result cache limit` 等运行时报错，且对中文分词的支持普遍不佳，查询结果往往不符合预期。在分布式数据库中，全文索引的跨节点协调更为复杂，性能和稳定性难以保障。
如果业务中有模糊查询或全文搜索的性能需求，应优先考虑使用专业的全文检索引擎（如 Elasticsearch、Meilisearch），或将业务改造为合理的索引设计配合前缀匹配查询，利用数据库自身的 B-Tree 索引能力。

## 反例

```sql
-- ❌ 不推荐：全文索引稳定性差，中文支持弱
CREATE FULLTEXT INDEX idx_article_content ON article(content);
SELECT * FROM article WHERE MATCH(content) AGAINST('关键词');
```

## 正例

```sql
-- ✅ 推荐：使用专业全文检索引擎（Elasticsearch / Meilisearch）
-- 或通过合理的 B-Tree 索引 + 前缀匹配满足查询需求
CREATE INDEX idx_content ON article(content(100));
SELECT * FROM article WHERE content LIKE '关键词%';
```
