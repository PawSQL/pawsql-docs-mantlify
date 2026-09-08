---
id: audit-rule-aud-avoid-like-without-wildcards
title: 避免使用没有通配符的 LIKE 查询
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-avoid-like-without-wildcards
tags:
- audit-rule
- dml
description: 无通配符的 LIKE 等价于等值查询，多为漏写通配符；应改 = 或明确补 %/_。
localeOf: en-audit-rule-aud-avoid-like-without-wildcards
subtype: rule
language: zh
translationKey: audit-rule-aud-avoid-like-without-wildcards
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-avoid-like-without-wildcards |
| 规则名称 | 避免使用没有通配符的 LIKE 查询 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

不包含通配符（`%` 或 `_`）的 LIKE 查询在逻辑上与等值查询（`=`）完全相同，但语义上会带来歧义——阅读者无法判断开发者是有意使用 LIKE 进行模式匹配还是误用了 LIKE 替代等值比较。更关键的是，这种写法通常是开发者的疏忽导致的，可能不符合其期望的业务逻辑实现（例如原本想写 `LIKE '%keyword%'` 却漏掉了通配符）。
建议将没有通配符的 LIKE 查询统一替换为等值查询（`=`），使 SQL 语义更加精确和清晰。开发者应特别关注此类预警，确认是否为自己的真实意图。

## 反例

```sql
-- ❌ 不推荐：LIKE 没有通配符，语义上等价于等值查询，可能是疏忽
SELECT * FROM t WHERE name LIKE 'test';
```

## 正例

```sql
-- ✅ 推荐：使用等值查询替代
SELECT * FROM t WHERE name = 'test';

-- 如果确实需要模糊匹配，应明确添加通配符
SELECT * FROM t WHERE name LIKE '%test%';
```
