"""pawsql-doc command line interface.

Mirrors the pawsql-doc-agent command names (design 36) for the Phase 0-2
subset: validation, schema export, and metadata-driven reference generation.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List

from pawsql_doc import export_schemas
from pawsql_doc import validate as validate_mod
from pawsql_doc.gate import coverage_report, find_drift, format_issues, run_release_gate
from pawsql_doc.generators import (
    build_references,
    generate_single_config,
    generate_single_database,
    generate_single_rule,
)
from pawsql_doc.ingest import parse_rule_doc, render_skeleton
from pawsql_doc.loaders import _print_issues, load_metadata
from pawsql_doc.paths import resolve_root
from pawsql_doc.validate import validate_frontmatter, validate_metadata, validate_nav


def _abort_if_broken(root: Path) -> List:
    issues, counts = validate_metadata(root)
    if issues:
        _print_issues(issues)
        print(f"metadata validation FAILED ({len(issues)} issue(s))", file=sys.stderr)
        raise SystemExit(1)
    return counts


def _cmd_validate_metadata(root: Path, _args: argparse.Namespace) -> int:
    issues, counts = validate_metadata(root)
    _print_issues(issues)
    summary = "  ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    if issues:
        print(f"FAIL  metadata: {summary}")
        return 1
    print(f"PASS  metadata: {summary}")
    return 0


def _cmd_validate_frontmatter(root: Path, _args: argparse.Namespace) -> int:
    issues = validate_frontmatter(root)
    _print_issues(issues)
    if issues:
        print(f"FAIL  front matter: {len(issues)} issue(s)")
        return 1
    print("PASS  front matter")
    return 0


def _cmd_validate_nav(root: Path, _args: argparse.Namespace) -> int:
    issues = validate_nav(root)
    _print_issues(issues)
    if issues:
        print(f"FAIL  nav: {len(issues)} nav-referenced page(s) are not published/approved")
        return 1
    print("PASS  nav: every referenced page is published/approved")
    return 0


def _load_manifest(manifest: str) -> dict:
    """Read rules_manifest.tsv -> {rid.lower(): row}."""
    import csv

    rows: dict = {}
    with open(manifest, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            rows[str(row["rid"]).lower()] = row
    return rows


def _cmd_ingest_rules(root: Path, args: argparse.Namespace) -> int:
    """P0.0.5: turn vault rule docs + the D manifest into RuleMetadata yaml skeletons.

    Dry-run by default (prints to stdout); pass --out <dir> to write into
    metadata/rules/<fam>/<rid>.yaml for human review before product sign-off.
    """
    manifest = _load_manifest(args.manifest)
    vault = Path(args.vault)
    picks = manifest if args.all else {i.lower(): manifest[i] for i in args.ids}
    if not picks:
        print("no rules selected: pass --id <rid> (repeatable) or --all", file=sys.stderr)
        return 2
    written: List[Path] = []
    for rid, row in sorted(picks.items()):
        src_name = row["src"]
        path = vault / f"{src_name}.md"
        if not path.is_file():
            # tolerate the one file whose name carries a trailing space
            for cand in vault.glob(f"{src_name}*.md"):
                if cand.name.startswith(src_name):
                    path = cand
                    break
        if not path.is_file():
            print(f"skip {rid}: vault doc not found for '{src_name}'", file=sys.stderr)
            continue
        doc = parse_rule_doc(path.read_text(encoding="utf-8-sig"), source=f"20-engine/rules/规则文档/{path.name}")
        category = row["cat"]
        severity = doc.severity or row["sev"] or "warning"
        fam = row["fam"]
        yaml_text = render_skeleton(rid, category, doc, kind=fam, source=f"20-engine/rules/规则文档/{path.name}")
        if args.out:
            out_dir = Path(args.out) / fam
            out_dir.mkdir(parents=True, exist_ok=True)
            target = out_dir / f"{rid}.yaml"
            target.write_text(yaml_text, encoding="utf-8")
            written.append(target)
            print(f"  wrote {target}")
        else:
            print(f"# ===== {rid} [{fam}] severity={severity} category={category} =====\n{yaml_text}")
    if args.out:
        print(f"PASS  wrote {len(written)} skeleton(s) to {args.out}")
    else:
        print(f"# ---- dry-run: {len(picks)} rule(s) rendered; pass --out to write ----")
    return 0


def _cmd_export_schemas(root: Path, _args: argparse.Namespace) -> int:
    export_schemas.export_schemas(root)
    print("exported JSON Schemas -> schemas/")
    return 0


def _cmd_build_references(root: Path, _args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    from pawsql_doc.build import build
    try:
        written, stale = build(root, _args.mode, Path(_args.output) if _args.output else None)
    except ValueError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    for p in written:
        print(f"  wrote {p}")
    for p in stale:
        print(f"STALE (not deleted): {p}")
    print(f"PASS  generated {len(written)} reference page(s)")
    return 0


def _cmd_migrate(root, args):
    from pawsql_doc.migration import migrate, migrate_metadata
    changes = migrate(root, args.apply) + migrate_metadata(root, args.apply)
    for path in changes:
        print(path)
    print(f"{'Applied' if args.apply else 'Dry run'}: {len(changes)} files")
    return 0


def _cmd_quality(root, args):
    from pawsql_doc.quality import quality_report, write_report
    report = quality_report(root, publication=args.release)
    for key, values in report.items():
        print(f"{key}: {len(values)} issue(s)")
    if args.write_report:
        print(write_report(root, report))
    return int(bool(report['structure'] or report['existence'] or (args.release and any(report.values()))))


def _cmd_inventory(root, args):
    import json
    from pawsql_doc.migration import inventory
    result = inventory(root)
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result, default=str, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    else:
        print(json.dumps(result, default=str, ensure_ascii=False, indent=2))
    return 0


def _cmd_generate_rule(root: Path, args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    bundle, issues = load_metadata(root)
    if not any(r.id.lower() == args.rule.lower() for rules in bundle.rules.values() for r in rules):
        print(f"FAIL  rule '{args.rule}' not found", file=sys.stderr)
        return 1
    print("Refreshing references and catalogs together to preserve manifest consistency.")
    return _cmd_build_references(root, argparse.Namespace(mode="preview", output=None))


def _cmd_generate_database(root: Path, args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    bundle, issues = load_metadata(root)
    if not any(db.database.lower() == args.database.lower() for db in bundle.databases):
        print(f"FAIL  database '{args.database}' not found", file=sys.stderr)
        return 1
    print("Refreshing references and catalogs together to preserve manifest consistency.")
    return _cmd_build_references(root, argparse.Namespace(mode="preview", output=None))


def _cmd_generate_config(root: Path, args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    bundle, issues = load_metadata(root)
    if not any(cfg.name.lower() == args.config.lower() for cfg in bundle.configs):
        print(f"FAIL  config '{args.config}' not found", file=sys.stderr)
        return 1
    print("Refreshing references and catalogs together to preserve manifest consistency.")
    return _cmd_build_references(root, argparse.Namespace(mode="preview", output=None))


def _print_coverage(lines) -> None:
    print(f"{'category':24} {'ok/total':10} {'%':>7}")
    for line in lines:
        print(f"{line.category:24} {line.ok}/{line.total:<6} {line.pct:6.1f}%")


def _cmd_drift(root: Path, _args: argparse.Namespace) -> int:
    missing = find_drift(root)
    for line in format_issues(missing):
        print(line, file=sys.stderr)
    if missing:
        print(f"FAIL  drift: {len(missing)} missing required doc(s)")
        return 1
    print("PASS  drift: all required docs present")
    return 0


def _cmd_coverage(root: Path, _args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    _print_coverage(coverage_report(root))
    return 0


def _cmd_gate(root: Path, _args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    passed, lines, missing = run_release_gate(root)
    _print_coverage(lines)
    for line in format_issues(missing):
        print(line, file=sys.stderr)
    if passed:
        print("PASS  existence gate: required documentation coverage = 100% (not publication approval)")
        return 0
    print("FAIL  existence gate: required documentation coverage < 100%", file=sys.stderr)
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pawsql-doc", description=__doc__)
    parser.add_argument("--root", default=None, help="Repository root (default: auto-discovered)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate-metadata", help="Validate metadata/ tree and cross-references")
    sub.add_parser("validate-frontmatter", help="Validate front matter of docs/ and blog/ pages")
    sub.add_parser("validate-nav", help="Check docs.json nav references only published/approved pages")
    sub.add_parser("export-schemas", help="Export pydantic models to schemas/*.json")

    sub.add_parser("drift", help="Report required docs missing between metadata and content (exit 1 on gaps)")
    sub.add_parser("coverage", help="Print documentation coverage per category")
    sub.add_parser("gate", help="Existence gate: required file coverage must be complete")

    p = sub.add_parser("migrate-content-model", help="Idempotent v2 migration (dry-run by default)")
    choices = p.add_mutually_exclusive_group()
    choices.add_argument("--apply", action="store_true")
    choices.add_argument("--dry-run", action="store_true")
    p = sub.add_parser("quality", help="Structure, existence, completeness and release readiness")
    p.add_argument("--release", action="store_true")
    p.add_argument("--write-report", action="store_true")
    p = sub.add_parser("inventory", help="Read-only content inventory")
    p.add_argument("--output")

    p = sub.add_parser("build-references", help="Regenerate all metadata-driven reference pages")
    p.add_argument("--mode", choices=["preview", "release"], default="preview")
    p.add_argument("--output")
    p = sub.add_parser("generate-rule", help="Generate one rule reference page")
    p.add_argument("--rule", required=True)
    p = sub.add_parser("ingest-rules", help="P0.0.5: vault rule docs -> RuleMetadata yaml skeletons (dry-run by default)")
    p.add_argument("--vault", required=True, help="Path to vault 20-engine/rules/规则文档 directory")
    p.add_argument("--manifest", default=str(Path(__file__).resolve().parent.parent.parent.parent / "tools" / "data" / "rules_manifest.tsv"),
                   help="TSV manifest (from PLACEMENT D); default tools/data/rules_manifest.tsv")
    p.add_argument("--id", dest="ids", action="append", default=[], help="Rule id(s) to render; repeatable")
    p.add_argument("--all", action="store_true", help="Render every manifest row")
    p.add_argument("--out", default=None, help="Write skeletons into this metadata/rules root (default: print to stdout)")
    p = sub.add_parser("generate-db", help="Generate one database guide page")
    p.add_argument("--database", required=True)
    p = sub.add_parser("generate-config", help="Generate one configuration reference page")
    p.add_argument("--config", required=True)
    return parser


def main(argv: List[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    args = build_parser().parse_args(argv)
    try:
        root = resolve_root(args.root)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 2
    handler = {
        "migrate-content-model": _cmd_migrate,
        "quality": _cmd_quality,
        "inventory": _cmd_inventory,
        "validate-metadata": _cmd_validate_metadata,
        "validate-frontmatter": _cmd_validate_frontmatter,
        "validate-nav": _cmd_validate_nav,
        "export-schemas": _cmd_export_schemas,
        "build-references": _cmd_build_references,
        "generate-rule": _cmd_generate_rule,
        "ingest-rules": _cmd_ingest_rules,
        "generate-db": _cmd_generate_database,
        "generate-config": _cmd_generate_config,
        "drift": _cmd_drift,
        "coverage": _cmd_coverage,
        "gate": _cmd_gate,
    }[args.command]
    return handler(root, args)


if __name__ == "__main__":
    sys.exit(main())
