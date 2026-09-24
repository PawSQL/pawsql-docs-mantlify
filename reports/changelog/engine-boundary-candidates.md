# engine 历史发布的候选边界提交（待核对）

生成自 `E:/Workspace/pawsql-core` 主干 `master`：顶端 2026-09-23 `70b9e97d`，且与 `origin/master` 完全同步（无本地独有提交，tag 可直接推上去）。
候选规则：取**当月主干上的最后一个提交**作为该月的边界提交，即「该版本包含到此为止」。

## 核对要点

1. **哪些月真的交付了**：下表按「每月一版」给出候选。若实际交付不是每月一次，删掉未交付的行即可。
2. **月中交付**：候选一律取月末提交。若某版是月中切的，把该行的日期改成真实交付日，我再换成当日的提交。
3. **候选版本号那列是占位**：命名口径未定，见文末。
4. 最旧的边界（2022-05）没有前驱，在 changelog 里只作起点，不产出条目。

## 候选表

| 月份 | 提交数 | 候选边界日期 | commit | 该提交主题 | 候选版本号（待定） |
|---|---|---|---|---|---|
| 2022-05 | 3 | 2022-05-12 | `47e7c4c1` | fix alias process support view | 2022.05 |
| 2022-06 | 8 | 2022-06-30 | `c676a3a7` | container for every SQLQueryObject | 2022.06 |
| 2022-07 | 7 | 2022-07-25 | `61d8c5b6` | add if(predicate, value1, values) support for mysql. | 2022.07 |
| 2022-08 | 7 | 2022-08-30 | `171b1b16` | 1.DDL loader support pg_dump and mysqldump file 2.Improve p… | 2022.08 |
| 2022-09 | 5 | 2022-09-22 | `70ad234e` | 1. add ValueExpressionTimestampFunction to support timestam… | 2022.09 |
| 2022-10 | 7 | 2022-10-22 | `3c2345cf` | fix delete statement parsing | 2022.10 |
| 2022-11 | 12 | 2022-11-29 | `74e589dd` | transformer for oracle syntax | 2022.11 |
| 2022-12 | 23 | 2022-12-30 | `82cc7cd7` | order columns merge bug fixing. add PostgresVar($1) support… | 2022.12 |
| 2023-01 | 13 | 2023-01-30 | `331921c6` | 1. add regex predicate support for mysql and postgresql, in… | 2023.01 |
| 2023-02 | 15 | 2023-02-28 | `92aed38d` | support `create view as (select 1)` and '(t as t1 join t as… | 2023.02 |
| 2023-03 | 16 | 2023-03-31 | `ad56f09c` | unique constraint parsing | 2023.03 |
| 2023-04 | 69 | 2023-04-16 | `a5ed26d5` | improve SATTC for in(null) processing | 2023.04 |
| 2023-05 | 90 | 2023-05-31 | `cb885804` | StatementExtractor enhancement, validate syntax | 2023.05 |
| 2023-06 | 72 | 2023-06-29 | `50d1c5b6` | add a loadQueries with query text as input | 2023.06 |
| 2023-07 | 143 | 2023-07-31 | `6f32ba6f` | qualify table if there are two schemas in config | 2023.07 |
| 2023-08 | 76 | 2023-08-31 | `be065cde` | try sll first in sql parser | 2023.08 |
| 2023-09 | 67 | 2023-09-27 | `863c5688` | fix bug in SATRewriter for is null/is not null. | 2023.09 |
| 2023-10 | 38 | 2023-10-30 | `851dc652` | add pg datatype bpchar | 2023.10 |
| 2023-11 | 60 | 2023-11-30 | `8f9b16c9` | qualify columns for oracle in writer | 2023.11 |
| 2023-12 | 96 | 2023-12-31 | `2c5904ab` | Merge branch 'master' into AuditBranch | 2023.12 |
| 2024-01 | 65 | 2024-01-18 | `42ccc384` | add RulePredicateSSQRewrite, fix bug in ProjectionPushdownR… | 2024.01 |
| 2024-02 | 21 | 2024-02-27 | `f186bcaf` | universal ddlparser improvements | 2024.02 |
| 2024-03 | 13 | 2024-03-29 | `177b1116` | explain syntax optimization | 2024.03 |
| 2024-04 | 28 | 2024-04-29 | `5be20ad4` | move tigerose to pawsql | 2024.04 |
| 2024-05 | 41 | 2024-05-27 | `b7e86fb8` | add a TODO, otherwise, for 2 type. there will be more resul… | 2024.05 |
| 2024-06 | 9 | 2024-06-26 | `f02e4911` | 1. support #{name} 2. polardb drds, gaussdbdws 兼容分库分表语法, TO… | 2024.06 |
| 2024-07 | 59 | 2024-07-31 | `a91ee237` | bug fixing | 2024.07 |
| 2024-08 | 26 | 2024-08-30 | `796079a9` | for RuleJoinEliminationRewrite, 如果是内连接，必须是主外键关系; 而外连接只需要非空唯一 | 2024.08 |
| 2024-09 | 26 | 2024-09-30 | `86e9a47a` | if the input sql is a create as select statement, optimize … | 2024.09 |
| 2024-10 | 15 | 2024-10-30 | `d3801962` | disable QueryFolding for oracle | 2024.10 |
| 2024-11 | 19 | 2024-11-30 | `fe398804` | disable queryfolding for dameng | 2024.11 |
| 2024-12 | 40 | 2024-12-31 | `ea7eb51c` | 修复一个表上存在多个重名的约束的缺陷 | 2024.12 |
| 2025-01 | 6 | 2025-01-16 | `044d0179` | fix a bug in DBConfig.isShardingDatabase | 2025.01 |
| 2025-02 | 19 | 2025-02-27 | `4aef7700` | support local and global variable definition in  in sqlpars… | 2025.02 |
| 2025-03 | 31 | 2025-03-31 | `ea71a2f6` | support local/global variables and replace it in query | 2025.03 |
| 2025-04 | 33 | 2025-04-30 | `2f7b62d5` | following rules will be executed after all statements are p… | 2025.04 |
| 2025-05 | 26 | 2025-05-30 | `7dc60408` | SQLParserManager, for mssql, use SQLScriptParser; implement… | 2025.05 |
| 2025-06 | 20 | 2025-06-27 | `723b5421` | 修復mssql的表定義解析 | 2025.06 |
| 2025-07 | 10 | 2025-07-30 | `32351dc0` | fix a bug about online partitioned clause parsing for hive;… | 2025.07 |
| 2025-08 | 12 | 2025-08-29 | `9fcbb50a` | add line information for sqlobjects | 2025.08 |
| 2025-09 | 31 | 2025-09-30 | `8108de7b` | 所有SQL在性能验证时都进行SQL转换，以消除SQL中存在变量导致验证失败 | 2025.09 |
| 2025-10 | 20 | 2025-10-30 | `cdcbac4b` | 修复sattc推荐重复条件的缺陷 | 2025.10 |
| 2025-11 | 13 | 2025-11-27 | `5a29cc1d` | 对于oracle的这些函数，不需要添加括号。                   //SYSTIMESTAMP    … | 2025.11 |
| 2025-12 | 23 | 2025-12-29 | `62ca3954` | 修复字典 | 2025.12 |
| 2026-01 | 18 | 2026-01-30 | `9c42452b` | 修复type1查询折叠时的cte处理逻辑 | 2026.01 |
| 2026-02 | 7 | 2026-02-25 | `1cb3417b` | support arrayComparison predicate | 2026.02 |
| 2026-03 | 22 | 2026-03-30 | `87d4b135` | 将冗余索引和重复索引检查区分开，使用不用的预警级别RuleDuplicateIndexDisallowed | 2026.03 |
| 2026-04 | 50 | 2026-04-30 | `648ac6da` | groupconcat修改为analyticfunction | 2026.04 |
| 2026-05 | 18 | 2026-05-28 | `e325f3a5` | 优化NotInNullableSubQueryRewrite和UnnecessaryDistinctEliminati… | 2026.05 |
| 2026-06 | 35 | 2026-06-30 | `1e834105` | 支持create extension for pg | 2026.06 |
| 2026-07 | 4 | 2026-07-23 | `780b235c` | IncColumn4PrimaryKeyRequired只对非分布式数据库生效;IncColumn4PrimaryKe… | 2026.07 |
| 2026-08 | 4 | 2026-08-26 | `c9350d0e` | 如果database为空，某些数据库使用用户名作为database | 2026.08 |
| 2026-09 | 1 | 2026-09-23 | `70b9e97d` | 新增规则 EmptyString4DefaultDisallowed/ PKOrUINotContainingShar… | 2026.09 |

共 53 个月（2022-05 ~ 2026-09），无空月。

## 待定：版本号命名口径

两选一，直接决定 changelog 页面上的版本标题：

- **日期式 `2026.06`**：与提交节奏天然对齐，零歧义；但与文档站既有的产品版本轴（`metadata/features/*.yaml` 的
  `introducedVersion: 8.5.0`、规则页的「引入版本 8.5.0」）对不上，会出现两条互不相干的版本轴。
- **产品版本 `8.5.0`**：engine 的 tag 直接沿用该次发布的产品版本号，engine changelog 的标题就能与规则/特性的
  「引入版本」对齐，整站一条轴。前提是你们能给出「产品版本 ↔ 交付时点」的对应关系（这次核对的产出正好就是它）。

## 附：master 上的分支情况

所有交付提交都在 `master` 上（含 `workable jar for tpds`、`workable version as HiveBranch` 这两个发包提交）。
`origin/TSQLBranch` 与 `master` 同顶端；`origin/HiveBranch`(2025-05)、`origin/AuditBranch`(2024-07)、
`origin/oracle_version`(2023-06)、`origin/cloud(dev)`(2023-09) 均已停更，不影响边界选取。
