---
id: audit-rule-aud-modifyingpartitionkeyvaluedisallowed
title: 禁止修改分区键的值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-modifyingpartitionkeyvaluedisallowed
tags:
- audit-rule
- dml
description: 直接更新分区键的值会导致数据需要跨分区移动，这是极其昂贵的操作。在分区表中，分区键的值决定了数据行所在的物理分区，修改分区键值意味着数据库必须从原分区删除该行、再将其插入到目标分区，这涉及两次物理位置的变更和索引更新。在大数据量场景下，这类操作可能引发严重的锁竞争和性能退化。
localeOf: en-audit-rule-aud-modifyingpartitionkeyvaluedisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-modifyingpartitionkeyvaluedisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-modifyingpartitionkeyvaluedisallowed |
| 规则名称 | 禁止修改分区键的值 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

直接更新分区键的值会导致数据需要跨分区移动，这是极其昂贵的操作。在分区表中，分区键的值决定了数据行所在的物理分区，修改分区键值意味着数据库必须从原分区删除该行、再将其插入到目标分区，这涉及两次物理位置的变更和索引更新。在大数据量场景下，这类操作可能引发严重的锁竞争和性能退化。
分区键的值在设计之初就应被视为不可变的。如果业务确实需要修改，应通过"删除 + 插入"的方式显式实现，使操作的影响范围和代价对开发者完全可见。

## 反例

```sql
-- ❌ 不推荐：直接修改分区键，触发跨分区数据迁移
UPDATE t_log SET log_date = '2024-01-02' WHERE id = 100;
```

## 正例

```sql
-- ✅ 推荐：通过 DELETE + INSERT 显式处理分区变更
BEGIN;
DELETE FROM t_log WHERE id = 100;
INSERT INTO t_log (id, log_date, content) VALUES (100, '2024-01-02', '...');
COMMIT;
```
