---
id: audit-rule-aud-foreignkeydisallowed
title: 禁止创建外键
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-foreignkeydisallowed
tags:
- audit-rule
- ddl
description: 禁止创建外键约束。外键会增加数据库操作的复杂性和性能开销——每次 INSERT/UPDATE/DELETE 都需要对被引用表进行级联检查或加锁，在并发写入场景下容易引发死锁和性能瓶颈。在分布式数据库（如
  TDSQL）中，外键的跨节点约束检查更是难以保证性能和一致性。
localeOf: en-audit-rule-aud-foreignkeydisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-foreignkeydisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-foreignkeydisallowed |
| 规则名称 | 禁止创建外键 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止创建外键约束。外键会增加数据库操作的复杂性和性能开销——每次 INSERT/UPDATE/DELETE 都需要对被引用表进行级联检查或加锁，在并发写入场景下容易引发死锁和性能瓶颈。在分布式数据库（如 TDSQL）中，外键的跨节点约束检查更是难以保证性能和一致性。
推荐通过应用层逻辑保证主外键的引用完整性，在业务代码中使用事务显式维护数据的一致性关系，保持数据库层的简洁和高性能。

## 反例

```sql
-- ❌ 不推荐：外键约束，增加写入开销和死锁风险
CREATE TABLE child (
    id INT PRIMARY KEY,
    parent_id INT,
    FOREIGN KEY (parent_id) REFERENCES parent(id)
);
```

## 正例

```sql
-- ✅ 推荐：在应用层保证参照完整性
CREATE TABLE child (
    id INT PRIMARY KEY,
    parent_id INT,
    INDEX idx_parent_id (parent_id)
);
-- 应用层：在事务中先检查 parent 是否存在，再插入 child
```
