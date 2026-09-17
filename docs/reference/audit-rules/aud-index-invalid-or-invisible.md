---
id: audit-rule-aud-index-invalid-or-invisible
title: 索引失效或不可见
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-index-invalid-or-invisible
tags:
- audit-rule
- index
description: 检测到索引处于失效（INVALID / UNUSABLE）或不可见（INVISIBLE）状态时，该索引无法被优化器使用，但仍在磁盘上占据存储空间，并可能在
  DML 操作时仍消耗维护资源，影响系统整体性能。
localeOf: en-audit-rule-aud-index-invalid-or-invisible
subtype: rule
language: zh
translationKey: audit-rule-aud-index-invalid-or-invisible
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-index-invalid-or-invisible |
| 规则名称 | 索引失效或不可见 |
| 类别 | index（索引） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

检测到索引处于失效（INVALID / UNUSABLE）或不可见（INVISIBLE）状态时，该索引无法被优化器使用，但仍在磁盘上占据存储空间，并可能在 DML 操作时仍消耗维护资源，影响系统整体性能。
索引的失效/不可见状态可能是由于维护操作（如分区 DDL、大量数据导入）导致的，也可能是人为手动设置的。应及时排查原因并恢复索引可用性，或直接删除不再需要的索引。
