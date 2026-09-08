# 内容模板与审核要求（v2）

产品统一为 `pawsql`。类型：explanation、guide、use-case、reference、support、article。
详情页使用 `layout: detail`，目录使用 `layout: index`。子类型与取值以
`schemas/frontmatter-v2.schema.json` 为准；兼容 Schema 只用于读取旧内容。

| 类型 | 建议正文结构（不是字数指标） |
|---|---|
| explanation | 定义、用途、机制、限制、下一步 |
| guide | 目标、前提、步骤、预期结果、验证、故障入口 |
| use-case | 用户、问题、目标、流程、依赖、成功标准 |
| reference | 标识、事实、适用范围、限制、示例、依据 |
| support | 症状、诊断、处理、验证 |
| article | 主题、正文、来源、责任人、日期 |

草稿可以缺项。发布时使用 `sections` 将语义槽位映射到实际正文标题，避免固定中文标题：

```yaml
id: example-guide
translationKey: example-guide
language: zh
product: pawsql
title: 示例操作指南
description: 人工编写的一句话摘要。
type: guide
subtype: operation
layout: detail
status: draft
sections:
  goal: 操作目标
  prerequisites: 准备工作
  steps: 操作步骤
  expectedResult: 预期结果
  verification: 验证结果
  troubleshooting: 故障处理
```

该映射只确认标题存在，不能代替内容审核或数据库执行验证。
安装指南还需环境依赖、启动验证与卸载入口；集成指南需两端版本、权限及连通验证；
升级/迁移指南需备份、起止环境、兼容差异及回退条件。
发布说明需产品/组件版本、日期、变化和升级动作。

规则直接维护 metadata，不使用人工详情页模板。优化规则必须补 NULL、重复行等相关边界，
审核规则应表达预期触发/不触发；案例 `pending` 不等同于执行通过。
