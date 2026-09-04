---
id: optimizer-rules-index
title: 优化算法
description: PawSQL 优化器规则/算法全量目录（由 metadata/rules/optimizer 生成）
type: reference
status: draft
tags:
- optimizer-rules
- zh
localeOf: en-optimizer-rules-index
---

> 生成文件：由已生成的规则页汇总，勿手改；`build-references` 会自动重建。

# 优化算法

共 5 条规则。

| 规则 | ID |
|---|---|
| [COUNT 标量子查询重写](reference/optimizer-rules/opt-count-to-exists) | `opt-count-to-exists` |
| [EXISTS 查询转换为表连接](reference/optimizer-rules/opt-exists-to-join) | `opt-exists-to-join` |
| [NPE 重写（空指针异常预防）](reference/optimizer-rules/opt-npe-rewrite) | `opt-npe-rewrite` |
| [OR 条件 SELECT 重写](reference/optimizer-rules/opt-or-union) | `opt-or-union` |
| [使用 UNION ALL 代替 UNION](reference/optimizer-rules/opt-use-union-all) | `opt-use-union-all` |
