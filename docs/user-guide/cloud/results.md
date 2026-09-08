---
id: zh-user-guide-cloud-results
title: 优化结果解析
description: 阅读 PawSQL Cloud 的优化详情：重写优化、规则审查、索引推荐、索引分析与性能验证，以及 SQL / 执行计划比对。
type: guide
product: pawsql
status: draft
tags:
- cloud
- saas
- user-guide
- results
- zh
subtype: operation
language: zh
translationKey: user-guide-cloud-results
layout: detail
deployments:
- public-cloud
---

# 优化结果解析

优化任务完成后，在**优化详情页面**查看结果。

> TODO(截图待补)：优化详情页面（源图未归档，待补齐）。

## 优化详情包括

- **原始 SQL**
- **重写优化**
  - 重写后的 SQL
  - 重写所应用的优化策略
  - 重写优化对应的 SQL 片段
- **规则审查情况**
  - 违反的审查规则
  - 违反规则的 SQL 片段
- **索引推荐情况**
  - 推荐的索引
  - 索引推荐的依据
- **索引分析**
  - 各表上的索引列表及其是否冗余
  - 现有索引如何帮助此 SQL
  - 单表索引个数超过阈值的提示
- **性能验证**
  - 性能提升比
  - 验证生效的推荐索引
  - 优化前的执行计划
  - 优化后的执行计划

## 重写 SQL 比对

点击优化页面右上方的**对比 SQL** 按钮，可以展示重写前后 SQL 文本的变化。

> TODO(截图待补)：SQL 对比视图（源图未归档，待补齐）。

## 执行计划比对

点击优化页面右上方的**对比执行计划** 按钮，可以展示优化前后的执行计划。

> TODO(截图待补)：执行计划对比视图（源图未归档，待补齐）。

上一节：[三步完成您的 SQL 优化](user-guide/cloud/quickstart)。
