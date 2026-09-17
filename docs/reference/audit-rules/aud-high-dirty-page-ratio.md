---
id: audit-rule-aud-high-dirty-page-ratio
title: 脏页率超过阈值，建议进行回收
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-high-dirty-page-ratio
tags:
- audit-rule
- ddl
description: 当数据库缓冲池中脏页（已修改但未刷入磁盘的数据页）的比率超过配置阈值时，可能引发磁盘空间紧张、I/O 性能瓶颈和事务延迟。过高的脏页率意味着数据库积压了大量待刷盘的修改，一旦发生故障恢复时间将显著延长。
localeOf: en-audit-rule-aud-high-dirty-page-ratio
subtype: rule
language: zh
translationKey: audit-rule-aud-high-dirty-page-ratio
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-high-dirty-page-ratio |
| 规则名称 | 脏页率超过阈值，建议进行回收 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

当数据库缓冲池中脏页（已修改但未刷入磁盘的数据页）的比率超过配置阈值时，可能引发磁盘空间紧张、I/O 性能瓶颈和事务延迟。过高的脏页率意味着数据库积压了大量待刷盘的修改，一旦发生故障恢复时间将显著延长。
建议及时执行 `CHECKPOINT`（PostgreSQL）或调整 InnoDB 的刷盘策略参数（如 `innodb_max_dirty_pages_pct`），将脏页率控制在合理范围内。默认阈值为 0.3（30%），可通过配置调整。
