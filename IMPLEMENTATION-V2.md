# 内容模型 v2 实施与验收

日期：2026-09-08。状态：模型、导航、迁移与生成基础设施已实现；内容采编/事实审核未完成，未生产部署。

## 已完成

- 唯一产品 pawsql；注册五个组件、六项能力以及版本/部署/入口等独立维度；历史三个产品 YAML 合并为一个，旧版本可由 Git 恢复。
- 六类内容、子类型和 index/detail 布局；导出兼容 Schema 与 canonical v2 Schema；v2 仓库校验必需字段。
- ID/语言配对、稳定文档引用、各语言独立审核状态、翻译源摘要、实体证据模型。
- 规则适用/排除条件、修复方式、正常/边界示例；数据库条件化兼容性；配置默认值及范围类型约束。
- build-references 自动生成当前元数据的双语目录；manifest 保护生成物，报告过期文件；重复构建确定性验证。
- frontmatter/元数据幂等迁移，不覆盖原正文，不批量移动已有 URL。
- 中英文各五个标签、文档六组导航；补充中英文使用方式说明、中文帮助与排障页；数据库范围统一链接条件化矩阵。
- OR 重写样例补足 NULL、重复行和重叠分支；回归测试不冒充产品验证。
- 默认 CI 检查结构/存在性、上传质量报告并检查生成物；显式 release 输出到新暂存目录。
- 更新 README、迁移文档、类型模板、内容模型规范，以及原内容库技术设计说明书 v1.3。

## 验证记录

| 检查 | 结果 |
|---|---|
| Python 测试 | 68 项通过 |
| 生成页面 | 127；stale 0；连续构建摘要一致 |
| 迁移 dry-run | 0 文件变化 |
| structure / existence | 0 / 0 |
| completeness / release | 388 / 298（全量预览报告的问题条数，不是页面数） |
| 必需文件覆盖率 | 100%；不是发布审批 |
| release 负向验证 | 按发布范围报告 completeness 240 / release 236，退出码 1，目标目录未创建 |
| Mintlify 本地预览 | CLI 4.2.876，http://localhost:3013 |
| 浏览器抽查 | 中文默认页、五标签/六组、规则目录、面包屑、英文切换成功 |

搜索提示需要 Mintlify 登录；本轮没有登录或验证搜索服务。未验证所有页面、动态链接、生产网络及部署授权。完整缺口见 [reports/content-quality.json](reports/content-quality.json)。

## 用户手册内容批次（2026-09-10 追加）

以下批次把 `99-待归类` 的手册源文档按内容模型落位，并做了产品口径下的结构收敛。正文尽量保留原文，只规范化 frontmatter、重复 H1、链接与展现形式。

**安装与接入**（`pawsql-user-guide-group-02-installation`，7 页 × 中英）
- 补齐 `type/subtype/layout/product/status/language`；保留既有 `id/translationKey/localeOf`
- 删除与 frontmatter `title` 重复的正文 H1（共 14 处）
- 路由对齐：`user-guide/developer-tools → dev-tools`；en 侧 `/en/help → /en/faq`；统一去尾斜杠
- 移除指向未迁移页面的卡片

**开始使用**（`get-started`：quickstart、choose-access × 中英）
- 用源文档替换占位页；源使用旧 IA 路由，映射到现有页面：
  `user-guide/install-and-access[/ide|/mcp|/private-deployment] → user-guide/installation[/ide-plugins|/pawsql-mcp|/pawsql-server]`、
  `use-cases/sql-quality-gate → sql-quality-gate-cicd`、`use-cases/dba-slow-sql-governance → slow-sql-optimization`
- en 页内部链接统一补 `/en` 前缀

**工作空间与上下文**（`pawsql-user-guide-group-03-workspaces`，9 页 × 中英）
- 同批规范化；中文「常见问题」共 20 条改为 `<AccordionGroup>` 折叠展示
- 组件实测结论：Markdown `- [ ]` 已原生渲染为复选框列表，保持原样；`<Check>` 在 Mintlify 中是提示框（callout）而非清单组件，未用于待办清单

**产品口径下的结构收敛**
- 删除 `user-guide/cloud/`（index / quickstart / results）：内容已由 `/getting-started/quickstart` 承载，引用全部重定向
- 删除工作空间 5 页：`database-context`、`refresh-metadata`（联机库自动更新）、`manage-workspace`、`permissions`（工作空间从属于团队）、`manage-connections`（无独立连接管理功能）
- `index` 与 `create-workspace` 合并为一页（概念 + 两种方式对比 + 基本信息建议 + 使用原则），删除 `create-workspace`；两个创建分支页只保留该方式特有内容
- 删除随页面替换而失效的 `tools/tests/test_quickstart_q2.py`

**本批验证**：`validate-frontmatter` / `validate-nav` PASS；`user-guide` 全树链接 38/38 可达；相关页面 MDX 编译通过；pytest 76 项通过。

> 注：上述结构收敛改变了工作空间分组（4 页 → 3 页）与「安装与接入」组内容，`MIGRATION-PLAN.md` 批次表中部分目标路径（如 `docs/products/*`）已不适用，以本节记录为准。

## 使用场景重写与开发工具集成批次（2026-09-15 追加）

**使用场景五页重写**（`use-cases/*` × 中英，共 10 页，含新增 database-migration en 镜像）
- 统一为六槽骨架：用户 / 问题 / 目标 / 流程 / 依赖能力 / 成功标准，用 frontmatter `sections` 映射语义槽位到实际标题
- 把重复示例（`DATE(create_time)`、相关子查询、深分页、迁移漏斗数字）下推到能力页，正文改为「叙述 + 链接」，避免跨页重复同一事实
- 企业统一治理页去重：三层治理模型改为映射表引用三个子场景，保留元层次内容（一套规则覆盖多团队、策略即代码、治理度量、分阶段实施、SQL Engineering 定位）
- 中文不再引用已有中文名的英文术语；成功标准改为「指标｜目标」定性表，移除无证据支撑的具体数字

**开发工具集成与 MCP**
- 用源文档填充 `dev-tools/mcp.mdx`（中英），适配仓库 frontmatter 约定与真实路由
- 导航分组「开发工具插件」→「开发工具集成」（MCP 非插件，属集成层）；同步更新 index 标题与 8 处跨页引用
- 删除 `installation/pawsql-mcp.mdx`（与 `dev-tools/mcp.mdx` 重复），引用统一指向新位置
- 新增 DBeaver 集成页；清理英文导航残留幽灵条目 `use-workspace`、`audit-and-optimize`

**性能巡检平台**（`performance/*` × 中英）
- 用真实内容替换占位页，补齐接入实例、采集慢 SQL、巡检任务、批量优化、治理进度等流程，并新增操作截图
- 巡检与慢查询治理重组：导航拆「慢查询治理」（慢查询采集 → SQL 聚合与去重 → 批量分析与优化 → 创建优化任务工单 → 跟踪治理进度）与「数据库对象巡检」（对象巡检任务 → 巡检任务报告 → 创建巡检问题工单）两个子分组
- 页面更名：采集慢 SQL → 慢查询采集、创建性能巡检任务 → 对象巡检任务、查看巡检报告 → 巡检任务报告
- 新增两页：创建优化任务工单（自批量分析与优化拆分）、创建巡检问题工单（自巡检报告发起）；「跟踪治理进度」归入慢查询治理分组

**本批验证**：`validate-frontmatter` / `validate-nav` PASS。

## 下一批内容工作

1. 产品负责人核定规则 ID/分类/版本/实现映射/数据库范围，提供可追溯证据。
2. 按模板补足规则适用与排除条件、真实数据库执行结果和边界样例。
3. 核定数据库兼容性与配置生效行为；补充缺失的中文数据库、配置正文及翻译。
4. 逐篇完成手写文档的章节映射、事实复核和审核责任记录；避免空标题通过形式检查。
5. 替换占位 OpenAPI；为生产 Mintlify 连接接入受保护的 release 流水线。

以上需真实产品信息及编辑复核，不能由生成脚本代替。当前实现不是“全部内容已完成”的声明。

## 参考资料分组重组（规划 · 2026-09-17 待执行）

参考资料（Reference）组内容框架与组织方式的实施规划。本轮范围：`rule` + `database` 落地；`configuration` 暂缓；`api` 完全由 openapi tab 承担；`glossary` / `cli` / `error-code` 暂缓。

### 已裁定决策

1. **database 归入 `reference/database/`**——URL 从顶层 `databases/` 迁移到 `reference/database/`，使 7 个 subtype 路径统一在 `reference/` 下。
2. **api 完全由 openapi tab 承担**——参考资料组内不建 api 页，`openapi/pawsql-integration.yaml` 与 `pawsql-optimization.yaml` 继续挂「API」tab。
3. **glossary 本轮暂缓**——术语沉淀后再建，与 `contributing/terminology`（贡献者写作规范）分离，不做迁移。

### 目标导航结构（中文「参考资料」group，英文镜像）

```
参考资料 (group)
├── 审核规则        → reference/audit-rules/index      目录页按 category 分组聚合
├── 优化规则        → reference/optimizer-rules/index  同上
└── 数据库兼容性    → reference/database/index         16 库 landing + 各库详情
```

configuration 暂缓，不挂导航。

### 组织方式

**rule 子组**
- `rule_index.py` 当前只生成扁平表格（`| 规则 | ID |`），需增强为按 `metadata/rules/*/*.yaml` 的 `category` 字段分组聚合，分类树取自 `metadata/taxonomies`。
- 补齐 PLACEMENT §D 剩余约 202 条规则（D.2 已裁定 audit 221 / optimizer 40）到 `metadata/rules/`，再 `build-references` 重建。

**database 子组**
- `structured.py::database_pages` 输出路径从 `databases/{db}/index.md` 改为 `reference/database/{db}/index.md`（zh/en 双语）。
- 新增 `reference/database/index.md` landing 页聚合 16 库（名 / 版本 / 能力状态），替代旧 `generate_compatibility_index` 的 `reference/compatibility/` 输出。
- 能力矩阵继续由 `sync_database_matrix` splice 进 `getting-started/supported-databases`（能力总览），与 landing 页分工：landing 是查阅入口，supported-databases 是「开始使用」里的能力总览。
- metadata 16 个 yaml 全 SAMPLE draft，正文需产品核稿后 release 门禁才放行；SAMPLE 里的 legacy claims 一律标 `unknown`，不自动升格为支持承诺。

**清理项（随本轮）**
1. 从参考资料组移除 `contributing/terminology`（贡献者规范，非用户参考项；当前英文组无对应镜像，本身不一致）。
2. 废弃旧 `database_generator.py` / `config_generator.py`（只输出英文 `docs/en/`，与 v2 双语模型冲突），统一走 `structured.py`。
3. 中英文导航页面列表对齐（当前中文 3 页 vs 英文 5 页，路径混杂）。

### 实施步骤

1. 改 `structured.py` database 输出路径 → `reference/database/`，新增 landing 页；移除旧生成器调用。
2. 增强 `rule_index.py` 按 category 分组聚合。
3. 逐批补齐 `metadata/rules/` 至 261 条，`build-references` 重建。
4. 更新 `docs.json` 两语言「参考资料」组：移除 terminology、挂 database 组、对齐页面。
5. 跑 `validate-nav` / `validate-frontmatter` / `gate` 全绿。

## 工作区保护

`docs/getting-started/overview.mdx` 原有用户正文改动保留在工作区。本次提交仅纳入该页针对 HEAD 的分类迁移，不代为提交已有正文编辑。原内容库 `.agents/` 未纳入提交。
