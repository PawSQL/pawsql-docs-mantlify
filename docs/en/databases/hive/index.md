---
id: database-hive
translationKey: database-hive
language: en
title: Apache Hive
type: reference
status: draft
entityRef:
  type: database
  id: database-hive
owners: []
subtype: database
layout: detail
product: pawsql
---

# Apache Hive

**Supported versions:** 2.3, 3.1, 4.0

| Capability | Status |
|---|---|
| SQL Review | Supported |
| Query Rewrite | Supported |
| Index Recommendation | Unsupported |
| Performance Validation | Unsupported |
| Plan Visualization | Partial (database/version-limited) |
| Performance Inspection | Partial (database/version-limited) |

PawSQL supports Apache Hive SQL with rules for partition pruning, join, skew, and Top-N analysis in analytical workloads.

- Cost-based index recommendation

- Semantic query rewrite

- SQL audit rule review

Version list and capability status are sample data pending confirmation from the product team.

Status: supported / partial (database- or version-limited) / unsupported.
