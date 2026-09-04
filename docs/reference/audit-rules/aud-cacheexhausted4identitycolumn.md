---
id: audit-rule-aud-cacheexhausted4identitycolumn
title: 自增序列耗尽预警
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 自增列接近类型最大值（默认阈值 80%）时预警，提前规划扩容（如 INT→BIGINT），避免 INSERT 失败。
localeOf: en-audit-rule-aud-cacheexhausted4identitycolumn
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-cacheexhausted4identitycolumn |
| 规则名称 | 自增序列耗尽预警 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

当自增列的当前值接近其数据类型的最大值时，序列即将耗尽，后续的 INSERT 操作将失败并抛出主键冲突或溢出错误。这在高频写入的核心业务表中尤其致命，可能导致服务中断。
建议通过监控预警及时发现序列耗尽风险，并根据使用率提前规划扩容方案（如升级数据类型，从 INT 扩展至 BIGINT）。默认预警阈值为最大值的 80%，可通过配置调整。
