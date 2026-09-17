---
id: audit-rule-aud-modifytablecharsetdisallowed
title: 禁止修改表的默认字符集
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-modifytablecharsetdisallowed
tags:
- audit-rule
- ddl
description: 禁止修改表的默认字符集。修改表的字符集会触发全表数据重新编码，这个过程极其消耗资源且持有元数据锁，可能导致长时间的业务阻塞。更严重的是，在字符集转换过程中，如果存在无法映射的字符，可能导致数据静默损坏（被替换为
  `?` 或截断），且这一问题在转换完成后难以发现和恢复。
localeOf: en-audit-rule-aud-modifytablecharsetdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-modifytablecharsetdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-modifytablecharsetdisallowed |
| 规则名称 | 禁止修改表的默认字符集 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止修改表的默认字符集。修改表的字符集会触发全表数据重新编码，这个过程极其消耗资源且持有元数据锁，可能导致长时间的业务阻塞。更严重的是，在字符集转换过程中，如果存在无法映射的字符，可能导致数据静默损坏（被替换为 `?` 或截断），且这一问题在转换完成后难以发现和恢复。
字符集应在建表时一次性确定，并在整个数据库实例中保持统一。如果确实需要变更，应通过创建新表并逐步迁移数据的方式实现。

## 反例

```sql
-- ❌ 不推荐：修改表字符集，触发全表重建，可能导致数据损坏
ALTER TABLE t CONVERT TO CHARACTER SET latin1;
```

## 正例

```sql
-- ✅ 推荐：建表时指定统一字符集
CREATE TABLE t (
    id INT
) DEFAULT CHARSET=utf8mb4;
```
