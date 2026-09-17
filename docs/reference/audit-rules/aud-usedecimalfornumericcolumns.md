---
id: audit-rule-aud-usedecimalfornumericcolumns
title: 精确浮点数建议使用Decimal或Number
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-usedecimalfornumericcolumns
tags:
- audit-rule
- ddl
description: 对于需要精确表示的浮点数（如金额、汇率、统计数据），`FLOAT` 和 `DOUBLE` 类型采用二进制近似存储，在进行等值比较或聚合运算时可能产生精度误差，导致业务结果偏离预期。例如
  `0.1 + 0.2` 在浮点运算中并不精确等于 `0.3`。
localeOf: en-audit-rule-aud-usedecimalfornumericcolumns
subtype: rule
language: zh
translationKey: audit-rule-aud-usedecimalfornumericcolumns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-usedecimalfornumericcolumns |
| 规则名称 | 精确浮点数建议使用Decimal或Number |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于需要精确表示的浮点数（如金额、汇率、统计数据），`FLOAT` 和 `DOUBLE` 类型采用二进制近似存储，在进行等值比较或聚合运算时可能产生精度误差，导致业务结果偏离预期。例如 `0.1 + 0.2` 在浮点运算中并不精确等于 `0.3`。
建议使用 `DECIMAL`（MySQL/PostgreSQL/opengauss）或 `NUMBER`（Oracle）等精确数值类型来替代浮点型，以确保计算结果的精确性和一致性，避免因精度问题引发的财务或业务数据错误。

## 反例

```sql
-- ❌ 不推荐：使用 FLOAT / DOUBLE 存储精确数值
CREATE TABLE t (amount FLOAT);
CREATE TABLE t (price DOUBLE);
```

## 正例

```sql
-- ✅ 推荐：使用 DECIMAL 或 NUMBER 精确数值类型
CREATE TABLE t (amount DECIMAL(18,6));
CREATE TABLE t (price DECIMAL(10,2));
```
