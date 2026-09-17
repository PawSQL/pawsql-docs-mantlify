"""Auditable, idempotent content v2 migration; default dry run."""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from pawsql_doc.models.governance import LEGACY_TYPES
from pawsql_doc.validate import content_files, parse_frontmatter


def classify(data, route):
    data = dict(data)
    old = data.get("type")
    if old in LEGACY_TYPES:
        data["type"], subtype = LEGACY_TYPES[old]
        if subtype:
            data["subtype"] = subtype
    checks = [
        ("use-cases/", "use-case", None), ("features/", "explanation", None),
        ("reference/audit-rules/", "reference", "rule"),
        ("reference/optimizer-rules/", "reference", "rule"),
        ("reference/compatibility/", "reference", "database"),
        ("reference/database/", "reference", "database"),
        ("supported-databases", "reference", "database"),
        ("reference/configuration/", "reference", "configuration"),
        ("reference/api/", "reference", "api"),
        ("blog/", "article", "blog"), ("changelog/", "article", "release-note"),
        ("release-notes/", "article", "release-note"),
        ("contributing/terminology", "reference", "glossary"),
    ]
    for token, kind, subtype in checks:
        if token in route:
            data["type"] = kind
            if subtype:
                data["subtype"] = subtype
            else:
                data.pop("subtype", None)
            break
    if "quickstart" in route:
        data.update(type="guide", subtype="quickstart")
    if "contributing/" in route and "terminology" not in route:
        data.update(type="guide", subtype="operation")
    if route in {"index.mdx", "en/index.mdx", "getting-started/overview.mdx", "en/getting-started/overview.mdx"}:
        data.update(type="explanation")
        data.pop("subtype", None)
    language = "en" if route.startswith("en/") else "zh"
    if language == "en" and route in {"en/index.mdx", "en/blog/index.mdx"}:
        data["id"] = "en-" + data["id"].removeprefix("en-")
    data["language"] = language
    data.setdefault("translationKey", data.get("localeOf", data.get("id", "")) if language == "en" else data.get("id", ""))
    if data["translationKey"].startswith("en-"):
        data["translationKey"] = data["translationKey"][3:]
    if data["translationKey"].startswith("zh-"):
        data["translationKey"] = data["translationKey"][3:]
    # Only collection routes are indexes; cloud/index is an actual manual.
    collections = ("reference/audit-rules/", "reference/optimizer-rules/", "reference/compatibility/", "reference/database/", "blog/", "changelog/", "release-notes/", "use-cases/", "features/", "faq/", "tutorials/")
    stem = route.removeprefix("en/")
    data["layout"] = "index" if any(stem == p + "index.md" or stem == p + "index.mdx" for p in collections) else "detail"
    if "supported-databases" in route:
        data["layout"] = "index"
    if data.get("product") != "pawsql":
        previous = data.get("product", "")
        component = previous.removeprefix("pawsql-")
        if component in {"engine", "optimizer", "auditor", "advisor", "patroller"}:
            data.setdefault("components", [component])
        if component == "cloud":
            data.setdefault("deployments", ["public-cloud"])
        data["product"] = "pawsql"
    return data


def migrate(root: Path, apply=False):
    changes = []
    import hashlib
    manifest_path = root / "metadata/documentation/generated-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    manifest_changed = False
    for path in content_files(root):
        text = path.read_text(encoding="utf-8-sig")
        data, error = parse_frontmatter(text)
        if not data or error:
            continue
        result = classify(data, path.relative_to(root / "docs").as_posix())
        if result == data:
            continue
        rel = path.relative_to(root).as_posix()
        if rel in manifest and hashlib.sha256(path.read_bytes()).hexdigest() != manifest[rel]:
            raise ValueError(f"migration would overwrite an externally modified generated file: {rel}")
        changes.append(path.relative_to(root).as_posix())
        if apply:
            # Preserve all authored body text, including existing user edits.
            match = re.match(r"\A---\r?\n.*?\r?\n---(?=\r?\n|$)", text, re.S)
            if not match:
                raise ValueError(f"invalid frontmatter: {path}")
            path.write_text("---\n" + yaml.safe_dump(result, allow_unicode=True, sort_keys=False) + "---" + text[match.end():], encoding="utf-8", newline="\n")
            if rel in manifest:
                manifest[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
                manifest_changed = True
    if apply and manifest_changed:
        manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    return changes


def inventory(root: Path):
    result = []
    for path in content_files(root):
        data, error = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        result.append({"path": path.relative_to(root).as_posix(), "frontmatter": data, "error": error})
    return result


def migrate_metadata(root: Path, apply=False):
    """Mechanical changes only. Preserve comments preceding the YAML mapping."""
    changes = []
    documents = {}
    for file in content_files(root):
        fm, err = parse_frontmatter(file.read_text(encoding="utf-8-sig"))
        if fm and not err:
            documents[file.relative_to(root).as_posix()] = {"documentId": fm["id"], "language": fm.get("language", "en" if "/en/" in file.as_posix() else "zh")}
    for category in ("features", "rules", "databases", "configs", "mappings"):
        for path in sorted((root / "metadata" / category).rglob("*.yaml")):
            text = path.read_text(encoding="utf-8-sig")
            data = yaml.safe_load(text)
            original = json.dumps(data, sort_keys=True)
            if category == "features":
                old = data.get("product", "").removeprefix("pawsql-")
                data["product"] = "pawsql"
                data.pop("type", None)
                if old in {"engine", "optimizer", "auditor", "advisor", "patroller"}:
                    data.setdefault("components", [old])
                for requirement in data.get("documentation", {}).values():
                    paths = requirement.get("paths", [])
                    matched = [documents[p] for p in paths if p in documents]
                    if matched:
                        requirement["documents"] = requirement.get("documents", []) + matched
                        requirement["paths"] = [p for p in paths if p not in documents]
            if category == "mappings":
                for doc in data.get("documents", []):
                    if doc.get("path") in documents:
                        doc.update(documents[doc.pop("path")])
            if category == "rules":
                data.setdefault("kind", path.parent.name)
                data.setdefault("product", "pawsql")
                data.setdefault("applicability", {"status": "pending"})
                for content in data.get("content", {}).values():
                    if content:
                        content.setdefault("editorial", {"status": "draft", "owners": []})
            if category in {"databases", "configs"} and not data.get("content"):
                prose = {k: data.pop(k) for k in ("description", "notes", "keyFeatures", "example") if k in data}
                if prose:
                    prose["editorial"] = {"status": "draft"}
                    data["content"] = {"en": prose}
            if category == "databases" and not data.get("compatibility"):
                # Legacy claims remain in features, but have no verification evidence.
                mapping = {"optimizer": "sql-rewrite", "audit": "sql-audit", "planVisualizer": "plan-visualization"}
                data["compatibility"] = [
                    {"databaseVersions": data.get("supportedVersions", []), "capability": mapping[k], "status": "unknown", "evidenceIds": []}
                    for k in data.get("features", {}) if k in mapping
                ]
            if category == "configs":
                data.setdefault("behavior", {"activation": "unknown"})
            if json.dumps(data, sort_keys=True) != original:
                changes.append(path.relative_to(root).as_posix())
                if apply:
                    comments = []
                    for line in text.splitlines():
                        if line.startswith("#") or not line.strip():
                            comments.append(line)
                        else:
                            break
                    path.write_text("\n".join(comments) + "\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8", newline="\n")
    return changes


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    print(json.dumps(migrate(args.root, args.apply), ensure_ascii=True, indent=2))
