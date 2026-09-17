---
id: audit-rule-aud-stored-procedure-disallowed
title: 禁止使用存储过程
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-stored-procedure-disallowed
tags:
- audit-rule
- ddl
description: 禁止创建和使用存储过程。存储过程将业务逻辑固化在数据库中，导致应用与数据库高度耦合，不利于系统扩展、维护和分布式改造。在分布式数据库中，存储过程的跨节点执行和事务处理非常复杂，且慢查询日志难以定位存储过程内部的具体问题，故障排查难度极大。存储过程中的逻辑也不便于版本控制和代码审查，脱离了应用的标准
  CI/CD 流程。
localeOf: en-audit-rule-aud-stored-procedure-disallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-stored-procedure-disallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-stored-procedure-disallowed |
| 规则名称 | 禁止使用存储过程 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止创建和使用存储过程。存储过程将业务逻辑固化在数据库中，导致应用与数据库高度耦合，不利于系统扩展、维护和分布式改造。在分布式数据库中，存储过程的跨节点执行和事务处理非常复杂，且慢查询日志难以定位存储过程内部的具体问题，故障排查难度极大。存储过程中的逻辑也不便于版本控制和代码审查，脱离了应用的标准 CI/CD 流程。
实时交易处理中的业务逻辑应严格在应用层实现，保持数据库作为纯粹的数据存储和检索引擎的角色，以此确保架构的清晰分层和可维护性。

## 反例

```sql
-- ❌ 不推荐：存储过程耦合业务逻辑，难以维护和调试
DELIMITER //
CREATE PROCEDURE GetUserOrders(IN userId INT)
BEGIN
    SELECT * FROM orders WHERE user_id = userId;
END //
DELIMITER ;
```

## 正例

```sql
-- ✅ 推荐：业务逻辑在应用层实现
-- 应用代码示例：
-- const orders = db.query('SELECT * FROM orders WHERE user_id = ?', [userId]);
```
