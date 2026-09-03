# PawSQL Documentation (Mintlify) — v2 站点源

PawSQL 官方文档站点的 **Mintlify 内容仓库**（新站点，独立于旧 `website/` 试运行实现）。

> 依据《PawSQL Documentation Platform 技术设计说明书（Mintlify 版）v1.1》。
> 架构原则：**Mintlify 负责文档的呈现、编辑协作与发布；PawSQL 自建层负责产品知识建模（Metadata）、结构化 Reference 自动生成与质量闸门。**

## 仓库布局

```text
docs.json             Mintlify 站点配置（导航 / 语言 / 版本 / API Reference）
docs/                 站点内容（含 zh/ 语言镜像）
blog/                 Blog
openapi/              OpenAPI 单一事实来源（本地文件，§11）
metadata/             PawSQL 产品知识层（Feature / Rule / Database / Config / Mapping / Policy）
schemas/              JSON Schema（由 tools 中 pydantic 模型导出）
static/               Mintlify 静态资源
tools/                Python 生成器与校验器（后续可抽为 pawsql-doc-agent）
```

## 本地预览

```bash
npx mintlify dev          # 打开 http://localhost:3000
```

> Mintlify 连接 / 发布到新站点需要 Mintlify 账号与仓库授权，另行配置。

## 元数据驱动的内容生成

Rule / Database / Config 的结构化 Reference **由 Metadata 自动生成**，不要手改 `docs/reference/**` 下生成文件（改元数据后重建）。

```bash
cd tools
uv run python -m pawsql_doc build-references        # 全量重建 Reference
uv run python -m pawsql_doc generate-rule --rule redundant-index
uv run python -m pawsql_doc generate-db   --database postgresql
uv run python -m pawsql_doc generate-config --config explain.timeout
```

## 校验

```bash
uv run python -m pawsql_doc validate-metadata     # metadata/** 与 docs 引用一致性
uv run python -m pawsql_doc validate-frontmatter  # docs/**/*.md(x) front matter
uv run pytest -q                                  # 单元测试
```

## 提交约定

改元数据/内容 → 运行 `build-references` 并连同生成的 Reference 一起提交。
GitHub Actions `.github/workflows/validate.yml` 会在 push/PR 时校验上述一致性与测试。
