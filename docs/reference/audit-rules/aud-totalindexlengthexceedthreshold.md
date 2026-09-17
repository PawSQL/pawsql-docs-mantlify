---
id: audit-rule-aud-totalindexlengthexceedthreshold
title: 索引长度不得超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-totalindexlengthexceedthreshold
tags:
- audit-rule
- index
description: InnoDB 引擎对索引的最大长度有严格限制：单列索引最大长度为 3072 字节（utf8mb4 字符集下 VARCHAR(768)），复合索引中所有列的总长度也不能超过此限制。如果索引字段过长，可能导致索引创建失败或索引效率严重低下。
localeOf: en-audit-rule-aud-totalindexlengthexceedthreshold
subtype: rule
language: zh
translationKey: audit-rule-aud-totalindexlengthexceedthreshold
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-totalindexlengthexceedthreshold |
| 规则名称 | 索引长度不得超过阈值 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

InnoDB 引擎对索引的最大长度有严格限制：单列索引最大长度为 3072 字节（utf8mb4 字符集下 VARCHAR(768)），复合索引中所有列的总长度也不能超过此限制。如果索引字段过长，可能导致索引创建失败或索引效率严重低下。
建议通过创建前缀索引来避免此问题，仅对字段的前 N 个字符建立索引，在满足查询需求的前提下尽可能减小索引体积。默认阈值为 3072 字节。

## 反例

```sql
-- ❌ 不推荐：索引总长度超过阈值（utf8mb4 下 VARCHAR(1000) 索引约 4000 字节）
CREATE INDEX idx_content ON article(content VARCHAR(1000));
```

## 正例

```sql
-- ✅ 推荐：使用前缀索引控制索引大小
CREATE INDEX idx_content ON article(content(100));
```
