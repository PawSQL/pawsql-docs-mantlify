---
id: user-guide-optimization-or-union
title: OR to UNION Optimization
description: How the OR-to-UNION rewrite works and when it helps.
type: user-guide
product: pawsql-optimizer
versionIntroduced: 8.5.0
status: draft
tags: [optimization, rewrite, user-guide]
relatedFeatures: [OPT-OR-UNION]
---

# OR to UNION Optimization

When a query's `WHERE` clause combines OR-ed predicates that touch different columns, the optimizer cannot use an index per branch in a single plan. PawSQL rewrites the query so each branch can follow its own best access path, merging results with `UNION ALL` when the branches are provably disjoint.

- **What changes:** the query structure (results are preserved).
- **Why it helps:** each branch can now use a different index.
- **When it applies:** the rewrite is cost-based and only applied when the alternative plan is expected to be cheaper.

## Example

Before (single fused plan):

```sql
SELECT * FROM orders
WHERE status = 'open' OR customer_id = 42;
```

After the rewrite (UNION ALL applies when the branches cannot overlap):

```sql
SELECT * FROM orders WHERE status = 'open'
UNION ALL
SELECT * FROM orders
WHERE customer_id = 42 AND status <> 'open';
```

No manual action is needed — PawSQL applies this automatically where safe.

> Status: draft content for the new documentation site. See the [optimizer rule reference](docs/reference/optimizer-rules/opt-or-union) for the canonical rule page.
