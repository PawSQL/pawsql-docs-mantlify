---
id: audit-rule-aud-deleteupdate-forbidden-with-table-join
title: DELETE/UPDATE禁止使用连接
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-deleteupdate-forbidden-with-table-join
tags:
- audit-rule
- dml
description: 表连接的误操作可能导致 DELETE 或 UPDATE 影响的结果集行数非常大。对大结果集的 DELETE/UPDATE 操作可能会非常耗时，锁表时间较长，且在出现问题时难以对操作进行回滚。在高并发生产环境中，涉及多表连接的
  DML 操作还可能导致死锁和严重的性能下降。
localeOf: en-audit-rule-aud-deleteupdate-forbidden-with-table-join
subtype: rule
language: zh
translationKey: audit-rule-aud-deleteupdate-forbidden-with-table-join
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-deleteupdate-forbidden-with-table-join |
| 规则名称 | DELETE/UPDATE禁止使用连接 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

表连接的误操作可能导致 DELETE 或 UPDATE 影响的结果集行数非常大。对大结果集的 DELETE/UPDATE 操作可能会非常耗时，锁表时间较长，且在出现问题时难以对操作进行回滚。在高并发生产环境中，涉及多表连接的 DML 操作还可能导致死锁和严重的性能下降。
此规则检测 DELETE/UPDATE 语句中是否使用了多表连接（JOIN），对于涉及多表的 DML 操作进行预警，引导开发者采用更安全的方式（如拆分操作或使用子查询）来执行数据变更。

## 反例

```sql
-- ❌ 不推荐：DELETE 使用多表连接，影响行数可能非常大
DELETE t1 FROM t1 JOIN t2 ON t1.id = t2.id;

-- ❌ 不推荐：UPDATE 使用多表连接
UPDATE t1 JOIN t2 ON t1.id = t2.id SET t1.status = 1;
```

## 正例

```sql
-- ✅ 推荐：使用子查询替代表连接
DELETE FROM t1 WHERE id IN (SELECT id FROM t2);
```
