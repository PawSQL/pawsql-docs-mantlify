# PawSQL 博客迁移执行计划（BLOG-MIGRATION-PLAN）

**版本/日期：** v1 · 2026-09-22
**状态：** 草案，待 §11 产品/法务锁放行后按批次开工
**输入：** [PLACEMENT.md](PLACEMENT.md)（`docs/blog` 落位 77 行）、[MIGRATION-PLAN.md](MIGRATION-PLAN.md) §4 批次 P2.2/P2.3、[CONTENT-MODEL-V2.md](CONTENT-MODEL-V2.md)、原内容库《技术设计说明书》§25 Blog 方案
**位置约定：** 仓库根 = `pawsql-docs-v2`；站点内容根 = `docs/`；源 vault = `pawsql-docs-new`（**只读**）。本计划目标路径均相对仓库根，路由相对 `docs/`。

---

## 1. 目标与完成标志

把 vault 中 blog 类内容去重、清洗、核事实后落位到 `docs/blog/`（zh 默认）与 `docs/en/blog/`（en 镜像），并让 **「博客」tab 重新具备上线条件**。

**完成标志（三条同时满足）：**

1. `docs/blog/` 中部已发文章 ≥ 8 篇、覆盖 ≥ 2 个 category，且中英文镜像按 §4 配对；
2. `docs/docs.json` 中英两侧「博客」tab 恢复（2026-09-17 `3a58cfb` 因内容量不足移除），`validate-nav --release` 全绿；
3. 本计划 §6 去重表中每条「采用」行都已落位或显式登记为「排除」并注明理由。

> 博客与用户手册分离（设计说明书 §25）：博客是**市场/技术传播内容**，不进 `user-guide/`，不复用手册正文；同一事实只在一处成文（[style-guide.md](docs/contributing/style-guide.md) 单一事实源）。

## 2. 范围

**本次范围：**

- `70-content/blog/**` —— 35 个文件，去重后约 **13 篇**成文（见 §6.1）；
- `99-待归类` 中 PLACEMENT 已落位到 `docs/blog` 的 blog 类内容 —— 20 个文件，去重后约 **4 篇新增 + 2 篇已迁需返工**（见 §6.2）。

**本次不做（PLACEMENT 同样落位到 `docs/blog`，但另批）：**

| 源 | 行数 | 目标 | 说明 |
|---|---|---|---|
| `20-engine/internals`、`20-engine/indexrec` | 18 | `docs/blog/sql-optimization/` | 技术文章，题材与新站 `user-guide/optimization` 接近，需先定「文章 vs 文档」边界，避免与手册重复 |
| `70-content/comparisons` | 5 | `docs/blog/product-comparison/` | 竞品对比，随 §11 L4 一起定 |
| `70-content/newsletters` | 11 | `docs/blog/whats-new/` | 发布公告/社区精选，与 `release-notes` 拆分口径待定 |
| `40-audit/reviews`、`50-integration` 营销稿 | 5 | `docs/blog/product-comparison/`、`whats-new/`（按内容分归） | 与手册去重后并入 |

**明确排除：**

- 旧站 `www.pawsql.com/docs/blog/YYYY/*` 的 **39 篇英文文章** —— [GEO-PLAN.md](GEO-PLAN.md) 决策 9「旧站内容处置暂缓」，本轮不作为源。
- `70-content/blog/*.docx`、`99-待归类/*.docx` —— Word 导出件，正文以同名 `.md` 为准（见 §6）。

## 3. 已定决策（2026-09-22）

| # | 决策 | 取值 | 理由 |
|---|---|---|---|
| D1 | 同题多版本取舍基准 | **以技术原文为准**，`-polish` 只作素材 | style-guide 要求「避免营销腔」；AI Guardrails 禁止虚构性能数据/客户案例。`-polish` 稿带公众号口径、CTA 与社交引流位 |
| D2 | 语言策略 | **中文优先**；仅复用**已存在**的英文译文，不新译 | 不引入未审翻译；en 侧缺页留待翻译队列 |
| D3 | 范围 | `70-content/blog` + `99-待归类` blog 类 | 单靠前者约 13 篇，不足以支撑 tab 上线 |
| D4 | 去重原则 | 同题一律收敛为「一份成文 + 中英镜像」 | style-guide 明示 `-polish`/`_en` 残留是 SEO/RAG 大敌 |

## 4. 目标 IA 与字段约定

### 4.1 目录结构（**待 §11 L2 定稿**）

推荐按设计说明书 §25 与 PLACEMENT 采用分类目录；因博客尚未上线、无对外链接，现在重组的成本远低于上线后：

```text
docs/blog/
  index.mdx                        # 博客落地页（layout: index）
  sql-optimization/index.mdx       # SQL 优化技术
  sql-governance/index.mdx         # SQL 治理实践
  success-stories/index.mdx        # 客户案例
  product-comparison/index.mdx     # 工具选型与对比
  whats-new/index.mdx              # 产品动态
  <category>/<slug>.mdx            # 文章详情页（layout: detail，必填 category）
docs/en/blog/<同样结构>/<slug>.mdx
```

**备选：** 保持现有扁平 `docs/blog/<slug>.mdx`。若选扁平，本计划其余部分不变，仅去掉目录层级。
注：`id` 是稳定主键、路径不是（CONTENT-MODEL-V2 §4），移动文件不改 `id`。

### 4.2 category 词表（**L1 已定，2026-09-22**）

枚举定义在 `tools/src/pawsql_doc/models/core.py` 的 `BlogCategory`，显示名在 `BLOG_CATEGORY_LABELS`，已导出到 `schemas/frontmatter-v2.schema.json` 并由 `validate-frontmatter` 校验：**取值须落在枚举内；文章详情页（`layout: detail`）必填，集合页（`layout: index`）不填**。

| 值 | 中文名 | 英文名 |
|---|---|---|
| `sql-optimization` | SQL 优化技术 | SQL Optimization |
| `sql-governance` | SQL 治理实践 | SQL Governance |
| `success-stories` | 客户案例 | Success Stories |
| `product-comparison` | 工具选型与对比 | Product Comparisons |
| `whats-new` | 产品动态 | What's New |

> `FrontMatter.category` 此前是自由字符串，且 `docs/contributing/frontmatter.md` 把它误写成规则分类词表；两处均已修正。**规则分类（`ddl`/`dml`/…）是 `metadata/rules/*.yaml` 的字段，不写在页面里。**

**§6 各目标页的归类（B0 逐页定稿）。** 下表为按词表的初步归类，除标注「待定」外可直接采用：

| 目标页 | category |
|---|---|
| A 执行计划可视化、B NULL 陷阱、C 索引引擎 | `sql-optimization` |
| D TPCH 评测、E 索引设计 ×2、H 大模型局限 | `sql-optimization` |
| F/G 优化器短板 ×3、J 窗口函数索引推荐、N Oracle Quirk | `sql-optimization` |
| I 存储过程审核、M DBeaver 执行前审核 | `sql-governance` |
| O TDSQL-MySQL 案例、P openGauss 案例 | `success-stories` |
| Q Top 5 审核工具测评 | `product-comparison` |
| K Advisor 概览、L DBeaver 插件发布 | `whats-new`（待定：K 是能力概览，若不视为产品动态则需另议） |

**已有页面同步结果：** `tdsql-mysql-slow-query`、`opengauss-slow-query` 由 `case-study` 改为 `success-stories`；`en/blog/sql-optimization/or-to-union` 由 `engineering` 改为 `sql-optimization`。

### 4.3 frontmatter 模板

```yaml
---
id: blog-<slug>                # 稳定、URL 安全；与既有两页同风格
title: <≤60 字符，含检索关键词>
description: <一句话，≤155 字符，人工书写，禁占位/机器截断>
type: article
subtype: blog
layout: detail
category: <sql-optimization|sql-governance|success-stories|product-comparison|whats-new>   # 文章详情页必填，见 §4.2
status: draft                  # 只允许 draft → review → approved → published
language: zh
translationKey: blog-<slug>    # 同一内容中英共用
product: pawsql
authors: [pawsql]
tags: [<3-5 个检索标签>]
date: <首次发布日；源无日期则 TODO 待定，不编造>
relatedFeatures: [<关联 Feature id，可选>]
---
```

en 镜像：`id: en-blog-<slug>`、`language: en`、`localeOf: blog-<slug>`，`translationKey` 与 zh 页一致。
**既有不一致点：** [docs/en/blog/sql-optimization/or-to-union.mdx](docs/en/blog/sql-optimization/or-to-union.mdx) 的 `id` 为 `blog-or-to-union`（无 `en-` 前缀、无 `localeOf`），与 `en/blog/index.mdx` 的 `en-blog-index` 写法不一致 —— 本批内统一。

### 4.4 正文结构

`article` 类型的建议槽位是 主题 / 正文 / 来源 / 责任人 / 日期（[templates/content-types.md](templates/content-types.md)）。
`REQUIRED_SECTIONS` 未收录 `article`，因此**发布门禁不强制 `sections` 映射**；但成文应满足：有 H1（与 frontmatter `title` 不同义重复）、代码块标注语言、比较类内容用表格、段落自包含（GEO-PLAN G1-4）。

## 5. 源盘点基线（2026-09-22 实测）

**共同特征：** 两个源目录**没有任何文件带 YAML frontmatter**；全部为 Obsidian/Typora 导出件，行文、标题层级、图片引用格式各不相同。

| 源 | 文件数 | 去重后成文 | 非成稿 | 已有英文译文 |
|---|---|---|---|---|
| `70-content/blog` | 35 | 13 | 5 | 6 组（见 §6.1） |
| `99-待归类` blog 类 | 20 | 4 新增 + 2 返工 | 5 | 3（Oracle quirk 含 en） |

**目标侧现状：**

- `docs/blog/` 已有 3 页：`index.mdx`、`tdsql-mysql-slow-query.mdx`、`opengauss-slow-query.mdx`；`docs/en/blog/` 已有 2 页：`index.mdx`、`sql-optimization/or-to-union.mdx`。全部 `status: draft`。
- 工具已具备：`tools/src/pawsql_doc/migration.py` 已把 `blog/` 识别为 `type: article` / `subtype: blog`，`blog/**/index.mdx` 识别为 `layout: index`；`validate-frontmatter` 覆盖 `blog/` 路径。
- **工具缺口：** 无「文章落位」命令（无 frontmatter 骨架生成、无图片归集、无去重登记）。见 §7 B0.2。
- **导航现状：** `docs/docs.json` 中英两侧均无「博客」tab（`3a58cfb` 移除），`NAV_GROUP_TYPES` 未收录博客分组名（即分组不校验 type，加回时无需改校验器）。

## 6. 去重与取舍表

「采用」列即成文底本；「处置」列写明其余文件的归宿（合并素材 / 排除 / 待定）。

### 6.1 `70-content/blog`（35 → 13）

| 组 | 源文件 | 采用 | 目标页（slug） | 处置 |
|---|---|---|---|---|
| A 执行计划可视化 | `MySQL的执行计划可视化.md` / `Plan Visualization for MySQL.md` / `执行计划可视化.md` | `MySQL的执行计划可视化.md`（zh）+ en 译文 | `sql-optimization/plan-visualization` | `执行计划可视化.md` 为 AI 改写稿、章节重复，**排除**；6 张远程图需重取（§9） |
| B NULL 陷阱 | `关于null的陷阱.md` / `SQL查询中关于NULL的陷阱.md` / `…_en.md` | `关于null的陷阱.md`（zh）+ en 译文 | `sql-optimization/sql-null-traps` | en 稿有断裂结尾需修；base 稿为子集，**排除** |
| C 索引引擎 | `PawSQL索引引擎.md` / `Index Advisor Engine.md` | `PawSQL索引引擎.md` | `sql-optimization/index-advisor-engine` | 后者同题截断版，**排除** |
| D TPCH 评测 | `PawSQL针对TPCH的优化评测.md` / `Optimizing TPCH Queries with PawSQL.md` | `.md`（zh）+ en 译文 | `sql-optimization/tpch-optimization-benchmark` | 两稿同表，成立 |
| E 索引设计 | `如何创建高效的索引.md`(+`_en`) / `数据库索引的类型.md`(+`_en`) | 两组各自成文 | `sql-optimization/efficient-index-design` / `sql-optimization/index-types` | `数据库索引的类型_en.md` 第 5 行损坏、3 张图丢失，需修 |
| F MySQL 优化器短板 | `突破 MySQL 性能瓶颈….md` / `…-polish.md` / `How to leverage MySQL Optimizer with PawSQL.md`(+`-polish`) / `拆解 MySQL 优化盲区….md` / `MySQL 优化器搞不定的坑….md` | `突破 MySQL 性能瓶颈….md` | `sql-optimization/mysql-optimizer-blind-spots` | 与 G 组成「补齐优化器短板」系列（可直接套用 `pawsql-optimizer-article` skill 的三篇体例）；其余 4 稿**排除**，`拆解…` 素材并入 |
| G 方言短板 | `PawSQL 补齐 PostgreSQL 优化器短板….md` / `PawSQL 补齐 Oracle 优化器短板….md` / `How to leverage PostgreSQL Optimizer with PawSQL.md` | 两个「补齐短板」稿 | `sql-optimization/postgresql-optimizer-blind-spots` / `sql-optimization/oracle-optimizer-blind-spots` | `How to leverage PostgreSQL…` 已被取代，**排除** |
| H 大模型局限 | `大模型在处理SQL优化等精确性问题的局限.md` / `大模型在处理SQLSQL….md` / `大模型局限.md` | `大模型在处理SQL优化等精确性问题的局限.md` | `sql-optimization/llm-limits-in-sql-optimization` | `大模型局限.md` 顶部是**原始生成 prompt**，**排除** |
| I 存储过程审核 | `存储过程审核.md` / `PawSQL 在 T‑SQL 存储过程审核与优化上的突破.md` | `存储过程审核.md` | `sql-governance/stored-procedure-audit` | 后者为营销改写（含「立即体验」CTA），**排除** |
| J 窗口函数索引推荐 | `PawSQL的索引推荐,….md` / 同名 `.docx` | `.md` | `sql-optimization/window-function-index-recommendation` | 正文尾部被追加了一段重复改写，需删除；`.docx` **排除** |
| K 产品概览 | `PawSQL Advisor.md` | 原稿 | `whats-new/pawsql-advisor-overview` | 与 Advisor 手册去重（PLACEMENT §196 同因） |
| — 非成稿 | `Some clues of PawSQL rewrite engine.md`（292 B）、`PawSQL Explain.md`（1.2 K，无 H1）、`分区表索引.md`（双语草记）、`语之暗面的kimi大模型代码分析评测.md`（实验记录） | — | — | **本批排除**；`PawSQL Explain` 若需保留，并入 A 的执行计划可视化主题 |

### 6.2 `99-待归类` blog 类（20 → 4 新增 + 2 返工）

| 组 | 源文件 | 采用 | 目标页（slug） | 处置 |
|---|---|---|---|---|
| L DBeaver 发布 | `BLOG-OVERVIEW.md`(+`-polish`) | `BLOG-OVERVIEW.md` | `whats-new/dbeaver-plugin-release` | 与 DBeaver 插件手册去重（单一事实源） |
| M DBeaver 执行前审核 | `BLOG-AUDIT.md`(+`-polish`) | `BLOG-AUDIT.md` | `sql-governance/dbeaver-pre-execution-audit` | 与 L 共用截图，避免重复配图与重复功能描述 |
| N Oracle 方言 Quirk | `意想不到的SQL/` 3 个文件 | `SQL避坑指南 - …薛定谔行为.md`（zh）+ `Oracle GROUP BY Integer Literals - Schrödinger Behavior.md`（en） | `sql-optimization/oracle-group-by-integer-literal` | 原始笔记稿 `Oracle 的 GROUP BY 整型常量…md` **排除**（含 PawSQL 规则小节，并入成文） |
| O TDSQL-MySQL 案例 | `金融生产环境实战：…TDSQL-MySQL…md`(+`-polish`) / `金融级实战验证：…深度评测.md` | **`金融级实战验证：…深度评测.md`** | `success-stories/tdsql-mysql-slow-query`（**返工**） | 见 §6.3 |
| P openGauss 案例 | `…openGauss…md`(+`-polish`+`.docx`) | 已迁页（源自 `-polish`） | `success-stories/opengauss-slow-query`（**补图**） | 2 处 `{/* 图片待补 */}` 需补（原 `Pasted image 20260527162454/162551.png`、`products.png`，均已在 `00-assets/images/` 找到） |
| Q Top 5 审核工具测评 | `2026年Top 5 SQL审核工具深度测评….md`(+`-polish`) | `-polish.md`（唯一有 H1 的成稿） | `product-comparison/sql-audit-tools-review-2026` | **阻塞于 §11 L4**（竞品对比+宣称） |
| — 非成稿 | `TDSQL拉跨系列 - 1. 慢查询管理.md`（**0 字节**）、`- 2. 执行计划.md`（原始实验日志）、`BIC-QA优化规则.md`（约 90 条 KB 转储）、`PawSQL优化能力评测.md`（**含自拟 benchmark 数字**）、`SQL性能瓶颈智能评价分析.md`（内部设计规格 4.2.x） | — | — | **本批排除**，理由见 §12 R1/R6；`- 2. 执行计划` 若成文需重写，另立条目 |

### 6.3 返工项：TDSQL-MySQL 案例改用技术底本

现有 [docs/blog/tdsql-mysql-slow-query.mdx](docs/blog/tdsql-mysql-slow-query.mdx) 由 `-polish` 稿压缩而来，**丢了全部数据表**。按 D1，改用 `金融级实战验证：…深度评测.md`：

- **该稿独有、必须搬入：** 11 个业务系统的分系统表（慢SQL数/可优化/有效/召回率）、352 条命中规则的 Top-10 表、7 档性能提升分布、分布式与集中式召回率（72.3% / 72.2%）、未覆盖原因分类表（21/15/1/26）、以及「索引推荐是基本盘、组合优化才是胜负手」等结论段。
- **必须处理的合规项：** 该稿含 **12 处内部系统代号**（nocc/cams/gcs/gcams/bcams/ecif/fsms/srs/cmis/bmsmonitor 等）+ 行业与时间窗，**必须脱敏或删除再入库**（§11 L3）。
- **数字一致性：** `金融生产环境实战` 原稿正文出现「76.3%」与「76.6%」并存，深度评测与已迁页均为 76.6% —— 统一为 76.6%，并在 §11 L5 下留证据。
- **体例：** 删除 emoji 标题（📊🔍📈）、去掉「核心数据速览」式的公众号排版；保留 6 张图表（`/images/blog/tdsql-*.png` 已就位）。

## 7. 批次计划

每批 ≤ 8 页（含 en 镜像），按「低风险先行」排序：先跑通无事实/法务风险的纯技术稿，再处理带数字与宣称的稿件。

| 批次 | 内容 | 产物 | 依赖 |
|---|---|---|---|
| **B0 约定与工具** | 定 §4 目录结构、category 词表、图片命名；补 `import-blog` 脚手架命令（frontmatter 骨架 + 图片归集清单，dry-run 默认） | 约定落文 + 工具 | L1、L2 |
| **B1 纯技术（无事实风险）** | A 执行计划可视化、B NULL 陷阱、E 索引设计 2 篇、N Oracle Quirk | 5 篇 zh + 4 en 镜像 | B0 |
| **B2 优化器短板系列** | F MySQL、G PostgreSQL、G Oracle | 3 篇 zh | B0；可套 `pawsql-optimizer-article` skill |
| **B3 评测与产品能力** | D TPCH、C 索引引擎、H 大模型局限、J 窗口函数索引、I 存储过程审核、K Advisor 概览 | 6 篇 zh + 1 en 镜像（TPCH） | B0；D 需 L5 证据 |
| **B4 案例** | O TDSQL-MySQL 返工、P openGauss 补图 | 2 篇返工 | L3、L5 |
| **B5 DBeaver 产品稿** | L 插件发布、M 执行前审核 | 2 篇 zh | 与插件手册去重核对 |
| **B6 法务敏感** | Q Top 5 测评 | 1 篇 zh | L4 |
| **B7 导航上线** | 恢复中英「博客」tab + 5 个 category 落地页；英文缺页登记翻译队列 | `docs.json` 改动 | §1 完成标志 |

> 备选旁支：`拆解 MySQL 优化盲区`（F 组）与 `TDSQL拉跨系列 - 2. 执行计划` 素材独立成文，需先与手册核对是否重复；不在关键路径上。

## 8. 每篇处理配方

1. **选底本** —— 按 §6 表；同题其余文件不删源，仅在登记中标注「排除」。
2. **清洗** —— 去 `润色说明` 元块、版权页脚、公众号 CTA（「立即体验」「扫码关注」）、社交引流位、重复段、原始 prompt；删除与 frontmatter `title` 重复的正文 H1（Mintlify 固定渲染 title 为大标题）。
3. **frontmatter** —— 按 §4.3 补齐；`date` 无据不编，写 `TODO 待定`。
4. **图片** —— 按 §9 归集并改写引用。
5. **代码块** —— 统一标注 `sql` / `bash` / `yaml` / `json`；裸围栏补语言。
6. **去营销腔** —— 按 style-guide「避免营销腔」；删形容词堆砌与绝对化宣称，改为可验证陈述。
7. **事实核验** —— 性能数字、客户描述、竞品表述逐条过 §11；无证据者标 `unknown` 或删除，**不得保留无出处的数字**。
8. **单一事实源** —— 页脚「关于 PawSQL」目前只在 2 篇案例页各写一遍；本批起改为**不重复产品简介**，需要时链接到 `/features` 或抽成共享片段（避免 19 篇各写一份）。
9. **落位与登记** —— 建页 + 更新 `reports/` 与 §13 进度表。

## 9. 图片处理

**命名与路径（沿用现有约定）：** `docs/images/blog/<page-slug>-<name>.png`，正文引用站点绝对路径 `/images/blog/<page-slug>-<name>.png`。

**四类引用与处置：**

| 类型 | 例 | 处置 |
|---|---|---|
| vault 相对/绝对路径 | `..\images\三值逻辑.png`、`.\Bplustree.png`、`C:\...\typora-user-images\…` | **可回收**：已核实 `00-assets/images/` 存在同名文件（Bplustree.png / Hash_table.svg.png / 600px-R-tree.svg.png / 三值逻辑.png / products.png / Pasted image 20260527162454.png 等），复制并重命名 |
| Obsidian 嵌入 | `![[Pasted image 202608….png]]` | 同上；先在 `00-assets/images/` 与 `99-待归类/assets/` 内按文件名比对 |
| 远程 URL | 微信 / `zhimg` / `csdn` / `www.pawsql.com` | 重新下载入库（避免外链失效与被第三方统计）；取不到则就地留 `{/* 图片待补：<原始引用> */}` 且页面留 `draft` |
| `data:image/...;base64` | NULL 陷阱稿内 GIF | 必须落盘为文件后引用；不保留 base64 内联 |

**缺图约定：** 沿用既有写法 `{/* 图片待补：<原始引用> */}`（仓库有 `tools/tests/test_mdx_html_comments.py` 覆盖该形态），页面保持 `draft`，不阻塞成文。

## 10. 门禁与验收

每批提交前在 `tools/` 下全绿：

```bash
cd tools
uv run python -m pawsql_doc validate-frontmatter   # PASS
uv run python -m pawsql_doc validate-nav           # preview PASS
uv run python -m pawsql_doc quality                # 无新增 structure/existence 问题
uv run pytest -q
```

补充验收：

1. **链接** —— 新页内部链接（含 `/en` 前缀规则）逐条可达；不指向 `draft` 未落位页。
2. **浏览器抽查** —— `cd docs && npx mintlify dev`，抽查新页渲染、代码高亮、图片、中英切换。**启动前先停掉残留的 `mintlify dev`**（见 [CLAUDE.md](CLAUDE.md)）。
3. **去重复核** —— `grep` 确认 `-polish`、`_en`、重复编号未作为独立页面入库（D4）。
4. **幂等** —— 重复执行落位脚本应零改动。

> 通过门禁 ≠ 可发布：`status` 提升到 `published` 属 §11 L6 的对外发布动作，须单独批准。

## 11. 产品/法务锁（放行前阻塞）

| # | 待确认 | 阻塞 |
|---|---|---|
| **L1** | ~~blog `category` 词表定稿~~ **已定 2026-09-22**：`sql-optimization` / `sql-governance` / `success-stories` / `product-comparison` / `whats-new`，已入 `BlogCategory` 枚举并校验（§4.2） | 解除，B0 起生效 |
| **L2** | URL 结构：分类目录 `blog/<category>/<slug>` 还是保持扁平（§4.1） | B0、B7 |
| **L3** | **客户可披露范围**：行业、时间窗、11 个内部系统代号是否可脱敏后保留；是否需客户书面同意 | B4 |
| **L4** | **竞品对比可发布范围**：Top 5 测评对 Bytebase / NineData / DBdoctor / Yearning 的比较表述，及「≥95% 审核准确率」「1.3 万 GitHub Stars」等宣称的证据 | B6 |
| **L5** | **性能数据证据**：76.6% / 671.4% 中位数 /「30% 提升超百倍」/ openGauss 100% / TPCH 276%（及 `PawSQL优化能力评测` 中 8.3x/6.7x/15.1x 类自拟数字）——逐条给出可回溯来源，否则标 `unknown` 或删除 | B3、B4 |
| **L6** | 对外发布节奏与 `status` 提升批准人；英文缺页是否排翻译 | B7 |
| **L7** | `20-engine/internals` 等 18 篇技术文章的「文章 vs 手册」边界（本轮范围外，但影响 `docs/blog` 最终体量） | 后续批 |

## 12. 风险登记

| # | 风险 | 说明与对策 |
|---|---|---|
| **R1** | **编造数据入库** | `PawSQL优化能力评测.md` 含自拟 benchmark（78/42/35 例、8.3x/6.7x/15.1x）与「改写成功率 90%」「几乎没有假阳性」等未经证实宣称 —— **本批排除**，不得作为素材；如成文须先补证据 |
| **R2** | 数字互相矛盾 | TDSQL 案例原稿「76.3%」与「76.6%」并存；统一口径并在 L5 下留证 |
| **R3** | 内部信息泄露 | 深度评测稿含 12 处系统代号与行业-时间窗组合，可定位到具体客户；脱敏前不得入库 |
| **R4** | 与手册重复 | DBeaver 两篇（L/M）与插件手册、Advisor 概览（K）与 Advisor 手册、F 组与 `user-guide/optimization` 高度重叠 —— 遵守单一事实源，博客只写手册没有的视角，其余链接 |
| **R5** | 图片失效 | 远程图（微信/zhimg/csdn）随时可能 404；一律落盘本地，取不到就标 TODO 而非留外链 |
| **R6** | 非成稿混入 | 两个源目录共 10 个文件是草记/日志/0 字节/内部规格（§6 各处已列），落位前须显式排除，避免"文件搬到目标即算迁移" |
| **R7** | 标题与 H1 重复 | Mintlify 固定渲染 frontmatter `title` 为大标题，正文重复 H1 会双标题；清洗时统一删正文 H1（既有两页已按此处理，A 组等另有 H1 保留习惯，需逐篇核） |
| **R8** | en 页 id 前缀不一致 | `en/blog/sql-optimization/or-to-union.mdx` 缺 `en-` 前缀与 `localeOf`；本批统一，勿扩散 |
| **R9** | 导航过早恢复 | 博客 tab 曾因内容量不足被移除；B7 须在 §1 完成标志达成后执行，避免再现死链/空分组 |

## 13. 进度追踪

每批完成后在本表追加一行，并回填 [MIGRATION-PLAN.md](MIGRATION-PLAN.md) §4 的 P2.2/P2.3 行状态与 [PLACEMENT.md](PLACEMENT.md) 对应行。

| 批次 | 日期 | 结果 | 遗留 |
|---|---|---|---|
| B0 | — | — | — |
| B1 | — | — | — |
| B2 | — | — | — |
| B3 | — | — | — |
| B4 | — | — | — |
| B5 | — | — | — |
| B6 | — | — | — |
| B7 | — | — | — |

**既有事实（2026-09-17，`fc4b8e3`）：** 已迁 `docs/blog/{index,tdsql-mysql-slow-query,opengauss-slow-query}.mdx` 与 `docs/en/blog/{index,sql-optimization/or-to-union}.mdx`，全部 `status: draft`；其中 TDSQL-MySQL 页按 §6.3 **待返工**，openGauss 页 **待补图**。
