---
id: audit-rule-aud-use-drop-partition-instead-of-batch-delete
title: 批量删除建议使用分区表删除分区
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-drop-partition-instead-of-batch-delete
tags:
- audit-rule
- dml
description: 对于需要定期清理历史数据的表，应将其设计为分区表。使用`DROP PARTITION`删除一个分区的效率远高于使用`DELETE`逐条删除数据：`DROP
  PARTITION`是DDL操作，直接回收存储空间，速度极快且几乎不产生日志；而`DELETE`是DML操作，需要逐行记录日志以便回滚和主备同步，对于大表而言可能耗时数小时甚至数天，并在此期间持有大量行锁。
localeOf: en-audit-rule-aud-use-drop-partition-instead-of-batch-delete
subtype: rule
language: zh
translationKey: audit-rule-aud-use-drop-partition-instead-of-batch-delete
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-drop-partition-instead-of-batch-delete |
| 规则名称 | 批量删除建议使用分区表删除分区 |
| 类别 | dml（数据操作） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于需要定期清理历史数据的表，应将其设计为分区表。使用`DROP PARTITION`删除一个分区的效率远高于使用`DELETE`逐条删除数据：`DROP PARTITION`是DDL操作，直接回收存储空间，速度极快且几乎不产生日志；而`DELETE`是DML操作，需要逐行记录日志以便回滚和主备同步，对于大表而言可能耗时数小时甚至数天，并在此期间持有大量行锁。
该规则检测针对分区表的、以日期等分区字段为条件的DELETE操作，建议用户评估是否可以使用`DROP PARTITION`代替。

## 反例

```sql
-- ❌ 不推荐：使用DELETE逐行删除历史数据，效率低且产生大量日志
DELETE FROM t_log WHERE log_date < '2023-01-01';
```

## 正例

```sql
-- ✅ 推荐：按分区直接DROP，瞬间完成且不产生行级日志
ALTER TABLE t_log DROP PARTITION p202212;
```
