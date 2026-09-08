---
id: audit-rule-aud-create-index-using-online-mode
title: 建议使用在线模式创建索引
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-create-index-using-online-mode
tags:
- audit-rule
- ddl
description: 建索引优先在线模式（MySQL INPLACE/LOCK=NONE、PostgreSQL CONCURRENTLY），避免大表长锁阻塞 DML。
localeOf: en-audit-rule-aud-create-index-using-online-mode
subtype: rule
language: zh
translationKey: audit-rule-aud-create-index-using-online-mode
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-create-index-using-online-mode |
| 规则名称 | 建议使用在线模式创建索引 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

建议在创建索引时使用在线模式（如MySQL的`ALGORITHM=INPLACE, LOCK=NONE`、PostgreSQL的`CONCURRENTLY`等），因为在线模式可显著降低建索引过程中的锁持有时间与业务阻塞风险，减少对读写流量的影响，并提升变更窗口的可控性。
传统的非在线建索引方式会在操作期间对目标表施加排他锁，阻塞所有DML操作。对于大表而言，建索引可能持续数分钟甚至数小时，导致长时间的业务中断。使用在线模式可以避免此类问题，但需结合并发负载与日志/回滚段容量评估资源开销。

## 反例

```sql
-- ❌ 不推荐：传统建索引方式，可能在执行期间锁表，阻塞DML操作
CREATE INDEX idx_name ON large_table(name);
```

## 正例

```sql
-- ✅ 推荐：使用在线DDL模式，不阻塞并发的读写操作
ALTER TABLE large_table ADD INDEX idx_name(name), ALGORITHM=INPLACE, LOCK=NONE;

-- ✅ 推荐（PostgreSQL）：使用CONCURRENTLY模式
CREATE INDEX CONCURRENTLY idx_name ON large_table(name);
```
