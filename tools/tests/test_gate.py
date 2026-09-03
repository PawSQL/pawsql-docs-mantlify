from __future__ import annotations

from pathlib import Path

import yaml

from pawsql_doc.gate import (
    coverage_report,
    find_drift,
    format_issues,
    run_release_gate,
)
from pawsql_doc.generators import build_references


def _build(repo):
    from pawsql_doc.loaders import load_metadata

    bundle, issues = load_metadata(repo)
    assert issues == []
    build_references(repo, bundle)


def test_drift_reports_missing_before_generation(repo):
    missing = find_drift(repo)
    assert any("reference-doc" in i.field for i in missing)
    formatted = format_issues(missing)
    assert any(f.startswith("DOC-DRIFT") for f in formatted)


def test_gate_green_after_generation(repo):
    _build(repo)
    passed, lines, missing = run_release_gate(repo)
    assert passed
    assert missing == []
    assert all(line.ok == line.total for line in lines)
    assert len(lines) == 6


def test_delete_guide_fails_gate(repo):
    _build(repo)
    target = repo / "docs/databases/postgresql/index.md"
    target.unlink()
    passed, _, missing = run_release_gate(repo)
    assert not passed
    assert any("docs/databases/postgresql/index.md" in i.reason for i in missing)
    assert any("DOC-DRIFT" in f for f in format_issues(missing))


def test_required_mapping_doc_missing_detected(repo):
    # reference an existing feature but a missing required doc
    mapping = {
        "feature": "F-OPT-1",
        "documents": [{"path": "docs/user-guide/never-written.md", "relation": "user-guide", "required": True}],
    }
    (repo / "metadata/mappings/missing.yaml").write_text(
        yaml.safe_dump(mapping, sort_keys=False), encoding="utf-8"
    )
    missing = find_drift(repo)
    assert any(i.field == "documents.path" for i in missing)


def test_coverage_report_categories(repo):
    _build(repo)
    lines = {line.category: line for line in coverage_report(repo)}
    assert lines["audit-rule-reference"].ok == 1
    assert lines["optimizer-rule-reference"].ok == 1
    assert lines["database-reference"].ok == 1
    assert lines["config-reference"].ok == 1
