# PawSQL 文档内容完整性蓝图（CONTENT-BLUEPRINT）

> 版本：v0.1 · 2026-09-08（草稿，待评审）
> 性质：**规划/清单**（目标态蓝图，非实施记录）
> 目的：回答“PawSQL 文档网站从完整性看应该包含哪些内容”，作为 [MIGRATION-PLAN.md](MIGRATION-PLAN.md) 的内容前置文档与批次输入。
> 规范基线：[CONTENT-MODEL-V2.md](CONTENT-MODEL-V2.md)；方法：[MIGRATION-PLAYBOOK.md](MIGRATION-PLAYBOOK.md)；落位表：[PLACEMENT.md](PLACEMENT.md)。
> 与迁移的关系：蓝图按**目标站完整性**推导，旧 vault 迁移只是内容供给之一；凡目标页无历史源的，标记 `new`（新建），不能用“旧文档没有”作为不做的理由。

---

## 1. 目的与用法

1. 定义**目标态**应存在的全部内容（page 级或 page 组级），供批次规划、缺位判定与发布验收使用。
2. 状态符号：`✅` 已有（至少 draft）/ `🔶` 占位或半成品 / `❌` 缺失 / `🆕` 建议新增。
3. 每条目标页标注：建议路由(slug)、type/subtype、来源（`new`/`重构`/`vault`/`生成`）、优先级、量级、依赖锁。
4. 验收 = §5 的覆盖矩阵三条 + 质量闸门；**“有页面”≠“内容完整”**（还需 §4 的事实/证据/复核）。

## 2. 推导维度与受控词表

内容需覆盖四张正交维度（词表取自 `metadata/taxonomies/dimensions.yaml`）：

| 维度 | 取值 |
|---|---|
| components（交付形态） | engine · optimizer · auditor · advisor · patroller |
| capabilities（能力） | sql-audit · sql-rewrite · index-recommendation · performance-validation · plan-visualization · performance-inspection |
| editions | community · enterprise |
| deployments | public-cloud · private |
| interfaces | web · api · cli |
| integrations | jetbrains · dbeaver · vscode · github-actions · cicd · mcp |
| audience | developer · dba · administrator · platform-engineer |

六类内容与 subtype 见 CONTENT-MODEL-V2 §2。任何“支持/能力/集成”的声称必须带版本与证据（supported/partial/unknown），不允许无依据承诺。

---

## 3. 站点内容地图（目标态）

### 3.1 「文档」tab — 六组

#### ① 开始使用
| # | 目标页 (slug) | type/subtype | 来源 | 现状 | 优先级 | 锁/备注 |
|---|---|---|---|---|---|---|
| 1.1 | overview（产品定位/能力总览） | explanation | new/重构 | ✅ | — | 已有 |
| 1.2 | quickstart（端到端首跑） | guide/quickstart | new | ✅ | — | 已有 |
| 1.3 | supported-databases（目录+能力矩阵+说明） | explanation | 重构 | ✅ | — | 已有；矩阵口径待统一(§6.3) |
| 1.4 | tutorials/每能力一条教学路径（审核/重写/索引/验证/计划/巡检 ≥6） | guide/quickstart | new/vault | 🔶 仅 en landing | P1 | |
| 1.5 | terminology/概念速览入口（链到⑤ glossary） | explanation | new | ❌ | P2 | 可并入 overview |

#### ② 安装与接入
| # | 目标页 | type/subtype | 来源 | 现状 | 优先级 | 锁/备注 |
|---|---|---|---|---|---|---|
| 2.1 | choose-access（部署形态×入口决策） | explanation | new | ✅ | — | 已有 |
| 2.2 | cloud 开通/连接/工作空间（public-cloud，web） | guide/installation | 重构(vault) | 🔶 user-guide/cloud 部分 | P1 | 锁5 DB/套餐快照 |
| 2.3 | engine 私有部署：环境要求/安装(Docker/裸机)/升级/卸载 | guide/installation | vault | ❌ | P1 | 拆页按 PLAYBOOK |
| 2.4 | IDE 接入：jetbrains / dbeaver / vscode（各一 setup+connect+权限） | guide/integration | new | ❌ | P1 | 锁3（Advisor/插件语义） |
| 2.5 | CI/CD：github-actions / cicd 门禁接入 | guide/integration | new/vault | ❌ | P1 | |
| 2.6 | MCP 接入 | guide/integration | new | ❌ | P2 | 三处合一（C 去重） |
| 2.7 | API 快速接入：认证/调用（webhook vs REST） | guide/integration | new | ❌ | P1 | 链 5 tab API |
| 2.8 | 最小集成矩阵（接入端 × 能力 × DB × 模式） | reference | new | ❌ | P1 | 单一事实源，勿抄 |

#### ③ 使用 PawSQL（按能力组织）
每能力给 concept + operation + 对应 reference 三件套；cloud/engine 差异处拆分。

| # | 目标页 | type/subtype | 现状 | 优先级 |
|---|---|---|---|---|
| 3.1 | sql-audit：跑审核/读报告/配规则集与豁免/当上线门禁 | guide/operation | ❌ | P0 |
| 3.2 | sql-rewrite：启用/审阅改写/等价性判定 | guide/operation | ❌ | P1 |
| 3.3 | index-recommendation：使用/应用/回滚/合并存量索引 | guide/operation | ❌ | P1 |
| 3.4 | performance-validation：基线→优化→验证闭环/读代价对比 | guide/operation | ❌ | P1 |
| 3.5 | plan-visualization：分析/可视化执行计划 | guide/operation | ❌ | P2 |
| 3.6 | performance-inspection：慢 SQL 采集/对象巡检/调度 | guide/operation | ❌ | P2 |
| 3.7 | 工作区/工单/项目：创建、历史、分享、权限（cloud） | guide/operation | 🔶 cloud 部分 | P1 |
| 3.8 | 每能力 explain 长文（why、边界、NULL/重复行） | explanation | ❌（并入4.x） | P1 |
| 3.9 | 结果阅读（审核/重写/索引三态结果） | guide/operation | 🔶 user-guide/cloud/results | P1 |

#### ④ 能力与原理（explanation）
| # | 目标页 | 现状 | 优先级 |
|---|---|---|---|
| 4.1 | architecture：解析器/SQL 中间表示/可插拔适配/代价模型 | ❌（features/index 为占位 landing） | P0 |
| 4.2 | 语义等价重写原理与限制（何时不适用） | ❌ | P0 |
| 4.3 | “支持数据库”分层模型（解析→元数据→优化器→计划） | 🔶 已内嵌 supported-databases §说明 | P1 |
| 4.4 | 各 capability 机制说明 ×6 | ❌ | P1 |
| 4.5 | features/index 用 Feature Manifest 生成目录（能力×版本×组件） | 🔶 占位 | P1 |

#### ⑤ 参考资料（reference，多为 metadata 驱动/生成）
| # | 目标页 | subtype | 现状 | 量级 | 优先级/锁 |
|---|---|---|---|---|---|
| 5.1 | audit-rules 目录 + 每条规则页 | rule | 🔶 59/261（audit54+opt5）双语已提交 | audit ~221 + optimizer ~40 | P0 · 锁1/2 |
| 5.2 | database 兼容：supported-databases 内嵌矩阵 + 每库单页 | database | 🔶 16 库 metadata；per-db 仅 en；状态 SAMPLE/unknown | 16 | P0.6 · 锁5 |
| 5.3 | configuration 参考（每参数：类型/默认/范围/作用域/生效/优先级/冲突） | configuration | ❌ 仅 1（en） | ~10+ | P1 |
| 5.4 | api/overview + OpenAPI | api | 🔶 openapi 占位 1.6KB | 1 真实合约 | P1 · 锁6 |
| 5.5 | CLI 参考（子命令/参数/示例） | cli | ❌ | 1 目录 | P2（若 CLI 为真实入口） |
| 5.6 | error-code（错误码/报错中心：连接/校验/超时…） | error-code | ❌ | 1 目录 | P2 |
| 5.7 | glossary/术语表（含 zh↔en 别名） | glossary | 🔶 contributing/terminology 单页 | 1 | P1 · D1/B5 |

#### ⑥ 帮助与排障（support）
| # | 目标页 | subtype | 现状 | 量级 | 优先级 |
|---|---|---|---|---|---|
| 6.1 | faq（按受众：developer/dba/devops 分组） | faq | 🔶 help/index、en/faq 单页 | 30+ | P1 |
| 6.2 | troubleshooting：连不上/分析失败/结果不符/性能未提升/插件异常 | troubleshooting | 🔶 help/index 框架 | 15+ | P1 |
| 6.3 | migration 专项（Oracle→Gauss 等） | troubleshooting | ❌ | 5+ | P2 · 锁4 |

### 3.2 其余四个 tab
| Tab | 目标内容 | 现状 | 优先级 |
|---|---|---|---|
| 用户场景 | ≥5 persona 端到端（IDE 自研 / CI-CD 门禁 / DBA 慢SQL治理 / 迁移信创 / 企业 SQL 治理） | 🔶 仅 index | P1 |
| API | OpenAPI（真实合约）+ 指南 + 认证/限流/错误结构 | 🔶 占位 | P1 · 锁6 |
| 博客 | engineering（实战/case study）× product/community；每篇日期/作者/来源/去营销 | 🔶 样例 2 | P2 · 锁7(案例合规) |
| 变更日志 | 版本化 release notes：新能力/行为变化/DB支持变化/升级动作（zh 补上） | 🔶 仅 en 样例 | P2 |

---

## 4. 导航之外的“内容底座”（缺失则整站不可信）

| 项 | 要求 | 关联 v2 项 |
|---|---|---|
| 双语对齐 | 至少“使用、能力与原理、参考、FAQ、release notes”有 zh；`localeOf/translationKey` 可校验 | §3/§4 |
| 自描述元数据 | 每页 `product/version/database/documentType/featureId/language` 一致键（RAG/搜索） | §4 B4 |
| Glossary/术语唯一 | 一概念一词、检索别名；`-polish`/多版本重复治理 | B5/D1/C2 |
| Evidence + owner | 每条规则/DB/config 支持依据（source/verifiedBy/verifiedAt）+ 审核记录；DB 状态不得长期 unknown 冒充支持 | §5/§8 |
| 单一事实源 | 兼容矩阵、参数、API 从 metadata/合约派生，不在多处手抄 | §13 原则 |
| 图片 | 有图必有语义 alt；缺图 `TODO(截图待补)`+draft，不进发布 | C3 |
| 导航=发布 | approved/published 才入导航；draft 仅本地/分支可检索 | B3 |

---

## 5. 完整性与验收（发布门槛）

一份站点“完整”至少满足三条覆盖矩阵，全部通过才算可发布：

1. **能力覆盖**：每 capability 至少 `1 explanation + 1 guide(operation) + 对应 reference`；每 integrations 至少 1 篇 `guide/integration`。
2. **事实覆盖**：规则/DB/config 中无“无依据支持承诺”；`unknown` 记录能被追踪为待核（有清单），不冒充支持。
3. **发布覆盖**：导航仅含 approved/published；`validate-nav` 通过；`drift/coverage` 100%；无断链（内部链接检查器在 CI）。

量级汇总（估）：rules ~260 · 教程 ≥6 · 接入指南 ~8 · 使用指南 ~12 · 能力/原理 ~8 · config ~10 · API/CLI/error-code/glossary 各 ≥1 · FAQ/troubleshooting 45+ · use-case ≥5 · blog/RN 按发布。当前人工正文远低于该量级（§7 差距）。

---

## 6. 建议落地顺序与登记

- 继续 MIGRATION-PLAN 顺序，但把本蓝图纳入每批的“内容范围”来源：
  - **P0**：规则 261 补完（锁1/2）+ 能力 3.x 使用指南（审核/重写/索引/验证）+ 4.x 架构原理
  - **P0.6/下一批**：DB/config 状态核定 + zh 单库/配置参考补齐
  - **P1**：接入（cloud/engine/IDE/CI/MCP/API）8 篇 + 使用指南补齐 + FAQ/troubleshooting + use-case + glossary
  - **P2**：CLI/error-code + migration + blog/RN + 案例合规
- 每完成一条：蓝图状态列 `🔶→✅` 并回填日期/commit；未完成项保留 `❌/🔶`，发布时按 §5 门槛截断。

### 6.1 相关产品锁（沿用 MIGRATION-PLAN §6，另加）
| 锁 | 待确认 | 阻塞 |
|---|---|---|
| 1/2 | 规则分类字典 + Rule ID 注册表 | 规则 261 全部 |
| 3 | “Advisor/IDE 插件”语义 | 2.4/3.x 接入 |
| 4 | Ora2pg / 迁移工具范围 | 6.3 |
| 5 | DB 版本/能力快照（metadata 权威） | 5.2/2.2 |
| 6 | 审核平台 API 现行合约 | 5.4/API tab |
| 7 | 客户案例/blog 可发布范围 | blog |
| 8 | legal 去重 | 非主链 |
| **D1** | **16 库 capability 状态核定（把 ✓/◐ 与 metadata unknown 收敛为单一事实源）** | 5.2 + §6.3 矩阵口径 |

---

## 7. 当前差距速览（2026-09-08 实测）

| 类别 | 目标 | 现状 |
|---|---|---|
| 规则参考 | ~260 双语 | 59（audit54+opt5） |
| 教程/接入/使用指南 | 教程≥6 · 接入~8 · 使用~12 | 教程 0 · 接入 1（choose-access）· 使用 ~3 |
| 能力与原理 | ~8 | 1（features/index 占位） |
| config | ~10 | 1（en） |
| API | 真实合约 | 占位 1.6KB |
| CLI/error-code | ≥1 目录 | 0 |
| FAQ/troubleshooting | 45+ | ~2 单页 |
| use-case | ≥5 | 2 index |
| release notes（zh） | 按发布 | 无 |

---

*本文件为规划物，不替代内容审核或数据库执行验证；任何状态 `✅` 仅表示页面/元数据存在，不等于内容已核准发布。*
