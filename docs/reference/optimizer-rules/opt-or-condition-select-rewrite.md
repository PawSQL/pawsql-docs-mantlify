---
id: optimizer-rule-opt-or-condition-select-rewrite
title: OR 条件 SELECT 重写
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: opt-or-condition-select-rewrite
tags:
- optimizer-rule
- rewrite
- mysql
- postgresql
- oracle
description: 拆分 OR 分支时保留 NULL 和重复行语义，再验证执行计划与性能。
localeOf: en-optimizer-rule-opt-or-condition-select-rewrite
subtype: rule
language: zh
translationKey: optimizer-rule-opt-or-condition-select-rewrite
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-or-condition-select-rewrite |
| 规则名称 | OR 条件 SELECT 重写 |
| 类别 | rewrite（重写） |
| 预警级别 | 提示 |
| 适用数据库 | mysql, postgresql, oracle |
| 引入版本 | 8.5.0 |
| 实现 | `OrToUnionRule` |

## 说明

OR 拆分可以为各分支提供不同访问路径，但性能收益依赖数据库、数据分布与索引。以下示例说明语义约束，不构成对 PawSQL 引入版本、自动触发条件或所有方言支持的确认。

## 为什么重要

OR 查询保留输入行的重复次数；UNION 会去重，而简单的“不等于”排除条件会遗漏 NULL 行。

## 如何修复

对确定性谓词，将第二分支限制为第一分支不为真，再使用 UNION ALL。应用前验证方言、NULL、重复行和性能；产品自动改写行为仍待核实。

## 前置条件

- 分支排除条件必须保留 NULL 三值逻辑。

- 必须保留重复行；不能无条件用 UNION 去重代替 OR。

## 排除条件

- 包含易变函数或副作用的谓词需要独立证明，不适用下面的示例推导。

## 验证案例

### 普通分支拆分

`postgresql` · `multiset-equal` · `pending`

```sql
CREATE TABLE demo(a integer, b integer);
INSERT INTO demo VALUES (1, 0), (2, 1), (2, 0);
```

```sql
SELECT * FROM demo WHERE a = 1 OR b = 1;
```

```sql
SELECT * FROM demo WHERE a = 1
UNION ALL
SELECT * FROM demo WHERE b = 1 AND (a <> 1 OR a IS NULL);
```

### NULL、重复行与分支重叠

`postgresql` · `multiset-equal` · `pending`

```sql
CREATE TABLE demo(a integer, b integer);
INSERT INTO demo VALUES (NULL, 1), (1, 1), (1, 1), (2, 1), (2, NULL);
```

```sql
SELECT * FROM demo WHERE a = 1 OR b = 1;
```

```sql
SELECT * FROM demo WHERE a = 1
UNION ALL
SELECT * FROM demo WHERE b = 1 AND (a <> 1 OR a IS NULL);
```
