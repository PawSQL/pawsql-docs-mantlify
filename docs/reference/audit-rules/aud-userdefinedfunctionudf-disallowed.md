---
id: audit-rule-aud-userdefinedfunctionudf-disallowed
title: 禁止创建自定义函数
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-userdefinedfunctionudf-disallowed
tags:
- audit-rule
- ddl
description: 禁止创建自定义函数（UDF）。自定义函数将计算逻辑嵌入数据库层，其维护性差、依赖关系隐式复杂，且会导致 SQL 无法跨数据库无缝迁移。在生产环境中，自定义函数中的错误难以追踪和调试，且无法纳入标准的
  CI/CD 流程进行版本管理。
localeOf: en-audit-rule-aud-userdefinedfunctionudf-disallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-userdefinedfunctionudf-disallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-userdefinedfunctionudf-disallowed |
| 规则名称 | 禁止创建自定义函数 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止创建自定义函数（UDF）。自定义函数将计算逻辑嵌入数据库层，其维护性差、依赖关系隐式复杂，且会导致 SQL 无法跨数据库无缝迁移。在生产环境中，自定义函数中的错误难以追踪和调试，且无法纳入标准的 CI/CD 流程进行版本管理。
此外，在分布式数据库中，自定义函数默认无法下推到数据节点执行，只能将数据拉取到协调节点处理，性能极差。即使配置为可下推，函数内 SQL 也只能访问当前节点数据，存在返回不完整结果的严重风险。业务逻辑应严格在应用层实现和复用。

## 反例

```sql
-- ❌ 不推荐：UDF 分布式环境兼容性差，难以维护
CREATE FUNCTION my_func() RETURNS INT
BEGIN
    RETURN 1;
END;
```

## 正例

```sql
-- ✅ 推荐：业务逻辑在应用层实现
-- 应用代码示例：
-- const result = someBusinessLogic();
```
