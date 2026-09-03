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
from pawsql_doc.loaders import _print_issues, load_metadata
from pawsql_doc.paths import resolve_root
from pawsql_doc.validate import validate_frontmatter, validate_metadata


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


def _cmd_export_schemas(root: Path, _args: argparse.Namespace) -> int:
    export_schemas.export_schemas(root)
    print("exported JSON Schemas -> schemas/")
    return 0


def _cmd_build_references(root: Path, _args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    bundle, issues = load_metadata(root)
    written = build_references(root, bundle)
    for p in written:
        print(f"  wrote {p.relative_to(root).as_posix()}")
    print(f"PASS  generated {len(written)} reference page(s)")
    return 0


def _cmd_generate_rule(root: Path, args: argparse.Namespace) -> int:
    counts = _abort_if_broken(root)
    bundle, issues = load_metadata(root)
    path = generate_single_rule(root, bundle, args.rule)
    if path is None:
        print(f"FAIL  rule '{args.rule}' not found", file=sys.stderr)
        return 1
    print(f"  wrote {path.relative_to(root).as_posix()}")
    return 0


def _cmd_generate_database(root: Path, args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    bundle, issues = load_metadata(root)
    path = generate_single_database(root, bundle, args.database)
    if path is None:
        print(f"FAIL  database '{args.database}' not found", file=sys.stderr)
        return 1
    print(f"  wrote {path.relative_to(root).as_posix()}")
    return 0


def _cmd_generate_config(root: Path, args: argparse.Namespace) -> int:
    _abort_if_broken(root)
    bundle, issues = load_metadata(root)
    path = generate_single_config(root, bundle, args.config)
    if path is None:
        print(f"FAIL  config '{args.config}' not found", file=sys.stderr)
        return 1
    print(f"  wrote {path.relative_to(root).as_posix()}")
    return 0


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
        print("PASS  release gate: required documentation coverage = 100%")
        return 0
    print("FAIL  release gate: required documentation coverage < 100%", file=sys.stderr)
    return 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pawsql-doc", description=__doc__)
    parser.add_argument("--root", default=None, help="Repository root (default: auto-discovered)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate-metadata", help="Validate metadata/ tree and cross-references")
    sub.add_parser("validate-frontmatter", help="Validate front matter of docs/ and blog/ pages")
    sub.add_parser("export-schemas", help="Export pydantic models to schemas/*.json")

    sub.add_parser("drift", help="Report required docs missing between metadata and content (exit 1 on gaps)")
    sub.add_parser("coverage", help="Print documentation coverage per category")
    sub.add_parser("gate", help="Release gate: fail unless required coverage = 100%")

    p = sub.add_parser("build-references", help="Regenerate all metadata-driven reference pages")
    p = sub.add_parser("generate-rule", help="Generate one rule reference page")
    p.add_argument("--rule", required=True)
    p = sub.add_parser("generate-db", help="Generate one database guide page")
    p.add_argument("--database", required=True)
    p = sub.add_parser("generate-config", help="Generate one configuration reference page")
    p.add_argument("--config", required=True)
    return parser


def main(argv: List[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = resolve_root(args.root)
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 2
    handler = {
        "validate-metadata": _cmd_validate_metadata,
        "validate-frontmatter": _cmd_validate_frontmatter,
        "export-schemas": _cmd_export_schemas,
        "build-references": _cmd_build_references,
        "generate-rule": _cmd_generate_rule,
        "generate-db": _cmd_generate_database,
        "generate-config": _cmd_generate_config,
        "drift": _cmd_drift,
        "coverage": _cmd_coverage,
        "gate": _cmd_gate,
    }[args.command]
    return handler(root, args)


if __name__ == "__main__":
    sys.exit(main())
