---
id: audit-rule-aud-use-alter-table-to-set-auto-increment-start-in-t
title: TDSQL中使用ALTER设置自增列的起始值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-use-alter-table-to-set-auto-increment-start-in-t
tags:
- audit-rule
- ddl
description: 在 TDSQL 分布式实例中，`CREATE TABLE` 语句中直接指定 `auto_increment` 起始值可能不会生效。这是因为分布式环境下自增列的初始值管理机制与单机
  MySQL 不同，`CREATE TABLE` 中的 `AUTO_INCREMENT = N` 参数在分布式架构下无法被正确传递到各分片节点。
localeOf: en-audit-rule-aud-use-alter-table-to-set-auto-increment-start-in-t
subtype: rule
language: zh
translationKey: audit-rule-aud-use-alter-table-to-set-auto-increment-start-in-t
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-use-alter-table-to-set-auto-increment-start-in-t |
| 规则名称 | TDSQL中使用ALTER设置自增列的起始值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 提示 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

在 TDSQL 分布式实例中，`CREATE TABLE` 语句中直接指定 `auto_increment` 起始值可能不会生效。这是因为分布式环境下自增列的初始值管理机制与单机 MySQL 不同，`CREATE TABLE` 中的 `AUTO_INCREMENT = N` 参数在分布式架构下无法被正确传递到各分片节点。
必须使用独立的 `ALTER TABLE ... AUTO_INCREMENT = N` 语句在表创建完成后设置自增列的起始值，确保配置在分布式环境下正确生效。

## 反例

```sql
-- ❌ 不推荐（TDSQL 分布式实例中可能不生效）：CREATE 时指定 auto_increment
CREATE TABLE t (
    id BIGINT AUTO_INCREMENT PRIMARY KEY
) shardkey=id auto_increment=10000;
```

## 正例

```sql
-- ✅ 推荐：先用 CREATE 建表，再用 ALTER 设置自增起始值
CREATE TABLE t (
    id BIGINT AUTO_INCREMENT PRIMARY KEY
) shardkey=id;
ALTER TABLE t AUTO_INCREMENT = 10000;
```
