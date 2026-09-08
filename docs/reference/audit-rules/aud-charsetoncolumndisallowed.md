---
id: audit-rule-aud-charsetoncolumndisallowed
title: 禁止指定列的字符集
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-charsetoncolumndisallowed
tags:
- audit-rule
- ddl
description: 禁止列级单独指定字符集（JOIN 隐式转换致索引失效/全表扫描）；字符集在表级统一。
localeOf: en-audit-rule-aud-charsetoncolumndisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-charsetoncolumndisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-charsetoncolumndisallowed |
| 规则名称 | 禁止指定列的字符集 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止为列单独指定字符集。当列的字符集与表或数据库的默认字符集不一致时，`JOIN` 操作中需要进行隐式字符集转换，这会导致索引失效并引发全表扫描——此类性能问题隐蔽且影响范围大。此外，字符集不一致还可能造成数据比较结果不符合预期，产生难以排查的业务逻辑错误。
推荐在表级别统一指定字符集，让所有列继承一致的字符集设置，避免列级别的特殊化配置。

## 反例

```sql
-- ❌ 不推荐：列级别单独指定字符集，可能导致 JOIN 索引失效
CREATE TABLE t (
    id INT,
    name VARCHAR(100) CHARACTER SET latin1
);
```

## 正例

```sql
-- ✅ 推荐：在表级别统一指定字符集
CREATE TABLE t (
    id INT,
    name VARCHAR(100)
) DEFAULT CHARSET=utf8mb4;
```
