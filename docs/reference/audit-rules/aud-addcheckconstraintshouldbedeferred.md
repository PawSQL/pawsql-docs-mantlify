---
id: audit-rule-aud-addcheckconstraintshouldbedeferred
title: 添加CHECK约束时需添加NO VALID
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 给已有数据的表加 CHECK 约束时应指定 NO VALID 跳过全表校验，历史数据分批离线验证。
localeOf: en-audit-rule-aud-addcheckconstraintshouldbedeferred
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-addcheckconstraintshouldbedeferred |
| 规则名称 | 添加CHECK约束时需添加NO VALID |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

当通过 `ALTER TABLE` 为已有数据的表添加 CHECK 约束时，如果未指定 `NO VALID`（或等效的非验证选项），数据库会立即对表中所有现有数据进行全量校验。对于大表而言，这将触发长时间的全表扫描和锁持有，严重阻塞并发写入，甚至导致变更超时或失败。指定 `NO VALID` 可以跳过对历史数据的验证，仅对后续新写入数据强制执行约束，从而在保证新数据质量的同时避免对现有系统的性能冲击。
验证历史数据的合规性应在变更窗口之外、通过分批校验脚本逐步完成，并在确认所有数据满足约束后再考虑将约束切换为全量生效。

## 反例

```sql
-- ❌ 不推荐：未指定 NO VALID，立即校验全表数据
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount > 0);
```

## 正例

```sql
-- ✅ 推荐：添加约束时指定 NO VALID，仅对新数据生效
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount > 0) NO VALID;
```
