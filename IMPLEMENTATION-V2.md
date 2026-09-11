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

**工作空间与数据库上下文**（`pawsql-user-guide-group-03-workspaces`，9 页 × 中英）
- 同批规范化；中文「常见问题」共 20 条改为 `<AccordionGroup>` 折叠展示
- 组件实测结论：Markdown `- [ ]` 已原生渲染为复选框列表，保持原样；`<Check>` 在 Mintlify 中是提示框（callout）而非清单组件，未用于待办清单

**产品口径下的结构收敛**
- 删除 `user-guide/cloud/`（index / quickstart / results）：内容已由 `/getting-started/quickstart` 承载，引用全部重定向
- 删除工作空间 5 页：`database-context`、`refresh-metadata`（联机库自动更新）、`manage-workspace`、`permissions`（工作空间从属于团队）、`manage-connections`（无独立连接管理功能）
- `index` 与 `create-workspace` 合并为一页（概念 + 两种方式对比 + 基本信息建议 + 使用原则），删除 `create-workspace`；两个创建分支页只保留该方式特有内容
- 删除随页面替换而失效的 `tools/tests/test_quickstart_q2.py`

**本批验证**：`validate-frontmatter` / `validate-nav` PASS；`user-guide` 全树链接 38/38 可达；相关页面 MDX 编译通过；pytest 76 项通过。

> 注：上述结构收敛改变了工作空间分组（4 页 → 3 页）与「安装与接入」组内容，`MIGRATION-PLAN.md` 批次表中部分目标路径（如 `docs/products/*`）已不适用，以本节记录为准。

## 下一批内容工作

1. 产品负责人核定规则 ID/分类/版本/实现映射/数据库范围，提供可追溯证据。
2. 按模板补足规则适用与排除条件、真实数据库执行结果和边界样例。
3. 核定数据库兼容性与配置生效行为；补充缺失的中文数据库、配置正文及翻译。
4. 逐篇完成手写文档的章节映射、事实复核和审核责任记录；避免空标题通过形式检查。
5. 替换占位 OpenAPI；为生产 Mintlify 连接接入受保护的 release 流水线。

以上需真实产品信息及编辑复核，不能由生成脚本代替。当前实现不是“全部内容已完成”的声明。

## 工作区保护

`docs/getting-started/overview.mdx` 原有用户正文改动保留在工作区。本次提交仅纳入该页针对 HEAD 的分类迁移，不代为提交已有正文编辑。原内容库 `.agents/` 未纳入提交。
