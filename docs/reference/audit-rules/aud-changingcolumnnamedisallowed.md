---
id: audit-rule-aud-changingcolumnnamedisallowed
title: 禁止修改字段名
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止直接改字段名（破坏上下游依赖）；需要时用灰度：加新列→双写→切换→下线旧列。
localeOf: en-audit-rule-aud-changingcolumnnamedisallowed
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-changingcolumnnamedisallowed |
| 规则名称 | 禁止修改字段名 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

禁止修改字段名（`RENAME COLUMN` / `CHANGE COLUMN`）。重命名字段会对所有依赖该字段的应用程序、报表、ETL 脚本和视图造成影响，导致线上业务瞬间中断。在不支持不停机发布的架构中，这种修改需要在维护窗口内协调大量上下游系统，风险极高。
如果确实需要重命名字段，应由 DBA 在充分评估依赖关系后手工干预，通过灰度方案（如新增列 + 双写 + 切换 + 下线旧列）实现平滑过渡，而不是直接执行 `RENAME` 操作。

## 反例

```sql
-- ❌ 不推荐：直接重命名列，破坏上下游依赖
ALTER TABLE t CHANGE old_name new_name VARCHAR(50);
```

## 正例

```sql
-- ✅ 推荐：灰度方案
-- 1. ALTER TABLE t ADD COLUMN new_name VARCHAR(50);
-- 2. 双写 + 历史数据回填
-- 3. 切换所有消费方使用 new_name
-- 4. ALTER TABLE t DROP COLUMN old_name;
```
