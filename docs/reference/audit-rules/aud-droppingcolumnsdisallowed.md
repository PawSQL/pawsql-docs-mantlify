---
id: audit-rule-aud-droppingcolumnsdisallowed
title: 禁止删除字段
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-droppingcolumnsdisallowed
tags:
- audit-rule
- ddl
description: 禁止直接删除表中的字段（`DROP COLUMN`）。删除字段会导致历史 SQL、报表、ETL 脚本与应用代码瞬间失效，且数据不可逆丢失。即使当前认为某个字段已无用途，也可能存在未被充分评估的下游依赖（如定时任务、数据导出、监控大盘等），直接删除将引发大面积故障。
localeOf: en-audit-rule-aud-droppingcolumnsdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-droppingcolumnsdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-droppingcolumnsdisallowed |
| 规则名称 | 禁止删除字段 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止直接删除表中的字段（`DROP COLUMN`）。删除字段会导致历史 SQL、报表、ETL 脚本与应用代码瞬间失效，且数据不可逆丢失。即使当前认为某个字段已无用途，也可能存在未被充分评估的下游依赖（如定时任务、数据导出、监控大盘等），直接删除将引发大面积故障。
正确做法是先做血缘与依赖分析，将字段标记为废弃并停止写入，经过充分的观察期确认无任何引用后，再在备份与变更窗口内安全下线。

## 反例

```sql
-- ❌ 不推荐：直接删除列，不可逆，可能破坏下游依赖
ALTER TABLE t DROP COLUMN some_col;
```

## 正例

```sql
-- ✅ 推荐：标记废弃 → 观察期 → 灰度下线
-- 1. 停止应用写入该字段
-- 2. 观察 N 个业务周期，确认无查询引用
-- 3. 备份数据
-- 4. ALTER TABLE t DROP COLUMN some_col;
```
