# PawSQL 内容迁移执行计划（MIGRATION-PLAN）

**版本/日期：** v1 · 2026-09-04
**状态：** 草案，待产品评审后按批次开工
**输入：** `PLACEMENT.md`（文件级落位，A 迁入 143 / B 排除 104 / C 去重 13 组 / D 规则 261 初判）、`MIGRATION-PLAYBOOK.md`（方法论）、`docs/docs.json`（Mintlify 多语言 zh 默认 + en）
**位置约定：** 仓库根=`pawsql-docs-v2`（含 `metadata/`、`tools/`）；站点内容根=`docs/`（含 `docs.json`）。本计划中所有目标路径均为**相对仓库根**；页面路由相对内容根 `docs/`（中文默认页无 `en/` 前缀，英文镜像页带 `en/`）。

---

## 1. 目标与原则

1. 把 vault 内容按 PLACEMENT 落位到 v2，语言按 `zh 默认树 ↔ docs/en 镜像`（规则类 metadata 双语双输出）。
2. **源 vault 只读**：任何迁移都从 vault `复制/整理`，绝不移动源文件（保留 Evidence）。
3. **结构化 Reference 一律 metadata 驱动**：只写 `metadata/**`，用 `build-references` 生成 `docs/reference/**`（zh 默认）与 `docs/en/reference/**`（en 镜像），生成页与元数据**同批提交**。
4. **批次小步、闸门必过**：每批 ≤ ~30 个文件/规则；验收 = 下方「质量闸门」全绿 + PLACEMENT 行状态更新。
5. **产品确认是硬依赖**：未过确认锁的内容不进入自动批（见 §6）。
6. 人工内容（手册/Blog/FAQ）走 `copy 整理`，遵循 PLAYBOOK §4-§7；不确定事实 `draft` + `TODO`，不虚构。

## 2. 执行协议（每个批次通用）

1. **选批**：从 PLACEMENT 按 §4 顺序取该批 A/C/D 行，标注 `批次号` 到 PLACEMENT（新增“批次/状态”列，落地时维护）。
2. **（规则类）写元数据**：`metadata/rules/{audit|optimizer}/<id>.yaml`，根字段=中性事实（id/category/severity/database/版本）、`content.en/zh`=语言正文、id/category 按 PLAYBOOK §8 与 D 初判核对；不确定条目标 `draft` 注释。
3. **（手册类）整理落位**：目标页 front matter（type/product/status/tags/description）+ 清洗（去版权/TOC/页脚）+ 图片处理（`docs/static/<page>/`，断图 `TODO(截图待补)`）+ 代码块语言。
4. **重建**：`cd tools && uv run python -m pawsql_doc --root .. build-references`（或 venv python）。
5. **闸门**（§3 命令全跑，全绿才提交）。
6. **提交**：规则=元数据 + 生成页同一 commit；手册=页面 + `docs.json` 导航改动同一 commit；绝不混合无关内容。仓库存在外部自动提交时，人工 commit 可选，以磁盘内容为准但确保生成页已落盘。
7. **登记**：更新 PLACEMENT 行状态（`migrated/date/batch`）与 PLAYBOOK 附录 B 进度表。

## 3. 质量闸门（每批/每提交必须全绿）

```bash
cd tools
.venv/Scripts/python.exe -m pawsql_doc --root .. validate-metadata      # PASS
.venv/Scripts/python.exe -m pawsql_doc --root .. validate-frontmatter   # PASS
.venv/Scripts/python.exe -m pawsql_doc --root .. build-references       # 生成 0 diff
git diff --exit-code -- docs/reference docs/en/reference docs/en/databases  # 无漂移
.venv/Scripts/python.exe -m pawsql_doc --root .. drift && ... gate      # coverage 100%
.venv/Scripts/python.exe -m pytest -q                                   # 全绿
```

（uv 可用时以 `uv run python -m pawsql_doc --root .. <cmd>` 替代 venv 直接调用。）

## 4. 批次计划（顺序执行；规则 P0 优先、量最大）

> 规则总数 261，试点已迁 10（audit 6 + optimizer 4）。D 初判为**草案**，每子批开工前须对 D 行完成一轮人工/产品校对（§6 锁 1/2）。

| 批次 | 内容（PLACEMENT 范围） | 产物 | 解锁/依赖 | 备注 |
|---|---|---|---|---|
| **P0.0 基线** | 全量 D 分类校对 + Rule ID 注册表 | D 表定稿、首批规则清单 | 锁 1、2 | 先定 audit 分类字典 |
| **P0.1 audit 组 A** | D 中 `audit` 约 25-30 条（对象设计/DDL：命名、类型、约束、阈值） | metadata/rules/audit + en/zh 参考页 | P0.0 | **试运行**，校准吞吐与质量 |
| P0.2 audit 组 B | D `audit` 数据操作/DML（INSERT/UPDATE/DELETE 检查） | 同上 | P0.1 验收 | |
| P0.3 audit 组 C | D `audit` 性能/索引失效（表达式、失效、重复、倾斜） | 同上 | | 与 optimizer 索引推荐边界核对 |
| P0.4 optimizer 组 A | D `optimizer` 子查询/重写（EXISTS/IN/COUNT/去重/折叠） | metadata/rules/optimizer + en/zh 页 | | |
| P0.5 optimizer 组 B | D `optimizer` UNION/Lateral/谓词下推/排序/常量优化 | 同上 | | |
| P0.6 db/config Reference | 补齐 `metadata/databases/*.yaml`（版本/能力）与 `metadata/configs` | 兼容矩阵 `docs/reference/compatibility`（zh）+ `docs/en/reference/compatibility`、各库 `docs/databases/<db>/index.md`（zh）+ `docs/en/databases/<db>/index.md` | 产品锁 5（DB 快照） | 生成页由工具产出（当前 db/config 仅 en 树，P0.6 补 zh 双输出） |
| P0.7 Mapping/Feature | 为已迁规则补 feature+mapping 数据 | metadata/features|mappings | | Gate 消费，先数据后门 |
| P1.1 Cloud | PLACEMENT A：Cloud 中文默认树 + Community 落地页 + Enterprise/Installation 安装(zh/en) | `docs/products/cloud`（zh）、`docs/en/products/community`、installation 页 | 锁 5（DB/套餐快照） | 已迁 3 页 zh 默认树为样板 |
| P1.2 Engine 安装 | `20-engine/install/*`（Engine/Linux/Docker） | `docs/user-guide/installation/*`（zh）+ `docs/en/user-guide/installation/*` | | 拆页按 PLAYBOOK |
| P1.3 Advisor/JetBrains | `40-audit/manuals/Advisor*` | `docs/products/advisor`（zh）+`docs/en/products/advisor` | 锁 3（Advisor 语义） | |
| P1.4 Audit 平台/巡检 | `PawSQL审核平台用户手册`、`PawSQL性能巡检用户手册` | `docs/products/audit|patroller` zh/en | | |
| P1.5 集成 | `50-integration` VSCode/MCP/GitHub/GitLab（含图片） | `docs/products/{vscode,mcp}`、user-guide、`docs/static` | | mcp 三处合一（C） |
| P1.6 API 定稿 | `20-engine/api`+`50-integration/api` 版本仲裁 | `openapi/*` 或 `docs/reference/api` | 锁 6 | 仅现行 1 份 |
| P2.1 Release Notes | newsletters 月度/更新日志 | `docs/release-notes/` en/zh | | 拆 en/zh、去模板占位 |
| P2.2 Blog 技术 | `20-engine/internals`、case-studies | `docs/blog/engineering/` | | 去营销腔/去内部 |
| P2.3 Blog 产品/案例 | comparisons/reviews/GitLab 营销/99 金融案例/评测 | `docs/blog/product/`、`case-study` | 锁 7（客户案例合规） | 一律含 -polish 去重（C） |
| P2.4 FAQ/定位 | `10-product/about`（FAQ、用户场景）、FAQ | `docs/faq`/`docs/products` | | 视频脚本/Github 主页已排除（B） |
| P2.5 数据库接入 | `70-content/vendor-guides` + 支持矩阵 | `docs/databases/<db>/`、`docs/user-guide/optimization` | | MySQL.md vs MySQL数据库.md 再并 1 份 |
| P2.6 兼容/迁移 | `60-migration` | `docs/reference/compatibility` | 锁 4（Ora2pg） | |
| P3 RAG/MCP | 站点发布后 | 接入层（另立项目） | 站点上线 | 本计划外 |

## 5. 每类内容转换配方（指针）

- 规则：PLAYBOOK §8 + D 表 + 试点 10 条 yaml 样板（`metadata/rules/*/`）。
- 手册/产品/Blog/FAQ：PLAYBOOK §4（格式）、§6（优化/Guardrail）、§7（语言）、§9（去重）。
- 图片：PLAYBOOK §5；目标 `docs/static/<页面>/`；缺图 `TODO(截图待补)` + `draft`。
- 导航：每批把新页加入 `docs/docs.json` 对应 language 的 group（zh 默认无前缀 / en 前缀）；规则页按族加进 Reference 组（量大多时先加 index/组，不放全量以防导航过长——P0 各子批完成后整理一次）。

## 6. 产品确认锁（阻塞清单；解锁后才跑相关批）

| # | 待确认 | 阻塞批次 |
|---|---|---|
| 1 | 规则分类短词 + audit/optimizer 归属字典（D 校对） | P0 全部 |
| 2 | Rule ID 注册表映射（对齐 Rules.md/线上 RuleXxx；试点用 slug 占位） | P0 全部 |
| 3 | “PawSQL Advisor”语义（IntelliJ 插件 vs 审核能力）→ products/{advisor,jetbrains} | P1.3、P1.5 |
| 4 | Ora2PgSQL 是否仍为支持产品 | P2.6 |
| 5 | 支持数据库/版本快照（metadata/databases 权威） | P0.6、P1.1 |
| 6 | 审核平台 API 现行版本定稿 | P1.6 |
| 7 | 客户案例/blog 可发布范围（金融案例含数字） | P2.3 |
| 8 | legal 去重定稿（site legal，不入导航） | 排程（不依赖主链） |

## 7. 风险与依赖

- **规则量最大（251 条）**：靠子批 + 生成器分摊；已实现 `tools` 的 `ingest-rules`（读 vault `规则文档/` + `tools/data/rules_manifest.tsv`（源自 PLACEMENT §D）→ 骨架 yaml；dry-run 默认、`--out` 落盘供评审），把“读文档 → 结构化骨架”自动化（P0.0.5）。
- **翻译补齐**：zh 默认树为站点默认语言，en 镜像先入 `docs/en`；中文缺失页面列为翻译队列（AI draft + 产品复核），不做自动承诺。
- **外部自动提交**：本仓库由外部进程自动 commit；批处理时以磁盘内容为准，避免中途误提交半成品（先建批内全部文件再跑闸门）。
- **图片缺口**：大量截图原始文件缺失（Typora 绝对路径），以 TODO 标记推进，不阻塞正文。
- **Mintlify 预览/发布**需账号授权，本地 `cd docs && npx mintlify dev` 验证导航与页面，不属自动闸门。

## 8. 进度追踪

- PLACEMENT.md：行尾加 `| 批次 | 状态 |` 列，逐批更新（`todo→in-progress→migrated`）。
- MIGRATION-PLAYBOOK.md 附录 B：登记每批日期/结果/遗留。
- 本计划随执行回填实际子批范围与闸门截图。

## 9. 首个执行批（P0.1 建议）

在 P0.0 定稿 D 与 audit 分类字典后，取 **25 条以内**、`类别` 首段=“对象设计/数据操作（命名/类型/约束/阈值）”的 audit 规则：逐条写双语 yaml → build-references → 闸门 → 提交 → 回填 PLACEMENT。目标：校准“每规则单批质量与吞吐”，跑通后按 §4 顺序滚动。
