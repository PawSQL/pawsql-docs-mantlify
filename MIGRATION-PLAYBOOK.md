# PawSQL 内容迁移方法论 / 转换手册

> 本手册依据《PawSQL Documentation Platform 技术设计说明书（Mintlify 版）v1.1》，把 Obsidian 内容库
> （`pawsql-docs-new` vault）的原始技术内容**确定性、可复用地**转换为本仓库（`pawsql-docs-v2`，Mintlify）
> 的目标结构，供后续分批批量执行。转换是**内容搬运 + 结构重建**，不是照抄：每个目标文件都需满足 v2 的
> Front Matter / Metadata / 生成器约束，并符合站点语言策略。
>
> 规则正文等“结构化 Reference”一律 **metadata 驱动生成**（不要手改 `docs/reference/**`）；人工页（user-guide /
> product / blog）按本手册规则人工整理。

---

## 1. 目标与边界

| 判定 | 内容 | 去处 |
|---|---|---|
| 可迁移 | 产品/用户手册类、规则/配置/数据库类结构化 Reference、API/安装手册、教程、FAQ、合规的 Blog / Release Notes / Newsletter | 本仓库对应目录（见 §2） |
| 保留为 Evidence（不迁出） | 源中文正文（如 `规则文档/` 原文） | 留在 vault，作为 metadata 双语内容的对照源；metadata 文件头注释记录来源 |
| 不迁移 | `80-design/`（内部设计/roadmap/xmind）、`90-reference/`（含华为 DSC 反编译源码，授权风险；SOAR 第三方衍生）、`99-待归类/.workbuddy/` 与工具态、个人/临时文件（`~$*`、`*.base`）、`Excalidraw/`、`templates/`、`textgenerator/`、`Clippings/` | 留在 vault |
| 法律类（`30-cloud/legal/`） | 去重定稿后再决定：建议独立 site legal 页面（Terms/Privacy/License），不进文档导航 | 待产品/法务定稿 |

## 2. 源 → 目标目录总映射

| 源（vault 相对路径） | 内容类型 | 目标（v2） |
|---|---|---|
| `10-product/about/`（关于/FAQ/用户场景） | Product/About + FAQ | 默认树 `docs/products/<product>/` 英文版；中文版 `docs/zh/products/`；FAQ→`docs/faq/` 或 `docs/zh/faq/`。视频脚本、Github 主页草稿不迁 |
| `10-product/getting-started/` | Getting Started | `docs/getting-started/` 或 `docs/zh/getting-started/`（与 Mapper 文件教程重复，见 §9） |
| `20-engine/api/`（V1/V2/V3、pawsql-api、审核平台 API） | API Reference | `openapi/pawsql-openapi.yaml`（若有 OpenAPI 源）或 `docs/reference/api/`。多版本先定稿（见 §9） |
| `20-engine/install/`（Engine、Linux、docker） | 安装手册 | 默认树 `docs/user-guide/installation/`；中文版 `docs/zh/user-guide/installation/` |
| `20-engine/rules/`（`Rules.md`、`audit-ddl`、`audit-dml`、`rewrite`、**`规则文档/` 261 篇**） | 规则 Reference | `metadata/rules/{audit,optimizer}/*.yaml`（双语）→ 生成 `docs/reference/{audit,optimizer}-rules/` + `docs/zh/reference/{audit,optimizer}-rules/`。**规范源 = `规则文档/`**；其余套用于 ID/字段核对 |
| `20-engine/indexrec/`、`internals/`、`internals/case-studies/` | 技术 Blog / 案例分析 / 支持矩阵 | Blog（engineering）`blog/engineering/`；支持情况矩阵可入 `docs/databases/`。内部笔记（`20240118.md`）不迁 |
| `30-cloud/guides|install/` | Cloud 使用手册 / 企业安装 | 英文版 `docs/products/cloud` + `docs/user-guide/`；中文版 `docs/zh/user-guide/cloud/`（本试点已落） |
| `40-audit/manuals/`（Advisor/审核平台/巡检） | 产品手册 | `docs/products/advisor|audit|patroller` + 中文镜像；与 50-integration 的 Advisor(IntelliJ) 语义对齐后命名 |
| `40-audit/standards/`（审核规则体系、质量标准、开发规范） | 方法论/参考 | `docs/reference/audit-rules/` 概念页或 `docs/contributing/` 规范（产品确认后） |
| `40-audit/design/`、`reviews/` | 内部设计 / 评测 | 不迁（内部）；`reviews/` 精选可作 Blog |
| `50-integration/{plugins,mcp,api,devops}` | 插件/MCP/API/CI 集成 | `docs/products/vscode|jetbrains|mcp` + `docs/reference/api` + `docs/user-guide/` 集成教程；截图随图管线（§5） |
| `60-migration/oracle/` | 迁移工具/兼容性 | 若 Ora2PgSQL 仍支持→`docs/reference/cli`；否则仅语法映射入 `docs/reference/compatibility/`（产品确认） |
| `70-content/vendor-guides/`（各库采集/慢日志） | 数据库接入教程 | `docs/databases/<db>/` + `docs/user-guide/optimization/`（workload/DDL 录入） |
| `70-content/newsletters/` | 更新日志/月报 | 更新日志→`docs/release-notes/`；社区精选/发布公告→`blog/` |
| `70-content/blog|comparisons/` | Blog | `blog/{engineering,database,product}/`；`-polish`/`_en`/zh 变体归并见 §7/§9 |
| `99-待归类/` | 待分类 | 逐文件判定（BLOG-* → blog；金融案例 → blog case study；评测数据 xlsx → blog 数据源；TDSQL 系列 → blog/faq）；`.workbuddy` 删 |

## 3. Front Matter / 文档类型 / 状态

字段与校验见 `docs/contributing/frontmatter.md` 与 `schemas/frontmatter.schema.json`；风格见 `style-guide.md`，术语见 `terminology.md`。

- 每页必填 `id`（稳定、URL 安全）、`title`、`type`。
- `type` 取值：`product` · `user-guide` · `tutorial` · `reference` · `faq` · `troubleshooting` · `release-note` · `blog`。
- `status`：`draft → review → approved → scheduled → published → archived`。**凡未经产品核对的内容一律 `draft`**，正文顶部加注状态说明。
- 人工页写 `description`（一句话、含检索关键词）以提升 AI 检索质量；`tags` 数组；引用产品用 `product`（值为 `metadata/products/*.yaml` 的 `id`）。
- 中英镜像约定：中文页 `id` 以 `zh-` 开头；英中文页面互为翻译对，导航分列默认树与"中文（镜像）"组。
- 生成页：由生成器写 front matter（`{kind}-rule-<slug>` / `zh-{kind}-rule-<slug>`），**不要手改**。

## 4. 格式转换规则清单（确定性）

对每篇搬入目标树的 md(x)：

1. **去版权/页脚样板**：删除首部 `Copyright © …(注意 pawslq.com 拼写错)`、Typora `[TOC]`/`[toc]`、尾部"关于PawSQL / About PawSQL / 联系我们 / Contact us"整块（站点有统一 header/footer）。
2. **唯一 H1**：正文只保留一个 `#` 标题（即页面 title 下内容），其余标题降为 `##` 起；禁止 H1 后直接跳到 `####`（先 `## 背景` 再逐级）。
3. **代码块补语言**：为裸代码块补 `sql` / `bash` / `json` / `yaml` 等标签。
4. **行内 HTML 替换**：`<b>…</b>` → `**…**`；`__提示__` → `**提示**`；`&gt;` 恢复为 `>`（blockquote/比较符语义按上下文还原）。
5. **标题编号规整**：去掉或统一“数字.”编号风格，避免同层重复编号。
6. **断链与内部链接**：正文引用改为 Mintlify 页面路径（如 `docs/zh/user-guide/cloud/quickstart`）；无效的 `.md` 引用、`app.pawsql.com/docs/rule/RuleXxx` 类链接保留为原样或转对应 reference 页（产品核对）。
7. **文件名 sanitize**：去除尾随空格、emoji、`（严重）`、`-polish`、`_en`、`_en.md`、版本后缀等 → 转成目标 slug 文件名；同内容多份只保留一份（§9）。
8. **术语/大小写**：按 `docs/contributing/terminology.md`（PawSQL、产品名、数据库名）；同一概念全文统一。
9. **不确定事实不打磨**：性能/收益百分比、benchmark、支持范围等无源数字 → 不写或加 `unknown` 标记并 `draft`。
10. **移动/复制策略**：从 vault **复制**（不移动），原文件保留为 Evidence；目标文件落位后按 §10 校验。

## 5. 图片管线与断图处置

- vault 图片集中在 `00-assets/images/` 与 `50-integration/*/images|screenshots`、`70-content/newsletters/assets` 等处；大量 md 里是 **Typora 绝对路径**（`C:\Users\…`、`D:\pawsql docs\…`）或指向不存在目录的相对路径（`./assets/`、`.\assets\`），**多数原始图片并未归档到文档旁**。
- 规则：
  1. 迁移图片 → 目标 `static/`（如 `static/zh/cloud/*.png`）；md 内用 Mintlify 路径引用。
  2. 先在 vault 内按 alt/上下文检索真实图片（`00-assets/images/`、git 历史、相邻 PDF）；能找到就随文搬，找不到**不发明路径**。
  3. 缺失图片：在原文位置写 `> TODO(截图待补)：<图注>`，页面 `status: draft`，不伪造链接。
- 备注：`00-assets/**` 还有大量 PDF，与 md 内容同源（规则集、安装手册、API 文档），可作为 md 缺失时的校对源，不作为站点内容。

## 6. 内容优化规则

- 质量层级对应设计 §30：Build → Structure（FM/Metadata/Links 合法）→ Consistency（术语/版本/API/DB 一致）→ Evidence（AI 生成须可回溯）→ Coverage（Gate 100%）。
- Guardrails（§32）：不虚构 API/参数/版本/性能/benchmark/客户案例；不改产品语义；无证据标记 `unknown`；改已有文档先读全文、最小 Patch。
- 写作：读者=DB 工程师/DBA，直接具体；一个页面一个意图；先结论后细节；正文顶部 draft/生成说明标记；AI 检索视角写好 `description`、标题与导航措辞。
- 每条规则正文的“证据”来自：`规则文档/` 原稿、`Rules.md`、产品代码/注册表；metadata 文件头注释来源与待核对项。

## 7. 语言落地策略

- **默认树 `docs/**` 用英文**（面向全球站点默认语言）；**中文内容进 `docs/zh/` 镜像**。
- **Reference（规则页）采用“双语元数据 + 双输出”**：`metadata/rules/**/*.yaml` 根字段为英文，`zh:` 块为中文正文；`build-references` 同时生成英文页与 `docs/zh/reference/…` 中文页。规则不配英文时只出英文页亦可（无 `zh` 块）。
- **人工页**：中文版进 `docs/zh/`；英文版在默认树补齐。源语言为英文的文档直接进默认树。
- **变体归并**（避免重复）：同一主题保留“最新一份 + 英文版/中文版”两态；`-polish` 为公众号润色稿 → 不并入站点或作为 Blog 备稿；`_en`/原中文成对 → 拆为镜像对；不迁移邮件模板 `${username}` 等占位内容（属 release 草稿，见 §9）。

## 8. 规则文档 → Rule Metadata 映射

规范源 = vault `20-engine/rules/规则文档/`（261 篇）。每条内部 H4 模板 → yaml 字段：

| 源字段 | 目标（RuleMetadata） | 说明 |
|---|---|---|
| 标题（H1，中文） | `zh.name`；英文 `name` | 英文名取“英文名”字段 |
| `英文名` | `name` | 英文正文用；无则按标题意译并 `draft` |
| `类别`（层级，如 `数据操作>性能>排序分组`） | `category`（短词） | 一级映射：对象设计→`ddl`、数据操作→`dml`、索引失效→`index`…无法短化的记 `unknown` 待产品确认 |
| `审查对象`（SELECT/UPDATE/…） | 入 `description`/`tags` | 表明适用语句类型 |
| `默认预警级别` | `severity` | 提示(Notice)→`info`、警告(Warning)→`warning`、错误/严重→`error` |
| `数据库类型` | `database` | `ALL` → **留空 `[]`**（生成页显示"所有支持数据库/All supported databases"）；具体列表照抄小写 slug |
| `默认阈值`/`可配置` | 正文（description/howToFix）+ yaml 注释 | 如 CHAR 阈值 64、命名正则 `^pk_{table}_{columns}$` |
| `触发条件` | `whyItMatters`/`howToFix`（归纳） | 逐条如实转述，不扩写 |
| `SQL样例`（❌ 不推荐 / ✅ 推荐） | `badExample` / `goodExample`（英文）与 `zh.badExample/goodExample`（中文，注释原样） | 注释随语言翻译；SQL 本体保持 |
| Rule ID | `id` | **优先复用产品注册表已有规则码**（如 `RuleNPERewrite`，来自 `Rules.md`/`DML Rules.md`/`app.pawsql.com/docs/rule/RuleXxx`）；无则铸 slug（audit `aud-…`、optimizer `opt-…`），文件头注释 `TODO(产品核对)` |
| 引入/弃用版本、实现类 | `introducedVersion`/`deprecatedVersion`/`implementationClass` | 源没有就不填，避免虚构版本 |

**audit vs optimizer 归属**：审核/检查类（对象设计、DDL/DML 检查、索引失效预警）→ `metadata/rules/audit/`；重写/优化类（NPE、UNION ALL、EXISTS→JOIN、COUNT→EXISTS、谓词下推等）→ `metadata/rules/optimizer/`。归属/分类不明确时该条 `draft` 并在注释说明。

## 9. 去重矩阵（先裁决后迁移）

| 位置 | 重复 | 裁决 |
|---|---|---|
| Cloud 手册 | `30-cloud/guides/PawSQL Cloud使用手册.md` == `Cloud实践指南.md` == `40-audit/manuals/巡检平台实践指南.md`（字节相同/误标） | 保 1 份（使用手册），其余删/归档 |
| Quick Start | `10-product/getting-started/…/Quick Start with PawSQL Cloud.md` == `70-content/vendor-guides/Workload-Documentation-For-Mapper-File-Type.md` | 归入 workload/DDL 录入教程 |
| 规则体系 | `Rules.md` + `DDL Rules.md` + `DML Rules.md`+`DML audit Rules.md` + audit-dml/rewrite 逐条 + `规则文档/`（同一规则 3+ 表达） | 规范=`规则文档/`；其余仅作 ID/字段对照 |
| 审核平台 API | `20-engine/api/*` 与 `50-integration/api/*` 共 6 份版本/视角不同 | 产品定稿 1 份 → OpenAPI/API reference |
| 设计文档 | `40-audit/SQL 审核优化系统高阶设计文档.md`（根，19.9KB）vs `design/…`（14.6KB） | 内部不迁 |
| Blog 重复 | NULL 陷阱 ×3、大模型局限 ×3（其一为 LLM 写作提示词，非成文）、`-polish` 成对、docx+md 孪生 | 每主题保 1 份成文 + 中英镜像 |
| Newsletter | 邮件模板含 `${username}`、日期版本 | 去模板占位 → release-notes/blog |
| legal | ToS ×6 / Privacy ×4 / License en/zh | 法务去重定稿 → site legal |
| API 版本栈 | Engine 接口 V1/V2/V3（V3 传统字“文檔”）、pawsql-api、审核平台接口 | 按现行版本定稿后并入 API reference |

## 10. 质量闸门（每批必须全绿）

在仓库根执行（`tools/` 下）：

```bash
cd tools
uv run python -m pawsql_doc --root .. validate-metadata      # metadata/** 一致性
uv run python -m pawsql_doc --root .. validate-frontmatter   # docs|blog 全部 FM 合法
uv run python -m pawsql_doc --root .. build-references       # 重建 Reference（双输出）
git diff --exit-code -- docs/reference docs/zh/reference docs/databases   # 生成页已提交、无漂移
uv run python -m pawsql_doc --root .. drift && uv run python -m pawsql_doc --root .. gate  # 覆盖率=100%
uv run python -m pytest                                       # 单元测试
```

Windows 下如 `uv run` 不便，可用 `tools/.venv/Scripts/python.exe -m pawsql_doc --root .. <cmd>`。

> 规则：**metadata 变更必须连同 `build-references` 生成结果一起提交**；人工页 front matter 必须过校验；本地 `npx mintlify dev` 人工过一遍导航与页面。

## 11. 分批批量计划

每批走同一 checklist：选定切片 → 复制/转换（§4-§8）→ 去重裁决（§9）→ 写 metadata/内容 → `build-references` → 全量闸门（§10）→ 提交（元数据+生成页同 commit）。

- **P0（结构化 Reference 全量）**：`规则文档/` 261 篇 → 双语 Rule Metadata + 生成页；`metadata/databases`（各库版本/能力）→ 兼容矩阵；`metadata/configs` → 配置 Reference。**优先级最高，纯 metadata 驱动。**
- **P1（手册/产品页）**：Engine 安装、Cloud 手册英文版、40-audit/manuals（Advisor/审核平台/巡检）、50-integration（VSCode/JetBrains/MCP/GitLab/GitHub）→ 产品页 + user-guide + 教程。
- **P2（Blog / Release Notes）**：70-content 精选成文（去重后）、newsletters→release-notes、FAQ。
- **P3（知识层）**：RAG/MCP 接入（用已发布 docs）；此处不做。

每批完成后更新本手册的进度记录（附录 B）。

## 12. 待产品确认清单（沉淀给产品负责人）

1. 规则分类规范：audit vs optimizer 归属、`category` 短词归一（含 261 条全覆盖表）。
2. 规则 ID 注册表：与 `Rules.md`/线上 `docs/rule/RuleXxx` 对齐（试点用 slug + 注释占位）。
3. “PawSQL Advisor”语义：IntelliJ 时代插件 vs Cloud 审核能力 → 决定 `products/{advisor,jetbrains}` 归属。
4. Ora2PgSQL 是否仍为支持产品（决定 `60-migration` 是否进 `reference/cli`）。
5. 支持数据库/版本快照（Cloud 手册 DB 列表为 2023 快照）→ 以 `metadata/databases` 矩阵为准。
6. legal（30-cloud/legal 去重定稿 → site legal）。
7. 审核平台 API 现行版本定稿（20-engine/api vs 50-integration/api）。
8. `80-design/rules/*.xmind` → 规则注册表更新来源（对象/DDL/DML/重写各集合）。

---

## 附录 A：试点（2026-09）产物

- **tools 双语生成**：`RuleMetadata.zh`（`models/core.py`）、`rule_generator.py` 双输出、schema 导出、pytest 双语用例、CI diff 加入 `docs/zh/reference`。
- **规则切片 ×10**（audit 6 + optimizer 4）：`metadata/rules/{audit,optimizer}/*.yaml`（双语）→ `docs/reference/{audit,optimizer}-rules/` 英文页 + `docs/zh/reference/{audit,optimizer}-rules/` 中文页；`metadata/features|mappings` 2 组演示数据。
- **产品手册切片**：`30-cloud/guides/PawSQL Cloud使用手册.md` → `docs/zh/user-guide/cloud/{index,quickstart,results}.md`（去样板、断图 TODO、`draft`）；docs.json “中文（镜像）”“规则参考（中文）”两组。
- 全部过 §10 闸门（metadata/frontmatter/build/drift/gate/pytest 绿）。

## 附录 B：批处理进度记录

| 批次 | 范围 | 状态 | 日期 | 备注 |
|---|---|---|---|---|
| 试点 | 规则 ×10 + Cloud 手册 | 完成 | 2026-09 | 双语双输出模式验证 |
