---
id: audit-rule-aud-primarykeyrequired
title: 表必须建主键
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-primarykeyrequired
tags:
- audit-rule
- ddl
description: 要求每个表都必须定义一个主键，主键是关系数据库设计的核心原则。主键可以唯一标识每条记录，有助于确保数据的唯一性，同时作为聚簇索引（InnoDB）或默认索引来提升查询效率。缺少主键的表无法有效进行行级定位，在复制、备份和增量同步场景中也会带来困难。
localeOf: en-audit-rule-aud-primarykeyrequired
subtype: rule
language: zh
translationKey: audit-rule-aud-primarykeyrequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-primarykeyrequired |
| 规则名称 | 表必须建主键 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 错误 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

要求每个表都必须定义一个主键，主键是关系数据库设计的核心原则。主键可以唯一标识每条记录，有助于确保数据的唯一性，同时作为聚簇索引（InnoDB）或默认索引来提升查询效率。缺少主键的表无法有效进行行级定位，在复制、备份和增量同步场景中也会带来困难。
创建表时未定义主键将触发严重级别告警。如果需要使用自增列作为主键，应结合自增列的命名和类型规范进行设计。

## 反例

```sql
-- ❌ 不推荐：表未定义主键
CREATE TABLE orders (
    order_id BIGINT,
    amount DECIMAL(10,2)
);
```

## 正例

```sql
-- ✅ 推荐：明确定义主键
CREATE TABLE orders (
    order_id BIGINT PRIMARY KEY,
    amount DECIMAL(10,2)
);
```
