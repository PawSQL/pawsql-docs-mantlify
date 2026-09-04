---
id: en-audit-rule-aud-avoid-count-distinct-on-multiple-nullable-column
title: Avoid COUNT DISTINCT on Multiple Nullable Columns
type: reference
status: draft
tags:
- audit-rule
- dml
description: COUNT(DISTINCT col1, col2) drops rows where any column is NULL, unlike
  single-column COUNT(DISTINCT); use COALESCE defaults to get the expected counts.
localeOf: audit-rule-aud-avoid-count-distinct-on-multiple-nullable-column
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-avoid-count-distinct-on-multiple-nullable-column |
| Name | Avoid COUNT DISTINCT on Multiple Nullable Columns |
| Category | dml — DML / data modification |
| Severity | info |
| Databases | All supported databases |

## Description

When you compute with `COUNT(DISTINCT)` over multiple columns, the result may not match what you expect. `COUNT(DISTINCT col)` counts the distinct non-NULL values of that column, whereas `COUNT(DISTINCT col1, col2)` drops any row where at least one column is NULL. This difference is especially likely to make statistics diverge from business expectations when nullable columns are involved.

For example, counting distinct values of column a versus the pair (a, b): if column b holds NULLs, `COUNT(DISTINCT a, b)` is less than or equal to `COUNT(DISTINCT a)`, which may not match the developer's expectation and deserves attention.

## Bad Example

```sql
-- bad: multi-column COUNT(DISTINCT) over nullable columns may return unexpected results
select count(distinct t.a) a_cnt, count(distinct t.a, t.b) a_b_cnt
from (values
      row(1, 2),
      row(3, null)) as t(a, b);
-- result: a_cnt=2, a_b_cnt=1 - the row with NULL in b is excluded
```

## Good Example

```sql
-- good: replace NULLs with a default via COALESCE before distinct counting
select count(distinct t.a) a_cnt, count(distinct t.a, coalesce(t.b, -1)) a_b_cnt
from (values
      row(1, 2),
      row(3, null)) as t(a, b);
```
