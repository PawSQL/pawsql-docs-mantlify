"""Stage generated artifacts and fail closed on release readiness."""
from __future__ import annotations
import hashlib
import json
import shutil
import tempfile
from pathlib import Path
from pawsql_doc.generators import build_references
from pawsql_doc.loaders import load_metadata
from pawsql_doc.quality import quality_report


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(root: Path, mode="preview", output: Path | None = None):
    root = root.resolve()
    if mode == "release":
        report = quality_report(root, publication=True)
        if any(report.values()):
            raise ValueError("release not ready: " + ", ".join(f"{key}={len(value)}" for key, value in report.items()))
        if output is None:
            raise ValueError("release requires --output (new staging directory)")
        output = output.resolve()
        if output.exists() or output == root or output in root.parents or root in output.parents:
            raise ValueError("release output must be a new directory outside the source repository")
    bundle, issues = load_metadata(root)
    if issues:
        raise ValueError("invalid metadata")
    manifest_path = root / "metadata/documentation/generated-manifest.json"
    previous = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    for rel in previous:
        resolved = (root / rel).resolve()
        if not resolved.is_relative_to(root / "docs"):
            raise ValueError("unsafe generated-manifest path")
    with tempfile.TemporaryDirectory(prefix="pawsql-build-") as temporary:
        staging = Path(temporary)
        written = build_references(staging, bundle)
        expected = {p.relative_to(staging).as_posix(): digest(p) for p in written}
        for rel in expected:
            if not (root / rel).resolve().is_relative_to(root / "docs"):
                raise ValueError("unsafe generated output path")
        stale = sorted(set(previous) - set(expected))
        modified = [rel for rel, old_hash in previous.items() if (root / rel).is_file() and digest(root / rel) != old_hash]
        if modified:
            raise ValueError("generated files modified outside build: " + ", ".join(modified))
        if mode == "release":
            if stale:
                raise ValueError("release blocked by stale generated outputs: " + ", ".join(stale))
            # All staged content is checked before creating the requested destination.
            shutil.copytree(root / "docs", staging / "site")
            from pawsql_doc.validate import parse_frontmatter
            for p in (staging / "site").rglob("*"):
                if p.is_file() and p.suffix in {".md", ".mdx"}:
                    data, error = parse_frontmatter(p.read_text(encoding="utf-8-sig"))
                    if error or not data or data.get("status") not in {"approved", "published"}:
                        p.unlink()
            for p in written:
                data, error = parse_frontmatter(p.read_text(encoding="utf-8-sig"))
                if error or not data or data.get("status") not in {"approved", "published"}:
                    continue
                target = staging / "site" / p.relative_to(staging / "docs")
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, target)
            # Validate the actual staged navigation after filtering, not only source files.
            from pawsql_doc.validate import validate_nav
            release_root = staging / "release-root"
            release_root.mkdir()
            shutil.move(str(staging / "site"), str(release_root / "docs"))
            problems = validate_nav(release_root, release=True)
            if problems:
                raise ValueError("staged navigation invalid: " + str(problems))
            shutil.copytree(release_root / "docs", output)
            return [str(output)], stale
        for p in written:
            target = root / p.relative_to(staging)
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or target.read_bytes() != p.read_bytes():
                shutil.copy2(p, target)
        # Splicing the aggregate matrix into the authored supported-databases
        # pages runs against the real content root (staging has no such page),
        # keeping prose outside the markers untouched and the matrix in sync
        # with metadata/databases. These pages stay out of generated-manifest.
        from pawsql_doc.generators.structured import sync_database_matrix
        sync_database_matrix(root, bundle)
        # Keep stale ownership records: do not silently forget orphaned artifacts.
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps({**{k: previous[k] for k in stale}, **expected}, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
        return sorted(expected), stale
