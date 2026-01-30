# INDEX_SPEC.md — Index Format Spec (EN)

> **Goal**: unify index structures for RAG accuracy and maintainability.

## Required Section Order
1. `RAG_HEAD` (4–6 lines)
2. Main table
3. `Handle Mapping`
4. `Entry Pointers`

## RAG_HEAD Template
```
RAG_HEAD:
- Coverage…
- Key objects…
- Read priority…
- Current change (optional)…
```

## Main Table Fields (Recommended)
- `@handle`
- `name`
- `one_line_summary`
- `status` (optional)

## Handle Mapping
```
## Handle Mapping
| handle | aliases |
| --- | --- |
| @xxx | ["alias1","alias2"] |
```

## Entry Pointers
```
## Entry Pointers
- @xxx → path/to/entry.md
```

