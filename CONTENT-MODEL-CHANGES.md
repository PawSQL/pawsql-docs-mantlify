# 内容模型 & SEO/LLM 优化改动清单（CONTENT-MODEL-CHANGES）

> 历史规划：产品、类型、导航及门禁的当前规范见 [CONTENT-MODEL-V2.md](CONTENT-MODEL-V2.md)，实施记录见 [IMPLEMENTATION-V2.md](IMPLEMENTATION-V2.md)。本文未完成的事实整理事项仍作为待办，不代表已经实现。

**版本/日期：** v0.2 · 2026-09-04（决策已拍板，见 §3）
**性质：** 规划/清单（proposal）——标注待实施项与需产品决策项；不含代码实施。
**关联：** `docs/contributing/{frontmatter,style-guide,terminology}.md`、`MIGRATION-PLAYBOOK.md`、`MIGRATION-PLAN.md`、`PLACEMENT.md`
**原则：** 站点 = Mintlify 渲染 + 发布；**自建内容模型负责语义、引用、可信度与多语言一致性**——它是搜索引擎与 LLM/RAG 可用的关键。

---

## 0. 当前状态核对（2026-09-04，仓库实况）

- 语言：**中文为默认站点语言（`/`，内容根 `docs/` 下直接放 zh 页）**；英文镜像在 `/en`（`docs/en/**`）。
- 规则生成器由外部提交改为：**zh（默认）→ `docs/reference/{audit,optimizer}-rules/`**、**en（镜像）→ `docs/en/reference/...`**。
- 历史遗留不一致（P0a 批次已处理，见 git 记录）：
  1. ~~默认语言（zh）规则页 id 带 `zh-` 前缀~~ → 已翻转：zh 默认页 id 中性、en 镜像页 `en-` 前缀（A1）。
  2. ~~`metadata/mappings|features` required 路径指向 `docs/en/reference/...`~~ → 规则引用已切默认语言页；人工 en-only 页待 P1 补 zh 后切换（C1）。
  3. ~~`.github/workflows/validate.yml` no-diff 路径含 `docs/zh/reference`~~ → 外部提交已修为 `docs/reference docs/en/reference docs/en/databases`（C1，同步 PLAYBOOK/PLAN）。
  4. ~~`description` 生成页被机器截断到 200~~ → 生成器不再截断；规则取双语 `summary` 为 front-matter description（B1）。
  5. ~~`RuleZh`/“英文为主、中文为镜像”旧心智~~ → 已收敛为 `content:{zh,en}` 语言正文解耦（A2）。

## 1. 目标

让每一页“自描述、可引用、无歧义、可治理”，同时服务 人 / 搜索引擎 / LLM-RAG：

1. **单语言语义正确**：默认语言（zh）与镜像（en）的产出规则、id、门禁路径一致。
2. **结构化中性 + 语言正文解耦**：id/category/severity/database/version 属中性事实；name/正文属语言内容。
3. **可信度可机器判定**：`status` 与“是否出现在导航/是否可抓取”绑定；draft/review 不进生产导航。
4. **搜索/LLM 素材可检索**：description/title/术语受治理；正文单一事实源；分类词表受控；镜像配对可校验。

## 2. 改动项清单

> 状态：`已做`（外部提交已完成）/ `待实施` / `需决策`。P0a = 须在 251 条规则批量前完成；P1 = 可随批量。

| # | 项 | 区域/文件 | 现态→目标 | 优先级 | 状态 |
|---|---|---|---|---|---|
| A1 | 主语言语义统一（id/前缀） | 生成器 `rule_generator.py`、既有生成页 | 默认语言页 id 中性（去 `zh-`）；镜像语言用 `en-`；规则 id 优先复用产品注册表 | P0a | 已做 |
| A2 | 语言正文结构解耦 | `models/core.py`（Rule/Config/DB）、schema | 中性字段固定；语言正文收敛为 `content: { zh:{}, en:{} }`（替代“英文根 + 可选 zh 块”）；仍兼容现有 yaml（读旧字段→映射） | P0a | 已做 |
| A3 | `category` 受控词表 | `models/core.py`、schema、mapping 表 | 枚举（ddl/dml/index/rewrite/join/subquery/null/union/predicate/constant/unknown）+ 双语显示名；校验未知值 | P0a | 已做 |
| B1 | `description` 治理 | front matter schema+校验、生成器、`frontmatter.md` | published 页必填、人工书写、~≤155 字含关键词；生成器用完整值不再截断；校验器拒绝“空/默认/机器截断” | P0a | 已做 |
| B2 | 镜像配对 `localeOf` | front matter schema、`frontmatter.md`、校验 | 每页可选 `localeOf: <对应语言页 id>`；校验成对存在且非自指 | P0a | 已做 |
| B3 | 导航=发布（draft 不进生产） | docs.json 生成/维护约定、校验 | `status: published/approved` 才入导航；draft/review 仅本地/分支 | P0a | 已做（`validate-nav` 子命令；接入 CI 待发布批） |
| B4 | 实体键统一 | front matter + RAG metadata | 页面字段与 RAG 元数据同键（product/version/database/documentType/featureId/language）→ 页即自描述 | P1 | 待实施 |
| B5 | 检索别名（可选） | front matter | `keywords`/`aliases`（规则英文名↔中文名检索桥） | P1 | 可选项 |
| C1 | 门禁/CI 路径修正 | `.github/workflows/validate.yml`、`gate.py`（rule_reference_path） | no-diff 路径与 generated 语言树一致；required doc 指向默认语言页 | P0a | 已做 |
| C2 | 重复/变体治理 | 迁移批次（PLACEMENT C） | 全站无 `-polish`、无同主题多版本（SEO/RAG 大敌） | P0a 起 | 待实施 |
| C3 | 图片 alt / 缺图 | 内容管线、style-guide | 有图必有语义 alt；缺图 TODO+draft，不进发布 | P1 | 待实施 |
| D1 | 术语唯一 + Glossary | `terminology.md`、内容批次 | 一概念一词；关键实体建术语/词典页，供检索与 RAG 实体链 | P1 | 待实施 |
| D2 | SEO/LLM 写作规则入 style-guide | `style-guide.md` | description/title 写作、证据与 status 用于 AI 可信度、代码块语言、单页单意图锚点 | P0a | 已做 |

## 3. 产品决策（2026-09-04 已拍板）

| # | 项 | 决策 |
|---|---|---|
| A1 | 规则页 id 规范 | 默认语言（zh）页 id 中性（去 `zh-` 前缀）；镜像页 `en-` 前缀；规则 id 优先复用产品注册表、无则 slug |
| A2 | 语言正文结构 | `content:{zh,en}` 一步到位（替换「英文根 + 可选 zh 块」）；旧 yaml 字段读入时映射兼容 |
| A3 | `category` 受控词表 | 定稿 `ddl/dml/index/rewrite/join/subquery/null/union/predicate/constant/unknown`；双语显示名随生成器维护 |
| B3 | `draft` 与导航 | `published/approved` 才入 `docs.json`；draft/review 不进生产、不被抓取 |
| C1 | 门禁「必需文档」语言基准 | 以默认语言（zh）页为准；no-diff 路径对齐 `docs/reference docs/en/reference` |

### 仍待决策

- **B5 术语/别名优先级**：首批只做规则英文名↔中文名检索别名，还是全站术语统一（P1，不阻塞 P0.1）。
- **D 表低置信规则（~11 条）** 与 **Rule ID 注册表映射（锁 2）**：随批滚动、逐条/逐项确认。
- 其余 P1 项（B4 实体键、C2 重复治理、C3 图片、D1 Glossary）按 §4 顺序随批实施，无额外决策。

## 4. 建议落地顺序

- **P0a（先做，再铺 251 规则）**：A1/C1（语言语义与路径对齐，改动小、即时见效）→ B1+B3（description 与发布=导航）→ A3（category 词表）→ 更新 `frontmatter.md`/`style-guide.md`。
- **P1（随批量）**：A2（内容结构解耦，含存量 yaml 迁移脚本）、B2 localeOf 校验、B4/B5、D1/D2 执行。
- 文档侧本批已同步：`frontmatter.md`、`style-guide.md`、`MIGRATION-PLAYBOOK.md`、`MIGRATION-PLAN.md`（见各文件新内容）。
