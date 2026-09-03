from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A throwaway PawSQL docs repo with one entry per metadata kind."""
    root = tmp_path / "repo"
    (root / "metadata" / "products").mkdir(parents=True)
    (root / "metadata" / "features").mkdir(parents=True)
    (root / "metadata" / "rules" / "audit").mkdir(parents=True)
    (root / "metadata" / "rules" / "optimizer").mkdir(parents=True)
    (root / "metadata" / "databases").mkdir(parents=True)
    (root / "metadata" / "configs").mkdir(parents=True)
    (root / "metadata" / "mappings").mkdir(parents=True)
    (root / "metadata" / "policies").mkdir(parents=True)
    (root / "docs.json").write_text("{}", encoding="utf-8")

    _write_yaml(root / "metadata/products/optimizer.yaml", {
        "id": "pawsql-optimizer", "name": "PawSQL Optimizer", "kind": "optimizer",
    })
    _write_yaml(root / "metadata/features/f1.yaml", {
        "id": "F-OPT-1", "name": "Feature One", "type": "optimizer",
        "product": "pawsql-optimizer", "introducedVersion": "8.5.0",
    })
    _write_yaml(root / "metadata/rules/audit/aud-one.yaml", {
        "id": "AUD-ONE", "name": "Audit One", "category": "select",
        "severity": "warning", "database": ["mysql", "postgresql"],
    })
    _write_yaml(root / "metadata/rules/optimizer/rewrite.yaml", {
        "id": "OPT-REWRITE", "name": "Rewrite One", "category": "rewrite",
    })
    _write_yaml(root / "metadata/databases/pg.yaml", {
        "database": "postgresql", "supportedVersions": ["16"],
        "features": {"optimizer": True},
    })
    _write_yaml(root / "metadata/configs/explain-timeout.yaml", {
        "id": "C-TIMEOUT", "name": "explain.timeout", "configType": "integer",
        "default": 30, "scope": "optimizer",
    })
    _write_yaml(root / "metadata/mappings/m1.yaml", {
        "feature": "F-OPT-1", "documents": [],
    })
    _write_yaml(root / "metadata/policies/policy.yaml", {"policies": {}})
    return root


def _write_yaml(path: Path, data: dict) -> None:
    import yaml

    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
