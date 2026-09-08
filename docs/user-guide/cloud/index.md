---
id: zh-user-guide-cloud-index
title: PawSQL Cloud 使用手册
description: PawSQL Cloud 产品概述：能力范围、核心功能与支持的数据库。
type: guide
product: pawsql
status: draft
tags:
- cloud
- saas
- user-guide
- zh
subtype: operation
language: zh
translationKey: user-guide-cloud-index
layout: detail
deployments:
- public-cloud
---

# PawSQL Cloud 使用手册

PawSQL Cloud 是 PawSQL Advisor 的 SaaS 版本。它整合了业界关于关系数据库查询优化的最佳实践，通过查询重写优化与智能索引推荐，帮助应用开发人员及数据库管理人员一站式解决 SQL 性能问题。

PawSQL Cloud 免安装，既适合应用开发人员，也适合数据库管理人员等非开发人员使用。它能够记录优化历史，便于日后查看和跟踪；优化结果可以通过链接与同事共享，或发布到 Jira 等开发管理工具中。

> 状态：本文档由历史内容整理，页面处于 draft，功能细节与截图待与新版产品核对。

## 核心功能

- **规则审查**：基于规则的 SQL 审查，包括正确性审查与性能优化审查规则。
- **重写优化**：丰富的 SQL 重写优化，推荐语义等价、执行效率更高的 SQL。
- **智能索引推荐**：覆盖多种 SQL 语法组合场景，推荐最优的索引组合。
- **基于代价的性能验证**：确保基于 SQL 重写与索引推荐的新方案具有更好的性能。
- **索引分析**：定位冗余索引，节省系统资源。
- **执行计划可视化分析**：快速定位 SQL 性能瓶颈。

## 支持的数据库

PawSQL 基于自研 SQL 解析器，支持多种数据库类型及 SQL 方言，支持范围仍在不断增加中：

- MySQL 5.6 及以上（official）
- PostgreSQL 9.1 及以上（official）
- openGauss 1.0 及以上（official）
- MariaDB 5.6 及以上（alpha）
- Oracle 11g 及以上（alpha）
- KingbaseES V8（alpha）

> 注：以上为历史快照，确切的支持范围以[数据库兼容性矩阵](en/reference/compatibility/index)为准，待产品复核。

## 阅读路线

- [三步完成您的 SQL 优化](user-guide/cloud/quickstart) —— 创建工作空间、输入待优化 SQL、创建查询优化。
- [优化结果解析](user-guide/cloud/results) —— 优化详情、SQL 比对与执行计划比对。
