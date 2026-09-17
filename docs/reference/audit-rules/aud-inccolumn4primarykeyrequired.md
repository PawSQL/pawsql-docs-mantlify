---
id: audit-rule-aud-inccolumn4primarykeyrequired
title: 主键应使用自增列
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-inccolumn4primarykeyrequired
tags:
- audit-rule
- ddl
description: 自增列可以简化主键的生成过程，保证主键值的唯一性，并且在大多数场景下能提供高效的插入性能。使用自增主键能够确保数据按插入顺序物理存储，减少页分裂，提升写入吞吐量。
localeOf: en-audit-rule-aud-inccolumn4primarykeyrequired
subtype: rule
language: zh
translationKey: audit-rule-aud-inccolumn4primarykeyrequired
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-inccolumn4primarykeyrequired |
| 规则名称 | 主键应使用自增列 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

自增列可以简化主键的生成过程，保证主键值的唯一性，并且在大多数场景下能提供高效的插入性能。使用自增主键能够确保数据按插入顺序物理存储，减少页分裂，提升写入吞吐量。
对于单机数据库场景，尤其是使用 InnoDB 存储引擎的 MySQL，自增主键是最佳实践。但需要特别注意的是，在分布式数据库场景下，自增主键可能引发全局唯一性问题，应谨慎评估。

## 反例

```sql
-- ❌ 不推荐：主键未设置自增属性
CREATE TABLE t_user (
    id    BIGINT,
    name  VARCHAR(50),
    PRIMARY KEY (id)
);
```

## 正例

```sql
-- ✅ 推荐：主键使用自增列
CREATE TABLE t_user (
    id    BIGINT AUTO_INCREMENT,
    name  VARCHAR(50),
    PRIMARY KEY (id)
);
```
