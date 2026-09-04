---
id: en-audit-rule-aud-addcheckconstraintshouldbedeferred
title: AddCheckConstraintShouldBeDeferred
type: reference
status: draft
tags:
- audit-rule
- ddl
localeOf: audit-rule-aud-addcheckconstraintshouldbedeferred
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-addcheckconstraintshouldbedeferred |
| Name | AddCheckConstraintShouldBeDeferred |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

当通过 `ALTER TABLE` 为已有数据的表添加 CHECK 约束时，如果未指定 `NO VALID`（或等效的非验证选项），数据库会立即对表中所有现有数据进行全量校验。对于大表而言，这将触发长时间的全表扫描和锁持有，严重阻塞并发写入，甚至导致变更超时或失败。指定 `NO VALID` 可以跳过对历史数据的验证，仅对后续新写入数据强制执行约束，从而在保证新数据质量的同时避免对现有系统的性能冲击。
验证历史数据的合规性应在变更窗口之外、通过分批校验脚本逐步完成，并在确认所有数据满足约束后再考虑将约束切换为全量生效。

## Bad Example

```sql
-- ❌ 不推荐：未指定 NO VALID，立即校验全表数据
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount > 0);
```

## Good Example

```sql
-- ✅ 推荐：添加约束时指定 NO VALID，仅对新数据生效
ALTER TABLE orders ADD CONSTRAINT chk_amount CHECK (amount > 0) NO VALID;
```
