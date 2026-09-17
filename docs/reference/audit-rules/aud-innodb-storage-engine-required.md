---
id: audit-rule-aud-innodb-storage-engine-required
title: 必须使用INNODB存储引擎
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-innodb-storage-engine-required
tags:
- audit-rule
- ddl
description: 该规则要求所有创建表的操作必须指定InnoDB作为存储引擎。InnoDB是MySQL的默认存储引擎，支持事务（ACID）、行级锁定、外键约束和崩溃恢复等关键特性，能够提供更好的数据完整性和并发性能。相比之下，MyISAM等旧存储引擎不支持事务和行级锁，在高并发写入场景下容易出现表锁冲突，且不具备崩溃后的自动恢复能力。
localeOf: en-audit-rule-aud-innodb-storage-engine-required
subtype: rule
language: zh
translationKey: audit-rule-aud-innodb-storage-engine-required
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-innodb-storage-engine-required |
| 规则名称 | 必须使用INNODB存储引擎 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

该规则要求所有创建表的操作必须指定InnoDB作为存储引擎。InnoDB是MySQL的默认存储引擎，支持事务（ACID）、行级锁定、外键约束和崩溃恢复等关键特性，能够提供更好的数据完整性和并发性能。相比之下，MyISAM等旧存储引擎不支持事务和行级锁，在高并发写入场景下容易出现表锁冲突，且不具备崩溃后的自动恢复能力。
在MySQL、PolarDB（InnoDB引擎）和TDSQL（InnoDB引擎）等基于MySQL的数据库中，创建表时应显式指定`ENGINE=InnoDB`或依赖数据库默认设置确保使用InnoDB。

## 反例

```sql
-- ❌ 不推荐：使用MyISAM引擎，不支持事务和行级锁
CREATE TABLE t (id INT) ENGINE=MyISAM;
```

## 正例

```sql
-- ✅ 推荐：使用InnoDB引擎，支持事务、行级锁和崩溃恢复
CREATE TABLE t (id INT) ENGINE=InnoDB;
```
