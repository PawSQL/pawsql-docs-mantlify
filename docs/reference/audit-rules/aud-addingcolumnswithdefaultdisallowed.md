---
id: audit-rule-aud-addingcolumnswithdefaultdisallowed
title: 禁止新增有默认值的列
type: reference
status: draft
tags:
- audit-rule
- ddl
description: 禁止直接新增带默认值的列，因为这类变更可能触发表重写或长时间锁表、对大表产生严重 I/O 与复制延迟风险，且会在无感知下改变写入语义。对于已有数据的表，数据库需要对每一行回填默认值，这不仅耗时还可能阻塞其他操作。
localeOf: en-audit-rule-aud-addingcolumnswithdefaultdisallowed
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-addingcolumnswithdefaultdisallowed |
| 规则名称 | 禁止新增有默认值的列 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 所有支持数据库 |

## 说明

禁止直接新增带默认值的列，因为这类变更可能触发表重写或长时间锁表、对大表产生严重 I/O 与复制延迟风险，且会在无感知下改变写入语义。对于已有数据的表，数据库需要对每一行回填默认值，这不仅耗时还可能阻塞其他操作。
正确做法是先加可空列、应用层显式写值并完成数据回填后，再分阶段加默认值与非空约束。此规则是数据库变更管理的重要安全规范。

## 反例

```sql
-- ❌ 不推荐：新增列时直接指定默认值，可能触发表重写
ALTER TABLE orders ADD COLUMN status VARCHAR(20) DEFAULT 'pending';
ALTER TABLE orders ADD COLUMN amount DECIMAL(10,2) NOT NULL DEFAULT 0.00;
```

## 正例

```sql
-- ✅ 推荐：先加可空列，回填数据后再加默认值
ALTER TABLE orders ADD COLUMN status VARCHAR(20);
-- 应用层回填数据...
ALTER TABLE orders ALTER COLUMN status SET DEFAULT 'pending';
```
