---
id: audit-rule-aud-droptableviewdisallowed
title: 禁止删除表/视图
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-droptableviewdisallowed
tags:
- audit-rule
- ddl
description: 禁止直接删除表或视图。删除表或视图会造成所有依赖对象与线上查询瞬间失效，引发大面积故障且数据不可逆丢失。在高流量生产系统中，一条 `DROP
  TABLE` 语句可能在数秒内引发雪崩式的连锁故障，且即使有备份，恢复时间也往往以小时甚至天计。
localeOf: en-audit-rule-aud-droptableviewdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-droptableviewdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-droptableviewdisallowed |
| 规则名称 | 禁止删除表/视图 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止直接删除表或视图。删除表或视图会造成所有依赖对象与线上查询瞬间失效，引发大面积故障且数据不可逆丢失。在高流量生产系统中，一条 `DROP TABLE` 语句可能在数秒内引发雪崩式的连锁故障，且即使有备份，恢复时间也往往以小时甚至天计。
正确做法是先做依赖分析与访问审计，确认无引用后将对象重命名，经过充分的观察期后，再通过备份与变更窗口审慎清理。

## 反例

```sql
-- ❌ 不推荐：直接删除表/视图，不可逆，可能引发大范围故障
DROP TABLE t;
DROP VIEW v;
```

## 正例

```sql
-- ✅ 推荐：重命名 → 观察期 → 确认后删除
-- 1. RENAME TABLE t TO t_deprecated_20240101;
-- 2. 观察 N 个业务周期，确认无任何报错引用
-- 3. DROP TABLE t_deprecated_20240101;  -- 在变更窗口执行
```
