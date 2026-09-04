---
id: user-guide-sql-audit
title: SQL Audit
description: How SQL audit works and where to find the rule references.
type: user-guide
product: pawsql-advisor
status: draft
tags: [audit, user-guide, sql-review]
---

# SQL Audit

PawSQL audits SQL and DDL before they reach production. Every finding points back to a rule with a stable id, a severity and a concrete fix.

## Finding your rule

Browse the generated rule references:

- [Audit rules](en/reference/audit-rules/sql-index-023) - index, select, DML, object and more
- [Optimizer rules](en/reference/optimizer-rules/opt-or-union) - rewrite algorithms used by the optimizer

Each reference page is **generated from metadata** (`metadata/rules/*.yaml`). To change a rule's text, change the YAML and re-run the generator - never edit the generated page by hand.

## Rule catalogs are metadata

The full audit and optimizer rule catalogs live in `metadata/rules/` and are the single source of truth for rule reference pages, which keeps examples and version history consistent across the site.

> Status: draft content for the new documentation site.
