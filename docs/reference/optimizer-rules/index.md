---
id: optimizer-rules-index
title: 优化算法
description: 优化算法：查阅规则条件、示例和限制。
type: reference
subtype: rule
layout: index
status: draft
translationKey: optimizer-rules-index
language: zh
localeOf: en-optimizer-rules-index
product: pawsql
---

共 5 条规则。

| 规则 | ID | 分类 | 严重级别 |
|---|---|---|---|
| [OR 条件 SELECT 重写](/reference/optimizer-rules/opt-or-union) | `OPT-OR-UNION` | rewrite | info |
| [COUNT 标量子查询重写](/reference/optimizer-rules/opt-count-to-exists) | `opt-count-to-exists` | rewrite | info |
| [EXISTS 查询转换为表连接](/reference/optimizer-rules/opt-exists-to-join) | `opt-exists-to-join` | rewrite | info |
| [NPE 重写（空指针异常预防）](/reference/optimizer-rules/opt-npe-rewrite) | `opt-npe-rewrite` | rewrite | warning |
| [使用 UNION ALL 代替 UNION](/reference/optimizer-rules/opt-use-union-all) | `opt-use-union-all` | rewrite | info |
