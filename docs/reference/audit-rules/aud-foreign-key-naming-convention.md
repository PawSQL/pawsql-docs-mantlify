---
id: audit-rule-aud-foreign-key-naming-convention
title: 外键命名规范
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-foreign-key-naming-convention
tags:
- audit-rule
- index
description: 外键命名规范要求为外键约束指定统一、可辨识的名称，通常格式为包含引用表名、引用列名、被引用表名和被引用列名的组合（如`fk_引用表_引用列_被引用表_被引用列`）。规范的命名便于团队成员快速理解表之间的依赖关系，在排查数据完整性问题和进行数据库变更时尤为重要。
localeOf: en-audit-rule-aud-foreign-key-naming-convention
subtype: rule
language: zh
translationKey: audit-rule-aud-foreign-key-naming-convention
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-foreign-key-naming-convention |
| 规则名称 | 外键命名规范 |
| 类别 | index（索引） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

外键命名规范要求为外键约束指定统一、可辨识的名称，通常格式为包含引用表名、引用列名、被引用表名和被引用列名的组合（如`fk_引用表_引用列_被引用表_被引用列`）。规范的命名便于团队成员快速理解表之间的依赖关系，在排查数据完整性问题和进行数据库变更时尤为重要。
不规范的命名会增加沟通成本，降低代码可读性。在跨团队协作或大型项目中，混乱的外键命名可能导致误删约束或错误的级联操作，引发数据不一致。

## 反例

```sql
-- ❌ 不推荐：外键名称无意义，无法识别引用关系
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    CONSTRAINT fk_1 FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

## 正例

```sql
-- ✅ 推荐：外键名称清晰反映引用关系
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    CONSTRAINT fk_orders_customer_id_customers_id
        FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```
