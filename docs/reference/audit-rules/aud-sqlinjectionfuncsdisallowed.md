---
id: audit-rule-aud-sqlinjectionfuncsdisallowed
title: 禁止使用常见 SQL 注入函数
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-sqlinjectionfuncsdisallowed
tags:
- audit-rule
- dml
description: SQL 注入是一种常见的网络攻击技术，它利用不安全的输入验证和构造 SQL 查询来获取未授权的信息或向数据库注入恶意代码。常见的 SQL
  注入函数包括 `database()`、`user()`、`version()`、`sleep()`、`load_file()` 等——攻击者通过在输入参数中拼接这些函数，可以获取数据库结构信息、探测注入点是否存在（延时注入）、甚至读取服务器文件。
localeOf: en-audit-rule-aud-sqlinjectionfuncsdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-sqlinjectionfuncsdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-sqlinjectionfuncsdisallowed |
| 规则名称 | 禁止使用常见 SQL 注入函数 |
| 类别 | dml（数据操作） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

SQL 注入是一种常见的网络攻击技术，它利用不安全的输入验证和构造 SQL 查询来获取未授权的信息或向数据库注入恶意代码。常见的 SQL 注入函数包括 `database()`、`user()`、`version()`、`sleep()`、`load_file()` 等——攻击者通过在输入参数中拼接这些函数，可以获取数据库结构信息、探测注入点是否存在（延时注入）、甚至读取服务器文件。
该规则要求在 SQL 审计中检测并禁止使用这些高危函数。对于确实需要使用内置函数的场景，应在应用层通过参数化查询完成，而非在 SQL 文本中直接拼接。

## 反例

```sql
-- ❌ 不推荐：SQL 中包含危险注入函数
SELECT * FROM t WHERE name = CONCAT('input', @@version);

-- ❌ 不推荐：延时注入探测
SELECT * FROM t WHERE id = 1 AND SLEEP(5);
```

## 正例

```sql
-- ✅ 推荐：使用参数化查询，避免函数注入
-- PREPARE stmt FROM 'SELECT * FROM t WHERE name = ?';
```
