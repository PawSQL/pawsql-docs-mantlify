# AGENTS.md

PawSQL 文档站点的 Mintlify 内容仓库。本文件是给 Codex / 贡献者的**操作约定**；规范细节以仓库内文档为准，不要在本文件重复。

## 权威文档（冲突时以此顺序为准）

- **[CONTENT-MODEL-V2.md](CONTENT-MODEL-V2.md)** — 当前内容模型规范（唯一产品 `pawsql`、六类内容、子类型、维度）。**取代**旧规划中冲突的产品分类/内容类型/导航规定。
- **[CONTENT-MODEL-CHANGES.md](CONTENT-MODEL-CHANGES.md)** — 内容模型/SEO-LLM 改动清单（A1/A2/A3、B1/B2/B3、C1 已做；P1 项见文件）。
- **[IMPLEMENTATION-V2.md](IMPLEMENTATION-V2.md)** — 实施与验收状态、待办。
- **[CONTENT-BLUEPRINT.md](CONTENT-BLUEPRINT.md)** / **[MIGRATION-PLAN.md](MIGRATION-PLAN.md)** / **[MIGRATION-PLAYBOOK.md](MIGRATION-PLAYBOOK.md)** / **[PLACEMENT.md](PLACEMENT.md)** — 目标完整性蓝图、迁移计划、方法论、落位表。
- 写作与字段：`docs/contributing/{frontmatter,style-guide,terminology}.md`。

## 仓库布局

```text
docs/         Mintlify 内容根（docs.json 在此）
  docs.json   多语言导航 / OpenAPI / 主题
  index.mdx   中文首页（/）
  <页面>      中文默认内容（路由 /…）
  en/         英文副语言树（路由 /en/…）
metadata/     产品知识层：products / features / rules / databases / configs / mappings / policies
schemas/      JSON Schema（由 tools 的 pydantic 模型导出）
tools/        Python 实现：pawsql_doc（生成器 / 校验 / 门禁 / 迁移）
templates/    内容类型模板；reports/ 质量与清单报告；static/ 静态资源
```

## 语言模型

- **中文为默认语言**（内容根 `/`）；**英文为副语言**（`docs/en/`，路由 `/en/…`）。
- 页面 `id`：中文页中性；英文镜像页 `en-` 前缀；中英镜像互写 `localeOf`（指向对方 `id`，禁止自指，校验强制成对存在）。
- `docs.json` 用 `navigation.languages`（zh 在前），每个语言下可有自己的 `tabs` 与（嵌套）`groups`。

## 常用命令

预览（**先停掉上一次的 dev 服务**，见下）：

```bash
cd docs && npx mintlify dev        # http://localhost:3000
```

校验与门禁（在 `tools/` 下用 `uv run`）：

```bash
cd tools
uv run python -m pawsql_doc validate-metadata     # metadata/** 与 docs 引用一致性
uv run python -m pawsql_doc validate-frontmatter  # front matter（description 治理 + localeOf 配对 + type/subtype）
uv run python -m pawsql_doc validate-nav          # 导航校验：默认 preview（存在性 + group/type）；--release 校验 published/approved
uv run python -m pawsql_doc drift                 # 必需文档缺失即 exit 1
uv run python -m pawsql_doc coverage              # 分项覆盖率
uv run python -m pawsql_doc gate                  # 存在性门禁（≠ 发布批准）
uv run python -m pawsql_doc quality               # 结构/存在性/完整性/发布就绪
uv run python -m pawsql_doc inventory             # 只读内容清单
uv run pytest -q
```

生成（改 `metadata/**` 后重建，**勿手改生成页**）：

```bash
uv run python -m pawsql_doc build-references              # 全量重建 Reference（规则/数据库/配置 + 规则目录 landing）
uv run python -m pawsql_doc generate-rule --rule <id>
uv run python -m pawsql_doc generate-db   --database <name>
uv run python -m pawsql_doc generate-config --config <name>
uv run python -m pawsql_doc ingest-rules --vault <规则文档目录> --id <rid>   # 默认 dry-run
uv run python -m pawsql_doc migrate-content-model                            # v2 迁移，默认 dry-run
```

## 规则与约定

- **生成页勿手改**：`docs/reference/**` 与 `docs/en/reference/**`（含规则目录 `index.md`）由 `build-references` 生成；改 `metadata/**` 后重建并连同生成物一起提交。
- **导航 = 发布**：`docs.json` 只应收录 `status: published/approved` 页（`validate-nav --release`）；`draft/review` 仅本地/分支。本仓库当前用于**预览**，通过门禁 ≠ 允许生产发布。
- **Front matter 必填**：`id/title/type/status`；`type` 需带合法 `subtype`；`published` 页 `description` 必填且人工书写（禁占位/机器截断）。
- **单一事实源**：规则/配置/数据库正文只在 `metadata/**`；页面间不重复同一事实。
- **事实纪律**：不得虚构 API/参数/版本支持/性能数据/客户案例；无证据标 `unknown`。
- 提交信息用 `type(scope): 中文描述` 风格，聚焦"为什么"。

## 环境与操作（Windows / Git Bash）

- **不要用系统 `python`**（是 Microsoft Store 占位）；一律 `cd tools && uv run ...`。
- 一次性脚本里写路径用 `E:/Workspace/pawsql-docs-v2/...`。MSYS 只转换 **argv** 中的 `/e/...`，脚本内字符串不会转换，用 `/e/...` 会找不到文件。
- **启动验证前先停掉旧的 mintlify dev**：`TaskStop`/`Ctrl+C` 不杀 node 子进程，会残留占端口（表现为 `port 3000 is already in use...` 且 `curl` 一直 000）。清理：

  ```bash
  powershell.exe -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='node.exe'\" | Where-Object { \$_.CommandLine -match 'mintlify' } | ForEach-Object { Stop-Process -Id \$_.ProcessId -Force }"
  ```

  精确匹配 `mintlify`，**勿误杀其它 node 应用，绝不动 3306 (MySQL)**。验证结束后同样停掉。
- 文件行尾经 `.gitattributes` 归一化（git 提示 CRLF→LF 属正常）。

## 注意

- 这是一个多会话并行编辑的仓库：动 `git add -A` 前先 `git status` 核对，避免把他人未完成改动一并提交。
