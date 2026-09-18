# GEO 规划（GEO-PLAN）

> 本文是**规划/清单**，不含实施。内容与导航的当前规范见 [CONTENT-MODEL-V2.md](CONTENT-MODEL-V2.md)；实施与验收状态见 [IMPLEMENTATION-V2.md](IMPLEMENTATION-V2.md)；早先的 SEO/LLM 清单见 [CONTENT-MODEL-CHANGES.md](CONTENT-MODEL-CHANGES.md)（本文在其基础上，把重点从"可检索"推进到"可被引用"）。

**版本/日期：** v0.1 · 2026-09-17
**性质：** proposal——标注待实施项与需产品决策项
**关联：** `docs/contributing/{frontmatter,style-guide,terminology}.md`、`docs/docs.json`

**GEO 指什么：** Generative Engine Optimization——让 ChatGPT / Claude / Perplexity / Google AI Overviews 这类生成式引擎能**抓取、理解并引用**本站内容。与 SEO 的差别在于目标不是排名与点击，而是"被 AI 当作事实来源引用"。因此评价标准是：内容能否被抓到、能否被正确切分、能否被逐句引用而不产生歧义。

---

## 0. 现状核对（2026-09-17 实测）

| 项 | 实测结果 | 结论 |
|---|---|---|
| `https://www.pawsql.com/llms.txt` | HTTP 200，`content-type: text/html`，正文是 React SPA 外壳（`<div id="root">`、"You need to enable JavaScript"） | **没有真的 llms.txt**；200 是 SPA 兜底路由的假阳性。AI 工具按标准请求拿到的是 JS 外壳 |
| `https://www.pawsql.com/docs/zh/llms.txt` | 同上 | 旧文档站同样没有 |
| `https://www.pawsql.com/robots.txt` | `User-agent: *` / `Allow: /` + 两条 `Sitemap:`（指向产品站 sitemap） | 抓取是放行的，但没有 AI bot 相关声明，sitemap 也不含文档页 |
| 产品站首页 JSON-LD | 有 `Organization`（name/url/logo/description + `sameAs` GitHub、X） | 这是现成的发布者实体资产，新站 `seo.organization` 可直接复用其 `sameAs` |
| `docs.pawsql.com` | **已上线**（2026-09-18 实测）：`/llms.txt` 返回 `text/plain` 且内容为本站中文页面，`robots.txt`、`sitemap.xml`、页面 `.md` 端点均可达，JSON-LD 含 Organization/WebSite/WebPage | 与 IMPLEMENTATION-V2 的"未生产部署"**不符，以实测为准**。线上当前是**未含本次 `seo`/`markdown` 配置的旧版本** |
| 本地 `mintlify dev` | `/llms.txt`、`/llms-full.txt`、`/robots.txt`、`/sitemap.xml`、页面 `.md` 端点**全部 404**；页面 DOM 中**不输出 `application/ld+json`**（JS 执行后仍无） | 这些由 Mintlify 托管层生成，本地无法验证，**验收必须在线上做** |

**已核实的边界（2026-09-17 写入 G0-2/G0-3 后实测）**：`docs.json` 的 `seo.organization` 与 `markdown.instructions` 会被正确解析并随页面配置载荷下发（值确实出现在页面 HTML 中），所以"本地看不到输出"**不是配置写错**，而是托管层才渲染。G2-1 验收脚本因此必须覆盖 JSON-LD `@graph` 与 Agent Instructions 块两类输出。

**实测发现并修复：llms.txt 有 12 个条目重复（2026-09-18）**。线上 `llms.txt` 中 12 个页面各出现两次，数量等于 `docs.json` 里 12 个带 `root` 的分组——每个分组的 `root` 页同时也列在 `pages` 数组里，Mintlify 于是收录两遍。

**修复方式：从各分组的 `pages` 中移除 `root` 页**（中英各 12 处，共 24 项）。

曾一度误判为不可修复：只看 DOM 时发现分组标题是 `<button>`、`href` 为 `null`，便推断"标题不可导航、`pages` 里那条是唯一入口"。**该推断是错的**——按钮通过 JS 导航，没有 `href`。实测点击后：

- 顶层分组「快速开始」→ `/getting-started`（什么是 PawSQL?）
- 嵌套子分组「安装与接入」→ `/user-guide/installation`（安装与接入概览）

分组标题本身就是 root 页的入口，`pages` 里那一条是纯重复项。移除后侧栏结构不变、页面全部可达。

**教训**：判断元素是否可交互要看行为，不要只看属性。此前的"替代方案"（删 `root` 字段）确实会破坏分组标题，但那不是本问题需要走的路。

**Mintlify 部署后自动提供**（据官方文档，非本仓库实现）：`/llms.txt` 与 `/.well-known/llms.txt`、`/llms-full.txt` 与 `/.well-known/llms-full.txt`、每页 `.md` 后缀与 `Accept: text/markdown`、结构化 404（回带 llms.txt 指引与相关页）、JSON-LD `@graph`（Organization / WebSite / WebPage / BreadcrumbList / TechArticle / APIReference）、sitemap、robots.txt、OG 图、响应头 `Link` 与 `X-Llms-Txt` 发现机制、`/_llms/` 分片索引。

即：**管道是白送的，本仓库要负责的是"喂进去的内容形态"与"上线时把开关拨对"**。

---

## 1. 目标

1. **可发现**：AI 工具能通过 llms.txt / llms-full.txt / `.md` 端点拿到干净的 Markdown，而不是 JS 外壳。
2. **可引用**：每个事实有明确主语、单一出处、可被整句摘录而不失真。
3. **可消歧**：产品名、组件名、规则名在站点内唯一，且与外部实体（GitHub、官网）通过 `sameAs` 关联。
4. **可度量**：有办法回答"AI 现在引不引用我们、引用哪一页"。

---

## 2. 改动项清单

状态：`已具备`（无需改动）/ `待实施` / `已实施`（配置已写入，线上验收见 G2-1）/ `需决策` / `暂缓`。优先级 P0 = 上线前必须；P1 = 首发后随批；P2 = 持续。

### 2.1 发布与配置层（P0 为主）

| # | 项 | 区域/文件 | 现态 → 目标 | 优先级 | 状态 |
|---|---|---|---|---|---|
| G0-1 | 站点部署与域名 | Mintlify dashboard | **已上线**于 `docs.pawsql.com`（根域、无 base path）；待把含新配置的提交部署上去 | P0 | 已实施 |
| G0-2 | `seo.organization` | `docs/docs.json` | 无 → 稳定 `@id`、name、`legalName`、url、logo、`sameAs`（复用产品站已有 Organization JSON-LD 的 GitHub/X 链接） | P0 | 已实施 |
| G0-3 | `markdown.instructions` | `docs/docs.json` | 无 → 注入**中英双语** Agent Instructions 块（3 条），交代产品定位、术语口径与事实纪律 | P0 | 已实施 |
| G0-4 | 抓取策略 | 托管层 robots | 已定：延续放行 AI bot（§3.3） | P0 | 待实施 |
| G0-5 | 匿名可达 | 托管认证设置 | 已定：内容页与 `llms.txt`/`llms-full.txt` 对匿名公开（§3.4） | P0 | 待实施 |
| G0-6 | `seo.indexing` | `docs/docs.json` | 已定：仅导航内页，维持默认，不设 `"all"`（§3.5） | P1 | 已具备 |
| G0-7 | `seo.metatags` | `docs/docs.json` | 无 → 放 `google-site-verification` 等站点级验证串 | P1 | 待实施 |
| G0-8 | 旧域跨站 301 | **旧主机侧**（`www.pawsql.com`，非 `docs.json`） | 224 个旧 URL 301 到新站对应页 | — | 暂缓（§3.9） |
| G0-9 | 新站内部 `redirects` 机制 | `docs/docs.json` | 无 → 启用 `redirects` 数组，随新站页面改名/合并/拆分滚动登记（Mintlify 原生；默认 308，`:slug*` 通配，无条数上限）。**与旧站无关** | P2 | 待实施 |
| G0-10 | 旧→新映射台账 | — | 按「新站页面 ← 它取代的旧 URL」方向登记 | — | 暂缓（§3.9） |
| G0-11 | 消除 llms.txt 重复条目 | `docs/docs.json`（24 处：12 个分组 × 中英） | 分组 `root` 页同时列在 `pages` → llms.txt 每条收两遍 → 已从 `pages` 移除（分组标题本身即 root 页入口，见 §0） | P1 | 已实施 |

### 2.2 内容层（P1 为主）

| # | 项 | 区域/文件 | 现态 → 目标 | 优先级 | 状态 |
|---|---|---|---|---|---|
| G1-1 | `description` 治理 | frontmatter + 校验 | 已做（CONTENT-MODEL-CHANGES B1） | — | 已具备 |
| G1-2 | `keywords` / `aliases` 落地 | frontmatter | **仅 1 页使用** → published 页按需覆盖（规则英文名↔中文名、旧术语桥） | P1 | 待实施 |
| G1-3 | 字段纳入校验 | `tools/` | `keywords`/`noindex` 等可写但不校验（FrontMatter 允许额外字段） | P1 | 待实施 |
| G1-4 | 可引用段落形态 | `style-guide.md` + 内容批次 | 部分已符合 → 明确要求：问句化 H2、段落自包含（不依赖"如上所述"）、比较类内容用表格 | P1 | 待实施 |
| G1-5 | 单一事实源 / 去重 | 内容批次（CONTENT-MODEL-CHANGES C2） | 待实施 → 同一事实只在一页成文，其余引用 | P1 | 待实施 |
| G1-6 | FAQ 型内容 | 内容批次 | `type: faq` **0 页** → 按检索问句补 FAQ 页 | P2 | 待实施 |
| G1-7 | 新鲜度信号 | frontmatter | `lastReviewed` **仅 1 页** → published 页补齐 | P2 | 待实施 |
| G1-8 | 术语公开化 | 新建 `reference/glossary`（zh+en）+ 拆分 `contributing/terminology.md` | 仅贡献者可见（`status: draft`）→ 公开页只收产品/用户术语，内部工具词留在贡献者文档；随参考资料发布，不进首发（§3.7） | P2 | 待实施 |

### 2.3 度量层

| # | 项 | 区域/文件 | 现态 → 目标 | 优先级 | 状态 |
|---|---|---|---|---|---|
| G2-1 | 线上 GEO 验收脚本 | `tools/src/pawsql_doc/geo.py` + `check-geo` 子命令 | 无 → 检查 llms.txt / llms-full.txt / `.md` / JSON-LD `@graph` / Agent Instructions 块的**可达性与内容**，并与 `docs/docs.json` 的声明逐项比对；含 AI bot UA 视角与 llms.txt 重复条目检测 | P0 | 已实施 |
| G2-2 | AI 引用基线 | 外部观测 | 无 → 记录主要引擎对若干目标问句的引用情况，作为后续对比基线 | P2 | 待实施 |
| G2-3 | 英文 AI 覆盖 | `docs/llms.txt`（自定义） | 英文页不进生成的 llms.txt（默认语言为 zh）→ 观察英文查询的实际覆盖缺口，再决定是否手写自定义 llms.txt | P2 | 待实施 |

---

## 3. 已裁定决策（2026-09-17）

| # | 项 | 决策 |
|---|---|---|
| 1 | 默认语言 | 维持**中文为默认语言**（内容根 `/`，英文镜像在 `/en`）。 |
| 2 | 域名 | 新站部署在 **`docs.pawsql.com`**，根域托管、无 `/docs` base path。 |
| 3 | 抓取策略（G0-4） | **延续放行 AI bot**（与旧站 `Allow: /` 一致）。 |
| 4 | 认证（G0-5） | 内容页与 `llms.txt`/`llms-full.txt` **对匿名访问公开**，不设登录墙。 |
| 5 | `seo.indexing`（G0-6） | **仅导航内页**——维持 Mintlify 默认，不设 `seo.indexing: "all"`，非导航页不进 llms.txt 与索引。 |
| 6 | 旧站处置（G0-8） | **301 重定向**旧站 URL 到新站（而非 canonical 并存）。 |
| 7 | 术语表公开（G1-8） | 建公开 `reference/glossary` 页，**只收产品/用户术语**；内部工具词留在 `docs/contributing/terminology.md`。**随参考资料整体发布，不进首发。** |
| 8 | 迁移原则 | **不做 1:1 迁移**：旧站内容按情况**重写、重组**，**完全以新站为准**。旧 URL 结构不作为约束。 |
| 9 | 旧站内容处置 | **暂缓**——暂时不考虑旧站内容。决策 6/8 中涉及旧站的部分保留为记录，等启动旧站内容工作时再执行。 |

**决策 1 的直接后果。** Mintlify 生成的 `llms.txt` / `llms-full.txt` **只列默认语言与默认版本**——即只有中文页，英文页不进这两个文件（每页 `.md` 端点仍可单独访问，按 URL 抓取时仍可被引用）。要覆盖英文 AI 查询只有两条路：手写 `docs/llms.txt` 覆盖生成版（代价是失去零维护、需随导航同步），或接受现状。**当前选择接受现状，英文侧的 AI 覆盖列为 P2 观察项（见 G2-3）。**

**决策 2 的直接后果。**
- **无 base path 问题**：`/llms.txt`、`/_llms/`、`/.well-known/`、`.md` 这些端点路径干净，不需要反代 path 白名单（官方文档专门警告的 base path 错配风险不存在）。
- **与旧站是不同域名**：旧文档站 `www.pawsql.com/docs/` 与新站并存会形成同主题重复内容。其处置（canonical 或 301）随决策 9 暂缓，但**风险本身没有消失**——旧站仍在线且被索引，启动旧站工作时需一并解决。
- **两级实体不要混写**：`seo.organization` 的发布者实体仍是 `https://www.pawsql.com`（组织），站点实体是 `docs.pawsql.com`（WebSite）。Organization 与 WebSite 是两个节点，`sameAs` 挂组织，不挂站点。

**决策 3–5 的直接后果。** 三者都是"维持现状/关闭开关"，不需要改配置：抓取与认证维持放行，`seo.indexing` 保持默认值即可。唯一要落实的是**上线后核对**——确认线上 `llms.txt` 与 `llms-full.txt` 在未登录状态下确实能匿名取得（列为 G2-1 的检查项）。

**决策 6 的直接后果（随决策 9 暂缓执行）。** 旧站 `/docs/` 下实测共 **224 个 URL**，但拆开后规模比表面小得多：

| 类别 | 数量 | 性质 |
|---|---|---|
| `/docs/guides/*` | 32 | 真文档，主题与新站 user-guide 接近 |
| `/docs/insides/*` | 14 | 真文档（库设计、改写引擎等） |
| `/docs/blog/YYYY/*` | **39** | 真文章（英文，服务端渲染） |
| `/docs/api/*` | 7 | API 文档 |
| 标签 / 分页 / archive | 126 | 纯导航页（`blog/tags` 105、`/docs/tags` 13、分页 7、archive 1） |
| 杂项（`/docs/`、`faq`、`aboutus`、`index_old`、`markdown-page`） | 6 | — |

即"153 个博客路径"里**只有 39 篇是文章**，其余是标签与分页。旧站内容经抽样确认为**服务端渲染的真内容**（blog / guides / insides 三类页面均无 SPA 壳），具备真实的检索与引用价值——所以这不是一批"没有价值的旧站"，真要处置时值得认真对待。

**决策 7 的直接后果。** 公开术语表按内容模型落在 `reference/` 下（CONTENT-MODEL-V2 把 `glossary` 列为 `reference` 的子类型），而 `reference/` 未进首发，因此**首发的 GEO 拿不到这个实体消歧锚点**，它的价值要等参考资料整体发布时才兑现。落地时需要拆分内容：
- 公开页只保留产品与用户术语（Optimizer、Query Rewrite、Index Recommendation、Audit Rule、SQL Review、Compatibility 等）；
- 内部工具词（Feature Manifest、Documentation Mapping、Drift、Coverage、Release Gate）属于贡献者词汇，留在 `docs/contributing/terminology.md`；
- 中英镜像按项目惯例配齐（`localeOf` 校验只在字段填写时强制成对存在，镜像本身非硬性要求）。

**决策 8 的直接后果（旧站部分随决策 9 暂缓，新站部分保留）。**
- **两个重定向面必须分清。** Mintlify 的 `redirects`（配在 `docs/docs.json`）**只作用于 `docs.pawsql.com` 自身的路径**。旧 URL 位于**另一个域**（`www.pawsql.com/docs/*`），请求根本到达不了 Mintlify——旧站 301 必须在**旧主机侧**配置，`docs.json` 帮不上忙。这一点容易误判成"写进 docs.json 就完事"。
- **`docs.json` 的 `redirects` 仍然要建，但与旧站无关**：新站自己重组时（改名、合并、拆分）会持续产生内链迁移需求。Mintlify 原生支持默认 308 永久、`permanent: false` 为 307、`:slug*` 通配与部分通配、无条数上限。
- 旧站侧的「映射台账方向」与「301 执行时机」随决策 9 暂缓。

---

## 4. 暂缓事项（暂不决策）

以下三项都只涉及旧站内容，按决策 9 暂缓。分析结论保留在此，启动旧站工作时可直接沿用：

1. **未存活内容怎么处置。** 重写重组后必然有一批旧内容不进新站。可选：301 到最接近的主题页 / 301 到站点首页 / 返回 410 告知已移除。
2. **126 个导航页的批量处置。** 它们没有内容、不依赖重写进度，届时可独立先做：统一 301 到博客索引，或直接 410。
3. **旧域 301 的执行时机。** 目标依赖内容重写完成，无法在部署日一次做完——随内容批次滚动上线，还是内容就绪后一次性切换。

另有一项**不因暂缓而消失**的风险：旧站仍在线且被索引，与新站形成同主题重复内容（见决策 2 后果）。启动旧站工作时需一并解决。

---

## 5. 建议落地顺序

1. **P0 配置层已完成**：G0-1 站点本就在线、G0-2/3 已写入 `docs.json`、G2-1 验收脚本已就绪。剩下的是**把含新配置的提交部署上去**，然后跑 `cd tools && uv run python -m pawsql_doc check-geo` 核对线上产出。
2. **G0-9 新站内 `redirects`** 随新站自身的重组建立（与旧站无关）。
3. **P1 内容层**随现有内容批次滚动：先 G1-4（写作规则）与 G1-2（keywords），再做 G1-5（去重）。
4. **P2** 视上线后的实际引用情况排，含 G1-6（FAQ）、G1-7（新鲜度）、G1-8（术语表）、G2-2/3。

---

## 6. 反向约束（明确不要做）

- **不要为 AI 写关键词堆砌段落**：本站同时服务人与 agent，可读性下降会连带损害可信度。
- **不要用 `<Visibility for="agents">` 制造人机不一致的事实**：该组件适合给 agent 补充"如何调用 API"这类等价信息，不适合让 AI 看到人类看不到的版本——那会被判为 cloaking。
- **不要跨页重复同一事实**：与 CONTENT-MODEL-V2 的单一事实源原则一致，对 GEO 同样加分——重复内容会让多个页面互相争夺同一次引用。
- **不要为凑检索词虚构版本号、参数或性能数字**：沿用仓库事实纪律，无证据标 `unknown`。
