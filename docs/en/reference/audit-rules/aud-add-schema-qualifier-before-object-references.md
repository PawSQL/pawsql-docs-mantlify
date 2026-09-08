---
id: en-audit-rule-aud-add-schema-qualifier-before-object-references
title: Add Schema Qualifier Before Object References
type: reference
status: draft
owners: []
entityRef:
  type: rule
  id: aud-add-schema-qualifier-before-object-references
tags:
- audit-rule
- dml
description: Prefix every referenced object with its schema/owner (schema.object)
  to avoid ambiguity and wrong references in cross-schema or multi-tenant setups.
localeOf: audit-rule-aud-add-schema-qualifier-before-object-references
subtype: rule
language: en
translationKey: audit-rule-aud-add-schema-qualifier-before-object-references
layout: detail
product: pawsql
---

> **Generated file.** Do not edit by hand — change the source metadata (`metadata/rules/audit/*.yaml`) and re-run the generator.

| Field | Value |
|---|---|
| Rule ID | aud-add-schema-qualifier-before-object-references |
| Name | Add Schema Qualifier Before Object References |
| Category | dml — DML / data modification |
| Severity | info |
| Databases | Unverified (database scope not declared) |

## Description

When developing SQL, prefixing every referenced database object with its owning schema/owner (that is, using the fully qualified `schema.object` name) improves readability and long-term maintainability. It lets reviewers quickly tell where each object comes from and avoids ambiguity or wrong references caused by same-named objects in different schemas.

Statements without a schema prefix are especially error-prone in cross-schema or multi-tenant environments - a query may accidentally reach a same-named table or view in the wrong schema.

## Bad Example

```sql
-- bad: no schema qualifier; may reference the wrong table in a cross-schema environment
SELECT * FROM my_table;
```

## Good Example

```sql
-- good: fully qualified schema.table makes the object source explicit
SELECT * FROM mydb.my_table;
```
