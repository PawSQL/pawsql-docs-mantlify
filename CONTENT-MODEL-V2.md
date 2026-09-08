# PawSQL 内容模型 v2

实施基线：2026-09-08。本文取代旧规划中冲突的产品分类、内容类型及导航规定；现有 URL 不因分类变化而批量移动。

## 1. 产品、组件与能力

唯一产品是 `pawsql`。`engine / optimizer / auditor / advisor / patroller` 是组件或形态，不是五个独立产品。Cloud 是 `deployments: [public-cloud]`，不是产品，也不意味着另一套能力。

| 维度 | 用途 | 注册来源 |
|---|---|---|
| product | 唯一产品 PawSQL | metadata/products |
| components | 交付组件或形态 | metadata/components |
| capabilities | 审核、重写、索引推荐、性能验证、执行计划可视化、性能巡检 | metadata/capabilities |
| editions | 社区版、企业版 | metadata/taxonomies/dimensions.yaml |
| deployments | 公网、私有部署 | 同上 |
| interfaces / integrations | Web/API/CLI 与 IDE、CI/CD、MCP 等接入方式 | 同上 |
| audience | 开发、DBA、管理员、平台工程师 | 同上 |

标签的存在不证明组件具有该能力，也不证明某版本提供该集成。组件与能力的正式对应关系仍需产品依据，未知关系保持 pending。

## 2. 六类内容

| type | subtype | 内容边界 |
|---|---|---|
| explanation | 无 | 定义、原理、能力与限制；回答是什么、为什么 |
| guide | quickstart / installation / operation / integration / upgrade / migration | 可执行任务：前提、步骤、预期结果、验证、排障 |
| use-case | 无 | 用户问题、端到端流程、依赖和成功标准；链接操作指南而非复制步骤 |
| reference | rule / database / configuration / api / cli / error-code / glossary | 精确查阅项、适用条件、参数、示例、事实依据 |
| support | faq / troubleshooting | 症状、诊断、处理、验证 |
| article | blog / release-note | 有作者责任、日期、出处的文章与版本记录 |

`layout: index` 表示目录/集合，`detail` 表示正文，不增设第七种文档类型。布局与语义类型、导航位置独立。模板及必需章节见 [templates/content-types.md](templates/content-types.md)。已有正文不由脚本填空或自动标记通过。

## 3. 导航与目录

中英文各自五个 tabs：文档、用户场景、API、博客、变更日志。文档下六组：开始使用、安装与接入、使用 PawSQL、能力与原理、参考资料、帮助与排障。

不同语言组内页面可以不同，但不存在的翻译不生成假正文。目录页聚合大量规则；侧栏不平铺所有规则。`styling.eyebrows` 保持 `breadcrumbs`。

- 站点输出：`docs/`；中文位于根，英文位于 `docs/en/`。
- 中立事实及语言正文：`metadata/`；模式：`schemas/`；工具：`tools/`。
- 质量报告：`reports/content-quality.json`；迁移前清单：`reports/content-inventory.json`。
- 原始内容库 `pawsql-docs-new` 不作为本轮生成目标，只更新其技术设计说明书。

## 4. 稳定标识与双语状态

`id` 全站唯一；同一内容使用同一 `translationKey`，每种 `language` 只出现一次。保留已有 ID（包括历史 English ID），兼容 `localeOf`；路径不是内容主键。

映射优先使用 `documentId + language`，旧 `path` 暂时兼容。迁移解析出冲突时报告问题，不猜测页面关联。每种语言独立保存 editorial：status、owners、lastReviewed；生成页继承状态，生成不等于审批。翻译可记录 sourceLanguage/sourceDigest，源正文变化会触发过期报告，审核日期变化不改变正文摘要。

## 5. 结构化 Reference

规则保存 kind、分类、严重级别、适用前提、排除条件、修复方式、正常/边界示例、验证记录、事实依据。空数据库列表表示范围待核实，不能解释为全部支持。

数据库兼容性按数据库版本、组件/产品版本范围、能力和限制记录 supported/partial/unsupported/unknown。旧 claims 迁移为 unknown，不自动转为支持承诺。配置参考记录类型、默认值、范围/枚举、作用域、生效方式、重启要求、优先级、依赖与冲突。

证据需具体来源、支持的字段及审核人/时间；SQL 示例运行成功不等于产品实现已经验证。OR → UNION ALL 示例补充 NULL、重复行、分支重叠；SQLite 回归测试只证明样例的该项语义，不证明 PostgreSQL/PawSQL 兼容性或性能。

## 6. 四层门禁

1. structure：模型字段、标识、引用、语言路径；阻止结构错误。
2. existence：必需文档文件存在；不等同于内容完整。
3. completeness：章节与结构化事实是否齐全；缺项需编辑/产品补充。
4. release：审批、事实依据、翻译状态、真实 API 合约、导航可发布性。

默认 CI 阻止 structure/existence 问题并上传完整报告；发布必须显式执行 release 模式，四层都通过才输出。Mintlify 的直接 Git 发布不会自动调用 Python 发布门禁，生产连接前需把此命令接入受保护的发布流水线，不应直接把当前草稿分支设为生产源。

## 7. 生成、迁移与发布

在 `tools/` 使用虚拟环境运行：

```bash
python -m pawsql_doc --root .. migrate-content-model --dry-run
python -m pawsql_doc --root .. migrate-content-model --apply
python -m pawsql_doc --root .. export-schemas
python -m pawsql_doc --root .. build-references
python -m pawsql_doc --root .. quality --write-report
python -m pawsql_doc --root .. build-references --mode release --output /absolute/new/staging-directory
python -m pytest -q
```

release 输出必须是仓库外尚不存在的新目录；失败不创建目标。预览保留草稿，发布只复制 approved/published 页并复核筛选后的导航。

`generated-manifest.json` 记录生成物摘要；发现人工改动立即停止。已失效生成物保留并报告 stale，由维护者确认后处理，不自动删除用户文件。规则索引仅使用当前 metadata。迁移只规范化 frontmatter 与元数据，保留正文；再次执行应零改动。

兼容的 `generate-rule / generate-db / generate-config` 命令先核对目标存在，再走统一全量构建，同时更新目录和 manifest，避免单页生成破坏后续校验。生成器统一使用 LF，Git 属性固定文本换行，防止 Windows/Linux 摘要不一致。

## 8. 尚需人工完成

逐批补足规则前提、排除条件、已运行示例和证据；核定数据库/配置事实；补齐中文数据库/配置正文及英文翻译；完成各类型正文的章节映射与审核；用真实 API 合约替换占位文件。完整性检查不是语义审核、浏览器检查不是生产部署验证。锚点、动态 MDX 链接和内容事实仍需人工核验。
