# PawSQL Documentation (Mintlify) — v2 站点源

PawSQL 官方文档站点的 **Mintlify 内容仓库**（新站点，独立于旧 `website/` 试运行实现）。

> 依据《PawSQL Documentation Platform 技术设计说明书（Mintlify 版）v1.1》。
> 架构原则：**Mintlify 负责文档的呈现、编辑协作与发布；PawSQL 自建层负责产品知识建模（Metadata）、结构化 Reference 自动生成与质量闸门。**

## 仓库布局

```text
docs/                  Mintlify 内容根（含 docs.json）
  docs.json            Mintlify 站点配置：多语言（默认中文 / en 副语言）、导航 / OpenAPI
  index.mdx            中文首页（/）
  getting-started|user-guide|reference|openapi    中文默认内容（路由 /…）
  en/                  英文副语言树（/en/…：getting-started|products|user-guide|databases|reference|faq|tutorials|release-notes|blog）
metadata/              PawSQL 产品知识层（Feature / Rule / Database / Config / Mapping / Policy）
schemas/               JSON Schema（由 tools 中 pydantic 模型导出）
tools/                 Python 生成器与校验器（后续可抽为 pawsql-doc-agent）
```

站点以**中文为默认语言**：`docs.json` 的 `navigation.languages` 中 **zh** 为默认（内容根 `/`，中文优先），**en** 为副语言（`docs/en/`，路由 `/en/…`）。

## 本地预览

```bash
cd docs
npx mintlify dev          # 打开 http://localhost:3000
```

> Mintlify 连接 / 发布到新站点需要 Mintlify 账号与仓库授权，另行配置（内容根目录设为 `docs/`）。

## 元数据驱动的内容生成

Rule / Database / Config 的结构化 Reference **由 Metadata 自动生成**，不要手改 `docs/reference/**`（中文默认树）与 `docs/en/reference/**`（英文）下生成文件（改元数据后重建）。

Rule Metadata 支持双语：根字段为中性事实（id/category/severity/database/版本），语言正文收敛于 `content: { en:{}, zh:{} }`（每语言可带 `summary` 作 front-matter description）。`build-references` 依 `content.zh` 在默认树生成中文页 `docs/reference/...`，依 `content.en` 在副语言树生成英文页 `docs/en/reference/...`（双输出，两页互写 `localeOf`）。旧式“英文根 + `zh:` 块”yaml 仍兼容（读入时自动映射）。P0 规则批量先用 `ingest-rules` 从 vault `规则文档/` 与 `tools/data/rules_manifest.tsv`（源自 PLACEMENT §D 初判）生成骨架，人工/产品核对后补齐英文正文再入仓。

```bash
cd tools
uv run python -m pawsql_doc build-references        # 全量重建 Reference
uv run python -m pawsql_doc generate-rule --rule redundant-index
uv run python -m pawsql_doc generate-db   --database postgresql
uv run python -m pawsql_doc generate-config --config explain.timeout
uv run python -m pawsql_doc ingest-rules --vault <规则文档目录> --id <rid>   # P0 规则批量：读 vault 规则文档→骨架 yaml（默认 dry-run 打印）
```

## 校验

```bash
uv run python -m pawsql_doc validate-metadata     # metadata/** 与 docs 引用一致性
uv run python -m pawsql_doc validate-frontmatter  # docs/**/*.md(x) front matter（description 治理 + localeOf 配对）
uv run python -m pawsql_doc validate-nav          # docs.json 引用页须 published/approved（导航=发布）
uv run python -m pawsql_doc drift                 # 必选文档缺失检测（有缺失则 exit 1）
uv run python -m pawsql_doc coverage              # 分项文档覆盖率
uv run python -m pawsql_doc gate                  # Release Gate：必需覆盖率 <100% 时 exit 1
uv run pytest -q                                  # 单元测试
```

## 提交约定

改元数据/内容 → 运行 `build-references` 并连同生成的 Reference 一起提交。
发布前 `gate` 必须 PASS（各分项 required coverage = 100%）。
GitHub Actions `.github/workflows/validate.yml` 会在 push/PR 时校验上述一致性与测试。

## 内容迁移（Obsidian vault → 本站）

把 `pawsql-docs-new`（Obsidian 内容库）按《技术设计说明书》转换为本站内容的方法论、目录映射、格式/去重/双语规则与质量闸门，见 **[MIGRATION-PLAYBOOK.md](MIGRATION-PLAYBOOK.md)**。试点（规则 ×10 + PawSQL Cloud 手册中文镜像）已按该手册完成并验证。

## 内容模型定稿

内容模型/SEO-LLM 改动的权威清单见 **[CONTENT-MODEL-CHANGES.md](CONTENT-MODEL-CHANGES.md)**（v0.2）：A1 语言 id、A2 `content:{zh,en}`、A3 `category` 受控词表、B1 `description` 治理、B2 `localeOf` 镜像、B3 导航=发布（`validate-nav`）、C1 门禁路径——均已做；P1 项（B4/B5、C2/C3、D1/D2）见文件。写作约定详见 `docs/contributing/{frontmatter,style-guide,terminology}.md`。

## 发布前（Go-live）清单

1. 内容评审：可发布页 `status` → `approved`/`published`（`draft`/`review` 仅留本地/分支）。
2. `uv run python -m pawsql_doc validate-nav` 全绿——导航只收 `published/approved` 页（B3）。
3. `uv run python -m pawsql_doc drift && uv run python -m pawsql_doc gate` 全绿；`build-references` 重建后 `git diff --exit-code` 干净。
4. 建 GitHub 远程并 push → Mintlify 连接（内容根 `docs/`）→ 发布后用线上 URL 验收（默认中文 `/` 与 `/en` 均可达、语言切换正常）。
