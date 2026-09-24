# CLAUDE.md

PawSQL 文档站点的 Mintlify 内容仓库。本文件是给 Claude Code / 贡献者的**操作约定**；规范细节以仓库内文档为准，不要在本文件重复。

## 权威文档（冲突时以此顺序为准）

- **[CONTENT-MODEL-V2.md](CONTENT-MODEL-V2.md)** — 当前内容模型规范（唯一产品 `pawsql`、六类内容、子类型、维度）。**取代**旧规划中冲突的产品分类/内容类型/导航规定。
- **[CONTENT-MODEL-CHANGES.md](CONTENT-MODEL-CHANGES.md)** — 内容模型/SEO-LLM 改动清单（A1/A2/A3、B1/B2/B3、C1 已做；P1 项见文件）。
- **[GEO-PLAN.md](GEO-PLAN.md)** — GEO（生成式引擎优化）规划：站点对 AI 引擎的可抓取/可引用改造清单、已裁定决策（默认语言 zh、域名 `docs.pawsql.com`）与待决策项。
- **[IMPLEMENTATION-V2.md](IMPLEMENTATION-V2.md)** — 实施与验收状态、待办。
- **[CONTENT-BLUEPRINT.md](CONTENT-BLUEPRINT.md)** / **[MIGRATION-PLAN.md](MIGRATION-PLAN.md)** / **[MIGRATION-PLAYBOOK.md](MIGRATION-PLAYBOOK.md)** / **[PLACEMENT.md](PLACEMENT.md)** — 目标完整性蓝图、迁移计划、方法论、落位表。
- **[BLOG-MIGRATION-PLAN.md](BLOG-MIGRATION-PLAN.md)** — 博客迁移计划（范围：`70-content/blog` + `99-待归类` blog 类）：去重取舍表、批次、图片处理、门禁与产品/法务锁。
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
uv run python -m pawsql_doc build-changelog                                  # 变更日志，默认 dry-run
uv run python -m pawsql_doc build-changelog --version <v> --refresh-llm --write   # LLM 归类并写入（需 pawsql-doc[llm]）
uv run python -m pawsql_doc tag-releases --component <name>                   # 按边界表回填源码仓 tag，默认 dry-run
uv run python -m pawsql_doc tag-releases --component <name> --apply          # 本地打 tag（--push 才推 origin）
```

变更日志（`build-changelog`）按**组件**分别维护，从各源码仓的 git tag 区间生成：

- **一源一页，无 landing**：来源配置在 `metadata/documentation/changelog-sources.yaml`，每个源用 `pages: {语言: 页面路径}` 指定自己写哪一页。页面是 `docs/changelog/{engine,server}/index.mdx`，两页都带 `rss: true`，导航在 `docs.json` 的「变更日志」tab 下直接列出这两页（不设聚合入口页）。新增组件 ＝ 加源配置 + 按模板建页 + 挂进导航。
- **页面不存在不会报错**：工具只写已存在页面的标记区，缺页面时告警并跳过（engine 页就是等它补 tag 后再建）。新增组件 ＝ 加一条源配置 + 按模板建页 + 挂进导航。
- 版本轴是 tag 区间，且**两仓的 tag 都是回填出来的**：engine 23 个（`engine-v1.2.0`…`v1.3.15`）+ server 11 个（`release-v1.2.1`…`v1.2.11`），**均在本地未推**。server 那 86 个 2022–2023 遗留 tag 被 `minVersion` 挡在区间外。
- 两段式：机械抽取写 `reports/changelog/<组件>-<版本>.commits.json`（已 gitignore）；归类写 `*.classified.json`（入库，含 `model`+`promptVersion`，任一变化即视为陈旧需 `--refresh-llm`，也含每条目的 `tags`）。渲染只读缓存，故生成不依赖网络。归类可以由工具内的 LLM 做（`--refresh-llm`），也可以由 agent 直接产出缓存 —— engine 首批 22 个版本就是 agent 归类的（`model: claude-code-agent`），纪律与 API 路径一致。
- 标记区是 `{/* CHANGELOG:START */}`…`END`，区外可自由编辑；这些页不进 `generated-manifest.json`，与「生成物被手改即报错」不冲突。
- **用 Mintlify 原生的 `<Update>` 组件渲染**（每版一块：`label`=版本、`description`=日期、`tags`=该版条目携带的标签并集），因此白得三样能力：每版可直链的锚点、右侧标签筛选、`<页面URL>/rss.xml` 订阅源（页面 front matter 里的 `rss: true` 负责显示 RSS 按钮）。入口与字段见 Mintlify 的 [Changelogs](https://www.mintlify.com/docs/create/changelogs) 与 [Update 组件](https://www.mintlify.com/docs/components/update)。
- **标签词表按组件分开**（`TAG_VOCABULARY` in `models/changelog.py`）：engine 是引擎子系统（审核引擎 / 优化算法 / 索引引擎 / SQL解析与数据库支持），server 是平台功能域（SQL 审核与优化 / 慢查询与巡检 / 工作空间与数据源 / 集成与开放接口 / 权限与安全）；两页共用 `缺陷修复` 作横切标签。**新增组件要同时加它的词表**，否则该组件的分类值会落在词表外（渲染时不会丢，会排在已知分组之后，但筛选器顺序会乱）。
- **`tags` 会顶掉右侧的版本目录**（Mintlify 里二者互斥）——本项目选了标签筛选，所以侧栏没有"跳到某版本"（每版锚点仍在，可直链）。标签由**条目级 `tags` 聚合**而来，不是手工写在页面上：手工标签活不过一次重新归类（换分类器身份会让缓存整体重算，手写的标签会静默消失）。`缺陷修复` 是横切标签——归在某个域下的缺陷修复会同时挂该域与 `缺陷修复`。
- **条目粒度：一个提交一条**——这条规则**由管道保证，不是约定**：
  - 分类器契约按组件派生（`llm.build_system_prompt(source)` 用该组件自己的词表，别再写死单一组件的分类），并在其中写明粒度规则：每个提交单独出条目；一条提交里列了多件独立的事就拆成多条（可多条引用同一个提交）；重复提交/重试/revert/cherry-pick 等同主旨的合并；一条提交列了十几项但同属一个主题的按主题归成几条。
  - **覆盖度由 `classify_commits` 兜底**：分类器没安置的提交会记进 `unclassifiedCommits`（不渲染），并在 `build-changelog` 的 NOTES 里告警，因此任何一次运行都不会少报某个版本。Agent 手工归类时同样要满足这条不变量。
- 条目文本照旧经 `escape_mdx`。
- `<Update>` 的子内容缩进 2 空格（对齐 Mintlify 自己的写法）；条目文本照旧经 `escape_mdx`，所以提交里的 `<`/`{` 不会破坏 JSX 结构。
- **英文页暂未启用**：条目文本保留提交的原始语言，所以只配了 `pages.zh`；`docs/en/changelog/` 目前不存在、`docs.json` 里也没有英文 Changelog tab。要开英文页＝建 `docs/en/changelog/<组件>/index.mdx`、两边互写 `localeOf`、配置里补 `pages.en`、再加回英文 tab，并先定下中英条目口径（LLM 同时产出中英，或英文另走翻译流程）。
- `internal` 是**只存不渲染**的桶（缓存里的审计轨迹，承接不对外可见的提交），它既不分节也不出标签，没有开关可以把它渲染出来；条目里的括号短哈希可用 `--no-commits` 关掉。
- 提交文本会进 MDX，条目一律经 `escape_mdx` 转义，勿在渲染层绕过。

回填源码仓 tag（`tag-releases`）是 `build-changelog` 的前置步骤 —— 没有 tag 就没有版本轴：

- 输入是 `metadata/documentation/changelog-release-boundaries/<组件>.yaml`（一组件一表；有多个时 `--component` 必填）：`component` 指向 changelog-sources 里的同名 source（复用其 repo/trunk，不重复写仓库路径），`start` + 每行的 `major` 标记算出全部版本号（普通交付 +1 patch，`major: true` 的行 minor +1、patch 归零）。**版本号不要在文件里写死**，否则标注重大版本时要重排后面所有行。
- 两仓的版本轴来源不同，都不是 git tag：**engine** 靠人工裁定的交付记录（`start: 1.2.0`，2024-10 起 23 版）；**server** 靠 `Dockerfile_local` 注释里的本地构建串 `1.2.x-build.YYYYMMDD`（取版本串首次出现的提交为边界、日期取串里的构建日，去掉 `-build.YYYYMMDD` 后缀 → `release-v1.2.1`…`v1.2.9`，2026-01~2026-07）。两仓都有缺口：engine 不回填 2024-10 之前，server 在 2026-07-07 后无版本信号。
- **遗留 tag 要用 `minVersion` 挡掉**：server 有 86 个 2022–2023 的 `release-v0.1.0`–`0.4.76`（多个指向同一提交）全在主干上，不设下限它们会各自渲染成一条假发布。设了 `minVersion: '1.2.1'` 后 server 当前可用区间为 0（等回到填的 tag）。
- **`verified: false` 的行会拦住整个计划**：边界表是人对真实交付的断言，不该由脚本猜。所有行核对为 `true` 才能 `--apply`。
- 任何可疑情况都**整体拒绝**（部分回填比不回填更糟，缺一个 tag 会静默改变某段区间）：提交不存在、不在主干上、边界顺序不单调、同名 tag 指向别的提交。同名 tag 指向同一提交则跳过（幂等）。
- tag 日期取表里的 `date`（真实交付日）：annotated tag 的 `creatordate` 是 tag 自己的日期，changelog 又读它，不设就会让回填的每个版本都显示成打 tag 那天。
- `--apply` 只在本地打 tag，`--push` 才推 origin 且必须与 `--apply` 同用。两个仓库都是共享仓，推送前先确认。

## 规则与约定

- **生成页勿手改**：`docs/reference/**` 与 `docs/en/reference/**`（含规则目录 `index.md`）由 `build-references` 生成；改 `metadata/**` 后重建并连同生成物一起提交。变更日志标记区内的条目同理，改来源提交后重跑生成。
- **导航 = 发布**：`docs.json` 只应收录 `status: published/approved` 页（`validate-nav --release`）；`draft/review` 仅本地/分支。本仓库当前用于**预览**，通过门禁 ≠ 允许生产发布。
- **Front matter 必填**：`id/title/type/status`；`type` 需带合法 `subtype`；`published` 页 `description` 必填且人工书写（禁占位/机器截断）。
- **单一事实源**：规则/配置/数据库正文只在 `metadata/**`；页面间不重复同一事实。
- **事实纪律**：不得虚构 API/参数/版本支持/性能数据/客户案例；无证据标 `unknown`。
- 提交信息用 `type(scope): 中文描述` 风格，聚焦"为什么"。

## 环境与操作（Windows / Git Bash）

- **不要用系统 `python`**（是 Microsoft Store 占位）。优先 `cd tools && uv run python -m pawsql_doc ...`。
- **若 `uv run` 报 `os error 4551`（应用程序控制策略已阻止此文件）**：本机策略会拦 `.venv/Scripts/python.exe` 与 `~/.local/bin/python3.*.exe`。改用 uv 自带的解释器，把 `tools/src` 与 venv 的 site-packages 一起放进 `PYTHONPATH`（两者同为 3.12，ABI 兼容）：

  ```bash
  cd tools
  PYTHONPATH="E:/Workspace/pawsql-docs-v2/tools/src;E:/Workspace/pawsql-docs-v2/tools/.venv/Lib/site-packages" \
    "/c/Users/sunke/AppData/Roaming/uv/python/cpython-3.12.13-windows-x86_64-none/python.exe" \
    -m pawsql_doc validate-frontmatter
  ```

  `pytest` 同理（把 `-m pawsql_doc validate-frontmatter` 换成 `-m pytest`）。解释器版本须与 `tools/.venv/pyvenv.cfg` 的 `version_info` 一致；uv 升级 Python 后按 `uv python list` 换路径。
- 一次性脚本里写路径用 `E:/Workspace/pawsql-docs-v2/...`。MSYS 只转换 **argv** 中的 `/e/...`，脚本内字符串不会转换，用 `/e/...` 会找不到文件。
- **启动验证前先停掉旧的 mintlify dev**：`TaskStop`/`Ctrl+C` 不杀 node 子进程，会残留占端口（表现为 `port 3000 is already in use...` 且 `curl` 一直 000）。清理：

  ```bash
  powershell.exe -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='node.exe'\" | Where-Object { \$_.CommandLine -match 'mintlify' } | ForEach-Object { Stop-Process -Id \$_.ProcessId -Force }"
  ```

  精确匹配 `mintlify`，**勿误杀其它 node 应用，绝不动 3306 (MySQL)**。验证结束后同样停掉。
- 文件行尾经 `.gitattributes` 归一化（git 提示 CRLF→LF 属正常）。

## 注意

- 这是一个多会话并行编辑的仓库：动 `git add -A` 前先 `git status` 核对，避免把他人未完成改动一并提交。
