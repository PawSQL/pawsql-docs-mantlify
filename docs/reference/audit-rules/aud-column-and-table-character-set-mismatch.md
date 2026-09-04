---
id: audit-rule-aud-column-and-table-character-set-mismatch
title: 列的字符集和表不一致
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 当列级别的字符集与表级别的字符集不一致时，可能导致隐式字符集转换、数据截断或乱码问题。在多语言环境下，字符集不一致还可能引发索引失效（MySQL
  中字符集不一致的字段进行 JOIN 时无法使用索引）和查询结果不符合预期等隐蔽性故障。
localeOf: en-audit-rule-aud-column-and-table-character-set-mismatch
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-column-and-table-character-set-mismatch |
| 规则名称 | 列的字符集和表不一致 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

当列级别的字符集与表级别的字符集不一致时，可能导致隐式字符集转换、数据截断或乱码问题。在多语言环境下，字符集不一致还可能引发索引失效（MySQL 中字符集不一致的字段进行 JOIN 时无法使用索引）和查询结果不符合预期等隐蔽性故障。
建议在表级别统一指定字符集，各列继承表的字符集配置，避免个别列使用不同的字符集。保持一致的字符集策略是数据库设计的基本规范。

## 反例

```sql
-- ❌ 不推荐：列级别字符集与表级别不一致
CREATE TABLE t_user (
    name VARCHAR(50) CHARSET latin1
) DEFAULT CHARSET utf8mb4;
```

## 正例

```sql
-- ✅ 推荐：列继承表的字符集，保持一致
CREATE TABLE t_user (
    name VARCHAR(50)
) DEFAULT CHARSET utf8mb4;
```
