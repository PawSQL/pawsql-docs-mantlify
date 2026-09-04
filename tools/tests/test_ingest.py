from __future__ import annotations

from pawsql_doc.ingest import parse_rule_doc, render_skeleton

SAMPLE = """# 禁止为列新增默认值

为列新增默认值之后，将来难以移除默认值（部分数据库不支持直接删除列默认值），且默认值在批量导入/迁移时容易与业务预期不符。应避免在表结构定义阶段轻易为列增加默认值。

#### 英文名
- Disallow Adding Default Values to Columns

#### 类别
- 对象设计 > 列定义 > 默认值

#### 审查对象
- `ALTER TABLE`

#### SQL样例
```sql
-- ❌ 不推荐：为已有列新增默认值
ALTER TABLE t ALTER COLUMN c SET DEFAULT 0;

-- ✅ 推荐：不要随意为列新增默认值；确需默认值时随建表一并定义
CREATE TABLE t (c INT DEFAULT 0);
```

#### 默认预警级别
- **警告 (Warning)**

#### 触发条件
- 语句对已有列执行了新增默认值的操作

#### 可配置
- 否

#### 数据库类型
- ALL
"""


def test_parse_rule_doc_fields():
    doc = parse_rule_doc(SAMPLE)
    assert doc.zh_name == "禁止为列新增默认值"
    assert doc.en_name == "Disallow Adding Default Values to Columns"
    assert doc.category_path == "对象设计 > 列定义 > 默认值"
    assert doc.review_objects == ["`ALTER TABLE`"]
    assert doc.severity_zh == "警告"
    assert doc.severity == "warning"
    assert doc.database_raw == []
    assert doc.triggers and "新增默认值" in doc.triggers[0]
    assert "❌" in doc.bad_sql and "ALTER COLUMN c SET DEFAULT" in doc.bad_sql
    assert "✅" in doc.good_sql and "CREATE TABLE t (c INT DEFAULT 0)" in doc.good_sql
    assert "新增默认值之后" in doc.intro


def test_render_skeleton_shape():
    doc = parse_rule_doc(SAMPLE)
    text = render_skeleton("aud-disallow-adding-default-values", "ddl", doc, "audit", "20-engine/rules/规则文档/x.md")
    assert text.startswith("# Canonical source: vault")
    assert "TODO(产品核对)" in text
    assert "id: aud-disallow-adding-default-values" in text
    assert "category: ddl" in text
    assert "severity: warning" in text
    assert "name: Disallow Adding Default Values to Columns" in text
    # zh content extracted from the doc, nothing invented
    assert "禁止为列新增默认值" in text
    assert "badExample" in text
    # prose sits under content.zh; en only carries the source-provided name
    assert "  zh:\n    name: 禁止为列新增默认值" in text
    assert "  en:\n    name: Disallow Adding Default Values to Columns" in text
    assert "description: 为列新增默认值之后" in text


def test_all_database_means_empty():
    doc = parse_rule_doc(SAMPLE)
    assert doc.database_raw == []


def test_review_tags_split_on_separators():
    from pawsql_doc.ingest import RuleDoc

    doc = RuleDoc(zh_name="x", review_objects=["`CREATE INDEX`、`ALTER TABLE ADD INDEX`", "`SELECT`"])
    text = render_skeleton("aud-x", "ddl", doc, "audit", "src")
    assert "review:CREATE INDEX" in text
    assert "review:ALTER TABLE ADD INDEX" in text
    assert "review:SELECT" in text
    assert "`、" not in text
