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
from pawsql_doc.models.governance import SUBTYPES

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
        if name == "frontmatter":
            schema["description"] = "Compatibility schema; frontmatter-v2.schema.json defines canonical documents."
        schema.setdefault("description", f"PawSQL {name} content model (generated).")
        target.write_text(
            json.dumps(schema, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8", newline="\n",
        )
        if name == "frontmatter":
            canonical = json.loads(json.dumps(schema))
            canonical["properties"]["type"] = {"type": "string", "enum": list(SUBTYPES)}
            canonical["required"] = sorted(set(canonical.get("required", [])) | {"layout", "language", "translationKey", "product"})
            canonical["properties"]["language"] = {"enum": ["zh", "en"]}
            canonical["properties"]["product"] = {"const": "pawsql"}
            canonical["allOf"] = [
                {"if": {"properties": {"type": {"const": kind}}, "required": ["type"]},
                 "then": {"properties": {"subtype": {"enum": sorted(allowed, key=str)}},
                          **({"required": ["subtype"]} if None not in allowed else {})}}
                for kind, allowed in SUBTYPES.items()
            ]
            (schema_dir / "frontmatter-v2.schema.json").write_text(json.dumps(canonical, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
