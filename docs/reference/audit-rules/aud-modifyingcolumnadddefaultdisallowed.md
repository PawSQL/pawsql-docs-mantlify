---
id: audit-rule-aud-modifyingcolumnadddefaultdisallowed
title: 禁止为列新增默认值
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-modifyingcolumnadddefaultdisallowed
tags:
- audit-rule
- ddl
description: 禁止随意为已有列新增默认值，因为这会改变历史与未来写入语义、掩盖上游数据缺陷。新增默认值后，所有未显式指定该列的 INSERT 语句将自动填充新默认值，可能使原本应暴露的缺失数据问题被静默掩盖。在部分数据库中，为已有大表新增默认值还可能触发表重写或长时间锁表，带来性能与可用性风险。
localeOf: en-audit-rule-aud-modifyingcolumnadddefaultdisallowed
subtype: rule
language: zh
translationKey: audit-rule-aud-modifyingcolumnadddefaultdisallowed
layout: detail
product: pawsql
---

> **生成文件，请勿手改。** 如需修改请更新源元数据 (`metadata/rules/audit/*.yaml`) 并重新运行生成器。

| 字段 | 值 |
|---|---|
| 规则 ID | aud-modifyingcolumnadddefaultdisallowed |
| 规则名称 | 禁止为列新增默认值 |
| 类别 | ddl（对象与结构定义） |
| 预警级别 | 警告 |
| 适用数据库 | 待验证（尚未声明数据库范围） |

## 说明

禁止随意为已有列新增默认值，因为这会改变历史与未来写入语义、掩盖上游数据缺陷。新增默认值后，所有未显式指定该列的 INSERT 语句将自动填充新默认值，可能使原本应暴露的缺失数据问题被静默掩盖。在部分数据库中，为已有大表新增默认值还可能触发表重写或长时间锁表，带来性能与可用性风险。
正确做法是先在应用层显式赋值并完成数据回填校验，确认所有路径均正确提供字段值后，再审慎引入默认值。

## 反例

```sql
-- ❌ 不推荐：直接为已有列新增默认值，掩盖数据缺陷
ALTER TABLE t ALTER COLUMN col SET DEFAULT 0;
```

## 正例

```sql
-- ✅ 推荐：先通过应用层回填数据，再统一引入默认值
-- 1. UPDATE t SET col = 0 WHERE col IS NULL;
-- 2. 应用层确保所有 INSERT 显式提供该列值
-- 3. 灰度验证后，ALTER TABLE 添加默认值
```
