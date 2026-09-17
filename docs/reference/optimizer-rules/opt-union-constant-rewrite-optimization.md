---
id: optimizer-rule-opt-union-constant-rewrite-optimization
title: UNION常量重写优化
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-union-constant-rewrite-optimization
tags:
- optimizer-rule
- rewrite
description: '`INSERT INTO ... SELECT ... UNION ALL SELECT ...` 这种写法是将多个常量值通过 `UNION
  ALL` 拼凑成结果集再插入目标表。这种写法不仅性能低下（需要构造派生表并执行 UNION ALL 合并），而且在特定 JDBC 配置下可能偶发结果集错误。'
localeOf: en-optimizer-rule-opt-union-constant-rewrite-optimization
subtype: rule
language: zh
translationKey: optimizer-rule-opt-union-constant-rewrite-optimization
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-union-constant-rewrite-optimization |
| 规则名称 | UNION常量重写优化 |
| 类别 | rewrite（重写） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

`INSERT INTO ... SELECT ... UNION ALL SELECT ...` 这种写法是将多个常量值通过 `UNION ALL` 拼凑成结果集再插入目标表。这种写法不仅性能低下（需要构造派生表并执行 UNION ALL 合并），而且在特定 JDBC 配置下可能偶发结果集错误。
PawSQL 检测此类模式并重写为原生的 `INSERT INTO ... VALUES (...), (...), ...` 多值插入形式，直接从值列表插入，避免了不必要的 UNION ALL 操作，同时在 JDBC 驱动层面更加可靠。

## 反例

```sql
-- ❌ 不推荐：通过 UNION ALL 拼凑常量插入，性能低下且不可靠
INSERT INTO t(a, b) SELECT 1, 'a' UNION ALL SELECT 2, 'b';
```

## 正例

```sql
-- ✅ 推荐：重写为原生多值 INSERT，简洁高效
INSERT INTO t(a, b) VALUES (1, 'a'), (2, 'b');
```
