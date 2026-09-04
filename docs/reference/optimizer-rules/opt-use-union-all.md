---
id: zh-optimizer-rule-opt-use-union-all
title: 使用 UNION ALL 代替 UNION
type: reference
status: draft
tags:
- optimizer-rule
- zh
- rewrite
description: 使用 UNION 获取两个结果集的并集时，数据库会对结果集进行去重操作。去重通常通过排序或哈希的方式实现，这两种方式都需要消耗大量的 CPU
  和内存资源。如果业务逻辑上可以保证两个结果集没有重复数据，或者允许结果集中存在重复行，应当使用 UNION ALL 来代替 UNION，可以获得显著的性能提升。
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/optimizer/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | opt-use-union-all |
| 规则名称 | 使用 UNION ALL 代替 UNION |
| 类别 | rewrite |
| 预警级别 | 提示 |
| 适用数据库 | 所有支持数据库 |

## 说明

使用 UNION 获取两个结果集的并集时，数据库会对结果集进行去重操作。去重通常通过排序或哈希的方式实现，这两种方式都需要消耗大量的 CPU 和内存资源。如果业务逻辑上可以保证两个结果集没有重复数据，或者允许结果集中存在重复行，应当使用 UNION ALL 来代替 UNION，可以获得显著的性能提升。

## 如何修复

当两个分支不可能产生重复行、或允许出现重复行时，将 UNION 改写为 UNION ALL，让数据库省去去重步骤。

## 反例

```sql
-- 不推荐：UNION 触发去重操作，消耗额外资源
SELECT name FROM t_user_2023
UNION
SELECT name FROM t_user_2024;
```

## 正例

```sql
-- 推荐：无需去重时使用 UNION ALL 提升性能
SELECT name FROM t_user_2023
UNION ALL
SELECT name FROM t_user_2024;
```
