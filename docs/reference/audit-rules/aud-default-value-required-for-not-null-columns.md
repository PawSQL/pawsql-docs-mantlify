---
id: audit-rule-aud-default-value-required-for-not-null-columns
title: 非空列需指定带默认值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-default-value-required-for-not-null-columns
tags:
- audit-rule
- ddl
description: 对于定义为 NOT NULL 的列，如果在 INSERT 语句中未显式指定该列的值且该列没有默认值，数据库将抛出错误，导致插入操作失败。这不仅增加了应用程序的异常处理复杂度，也可能在批量数据导入或数据迁移场景中造成大面积的插入失败。
localeOf: en-audit-rule-aud-default-value-required-for-not-null-columns
subtype: rule
language: zh
translationKey: audit-rule-aud-default-value-required-for-not-null-columns
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-default-value-required-for-not-null-columns |
| 规则名称 | 非空列需指定带默认值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

对于定义为 NOT NULL 的列，如果在 INSERT 语句中未显式指定该列的值且该列没有默认值，数据库将抛出错误，导致插入操作失败。这不仅增加了应用程序的异常处理复杂度，也可能在批量数据导入或数据迁移场景中造成大面积的插入失败。
为所有 NOT NULL 列指定默认值是一种防御性的数据库设计实践。它确保了即使在 INSERT 语句中遗漏了某些列，数据库也能通过默认值来生成合法数据，而非直接拒绝操作。默认值的选择应符合业务语义（如状态字段默认 0、布尔字段默认 false、时间字段默认当前时间戳等）。

## 反例

```sql
-- ❌ 不推荐：NOT NULL 列缺少 DEFAULT 值，INSERT 不指定该列会报错
CREATE TABLE user (
    id INT NOT NULL,
    status TINYINT NOT NULL,
    created_at DATETIME NOT NULL
);
```

## 正例

```sql
-- ✅ 推荐：为 NOT NULL 列指定合理的默认值
CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT,
    status TINYINT NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
