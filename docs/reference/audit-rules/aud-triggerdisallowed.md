---
id: audit-rule-aud-triggerdisallowed
title: 禁止使用触发器
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-triggerdisallowed
tags:
- audit-rule
- ddl
description: 禁止使用触发器。触发器将业务逻辑与数据库深度耦合，增加了系统的复杂性，不利于扩展和维护。触发器在后台自动执行，出现问题（如死锁、性能瓶颈、级联触发导致的雪崩效应）时难以定位和排查，排查工具和日志通常无法穿透触发器的执行边界。此外，触发器可能导致主从复制异常，引发数据不一致的风险。
localeOf: en-audit-rule-aud-triggerdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-triggerdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-triggerdisallowed |
| 规则名称 | 禁止使用触发器 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止使用触发器。触发器将业务逻辑与数据库深度耦合，增加了系统的复杂性，不利于扩展和维护。触发器在后台自动执行，出现问题（如死锁、性能瓶颈、级联触发导致的雪崩效应）时难以定位和排查，排查工具和日志通常无法穿透触发器的执行边界。此外，触发器可能导致主从复制异常，引发数据不一致的风险。
所有业务逻辑应在应用层显式实现，确保逻辑的可见性、可调试性和可版本管理性。对于数据审计、变更日志等需求，应通过应用层的切面或中间件实现，而非依赖数据库触发器。

## 反例

```sql
-- ❌ 不推荐：触发器隐式执行，难以排查和调试
CREATE TRIGGER trg_example
AFTER INSERT ON table1
FOR EACH ROW
BEGIN
    UPDATE table2 SET count = count + 1 WHERE id = NEW.id;
END;
```

## 正例

```sql
-- ✅ 推荐：在应用层显式实现业务联动逻辑
-- 应用代码示例：在事务中依次执行 INSERT 和 UPDATE
-- BEGIN;
-- INSERT INTO table1 ...;
-- UPDATE table2 SET count = count + 1 WHERE id = ?;
-- COMMIT;
```
