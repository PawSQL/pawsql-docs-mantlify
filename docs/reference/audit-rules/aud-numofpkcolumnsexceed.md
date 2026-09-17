---
id: audit-rule-aud-numofpkcolumnsexceed
title: 主键的列数目不得超过阈值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-numofpkcolumnsexceed
tags:
- audit-rule
- ddl
description: 过多的主键列会增加主键索引的大小，降低插入和查询性能。主键索引通常是聚簇索引，其大小直接影响数据页的存储密度和扫描效率。主键中包含的列越多，每次插入时维护索引的开销就越大，同时基于主键的关联查询也会更慢。
localeOf: en-audit-rule-aud-numofpkcolumnsexceed
subtype: rule
language: zh
translationKey: audit-rule-aud-numofpkcolumnsexceed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-numofpkcolumnsexceed |
| 规则名称 | 主键的列数目不得超过阈值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

过多的主键列会增加主键索引的大小，降低插入和查询性能。主键索引通常是聚簇索引，其大小直接影响数据页的存储密度和扫描效率。主键中包含的列越多，每次插入时维护索引的开销就越大，同时基于主键的关联查询也会更慢。
主键应当保持简洁，只包含必要的唯一标识字段。复合主键通常可以用一个自增代理键替代，从而在保持业务唯一性的同时获得最佳的性能。

## 反例

```sql
-- ❌ 不推荐：主键包含多个列（超过阈值）
CREATE TABLE order_items (
    order_id   BIGINT,
    product_id BIGINT,
    quantity   INT,
    PRIMARY KEY (order_id, product_id)
);
```

## 正例

```sql
-- ✅ 推荐：使用自增代理键作为主键，业务唯一性通过唯一约束保障
CREATE TABLE order_items (
    id         BIGINT AUTO_INCREMENT,
    order_id   BIGINT,
    product_id BIGINT,
    quantity   INT,
    PRIMARY KEY (id),
    UNIQUE KEY uk_order_product (order_id, product_id)
);
```
