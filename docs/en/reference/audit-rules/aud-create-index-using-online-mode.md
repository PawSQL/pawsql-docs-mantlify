---
id: en-audit-rule-aud-create-index-using-online-mode
title: Create Index Using Online Mode
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 建议在创建索引时使用在线模式（如MySQL的`ALGORITHM=INPLACE, LOCK=NONE`、PostgreSQL的`CONCURRENTLY`等），因为在线模式可显著降低建索引过程中的锁持有时间与业务阻塞风险，减少对读写流量的影响，并提升变更窗口的可控性。
localeOf: audit-rule-aud-create-index-using-online-mode
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-create-index-using-online-mode |
| Name | Create Index Using Online Mode |
| Category | ddl — DDL / object design |
| Severity | warning |
| Databases | All supported databases |

## Description

建议在创建索引时使用在线模式（如MySQL的`ALGORITHM=INPLACE, LOCK=NONE`、PostgreSQL的`CONCURRENTLY`等），因为在线模式可显著降低建索引过程中的锁持有时间与业务阻塞风险，减少对读写流量的影响，并提升变更窗口的可控性。
传统的非在线建索引方式会在操作期间对目标表施加排他锁，阻塞所有DML操作。对于大表而言，建索引可能持续数分钟甚至数小时，导致长时间的业务中断。使用在线模式可以避免此类问题，但需结合并发负载与日志/回滚段容量评估资源开销。

## Bad Example

```sql
-- ❌ 不推荐：传统建索引方式，可能在执行期间锁表，阻塞DML操作
CREATE INDEX idx_name ON large_table(name);
```

## Good Example

```sql
-- ✅ 推荐：使用在线DDL模式，不阻塞并发的读写操作
ALTER TABLE large_table ADD INDEX idx_name(name), ALGORITHM=INPLACE, LOCK=NONE;

-- ✅ 推荐（PostgreSQL）：使用CONCURRENTLY模式
CREATE INDEX CONCURRENTLY idx_name ON large_table(name);
```
