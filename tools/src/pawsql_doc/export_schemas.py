"""Export pydantic content models to JSON Schema files under <root>/schemas.

Keeps the hand-written YAML world and the JSON Schema world in sync:
schemas/*.json are generated artifacts, not edited by hand.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Type

from pydantic import BaseModel

from pawsql_doc import models

EXPORTS: Dict[str, Type[BaseModel]] = {
    "frontmatter": models.FrontMatter,
    "product": models.ProductMetadata,
    "feature-manifest": models.FeatureManifest,
    "rule-metadata": models.RuleMetadata,
    "database-metadata": models.DatabaseMetadata,
    "config-metadata": models.ConfigMetadata,
    "documentation-mapping": models.DocumentationMapping,
    "documentation-policy": models.DocumentationPolicy,
}


def export_schemas(root: Path) -> None:
    schema_dir = root / "schemas"
    schema_dir.mkdir(parents=True, exist_ok=True)
    for name, model in EXPORTS.items():
        target = schema_dir / f"{name}.schema.json"
        schema = model.model_json_schema()
        schema.setdefault("description", f"PawSQL {name} content model (generated).")
        target.write_text(
            json.dumps(schema, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
