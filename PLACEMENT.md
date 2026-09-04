# PawSQL 内容放置清单（PLACEMENT · 初稿）

> 依据《技术设计说明书 v1.1》与 MIGRATION-PLAYBOOK §2 目录映射；覆盖 vault 全部可迁移 `.md`。
> 状态：**draft 初稿，供评审**。行级目标为目录级；页面级 slug/拆分在逐批执行时确定。
> 语言约定：中文为默认树（`docs/**`），英文为镜像（`docs/en/**`）。`en`=英文源→`docs/en/**`；`zh`/`zh(英文待补)`=中文源→默认树 `docs/**`（英文后补）；规则类见 D 双语双输出（zh→`docs/reference`，en→`docs/en/reference`）。

## C. 去重 / 归并（同一内容保留一份）

| 保留（keeper） | 归档/不迁（归并到 keeper） |
|---|---|
| `30-cloud/guides/PawSQL Cloud使用手册.md` | `30-cloud/guides/PawSQL Cloud实践指南.md`, `40-audit/manuals/PawSQL巡检平台实践指南.md` |
| `50-integration/devops/pawsql-gitlab/PawSQL × GitLab ：提交代码即自动审核，SQL 质量零漏洞.md` | `50-integration/devops/pawsql-gitlab/PawSQL × GitLab ：提交代码即自动审核，SQL 质量零漏洞-polish.md` |
| `50-integration/mcp/pawsql-mcp-docs/mcp-docs-zh/pawsql-mcp-zh.md` | `10-product/PawSQL MCP.md`, `50-integration/api/pawsql mcp.md` |
| `70-content/blog/How to leverage MySQL Optimizer with PawSQL.md` | `70-content/blog/How to leverage MySQL Optimizer with PawSQL-polish.md` |
| `70-content/blog/SQL查询中关于NULL的陷阱.md` | `70-content/blog/SQL查询中关于NULL的陷阱_en.md`, `70-content/blog/关于null的陷阱.md` |
| `70-content/blog/大模型在处理SQL优化等精确性问题的局限.md` | `70-content/blog/大模型在处理SQLSQL优化等精确性问题上的局限性.md`, `70-content/blog/大模型局限.md` |
| `70-content/blog/突破 MySQL 性能瓶颈：PawSQL 补齐优化器的短板.md` | `70-content/blog/突破 MySQL 性能瓶颈：PawSQL 补齐优化器的短板-polish.md` |
| `70-content/vendor-guides/Workload-Documentation-For-Mapper-File-Type.md` | `10-product/getting-started/quick-start-cloud/Quick Start with PawSQL Cloud.md`, `70-content/vendor-guides/Mapper文件形式录入待优化索引3.md` |
| `99-待归类/2026年Top 5 SQL审核工具深度测评：选对工具，告别“问题SQL”上生产.md` | `99-待归类/2026年Top 5 SQL审核工具深度测评：选对工具，告别“问题SQL”上生产-polish.md` |
| `99-待归类/BLOG-AUDIT.md` | `99-待归类/BLOG-AUDIT-polish.md` |
| `99-待归类/BLOG-OVERVIEW.md` | `99-待归类/BLOG-OVERVIEW-polish.md` |
| `99-待归类/金融生产环境实战：PawSQL驱动TDSQL-MySQL慢查询优化，召回率76.6%，近7成自动化优化.md` | `99-待归类/金融生产环境实战：PawSQL驱动TDSQL-MySQL慢查询优化，召回率76.6%，近7成自动化优化-polish.md` |
| `99-待归类/金融生产环境实战：PawSQL驱动openGauss慢查询优化，正确率100%，释放近7成人力成本.md` | `99-待归类/金融生产环境实战：PawSQL驱动openGauss慢查询优化，正确率100%，释放近7成人力成本-polish.md` |

## B. 排除 / 不迁（目录与文件）

| 源 | 原因 |
|---|---|
| `10-product/about/Github主页.md` | GitHub README 草稿，另属站点主页素材 |
| `10-product/about/一分钟团队和项目介绍视频脚本.md` | 内部宣传视频脚本，不迁 |
| `20-engine/api/PawSQL Engine接口文档V1.0.md` | API 版本栈/多视角，待产品定稿现行 1 份后并入 openapi/ 或 docs/reference/api/；详见 C/去重 |
| `20-engine/api/PawSQL Engine接口文档V2.0.md` | API 版本栈/多视角，待产品定稿现行 1 份后并入 openapi/ 或 docs/reference/api/；详见 C/去重 |
| `20-engine/api/PawSQL Engine接口文檔V3.0.md` | API 版本栈/多视角，待产品定稿现行 1 份后并入 openapi/ 或 docs/reference/api/；详见 C/去重 |
| `20-engine/api/SQL 审核平台接口文档-update.md` | API 版本栈/多视角，待产品定稿现行 1 份后并入 openapi/ 或 docs/reference/api/；详见 C/去重 |
| `20-engine/api/pawsql-api-接口文档.md` | API 版本栈/多视角，待产品定稿现行 1 份后并入 openapi/ 或 docs/reference/api/；详见 C/去重 |
| `20-engine/indexrec/索引失效.md` | 疑似规则清单；若为规则转 规则文档 体系（audit/index），不单独迁 |
| `20-engine/internals/20240118.md` | 内部笔记 |
| `20-engine/rules/Rules.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-ddl/DDL Rules - en.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-ddl/DDL Rules.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/DML Rules.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/DML audit Rules.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/OrderByRandomFunctionWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleAddOrderByNullRewrite.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleCountDistinctMultiColumnsWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleCrossJoinWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleDiffOrderingSpecTypeWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleInSubqueryRewrite.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleNPERewrite.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleNaturalJoinWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleStraightJoinWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/en/RuleUpDeleteWithLimitWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleAddOrderByNullRewrite.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleCountDistinctMultiColumnsWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleCrossJoinWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleDiffOrderingSpecTypeWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleNPERewrite.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleNaturalJoinWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleStraightJoinWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/RuleUpDeleteWithLimitWarning.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/避免在查询中使用SELECT.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/避免采用随机函数进行排序-mysql.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/audit-dml/zh/避免采用随机函数进行排序.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/ccdc-mysql-lv1.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/ccdc-mysql.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/rewrite/en/Count(not null column) optimization.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/DiffDataTypeInPredicateRewrite.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/FuncWithColumnInPredicateRewrite.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/Join Elimination.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/Optimization Rules Overview.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/Optimizing Window Function Queries with PawSQL A Case Study in Index Recommendation.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/OrConditionsRewrite.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/Outer Join Conversion.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/PawSQL Pioneering Correlated Subquery Optimization.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/ProjectionPushDownRewrite.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/QueryFoldingRewrite.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/en/SATTCRewrite.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/COUNT标量子查询重写优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/DiffDataTypeInPredicateRewrite-cn.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/EXISTS子查询优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/HAVING条件下推到WHERE子句.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/IN子查询优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/Limit子句下推优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/MAXMIN子查询重写优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/OR连接的条件重写为UNION.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/Rewrite Rules.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/SATTC重写优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/分组字段重排序优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/外连接优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/子查询重写.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/小表建议使用复制表.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/投影下推.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/投影下推的典型应用场景.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/排序分组优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/查询折叠(Query Folding).md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/标识子查询优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/标量子查询优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/派生表 → LATERAL JOIN，12 秒变 0.2 秒-polish.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/派生表 → LATERAL JOIN，12 秒变 0.2 秒.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/深分页优化.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/相关子查询接关联.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/表关联LIMIT分页下推.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/表连接消除.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/计算导致SQL失效.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/计算导致索引失效.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/过滤条件下推优化（Filter Predicate Pushdown）.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/避免在DELETE语句中使用LIMIT.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/🚀 PawSQL 投影下推优化功能大升级！.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/rewrite/zh/🚀 优化SQL查询：掌握相关标量子查询的艺术.md` | 重写规则历史正文；规范源=规则文档，仅作对照，不迁正文 |
| `20-engine/rules/审查规则说明文档（简略版）.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/新增规则.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/规则说明文档（简略版）.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `20-engine/rules/重写优化算法列表.md` | 审核规则历史正文/内部草稿；规范源=规则文档，仅作对照或内部，不迁正文 |
| `30-cloud/PawSQL社区版.md` | CE vs Enterprise 功能差距设计稿（内部） |
| `30-cloud/legal/PRIVACY POLICY.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/PawSQL Community Edition License Agreement.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/PawSQL 社区版软件许可协议.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/Privacy Policy for PawSQL bt.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/Refund Policy.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/TERMS OF SERVICE.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/Terms of Service for PawSQL new.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/Terms of Service for PawSQL.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/Terms of Service-pg.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/Terms of service-bt.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/privacy notice pg.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `30-cloud/legal/privacy notice.md` | legal 待法务去重定稿 → 独立 site legal，不入文档导航 |
| `40-audit/SQL 审核优化系统高阶设计文档.md` | 内部设计（与 design/ 下重复） |
| `40-audit/design/PawSQL审核引擎的设计目标.md` | 内部设计 |
| `40-audit/design/PawSQL审核引擎设计.md` | 内部设计 |
| `40-audit/design/SQL审核优化系统高阶设计文档.md` | 内部设计 |
| `40-audit/design/SQL质量审核系统建设方案-新数.md` | 内部设计 |
| `40-audit/design/如何设计一个优秀的SQL审核工具.md` | 内部设计 |

## A. 迁入（目标=目录级）

| 源 | 目标目录 | 语言 | 处理/备注 |
|---|---|---|---|
| `10-product/about/About PawSQL.md` | `docs/en/products/` | en | 产品总览(英文) |
| `10-product/about/PawSQL 常见问题解答.md` | `docs/faq/` | zh(英文待补) | FAQ |
| `10-product/about/PawSQL的用户是谁？用户场景是什么？PawSQL为用户解决什么问题？.md` | `docs/products/` | zh(英文待补) | 定位页/用户场景；或转 blog(product) |
| `10-product/about/关于PawSQL.md` | `docs/products/` | zh(英文待补) | 产品总览(中文) |
| `20-engine/api/pawsql-api.md` | `docs/reference/api/` | zh(英文待补) | 现行 API 文档（暂定，产品复核） |
| `20-engine/indexrec/索引失效？别慌，PawSQL教你14招让数据库性能起飞.md` | `docs/blog/engineering/` | zh | 技术/营销文章 |
| `20-engine/indexrec/释放数据库潜力PawSQL,索引失效的终结者 🚀.md` | `docs/blog/engineering/` | zh | 技术/营销文章 |
| `20-engine/install/PawSQL Engine安装手册(Linux).md` | `docs/user-guide/installation/` | zh(英文待补) | 可拆分 Engine/Linux/Docker 三页 |
| `20-engine/install/PawSQL Engine安装手册.md` | `docs/user-guide/installation/` | zh(英文待补) | 可拆分 Engine/Linux/Docker 三页 |
| `20-engine/install/pawsql-docker-images安装说明.md` | `docs/user-guide/installation/` | zh(英文待补) | 可拆分 Engine/Linux/Docker 三页 |
| `20-engine/internals/DELETE还是TRUNCATE？一张图秒懂清空表的正确姿势！.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/EXISTS 能自动转 JOIN 吗？各数据库优化器内幕.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/EXISTS和COUNT子查询怎么选？一招提升子查询性能.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/Lateral查询详解：概念、适用场景与普通JOIN的区别.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/MySQL vs. PostgreSQL.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/PawSQL 重写优化技术在常用数据库上的支持情况.md` | `docs/reference/compatibility/` | zh(英文待补) | 重写支持矩阵 → 兼容性矩阵素材 |
| `20-engine/internals/PawSQL优化器：理解Lateral Join重写优化.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/PawSQL高级SQL优化  OR条件重写为UNION算法更新.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/SQL优化案例分享：PawSQL的EXISTS到JOIN重写优化解析.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/SQL优化算法分享  OR转化为UNION.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/case-studies/知乎SQL优化挑战赛-题目1解析.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/case-studies/知乎SQL优化挑战赛-题目2解析.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/case-studies/知乎SQL优化挑战赛-题目3解析.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/执行计划的节点类型.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/技术分享：谓词下推的实现逻辑与场景解析.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/深入理解PawSQL索引优化算法：让失效的索引重新生效.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `20-engine/internals/重写优化总结.md` | `docs/blog/engineering/` | zh | 技术文章 |
| `30-cloud/PawSQL-CE.md` | `docs/products/community/` | zh(英文待补) | 社区版落地页（中文；定价并入产品页，产品确认） |
| `30-cloud/guides/PawSQL Cloud.md` | `docs/en/products/cloud/` | en | Cloud 概述(英文) |
| `30-cloud/guides/PawSQL Cloud使用手册.md` | `docs/user-guide/cloud/` | zh(英文待补) | 已试点拆 3 页 |
| `30-cloud/install/PawSQL Enterprise安装手册.md` | `docs/user-guide/installation/enterprise/` | zh(英文待补) | 企业版自托管安装 |
| `30-cloud/install/PawSQL Installation.md` | `docs/en/user-guide/installation/` | en | Docker 部署(英文) |
| `30-cloud/pawsql-ce-en.md` | `docs/en/products/community/` | en | Community Edition 落地页(en) |
| `40-audit/manuals/PawSQL Advisor User Manual.md` | `docs/en/products/advisor/` | en | Advisor 英文手册；en/zh 镜像 |
| `40-audit/manuals/PawSQL Advisor使用手册.md` | `docs/products/advisor/` | zh(英文待补) | Advisor/JetBrains 语义待产品确认 |
| `40-audit/manuals/PawSQL审核平台用户手册.md` | `docs/products/audit/` | zh(英文待补) | 审核平台 |
| `40-audit/manuals/PawSQL性能巡检用户手册.md` | `docs/products/patroller/` | zh(英文待补) | 性能巡检 |
| `40-audit/reviews/SQLE、SQM和PawSQL：深度评测企业级SQL审核平台.md` | `docs/blog/product/` | zh | 竞品评测→blog(product) |
| `40-audit/reviews/SQL审核工具评测报告.md` | `docs/blog/product/` | zh | 竞品评测→blog(product) |
| `40-audit/reviews/企业级SQL审核工具的新玩家.md` | `docs/blog/product/` | zh | 竞品评测→blog(product) |
| `40-audit/standards/PawSQL审核规则体系.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/SQL开发规范.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/SQL语句的结构可以从以下几个维度进行分类.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/SQL质量标准.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/SQL质量标准、开发规范和审核规则关系.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/SQL质量管控流程.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/SQL质量管理的框架.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/如何衡量一个SQL规则集的优劣.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `40-audit/standards/精简但完备的审核规则集.md` | `docs/reference/audit-rules/` | zh(英文待补) | 规则体系/方法概念页；与 metadata/rules 对账后纳入 |
| `50-integration/api/PawSQL 审核平台接口文档.md` | `docs/reference/api/` | zh(英文待补) | 审核平台 API（与 20-engine/api 定稿合并） |
| `50-integration/api/SQL审核平台系统间接口规范.md` | `docs/reference/api/` | zh(英文待补) | 系统间接口规范（与上合并，产品复核） |
| `50-integration/devops/pawsql-github/PawSQL-DevOps.md` | `docs/en/user-guide/` | en | GitHub CI 集成教程 |
| `50-integration/devops/pawsql-gitlab/PawSQL × GitLab ：提交代码即自动审核，SQL 质量零漏洞.md` | `docs/blog/product/` | zh | GitLab 营销稿 |
| `50-integration/devops/pawsql-gitlab/gitlab-integration-tutorial.md` | `docs/user-guide/` | zh(英文待补) | GitLab 集成教程（配图走 static/） |
| `50-integration/mcp/pawsql-mcp-docs/mcp-docs-zh/pawsql-mcp-zh.md` | `docs/products/mcp/` | zh(英文待补) | MCP 手册(zh)，canonical |
| `50-integration/mcp/pawsql-mcp-docs/mcp-docs/pawsql-mcp-en.md` | `docs/en/products/mcp/` | en | MCP 手册(en) |
| `50-integration/plugins/PawSQL Advisor.md` | `docs/blog/product/` | zh | 插件营销稿(与 Advisor 手册去重) |
| `50-integration/plugins/PawSQL插件说明文档.md` | `docs/products/vscode/` | zh(英文待补) | VSCode 插件 |
| `60-migration/oracle/Ora2PgSQL使用手册.md` | `docs/reference/cli/` | zh(英文待补) | Ora2PgSQL CLI 手册（产品是否仍支持→决定迁/排） |
| `60-migration/oracle/Oracle vs. PostgreSQL - Data Types.md` | `docs/reference/compatibility/` | zh(英文待补) | 方言/数据类型映射矩阵素材 |
| `60-migration/oracle/Oracle到PostgreSQL的SQL迁移.md` | `docs/reference/compatibility/` | zh(英文待补) | 方言/数据类型映射矩阵素材 |
| `60-migration/oracle/Oracle到openGauss的SQL迁移.md` | `docs/reference/compatibility/` | zh(英文待补) | 方言/数据类型映射矩阵素材 |
| `70-content/blog/How to leverage MySQL Optimizer with PawSQL.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/How to leverage PostgreSQL Optimizer with PawSQL.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/Index Advisor Engine.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/MySQL 优化器搞不定的坑，PawSQL 怎么填.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/MySQL的执行计划可视化.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/Optimizing TPCH Queries with PawSQL.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL Advisor.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL Explain.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL 在 T‑SQL 存储过程审核与优化上的突破.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL 补齐 Oracle 优化器短板：最强优化器的精准盲区.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL 补齐 PostgreSQL 优化器短板：PG17 之后，盲区在哪里.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL的索引推荐,帮助优化窗口函数的查询性能.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL索引引擎.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/PawSQL针对TPCH的优化评测.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/Plan Visualization for MySQL.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/SQL查询中关于NULL的陷阱.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/Some clues of PawSQL rewrite engine.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/分区表索引.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/大模型在处理SQL优化等精确性问题的局限.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/如何创建高效的索引.md` | `docs/blog/engineering/` | zh | 中文版 |
| `70-content/blog/如何创建高效的索引_en.md` | `docs/en/blog/engineering/` | en | 英文版 |
| `70-content/blog/存储过程审核.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/执行计划可视化.md` | `docs/blog/engineering/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/拆解 MySQL 优化盲区：为什么数据库自带重写还需要 PawSQL.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/数据库索引的类型.md` | `docs/blog/engineering/` | zh | 中文版 |
| `70-content/blog/数据库索引的类型_en.md` | `docs/en/blog/engineering/` | en | 英文版 |
| `70-content/blog/突破 MySQL 性能瓶颈：PawSQL 补齐优化器的短板.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/blog/语之暗面的kimi大模型代码分析评测.md` | `docs/blog/product/` | zh | 70-content blog（主题细分待定稿） |
| `70-content/comparisons/DBbrain的鸡肋之殇和PawSQL的强势登场.md` | `docs/blog/product/` | zh | 竞品对比 |
| `70-content/comparisons/EverSQL向左，PawSQL向右.md` | `docs/blog/product/` | zh | 竞品对比 |
| `70-content/comparisons/EverSQL向左，PawSQL向右2.md` | `docs/blog/product/` | zh | 竞品对比 |
| `70-content/comparisons/EverSQL被Aiven收购是个好的归宿吗？.md` | `docs/blog/product/` | zh | 竞品对比 |
| `70-content/comparisons/vs EverSQL.md` | `docs/blog/product/` | zh | 竞品对比 |
| `70-content/newsletters/Digest 20231120.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/Official Release of PawSQL Advisor.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/PawSQL 2025年3月月度更新.md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/newsletters/PawSQL Advisor正式发布.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/PawSQL Update.md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/newsletters/PawSQL Updates.md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/newsletters/PawSQL审核平台正式发布 (en).md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/PawSQL审核平台正式发布.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/PawSQL新增的SQL审查重写规则.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/PawSQL更新日志(0326).md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/newsletters/PawSQL更新日志(0424) .md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/newsletters/PawSQL月度更新(202502).md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/newsletters/PawSQL月度更新(202505).md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/newsletters/PawSQL社区精选-2024三季度.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/PawSQL社区精选-2025一季度-en.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/PawSQL社区精选-2025一季度.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/文章精选1120.md` | `docs/blog/product/` | zh(英文待补) | 发布公告/社区精选 |
| `70-content/newsletters/月度更新(202406).md` | `docs/release-notes/` | zh(英文待补) | 月度/更新日志；拆为 release notes 条目（en/zh 变体归并） |
| `70-content/vendor-guides/DM.md` | `docs/databases/dm/` | zh(英文待补) | 慢日志/元数据采集指南 |
| `70-content/vendor-guides/Mapper文件形式录入待优化索引.md` | `docs/user-guide/optimization/` | zh(英文待补) | Mapper 录入（zh，去重合并至上一行英文/本文件二选一） |
| `70-content/vendor-guides/MySQL.md` | `docs/databases/mysql/` | zh(英文待补) | 慢日志/元数据采集指南 |
| `70-content/vendor-guides/MySQL数据库.md` | `docs/databases/mysql/` | zh(英文待补) | 慢日志/元数据采集指南 |
| `70-content/vendor-guides/Oracle.md` | `docs/databases/oracle/` | zh(英文待补) | 慢日志/元数据采集指南 |
| `70-content/vendor-guides/PostgreSQL.md` | `docs/databases/postgresql/` | zh(英文待补) | 慢日志/元数据采集指南 |
| `70-content/vendor-guides/SQLServer.md` | `docs/databases/sqlserver/` | zh(英文待补) | 慢日志/元数据采集指南 |
| `70-content/vendor-guides/Workload-Documentation-For-Mapper-File-Type.md` | `docs/user-guide/optimization/` | zh(英文待补) | Mapper 文件类型 workload 录入（canonical，zh） |
| `70-content/vendor-guides/openGauss.md` | `docs/databases/opengauss/` | zh(英文待补) | 慢日志/元数据采集指南 |
| `70-content/vendor-guides/pg_stat_statements.md` | `docs/user-guide/optimization/` | zh(英文待补) | 采集/配置指南 |
| `70-content/vendor-guides/如何启用慢SQL采集-MySQL.md` | `docs/user-guide/optimization/` | zh(英文待补) | 采集/配置指南 |
| `70-content/vendor-guides/如何在高斯分布式数据库获取表的分布方式和分布列.md` | `docs/user-guide/optimization/` | zh(英文待补) | 采集/配置指南 |
| `70-content/vendor-guides/获取MySQL慢查询_en.md` | `docs/user-guide/optimization/` | zh(英文待补) | 采集/配置指南 |
| `70-content/vendor-guides/获取openGauss慢查询.md` | `docs/user-guide/optimization/` | zh(英文待补) | 采集/配置指南 |
| `99-待归类/2026年Top 5 SQL审核工具深度测评：选对工具，告别“问题SQL”上生产.md` | `docs/blog/` | zh | 评审/营销稿 |
| `99-待归类/BIC-QA优化规则.md` | `docs/blog/` | zh | 案例/评测数据→blog 数据源 |
| `99-待归类/BLOG-AUDIT.md` | `docs/blog/` | zh | 评审/营销稿 |
| `99-待归类/BLOG-OVERVIEW.md` | `docs/blog/` | zh | 评审/营销稿 |
| `99-待归类/PawSQL 镜像版本.md` | `docs/products/cloud/` | zh | 实为云套餐/镜像发布说明；重命名并入 pricing/release |
| `99-待归类/PawSQL优化能力评测.md` | `docs/blog/` | zh | 案例/评测数据→blog 数据源 |
| `99-待归类/SQL性能瓶颈智能评价分析.md` | `docs/blog/` | zh | 案例/评测数据→blog 数据源 |
| `99-待归类/TDSQL拉跨系列 - 1. 慢查询管理.md` | `docs/blog/` | zh | 评审/营销稿 |
| `99-待归类/TDSQL拉跨系列 - 2. 执行计划.md` | `docs/blog/` | zh | 评审/营销稿 |
| `99-待归类/意想不到的SQL/Oracle GROUP BY Integer Literals - Schrödinger Behavior.md` | `docs/en/blog/database/` | en | Oracle GROUP BY quirk(en) |
| `99-待归类/意想不到的SQL/Oracle 的 GROUP BY 整型常量与其他数据库的区别.md` | `docs/blog/database/` | zh | Oracle 方言 Quirk（en/zh 镜像） |
| `99-待归类/意想不到的SQL/SQL避坑指南 - Oracle GROUP BY 整型常量的「薛定谔行为」.md` | `docs/blog/database/` | zh | Oracle 方言 Quirk（en/zh 镜像） |
| `99-待归类/金融生产环境实战：PawSQL驱动TDSQL-MySQL慢查询优化，召回率76.6%，近7成自动化优化.md` | `docs/blog/` | zh | 客户案例 |
| `99-待归类/金融生产环境实战：PawSQL驱动openGauss慢查询优化，正确率100%，释放近7成人力成本.md` | `docs/blog/` | zh | 客户案例 |
| `99-待归类/金融级实战验证：PawSQL在TDSQL-MySQL慢查询优化中的有效性与召回率深度评测.md` | `docs/blog/` | zh | 客户案例 |

## A0. 未显式归类（需评审归入 A/B/C）

| 源 | 建议目标 | 说明 |
|---|---|---|

## D. 规则文档 261 条 audit/optimizer 初判（供评审，未落地）

> 判定：审计/检查语义→`audit`；重写/优化语义→`optimizer`；文件名含“重写/优化/消除/转换/解关联/下推”或类别含“子查询优化/重写”→optimizer；启发式低置信标 `?`。
| 源文件 | 英文名 | 类别(原) | 族 | category | severity | db(空=ALL) | 拟用 id | 置信 |
|---|---|---|---|---|---|---|---|---|
| ALL修饰的子查询重写 | All Qualifier Subquery Rewrite | 数据操作 > 正确性 | optimizer | rewrite | error |  | `opt-all-qualifier-subquery-rewrite` | high |
| CHAR字段长度超过阈值 | Char Column Length Exceeds Threshold | 对象设计 > 列定义 > 数据类型 | audit | ddl | info |  | `aud-char-column-length-exceeds-threshold` | high |
| COUNT标量子查询重写 | COUNT Scalar Subquery Rewrite | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-count-scalar-subquery-rewrite` | high |
| CTAS 命名规范 | CTAS Naming Convention | 对象设计 > 命名规范 | audit | ddl | info |  | `aud-ctas-naming-convention` | high |
| DELETE_UPDATE禁止使用连接 | DELETE/UPDATE Forbidden with Table Join | 数据操作 > 性能 > SQL复杂度 | audit | dml | warning |  | `aud-deleteupdate-forbidden-with-table-join` | high |
| EXISTS查询转换为表连接 | EXISTS Subquery to Table Join Rewrite | 数据操作 > 性能 > 子查询优化 > 减少查询块 | optimizer | rewrite | info |  | `opt-exists-subquery-to-table-join-rewrite` | high |
| GROUPBY字段来自不同表 | GROUP BY Columns from Multiple Tables | 数据操作 > 性能 > 索引失效 > 分组 | audit? | index | info |  | `aud-group-by-columns-from-multiple-tables` | low |
| GROUP字段中有表达式导致索引失效 | Expression in GROUP BY Causes Index Invalidation | 数据操作 > 性能 > 索引失效 > 分组 | audit | index | info |  | `aud-expression-in-group-by-causes-index-invalidation` | high |
| HAVING条件下推 | HAVING Clause Pushdown to WHERE | 数据操作 > 性能 > 条件过滤 | optimizer | rewrite | info |  | `opt-having-clause-pushdown-to-where` | high |
| HIVE中COUNT(DISTINCT...) 导致数据倾斜优化 | COUNT(DISTINCT) Skew Optimization in Hive | 数据操作 > 性能 > 数据倾斜 | optimizer | rewrite | warning | Hive | `opt-countdistinct-skew-optimization-in-hive` | high |
| HIVE中DISTINCT导致的数据倾斜优化 | DISTINCT Skew Optimization in Hive | 数据操作 > 性能 > 数据倾斜 | optimizer | rewrite | warning | Hive | `opt-distinct-skew-optimization-in-hive` | high |
| HIVE中使用非分桶字段进行表关联 | Non-Bucket Column Table Join in Hive | 数据操作 > 性能 > 表关联 | audit? | dml | info | Hive | `aud-nonbucket-column-table-join-in-hive` | low |
| HIVE中全局排序导致的数据倾斜优化 | Global Sorting Skew Optimization in Hive | 数据操作 > 性能 > 数据倾斜 | optimizer | rewrite | warning | Hive | `opt-global-sorting-skew-optimization-in-hive` | high |
| HIVE中关联字段分桶数应保持整数倍 | Bucket Count Integer Multiple for Join in Hive | 数据操作 > 性能 > 表关联 | audit | dml | info | Hive | `aud-bucket-count-integer-multiple-for-join-in-hive` | high |
| HIVE中分组字段分布不均匀导致数据倾斜优化 | Group By Skew Optimization in Hive | 数据操作 > 性能 > 数据倾斜 | optimizer | rewrite | warning | Hive | `opt-group-by-skew-optimization-in-hive` | high |
| Hive中过滤谓词下推到表关联之前计算 | Predicate Pushdown Before Join in Hive | 数据操作 > 性能 > 条件过滤 | optimizer | rewrite | info | Hive | `opt-predicate-pushdown-before-join-in-hive` | high |
| Hive内部表需使用orc_parquet存储格式 | Hive Internal Tables Must Use ORC/Parquet Format | 对象设计 > 表/视图定义 | audit | ddl | error | Hive | `aud-hive-internal-tables-must-use-orcparquet-format` | high |
| Hive表需使用指定的压缩格式 | Hive Table Compression Format Required | 对象设计 > 表/视图定义 | audit | ddl | error | Hive | `aud-hive-table-compression-format-required` | high |
| INSERT...VALUES列和值数量一致 | INSERT VALUES Column and Value Count Match | 数据操作 > 正确性 | audit | dml | error |  | `aud-insert-values-column-and-value-count-match` | high |
| INSERT...VALUES应该指定列名 | INSERT VALUES Must Specify Column Names | 数据操作 > 可维护性 | audit | dml | error |  | `aud-insert-values-must-specify-column-names` | high |
| INSERT语句中值的数量超过阈值 | INSERT Value Count Exceeds Threshold | 数据操作 > 性能 > 其他 | audit | dml | info |  | `aud-insert-value-count-exceeds-threshold` | high |
| INSERT语句必须包含主键字段 | INSERT Must Include Primary Key Column | 数据操作 > 正确性 | audit | dml | warning |  | `aud-insert-must-include-primary-key-column` | high |
| INSERT语句禁止使用SYSDATE函数 | SYSDATE Function Forbidden in INSERT | 数据操作 > 正确性 | audit | dml | warning | MySQL | `aud-sysdate-function-forbidden-in-insert` | high |
| IN可空子查询可能导致结果集不符合预期 | Nullable IN Subquery May Produce Unexpected Results | 数据操作 > 正确性 > NULL值处理 | audit? | dml | error |  | `aud-nullable-in-subquery-may-produce-unexpected-resu` | low |
| IN子查询中没有LIMIT的排序消除 | Order Elimination in Subquery Without LIMIT | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-order-elimination-in-subquery-without-limit` | high |
| IN子查询优化 | IN Subquery Rewrite Optimization | 数据操作 > 性能 > 子查询优化 > 减少查询块 | optimizer | rewrite | info |  | `opt-in-subquery-rewrite-optimization` | high |
| LIMIT下推至UNION分支 | LIMIT Pushdown to UNION Branches | 数据操作 > 性能 > 减少访问数据量 | optimizer | rewrite | info |  | `opt-limit-pushdown-to-union-branches` | high |
| MAX_MIN子查询重写 | MAX/MIN Subquery Rewrite | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-maxmin-subquery-rewrite` | high |
| NPE重写 | NPE Rewrite (Null Pointer Exception Prevention) | 数据操作 > 正确性 > NULL值处理 | optimizer | rewrite | warning |  | `opt-npe-rewrite-null-pointer-exception-prevention` | high |
| ORDER子句重排序优化 | ORDER Clause Reorder Optimization | 数据操作 > 性能 > 索引失效 > 排序 | optimizer | index | info |  | `opt-order-clause-reorder-optimization` | high |
| ORDER字段中有表达式导致索引失效 | Expression in ORDER BY Causes Index Invalidation | 数据操作 > 性能 > 索引失效 > 排序 | audit | index | info |  | `aud-expression-in-order-by-causes-index-invalidation` | high |
| OR条件的SELECT重写 | OR Condition SELECT Rewrite | 数据操作 > 性能 > 条件过滤 | optimizer | rewrite | info |  | `opt-or-condition-select-rewrite` | high |
| OR条件的UPDELETE重写 | OR Condition UPDATE/DELETE Rewrite | 数据操作 > 性能 > 条件过滤 | optimizer | rewrite | info |  | `opt-or-condition-updatedelete-rewrite` | high |
| SATTC重写优化 | SATTC Rewrite Optimization | 数据操作 > 性能 > 条件过滤 | optimizer | rewrite | info |  | `opt-sattc-rewrite-optimization` | high |
| SELECT 语句必须带LIMIT | SELECT Statement Must Have LIMIT | 数据操作 > 性能 > 减少访问数据量 | audit | dml | info |  | `aud-select-statement-must-have-limit` | high |
| SQL长度超过阈值 | SQL Length Exceeds Threshold | 数据操作 > 性能 > SQL复杂度 | audit | dml | info |  | `aud-sql-length-exceeds-threshold` | high |
| TDSQL中使用ALTER设置自增列的起始值 | Use ALTER TABLE to Set Auto Increment Start in TDSQL | 对象设计 > 其他 | audit | ddl | info | TDSQL | `aud-use-alter-table-to-set-auto-increment-start-in-t` | high |
| UNION ALL统计查询优化 | UNION ALL Count Query Optimization | 数据操作 > 性能 > 减少访问数据量 | optimizer | rewrite | info |  | `opt-union-all-count-query-optimization` | high |
| UNION导致的数据倾斜优化 | UNION Skew Optimization in Hive | 数据操作 > 性能 > 数据倾斜 | optimizer | rewrite | warning | Hive | `opt-union-skew-optimization-in-hive` | high |
| UPDATE_DELETE操作使用 LIMIT 子句 | UPDATE/DELETE With LIMIT Warning | 数据操作 > 正确性 | audit? | dml | warning |  | `aud-updatedelete-with-limit-warning` | low |
| UPDATE_DELETE禁止使用ORDER子句 | ORDER BY Forbidden in UPDATE/DELETE | 数据操作 > 正确性 | audit | dml | warning |  | `aud-order-by-forbidden-in-updatedelete` | high |
| Union常量重写优化 | Union Constant Rewrite Optimization | 数据操作 > 正确性 | optimizer | rewrite | error |  | `opt-union-constant-rewrite-optimization` | high |
| VARCHAR字段长度超过阈值 | VARCHAR Column Length Exceeds Threshold | 对象设计 > 列定义 > 数据类型 | audit | ddl | warning |  | `aud-varchar-column-length-exceeds-threshold` | high |
| 不允许使用时间戳类型 | Timestamp Data Type Disallowed | 对象设计 > 列定义 > 数据类型 | audit | ddl | warning |  | `aud-timestamp-data-type-disallowed` | high |
| 为分组显式添加空排序(_MYSQL 5.7) | GROUP BY with ORDER BY NULL Optimization | 数据操作 > 性能 > 排序分组 | optimizer | rewrite | info | MySQL | `opt-group-by-with-order-by-null-optimization` | high |
| 主外键的数据类型不一致 | DiffDataTypesOfRIColumns | 对象设计 > 约束 | audit | ddl | warning |  | `aud-diffdatatypesofricolumns` | high |
| 主键列的数据类型限制 | DataTypeLimitOfPrimaryKey | 对象设计 > 约束 | audit | ddl | warning |  | `aud-datatypelimitofprimarykey` | high |
| 主键命名规范 | Primary Key Naming Convention | 对象设计 > 命名规范 > 索引/约束命名应符合规范 | audit | index | info |  | `aud-primary-key-naming-convention` | high |
| 主键应使用自增列 | IncColumn4PrimaryKeyRequired | 对象设计 > 约束 | audit | ddl | warning |  | `aud-inccolumn4primarykeyrequired` | high |
| 主键的列数目不得超过阈值 | NumOfPKColumnsExceed | 对象设计 > 约束 | audit | ddl | warning |  | `aud-numofpkcolumnsexceed` | high |
| 主键禁止使用自增 | IncColumn4PrimaryKeyDisallowed | 对象设计 > 约束 | audit | ddl | warning | 分布式数据库 | `aud-inccolumn4primarykeydisallowed` | high |
| 使用 = 替代 IN（单值） | Use Equals Instead of IN with Single Value | 数据操作 > 性能 > SQL 重写 | optimizer | rewrite | info |  | `opt-use-equals-instead-of-in-with-single-value` | high |
| 使用INSERT…UPDATE替代REPLACE语句 | Use INSERT ON DUPLICATE KEY UPDATE Instead of REPLACE | 数据操作 > 性能 > SQL 重写 | optimizer | rewrite | warning |  | `opt-use-insert-on-duplicate-key-update-instead-of-re` | high |
| 使用UNION ALL代替UNION | Use UNION ALL Instead of UNION | 数据操作 > 性能 > 排序分组 | optimizer | rewrite | info |  | `opt-use-union-all-instead-of-union` | high |
| 使用不存在的列 | Column with this Name Does Not Exist | 对象操作 > 语法错误 | audit | audit | error |  | `aud-column-with-this-name-does-not-exist` | high |
| 使用日期时间字段删除建议改为分区表删除分区 | Use DROP PARTITION Instead of DELETE for Date-Based Cleanup | 数据操作 > 性能 > 大事务 | audit | dml | warning |  | `aud-use-drop-partition-instead-of-delete-for-datebas` | high |
| 修饰子查询重写优化 | ANY/SOME/ALL Subquery Rewrite Optimization | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-anysomeall-subquery-rewrite-optimization` | high |
| 关联字段不均匀导致数据倾斜优化 | Data Skew Optimization for Uneven Join Keys | 数据操作 > 性能 > 数据倾斜 | audit? | dml | warning | Hive, Spark SQL | `aud-data-skew-optimization-for-uneven-join-keys` | low |
| 分区字段上有运算导致无法进行分区裁剪 | Partition Column Operation Prevents Partition Pruning | 数据操作 > 性能 > 分区裁剪 | audit? | dml | warning | Hive, Spark SQL | `aud-partition-column-operation-prevents-partition-pr` | low |
| 分区键上的过滤条件禁止使用to_date_to_timestamp函数 | No TO_DATE/TO_TIMESTAMP on Partition Key in Filter Conditions | 数据操作 > 性能 > 分区裁剪 | audit | dml | error | TDSQL, 分布式数据库 | `aud-no-todatetotimestamp-on-partition-key-in-filter-` | high |
| 分区键的长度不得超过阈值 | Partition Key Length Must Not Exceed Threshold | 对象设计 > 表/视图定义 | audit | ddl | warning |  | `aud-partition-key-length-must-not-exceed-threshold` | high |
| 分布式数据库不建议创建非分布表 | Avoid Non-Distributed Tables | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库 | `aud-avoid-nondistributed-tables` | high |
| 分布式数据库中使用IN替代OR | Use IN Instead of OR in Distributed Databases | 数据操作 > 分布式 > 过滤下推分片 | audit? | dml | info | 分布式数据库 | `aud-use-in-instead-of-or-in-distributed-databases` | low |
| 分布式数据库应避免出现ANTIJOIN操作 | Avoid ANTI JOIN Operations in Distributed Databases | 数据操作 > 分布式 > 过滤下推分片 | audit | dml | warning | 分布式数据库 | `aud-avoid-anti-join-operations-in-distributed-databa` | high |
| 分布式数据库应避免跨分片的DML操作 | Avoid Cross-Shard DML Operations in Distributed Databases | 数据操作 > 分布式 > 分布式事务 | audit | dml | warning | 分布式数据库 | `aud-avoid-crossshard-dml-operations-in-distributed-d` | high |
| 分布方式建议使用hash分布 | Prefer Hash Distribution | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库 | `aud-prefer-hash-distribution` | high |
| 分布键不建议使用多个字段 | Avoid Multiple Distribution Keys | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库 | `aud-avoid-multiple-distribution-keys` | high |
| 分布键应使用区分度大的字段 | Use High Cardinality Distribution Keys | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库 | `aud-use-high-cardinality-distribution-keys` | high |
| 分布键的数据类型限制 | Distribution Key Data Type Restriction | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库 | `aud-distribution-key-data-type-restriction` | high |
| 分布键的长度不得超过阈值 | Distribution Key Length Must Not Exceed Threshold | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库 | `aud-distribution-key-length-must-not-exceed-threshol` | high |
| 分布键的需使用指定的排序规则 | Distribution Key Must Use Specified Collation | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库 | `aud-distribution-key-must-use-specified-collation` | high |
| 分片表不支持UPDATE更新的值为子查询 | Sharded Table UPDATE Does Not Support Subquery Values | 数据操作 > 分布式 > 语法错误 | audit | dml | error | TDSQL, 分布式数据库 | `aud-sharded-table-update-does-not-support-subquery-v` | high |
| 分片表的分布键应设置非空约束 | Distribution Key Must Have NOT NULL Constraint | 对象设计 > 数据分布 | audit | ddl | info | 分布式数据库 | `aud-distribution-key-must-have-not-null-constraint` | high |
| 分组字段不包含分布键 | GROUP BY Fields Must Include Distribution Key | 数据操作 > 分布式 > 全局聚集 | audit | dml | warning | 分布式数据库 | `aud-group-by-fields-must-include-distribution-key` | high |
| 列名命名规范 | Column Naming Convention | 对象设计 > 命名规范 | audit | ddl | info |  | `aud-column-naming-convention` | high |
| 列必须有注释 | Comments on Column Required | 对象设计 > 注释 | audit | ddl | warning |  | `aud-comments-on-column-required` | high |
| 列的字符集和表不一致 | Column and Table Character Set Mismatch | 对象设计 > 字符集/排序规则 | audit | ddl | warning |  | `aud-column-and-table-character-set-mismatch` | high |
| 创建库必须指定数据库字符集 | Character Set Required for Database Creation | 对象设计 > 字符集/排序规则 | audit | ddl | warning |  | `aud-character-set-required-for-database-creation` | high |
| 创建库或模式时使用规定的排序规则 | Specific Collation Required for Database Creation | 对象设计 > 字符集/排序规则 | audit | ddl | error |  | `aud-specific-collation-required-for-database-creatio` | high |
| 创建库或模式时必须使用指定字符集 | Specific Character Set Required for Database Creation | 对象设计 > 字符集/排序规则 | audit | ddl | warning |  | `aud-specific-character-set-required-for-database-cre` | high |
| 创建约束前提前创建相关的索引 | Create Index Before Constraint | 对象设计 > 约束 | audit | ddl | warning |  | `aud-create-index-before-constraint` | high |
| 创建表_视图_索引时需指定ifNotExists | IF NOT EXISTS Required for Creating Objects | 对象设计 > 表/视图定义 | audit | ddl | warning |  | `aud-if-not-exists-required-for-creating-objects` | high |
| 删除表_视图_索引时需指定IfExists | IF EXISTS Required for Dropping Objects | 对象操作 > 删除对象 | audit | audit | warning |  | `aud-if-exists-required-for-dropping-objects` | high |
| 单表的索引个数超过阈值 | Number of Indexes Exceeds Threshold | 对象设计 > 索引 | audit | index | warning |  | `aud-number-of-indexes-exceeds-threshold` | high |
| 只能删除指定命名规范的列 | Drop Columns Only with Specified Naming Convention | 对象操作 > 删除对象 | audit | audit | warning |  | `aud-drop-columns-only-with-specified-naming-conventi` | high |
| 只能删除指定命名规范的表和视图 | Drop Tables/Views Only with Specified Naming Convention | 对象操作 > 删除对象 | audit | audit | warning |  | `aud-drop-tablesviews-only-with-specified-naming-conv` | high |
| 同表同字段比较 | Same Table Same Column Comparison | 数据操作 > 正确性 | audit? | dml | warning |  | `aud-same-table-same-column-comparison` | low |
| 唯一性索引命名规范 | Unique Key Naming Convention | 对象设计 > 命名规范 > 索引/约束命名应符合规范 | audit | index | info |  | `aud-unique-key-naming-convention` | high |
| 在一个查询块中引用多表应使用别名 | Use Table Aliases in Multi-Table Queries | 数据操作 > 可维护性 | audit | dml | info |  | `aud-use-table-aliases-in-multitable-queries` | high |
| 复制表与分片表外关联的查询优化 | Optimize Outer Join Between Replicated and Sharded Tables | 数据操作 > 分布式 > 跨分片关联 | audit | dml | info | 分布式数据库（Greenplum、PostgreSQL-XL、TiDB、TDSQL 等） | `aud-optimize-outer-join-between-replicated-and-shard` | high |
| 外连接优化 | Outer Join to Inner Join Conversion | 数据操作 > 性能 > 表关联 | audit | dml | info |  | `aud-outer-join-to-inner-join-conversion` | high |
| 外键命名规范 | Foreign Key Naming Convention | 对象设计 > 命名规范 > 索引/约束命名应符合规范 | audit | index | info |  | `aud-foreign-key-naming-convention` | high |
| 大的Hive应该使用分区表 | Use Partitioned Tables for Large Hive Tables | 对象设计 > 表/视图定义 | audit | ddl | warning | Hive | `aud-use-partitioned-tables-for-large-hive-tables` | high |
| 大的Hive表应该使用分桶策略 | Use Bucketing Strategy for Large Hive Tables | 对象设计 > 表/视图定义 | audit | ddl | warning | Hive | `aud-use-bucketing-strategy-for-large-hive-tables` | high |
| 大表不建议使用复制(Replicated)分布 | Avoid Replicated Distribution for Large Tables | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库（Greenplum、PostgreSQL-XL、TDSQL、DWS 等） | `aud-avoid-replicated-distribution-for-large-tables` | high |
| 大表建议使用分区表 | Use Partitioned Tables for Large Tables | 对象设计 > 表/视图定义 | audit | ddl | info |  | `aud-use-partitioned-tables-for-large-tables` | high |
| 子查询中的DISTINCT消除 | Eliminate Unnecessary DISTINCT in Subqueries | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-eliminate-unnecessary-distinct-in-subqueries` | high |
| 子查询的嵌套层次超过阈值 | Subquery Nesting Depth Exceeds Threshold | 数据操作 > 性能 > SQL复杂度 | audit | dml | warning |  | `aud-subquery-nesting-depth-exceeds-threshold` | high |
| 字段名已存在 | Column with this Name Already Exists | 对象操作 > 语法错误 | audit | audit | error |  | `aud-column-with-this-name-already-exists` | high |
| 定义约束时需指定DISABLE和NONVALIDATE | Specify DISABLE and NONVALIDATE for Hive Constraints | 对象设计 > 约束 | audit | ddl | warning | Hive | `aud-specify-disable-and-nonvalidate-for-hive-constra` | high |
| 对于入参建议使用变量绑定 | Use Variable Binding for Parameters | 数据操作 > 安全性 | audit | dml | warning |  | `aud-use-variable-binding-for-parameters` | high |
| 对分片表的INSERT_REPLACE时字段必须包含分布键 | Distribution Key Required in INSERT/REPLACE for Sharded Tables | 数据操作 > 分布式 > 分布式事务 | audit | dml | error | 分布式数据库（TDSQL、MySQL Sharding 等） | `aud-distribution-key-required-in-insertreplace-for-s` | high |
| 对象前需添加属主 | Add Schema Qualifier Before Object References | 数据操作 > 可维护性 | audit | dml | info |  | `aud-add-schema-qualifier-before-object-references` | high |
| 对象名称长度不得超过阈值 | Object Name Length Must Not Exceed Threshold | 对象设计 > 命名规范 | audit | ddl | warning |  | `aud-object-name-length-must-not-exceed-threshold` | high |
| 对象命名规范 | Object Naming Convention | 对象设计 > 命名规范 | audit | ddl | info |  | `aud-object-naming-convention` | high |
| 小于阈值的分布表建议设计为复制表 | Consider Replicated Distribution for Small Tables | 对象设计 > 数据分布 | audit | ddl | info | 分布式数据库（Greenplum、PostgreSQL-XL、TiDB、DWS 等） | `aud-consider-replicated-distribution-for-small-table` | high |
| 应使用主键作为分布键 | Use Primary Key as Distribution Key | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库（Greenplum、PostgreSQL-XL、openGauss、TDSQL、DWS 等） | `aud-use-primary-key-as-distribution-key` | high |
| 应使用指定的数据分布方式 | Use Specified Data Distribution Method | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库（TDSQL 等） | `aud-use-specified-data-distribution-method` | high |
| 应通过唯一性索引来进行数据更新操作 | Use Unique Index for Data Update Operations | 数据操作 > 性能 > 其他 | audit | dml | info |  | `aud-use-unique-index-for-data-update-operations` | high |
| 建议使用'__'代替'!=' | Use '<>' Instead of '!=' | 数据操作 > 可维护性 | audit | dml | warning |  | `aud-use-instead-of` | high |
| 建议使用在线模式创建索引 | Create Index Using Online Mode | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-create-index-using-online-mode` | high |
| 建议索引字段对区分度大于阈值 | Index Column Selectivity Should Exceed Threshold | 对象设计 > 索引 | audit | index | info |  | `aud-index-column-selectivity-should-exceed-threshold` | high |
| 必须使用INNODB存储引擎 | InnoDB Storage Engine Required | 对象设计 > 表/视图定义 | audit | ddl | warning | MySQL、PolarDB（InnoDB引擎）、TDSQL（InnoDB引擎） | `aud-innodb-storage-engine-required` | high |
| 必须显式的指定分布键 | Explicit Distribution Key Required | 对象设计 > 数据分布 | audit | ddl | warning | **分布式数据库**（包括但不限于：openGauss、PostgreSQL-XL、TDSQL、OceanBase、TiDB、DWS 等） | `aud-explicit-distribution-key-required` | high |
| 批量删除建议使用分区表删除分区 | Use DROP PARTITION Instead of Batch DELETE | 数据操作 > 性能 > 大事务 | audit | dml | info |  | `aud-use-drop-partition-instead-of-batch-delete` | high |
| 投影下推(PROJECTION PUSHDOWN) | Projection Pushdown | 数据操作 > 性能 > 减少访问数据量 | optimizer | rewrite | info |  | `opt-projection-pushdown` | high |
| 排序字段方向不同导致索引失效 | Mixed Sort Directions Cause Index Inefficiency | 数据操作 > 性能 > 索引失效 > 排序 | audit | index | info |  | `aud-mixed-sort-directions-cause-index-inefficiency` | high |
| 提前过滤不合法的值避免多余计算 | Filter Invalid Values Early to Avoid Unnecessary Computation | 数据操作 > 性能 > 数据倾斜 | audit | dml | info | Hive | `aud-filter-invalid-values-early-to-avoid-unnecessary` | high |
| 数据库命名规范 | Database Naming Convention | 对象设计 > 命名规范 | audit | ddl | info |  | `aud-database-naming-convention` | high |
| 数据库需指定默认排序规则（Collate） | Default Collation Required for Database | 对象设计 > 字符集/排序规则 | audit | ddl | warning |  | `aud-default-collation-required-for-database` | high |
| 数据操作语句影响的行数不得超过阈值 | DML Affected Rows Must Not Exceed Threshold | 数据操作 > 性能 > 大事务 | audit | dml | error |  | `aud-dml-affected-rows-must-not-exceed-threshold` | high |
| 整型建议采用 INT(10) 或 BIGINT(20) | Use INT(10) or BIGINT(20) for Integer Columns | 对象设计 > 列定义 > 数据类型 | audit | ddl | info | MySQL、PolarDB、TDSQL 等基于MySQL的数据库 | `aud-use-int10-or-bigint20-for-integer-columns` | high |
| 无分组的聚集函数导致的数据倾斜优化 | Data Skew Optimization for Aggregate Without GROUP BY | 数据操作 > 性能 > 数据倾斜 | optimizer | rewrite | warning | Hive | `opt-data-skew-optimization-for-aggregate-without-gro` | high |
| 无条件的DELETE建议重写为Truncate | Rewrite Unconditional DELETE to TRUNCATE | 数据操作 > 性能 > 其他 | audit? | dml | info |  | `aud-rewrite-unconditional-delete-to-truncate` | low |
| 时间列未设置默认值或默认值为空 | Default Value Required for Time Columns | 对象设计 > 列定义 > 默认值 | audit | ddl | warning |  | `aud-default-value-required-for-time-columns` | high |
| 时间戳列需指定默认值 | Default Value Required for Timestamp Columns | 对象设计 > 列定义 > 默认值 | audit | ddl | warning |  | `aud-default-value-required-for-timestamp-columns` | high |
| 条件标量子查询解关联 | Decorate Correlated Scalar Subqueries | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-decorate-correlated-scalar-subqueries` | high |
| 查询中表连接的个数超过阈值 | Number of Joined Tables Exceeds Threshold | 数据操作 > 性能 > SQL复杂度 | audit | dml | warning |  | `aud-number-of-joined-tables-exceeds-threshold` | high |
| 查询折叠(QUERY FOLDING) | Query Folding | 数据操作 > 性能 > 子查询优化 > 减少查询块 | optimizer | rewrite | info |  | `opt-query-folding` | high |
| 模式命名规范 | Schema Naming Convention | 对象设计 > 命名规范 | audit | ddl | info |  | `aud-schema-naming-convention` | high |
| 每个表只能有一个自增列 | OneIdentityColumnAllowed | 对象设计 > 表/视图定义 | audit | ddl | warning |  | `aud-oneidentitycolumnallowed` | high |
| 派生表转换为Lateral表关联 | Derived Table to LATERAL Join Conversion | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-derived-table-to-lateral-join-conversion` | high |
| 深分页优化 | Deep Pagination Optimization | 数据操作 > 性能 > 减少访问数据量 | optimizer | rewrite | warning |  | `opt-deep-pagination-optimization` | high |
| 添加CHECK约束时需添加NO VALID | AddCheckConstraintShouldBeDeferred | 对象设计 > 约束 | audit | ddl | warning |  | `aud-addcheckconstraintshouldbedeferred` | high |
| 禁止为列修改默认值 | ModifyingColumnChangeDefaultDisallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-modifyingcolumnchangedefaultdisallowed` | high |
| 禁止为列新增非空约束 | ModifyingColumnAddNotNullDisallowed | 对象操作 > 添加约束 | audit | audit | warning |  | `aud-modifyingcolumnaddnotnulldisallowed` | high |
| 禁止为列新增默认值 | ModifyingColumnAddDefaultDisallowed | 对象操作 > 添加约束 | audit | audit | warning |  | `aud-modifyingcolumnadddefaultdisallowed` | high |
| 禁止为列表中的列设置非空约束 | NonNullConstraint4ColumnsInListDisallowed | 对象操作 > 添加约束 | audit | audit | warning |  | `aud-nonnullconstraint4columnsinlistdisallowed` | high |
| 禁止为列表中的列设置非空默认值 | LargeObjectDefaultNonNullDisallowed | 对象设计 > 列定义 > 默认值 | audit | ddl | warning |  | `aud-largeobjectdefaultnonnulldisallowed` | high |
| 禁止使用=NULL判断空值 | NullValueComparisonDisallowed | 数据操作 > 正确性 > NULL值处理 | audit | dml | warning |  | `aud-nullvaluecomparisondisallowed` | high |
| 禁止使用CHECK约束 | CreateCheckConstraintDisallowed | 对象设计 > 约束 | audit | ddl | warning |  | `aud-createcheckconstraintdisallowed` | high |
| 禁止使用ENUM数据类型 | EnumDataTypeDisallowed | 对象设计 > 列定义 > 数据类型 | audit | ddl | warning |  | `aud-enumdatatypedisallowed` | high |
| 禁止使用SET数据类型 | SetDataTypeDisallowed | 对象设计 > 列定义 > 数据类型 | audit | ddl | warning |  | `aud-setdatatypedisallowed` | high |
| 禁止使用SYSDATE作为默认值 | UseSysdateAsDefaultDisallowed | 对象设计 > 列定义 > 默认值 | audit | ddl | warning |  | `aud-usesysdateasdefaultdisallowed` | high |
| 禁止使用全文索引 | FulltextIndexDisallowed | 对象设计 > 索引 | audit | index | warning |  | `aud-fulltextindexdisallowed` | high |
| 禁止使用函数索引 | FunctionalIndexDisallowed | 对象设计 > 索引 | audit | index | warning |  | `aud-functionalindexdisallowed` | high |
| 禁止使用分区表 | PartitionedTableDisallowed | 对象设计 > 表/视图定义 | audit | ddl | info | MySQL | `aud-partitionedtabledisallowed` | high |
| 禁止使用存储过程 | Stored Procedure Disallowed | 对象设计 > 其他 | audit | ddl | warning |  | `aud-stored-procedure-disallowed` | high |
| 禁止使用常见 SQL 注入函数 | SQLInjectionFuncsDisallowed | 数据操作 > 安全性 | audit | dml | warning |  | `aud-sqlinjectionfuncsdisallowed` | high |
| 禁止使用的数据类型 | DataTypesDisallowed | 对象设计 > 列定义 > 数据类型 | audit | ddl | warning |  | `aud-datatypesdisallowed` | high |
| 禁止使用自定义函数 | UserDefinedFunction(UDF) Disallowed | 对象设计 > 其他 | audit | ddl | error |  | `aud-userdefinedfunctionudf-disallowed` | high |
| 禁止使用视图 | ViewDisallowed | 对象设计 > 表/视图定义 | audit | ddl | warning | MySQL | `aud-viewdisallowed` | high |
| 禁止使用触发器 | TriggerDisallowed | 对象设计 > 其他 | audit | ddl | warning |  | `aud-triggerdisallowed` | high |
| 禁止修改分区键的值 | ModifyingPartitionKeyValueDisallowed | 数据操作 > 性能 > 其他 | audit | dml | warning |  | `aud-modifyingpartitionkeyvaluedisallowed` | high |
| 禁止修改分布键字段类型 | ModifyingDistributionKeyTypeDisallowed | 对象设计 > 数据分布 | audit | ddl | warning |  | `aud-modifyingdistributionkeytypedisallowed` | high |
| 禁止修改分片键的值 | ModifyingShardKeyValueDisallowed | 数据操作 > 分布式 > 语法错误 | audit | dml | warning |  | `aud-modifyingshardkeyvaluedisallowed` | high |
| 禁止修改列的数据类型 | ChangingColumnTypeDisallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-changingcolumntypedisallowed` | high |
| 禁止修改列的顺序 | ChangingColumn's Order Disallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-changingcolumns-order-disallowed` | high |
| 禁止修改字段名 | ChangingColumnNameDisallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-changingcolumnnamedisallowed` | high |
| 禁止修改表的默认字符集 | ModifyTableCharSetDisallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-modifytablecharsetdisallowed` | high |
| 禁止修改降低字段精度 | DecreasingPrecisionDisallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-decreasingprecisiondisallowed` | high |
| 禁止修改降低字段长度 | ShortenDataTypeLengthDisallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-shortendatatypelengthdisallowed` | high |
| 禁止创建外键 | ForeignKeyDisallowed | 对象设计 > 约束 | audit | ddl | warning |  | `aud-foreignkeydisallowed` | high |
| 禁止创建自定义函数 | UserDefinedFunction(UDF) Disallowed | 对象设计 > 其他 | audit | ddl | error |  | `aud-userdefinedfunctionudf-disallowed` | high |
| 禁止创建自定义类型 | UserDefinedType(UDT) Disallowed | 对象设计 > 其他 | audit | ddl | warning |  | `aud-userdefinedtypeudt-disallowed` | high |
| 禁止创建重复索引_冗余索引 | RedundantIndexDisallowed | 对象设计 > 索引 | audit | index | warning |  | `aud-redundantindexdisallowed` | high |
| 禁止删除字段 | DroppingColumnsDisallowed | 对象操作 > 删除对象 | audit | audit | warning |  | `aud-droppingcolumnsdisallowed` | high |
| 禁止删除索引 | DroppingIndexDisallowed | 对象操作 > 删除对象 | audit | audit | warning |  | `aud-droppingindexdisallowed` | high |
| 禁止删除索引中的列 | DroppingColumnsUsedInIndexDisallowed | 对象操作 > 删除对象 | audit | audit | warning |  | `aud-droppingcolumnsusedinindexdisallowed` | high |
| 禁止删除表_视图 | DropTable/ViewDisallowed | 对象操作 > 删除对象 | audit | audit | warning |  | `aud-droptableviewdisallowed` | high |
| 禁止在分区表上创建全局索引 | GlobalIndexOnPartitionedTableDisallowed | 对象设计 > 索引 | audit | index | warning | openGauss, DWS | `aud-globalindexonpartitionedtabledisallowed` | high |
| 禁止在分布式表上创建全局索引 | GlobalIndexOnDistributedTableDisallowed | 对象设计 > 索引 | audit | index | warning |  | `aud-globalindexondistributedtabledisallowed` | high |
| 禁止对象名称与关键字重名 | DuplicatedObjectNamesWithKeywords | 对象设计 > 命名规范 | audit | ddl | warning |  | `aud-duplicatedobjectnameswithkeywords` | high |
| 禁止对非整形常量进行GROUP BY | GroupByConstExprDisallowed | 数据操作 > 正确性 | audit | dml | warning |  | `aud-groupbyconstexprdisallowed` | high |
| 禁止对非整形常量进行ORDER BY | OrderByConstExprDisallowed | 数据操作 > 正确性 | audit | dml | warning |  | `aud-orderbyconstexprdisallowed` | high |
| 禁止指定列的字符集 | CharsetOnColumnDisallowed | 对象设计 > 字符集/排序规则 | audit | ddl | warning |  | `aud-charsetoncolumndisallowed` | high |
| 禁止新增有默认值的列 | AddingColumnsWithDefaultDisallowed | 对象操作 > 添加约束 | audit | audit | warning |  | `aud-addingcolumnswithdefaultdisallowed` | high |
| 禁止更新索引中的列 | UpdatingColumnsUsedInIndexDisallowed | 对象操作 > 更新对象 | audit | audit | warning |  | `aud-updatingcolumnsusedinindexdisallowed` | high |
| 禁止索引创建时指定collation | Collation4IndexDisallowed | 对象设计 > 索引 | audit | index | warning |  | `aud-collation4indexdisallowed` | high |
| 禁止表关联数目超过阈值（严重） | NumberOfJoinedTablesExceedCriticalThreshold | 数据操作 > 性能 > SQL复杂度 | audit | dml | error |  | `aud-numberofjoinedtablesexceedcriticalthreshold` | high |
| 禁止设置MAXVALUE默认分区 | MaxValueDefaultPartitionDisallowed | 对象设计 > 表/视图定义 | audit | ddl | info |  | `aud-maxvaluedefaultpartitiondisallowed` | high |
| 禁止通过COMPRESSED打开字段压缩功能 | CompressedAttributeDisallowed | 对象设计 > 表/视图定义 | audit | ddl | warning |  | `aud-compressedattributedisallowed` | high |
| 窗口分区字段分布不均匀导致数据倾斜 | WinFuncSkewedOptimization | 数据操作 > 性能 > 数据倾斜 | optimizer | rewrite | warning | Hive | `opt-winfuncskewedoptimization` | high |
| 精确浮点数建议使用Decimal或Number | UseDecimalForNumericColumns | 对象设计 > 列定义 > 数据类型 | audit | ddl | warning |  | `aud-usedecimalfornumericcolumns` | high |
| 索引中不应该有重复列 | DuplicateColumnsInIndex | 对象设计 > 索引 | audit | index | warning |  | `aud-duplicatecolumnsinindex` | high |
| 索引中的字段不可以为TEXT和LOB类型 | Text&LobColumnsInIndexDisallowed | 对象设计 > 索引 | audit? | index | warning |  | `aud-textlobcolumnsinindexdisallowed` | low |
| 索引中的字段数目超过阈值 | NumberOfColumnsInIndexExceedThreshold | 对象设计 > 索引 | audit | index | warning |  | `aud-numberofcolumnsinindexexceedthreshold` | high |
| 索引中避免使用可空列 | AvoidUsingNullableColumnsInIndex | 对象设计 > 索引 | audit | index | warning |  | `aud-avoidusingnullablecolumnsinindex` | high |
| 索引列上的运算导致索引失效 | RuleFuncWithColumnInPredicate | 数据操作 > 性能 > 索引失效 > 过滤条件 | audit | index | info |  | `aud-rulefuncwithcolumninpredicate` | high |
| 索引名不存在 | Index with this Name Does't Exists | 对象操作 > 语法错误 | audit | audit | error |  | `aud-index-with-this-name-doest-exists` | high |
| 索引名已存在 | Index with this Name Already Exists | 对象操作 > 语法错误 | audit | audit | error |  | `aud-index-with-this-name-already-exists` | high |
| 索引命名规范 | Index naming convention | 对象设计 > 命名规范 > 索引/约束命名应符合规范 | audit | index | info |  | `aud-index-naming-convention` | high |
| 索引失效或不可见 | Index Invalid or Invisible | 对象设计 > 索引 | audit | index | warning |  | `aud-index-invalid-or-invisible` | high |
| 索引必须要有名字 | IndexNameRequired | 对象设计 > 索引 | audit | index | info |  | `aud-indexnamerequired` | high |
| 索引的字段长度不应超过阈值 | LongLengthColumns4IndexDisallowed | 对象设计 > 索引 | audit | index | warning |  | `aud-longlengthcolumns4indexdisallowed` | high |
| 索引长度不得超过阈值 | TotalIndexLengthExceedThreshold | 对象设计 > 索引 | audit | index | info |  | `aud-totalindexlengthexceedthreshold` | high |
| 约束名已存在 | Constraint with this Name Already Exists | 对象操作 > 语法错误 | audit | audit | error |  | `aud-constraint-with-this-name-already-exists` | high |
| 经常更新的表应使用本地表 | FrequentlyUpdatedTablesShouldUseLocalTables | 数据操作 > 分布式 > 分布式事务 | audit | dml | info |  | `aud-frequentlyupdatedtablesshoulduselocaltables` | high |
| 脏页率超过阈值，建议进行回收 | High dirty page ratio | 对象设计 > 其他 | audit | ddl | warning |  | `aud-high-dirty-page-ratio` | high |
| 自增列不得使用有符号整数 | SignedInteger4IdentityColumnDisallowed | 对象设计 > 列定义 > 自增列 | audit | ddl | warning |  | `aud-signedinteger4identitycolumndisallowed` | high |
| 自增列命名规范 | Auto-increment column naming convention | 对象设计 > 命名规范 | audit | ddl | info |  | `aud-autoincrement-column-naming-convention` | high |
| 自增列的初始值应从0_1开始 | InitValue4IdentityColumn | 对象设计 > 列定义 > 自增列 | audit | ddl | warning |  | `aud-initvalue4identitycolumn` | high |
| 自增序列耗尽预警 | CacheExhausted4IdentityColumn | 对象设计 > 列定义 > 自增列 | audit | ddl | warning |  | `aud-cacheexhausted4identitycolumn` | high |
| 行数超过阈值的单表建议设计为分片表 | LargeTableShouldBeSharded | 对象设计 > 数据分布 | audit | ddl | info |  | `aud-largetableshouldbesharded` | high |
| 表_视图名不存在 | Table/View with this Name Does't Exists | 对象操作 > 语法错误 | audit | audit | error |  | `aud-tableview-with-this-name-doest-exists` | high |
| 表_视图名已存在 | Table/View with this Name Already Exists | 对象操作 > 语法错误 | audit | audit | error |  | `aud-tableview-with-this-name-already-exists` | high |
| 表上应使用指定的字符集 | SpecificCharSet4TableRequired | 对象设计 > 字符集/排序规则 | audit | ddl | warning | MySQL, PostgreSQL | `aud-specificcharset4tablerequired` | high |
| 表上应使用指定的排序规则 | SpecificCollation4TableRequired | 对象设计 > 字符集/排序规则 | audit | ddl | warning | MySQL | `aud-specificcollation4tablerequired` | high |
| 表关联字段数据类型长度不一致 | JoinColumnDataTypeMismatch | 数据操作 > 性能 > 表关联 | audit | dml | info |  | `aud-joincolumndatatypemismatch` | high |
| 表名命名规范 | Table naming convention | 对象设计 > 命名规范 | audit | ddl | info |  | `aud-table-naming-convention` | high |
| 表定义时禁止使用字符集 | CharsetOnTableDisallowed | 对象设计 > 字符集/排序规则 | audit | ddl | warning |  | `aud-charsetontabledisallowed` | high |
| 表必须包含的列名及数据类型 | SpecificColumnsRequired | 对象设计 > 表/视图定义 | audit | ddl | warning |  | `aud-specificcolumnsrequired` | high |
| 表必须建主键 | PrimaryKeyRequired | 对象设计 > 约束 | audit | ddl | error |  | `aud-primarykeyrequired` | high |
| 表必须有注释 | CommentsOnTableRequired | 对象设计 > 注释 | audit | ddl | warning | MySQL | `aud-commentsontablerequired` | high |
| 表的列数不建议超过阈值 | NumOfColumnsExceedThreshold | 对象设计 > 表/视图定义 | audit | ddl | warning |  | `aud-numofcolumnsexceedthreshold` | high |
| 表的字符集和数据库不一致 | CharsetsOnTable&DatabaseMismatch | 对象设计 > 字符集/排序规则 | audit | ddl | warning |  | `aud-charsetsontabledatabasemismatch` | high |
| 表连接消除 | JoinElimination | 数据操作 > 性能 > 表关联 | optimizer | rewrite | info |  | `opt-joinelimination` | high |
| 表连接缺少连接条件 | MissingJoinCondition | 数据操作 > 性能 > 表关联 | audit? | dml | info |  | `aud-missingjoincondition` | low |
| 表需定义更新时间戳列 | UpdateTimeStampColumnsRequired | 对象设计 > 表/视图定义 | audit | ddl | warning |  | `aud-updatetimestampcolumnsrequired` | high |
| 视图展开 | ViewExpansion | 数据操作 > 性能 > 子查询优化 | audit | dml | info |  | `aud-viewexpansion` | high |
| 访问分区表没有使用分区字段过滤 | Partition Table Queried Without Partition Key Filter | 数据操作 > 性能 > 条件过滤 | audit | dml | info |  | `aud-partition-table-queried-without-partition-key-fi` | high |
| 过滤条件中必须使用主键或索引列 | Filter Condition Must Use Primary Key or Index Column | 数据操作 > 性能 > 条件过滤 | audit | dml | info |  | `aud-filter-condition-must-use-primary-key-or-index-c` | high |
| 过滤谓词下推 | Filter Predicate Pushdown | 数据操作 > 性能 > 条件过滤 | optimizer | rewrite | info |  | `opt-filter-predicate-pushdown` | high |
| 连接字段类型不匹配导致索引失效 | Join Column Type Mismatch Causes Index Invalidation | 数据操作 > 性能 > 索引失效 > 关联条件 | audit | index | warning |  | `aud-join-column-type-mismatch-causes-index-invalidat` | high |
| 选择列标量子查询解关联 | Scalar Subquery Unnesting in Select List | 数据操作 > 性能 > 子查询优化 | optimizer | rewrite | info |  | `opt-scalar-subquery-unnesting-in-select-list` | high |
| 避免%开头的LIKE查询 | Avoid LIKE Pattern Starting with Wildcard | 数据操作 > 性能 > 索引失效 > 过滤条件 | audit | index | warning |  | `aud-avoid-like-pattern-starting-with-wildcard` | high |
| 避免COUNT DISTINCT多个可空列 | Avoid COUNT DISTINCT on Multiple Nullable Columns | 数据操作 > 正确性 > NULL值处理 | audit | dml | info |  | `aud-avoid-count-distinct-on-multiple-nullable-column` | high |
| 避免GROUP BY选择列的序号 | Avoid GROUP BY Column Ordinal Position | 数据操作 > 可维护性 | audit | dml | info |  | `aud-avoid-group-by-column-ordinal-position` | high |
| 避免ORDER BY选择列的序号 | Avoid ORDER BY Column Ordinal Position | 数据操作 > 可维护性 | audit | dml | info |  | `aud-avoid-order-by-column-ordinal-position` | high |
| 避免ORDERBY字段来自不同表 | Avoid ORDER BY Columns from Different Tables | 数据操作 > 性能 > 索引失效 > 排序 | audit | index | info |  | `aud-avoid-order-by-columns-from-different-tables` | high |
| 避免limit子句的查询语句使用for update | Avoid SELECT with LIMIT and FOR UPDATE | 数据操作 > 性能 > 其他 | audit | dml | warning | MySQL | `aud-avoid-select-with-limit-and-for-update` | high |
| 避免不同字段的OR条件 | Avoid OR Conditions on Different Columns | 数据操作 > 性能 > 索引失效 > 过滤条件 | audit | index | warning |  | `aud-avoid-or-conditions-on-different-columns` | high |
| 避免不必要的去重操作 | Avoid Unnecessary DISTINCT Operations | 数据操作 > 性能 > 其他 | audit | dml | info |  | `aud-avoid-unnecessary-distinct-operations` | high |
| 避免不必要的更新操作 | Avoid Unnecessary UPDATE Operations | 数据操作 > 性能 > 其他 | audit | dml | info |  | `aud-avoid-unnecessary-update-operations` | high |
| 避免使用CROSS JOIN | Avoid CROSS JOIN | 数据操作 > 性能 > 表关联 | audit | dml | warning |  | `aud-avoid-cross-join` | high |
| 避免使用NATURAL JOIN | Avoid NATURAL JOIN | 数据操作 > 可维护性 | audit | dml | warning |  | `aud-avoid-natural-join` | high |
| 避免使用STRAIGHT JOIN | Avoid STRAIGHT JOIN | 数据操作 > 性能 > 表关联 | audit | dml | warning | MySQL | `aud-avoid-straight-join` | high |
| 避免使用不必要的内置函数 | Avoid Unnecessary Built-in Functions | 数据操作 > 安全性 | audit | dml | info |  | `aud-avoid-unnecessary-builtin-functions` | high |
| 避免使用标量子查询 | Avoid Scalar Subqueries | 数据操作 > 性能 > SQL复杂度 | audit | dml | info |  | `aud-avoid-scalar-subqueries` | high |
| 避免使用没有通配符的 LIKE 查询 | Avoid LIKE Without Wildcards | 数据操作 > 正确性 | audit | dml | warning |  | `aud-avoid-like-without-wildcards` | high |
| 避免使用随机函数排序 | Avoid ORDER BY Random Function | 数据操作 > 性能 > 排序分组 | audit | dml | warning |  | `aud-avoid-order-by-random-function` | high |
| 避免在SELECT语句中使用LIMIT而没有ORDER BY | Avoid LIMIT Without ORDER BY in SELECT | 数据操作 > 正确性 | audit | dml | warning |  | `aud-avoid-limit-without-order-by-in-select` | high |
| 避免在SELECT语句添加FOR UPDATE | Avoid SELECT with FOR UPDATE | 数据操作 > 性能 > 其他 | audit | dml | warning |  | `aud-avoid-select-with-for-update` | high |
| 避免在UPDELETE语句中使用LIMIT而没有ORDER  | Avoid LIMIT Without ORDER BY in UPDATE/DELETE | 数据操作 > 正确性 | audit | dml | warning |  | `aud-avoid-limit-without-order-by-in-updatedelete` | high |
| 避免在查询中使用SELECT _ | Avoid SELECT * | 数据操作 > 可维护性 | audit | dml | info |  | `aud-avoid-select` | high |
| 避免对条件字段使用负向查询 | Avoid Negative Queries on Filter Columns | 数据操作 > 性能 > 索引失效 > 过滤条件 | audit | index | warning |  | `aud-avoid-negative-queries-on-filter-columns` | high |
| 避免对长字段进行分组 | Avoid GROUP BY on Long Columns | 数据操作 > 性能 > 排序分组 | audit | dml | warning |  | `aud-avoid-group-by-on-long-columns` | high |
| 避免对长字段进行排序 | Avoid ORDER BY on Long Columns | 数据操作 > 性能 > 排序分组 | audit | dml | warning |  | `aud-avoid-order-by-on-long-columns` | high |
| 避免常量字符串开头或结尾包含空格 | Avoid Leading or Trailing Spaces in String Literals | 数据操作 > 正确性 | audit | dml | warning |  | `aud-avoid-leading-or-trailing-spaces-in-string-liter` | high |
| 避免无条件且无分组的SELECT语句 | Avoid SELECT Without WHERE and GROUP BY | 数据操作 > 性能 > 减少访问数据量 | audit | dml | info |  | `aud-avoid-select-without-where-and-group-by` | high |
| 避免无条件的UPDELETE语句 | Avoid Unconditional UPDATE/DELETE Statements | 数据操作 > 正确性 | audit | dml | warning |  | `aud-avoid-unconditional-updatedelete-statements` | high |
| 避免更新主键的值 | Avoid Updating Primary Key Values | 数据操作 > 性能 > 其他 | audit | dml | warning |  | `aud-avoid-updating-primary-key-values` | high |
| 避免更新唯一约束的值 | Avoid Updating Unique Constraint Values | 数据操作 > 性能 > 其他 | audit | dml | warning |  | `aud-avoid-updating-unique-constraint-values` | high |
| 避免有派生表的查询语句使用for update | Avoid FOR UPDATE with Derived Tables | 数据操作 > 正确性 | audit | dml | warning | MySQL | `aud-avoid-for-update-with-derived-tables` | high |
| 避免查询排序时指定COLLATION | Avoid Specifying COLLATION in ORDER BY | 数据操作 > 性能 > 索引失效 > 排序 | audit | index | warning |  | `aud-avoid-specifying-collation-in-order-by` | high |
| 避免表关联字段不是分布键 | Avoid Joining on Non-Distribution Key Columns | 对象设计 > 数据分布 | audit | ddl | warning | 分布式数据库（包括但不限于：openGauss、PostgreSQL-XL、TDSQL、OceanBase、TiDB、DWS 等） | `aud-avoid-joining-on-nondistribution-key-columns` | high |
| 避免表引用使用重复的别名 | Avoid Duplicate Table Aliases | 数据操作 > 可维护性 | audit | dml | warning |  | `aud-avoid-duplicate-table-aliases` | high |
| 长度大于阈值的字段建立索引时使用前缀 | Use Prefix Index for Long VARCHAR Columns | 对象设计 > 索引 | audit | index | warning |  | `aud-use-prefix-index-for-long-varchar-columns` | high |
| 隐式类型转换导致索引失效 | Implicit Type Conversion Causes Index Invalidation | 数据操作 > 性能 > 索引失效 > 过滤条件 | audit | index | warning |  | `aud-implicit-type-conversion-causes-index-invalidati` | high |
| 非列表中的列应设置非空默认值 | Non-Null Default Value Required for Non-Excluded Columns | 对象设计 > 列定义 > 默认值 | audit | ddl | warning |  | `aud-nonnull-default-value-required-for-nonexcluded-c` | high |
| 非空列需指定带默认值 | Default Value Required for NOT NULL Columns | 对象设计 > 列定义 > 默认值 | audit | ddl | warning |  | `aud-default-value-required-for-not-null-columns` | high |

## E. 分批建议

- **P0（结构化 Reference）**：D 表全部（audit/optimizer 逐条 → metadata/rules 双语 + 生成页）；metadata/databases 兼容矩阵；configs。
- **P1（手册/产品页）**：20-engine/install、30-cloud（guides/install）、40-audit/manuals、50-integration（plugins/mcp/devops）、60-migration。
- **P2（Blog/Release/FAQ）**：20-engine/internals、70-content、99-待归类、10-product/about、reviews/comparisons。
- **P3（知识层）**：RAG/MCP（用已发布 docs）。

---
覆盖统计：全量 = 525；A(迁入)=142，B(排除)=104，C(去重归档)=18，D(规则 261)=261，A0(其余未归类)=0。