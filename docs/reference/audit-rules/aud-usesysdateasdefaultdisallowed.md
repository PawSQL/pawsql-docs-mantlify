---
id: audit-rule-aud-usesysdateasdefaultdisallowed
title: 禁止使用SYSDATE作为默认值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-usesysdateasdefaultdisallowed
tags:
- audit-rule
- ddl
description: 禁止使用 `SYSDATE()` 作为列的默认值。`SYSDATE()` 属于非确定性函数，其返回值依赖于调用时刻的系统时间。在基于 STATEMENT
  模式的主从复制环境下，主库执行语句的时间与备库重放日志的时间存在差异，导致同一 SQL 在主备库上产生不同的时间值，造成数据不一致。此外，`SYSDATE()`
  的时间语义不可审计，影响数据重放与回滚的可控性。
localeOf: en-audit-rule-aud-usesysdateasdefaultdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-usesysdateasdefaultdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-usesysdateasdefaultdisallowed |
| 规则名称 | 禁止使用SYSDATE作为默认值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用 `SYSDATE()` 作为列的默认值。`SYSDATE()` 属于非确定性函数，其返回值依赖于调用时刻的系统时间。在基于 STATEMENT 模式的主从复制环境下，主库执行语句的时间与备库重放日志的时间存在差异，导致同一 SQL 在主备库上产生不同的时间值，造成数据不一致。此外，`SYSDATE()` 的时间语义不可审计，影响数据重放与回滚的可控性。
正确做法是由应用层显式写入时间，或使用可控的 `CURRENT_TIMESTAMP`/`NOW()`（在基于 ROW 模式的复制中更为安全），并统一时区策略。

## 反例

```sql
-- ❌ 不推荐：SYSDATE() 非确定性，主从不一致风险
CREATE TABLE t (
    id INT,
    created_at DATETIME DEFAULT SYSDATE()
);
```

## 正例

```sql
-- ✅ 推荐：使用 CURRENT_TIMESTAMP 或应用层写入
CREATE TABLE t (
    id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
