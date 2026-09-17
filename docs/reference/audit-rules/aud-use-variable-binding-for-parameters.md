---
id: audit-rule-aud-use-variable-binding-for-parameters
title: 对于入参建议使用变量绑定
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-variable-binding-for-parameters
tags:
- audit-rule
- dml
description: 通过变量绑定（Parameter Binding / Prepared Statement），数据库可以重用已有的SQL执行计划，降低SQL硬解析的时间开销，这对于高并发OLTP场景尤为重要。同时，变量绑定还能有效防止SQL注入攻击，提升应用的安全性。将SQL中的常量替换为绑定变量后，数据库无需每次重新解析和规划执行路径，可直接复用缓存的执行计划。
localeOf: en-audit-rule-aud-use-variable-binding-for-parameters
subtype: rule
language: zh
translationKey: audit-rule-aud-use-variable-binding-for-parameters
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-variable-binding-for-parameters |
| 规则名称 | 对于入参建议使用变量绑定 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

通过变量绑定（Parameter Binding / Prepared Statement），数据库可以重用已有的SQL执行计划，降低SQL硬解析的时间开销，这对于高并发OLTP场景尤为重要。同时，变量绑定还能有效防止SQL注入攻击，提升应用的安全性。将SQL中的常量替换为绑定变量后，数据库无需每次重新解析和规划执行路径，可直接复用缓存的执行计划。
该规则支持两种模式：strict模式下，SQL中出现任意常量即触发告警；loose模式下，仅在WHERE条件及ORDER BY排序的字段中不存在变量绑定时触发告警。

## 反例

```sql
-- ❌ 不推荐：硬编码参数值，每次执行需要重新解析和规划
SELECT * FROM t WHERE name = 'test_value';
```

## 正例

```sql
-- ✅ 推荐：使用变量绑定，复用执行计划，防止SQL注入
-- （以JDBC PreparedStatement为例）
-- PreparedStatement ps = conn.prepareStatement("SELECT * FROM t WHERE name = ?");
-- ps.setString(1, "test_value");
SELECT * FROM t WHERE name = ?;
```
