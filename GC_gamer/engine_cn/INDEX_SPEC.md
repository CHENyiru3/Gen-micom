# INDEX_SPEC.md — 索引格式规范（CN）

> **目标**：统一所有索引结构，提升 RAG 命中率与可维护性。

## 必须段落顺序
1. `RAG_HEAD`（4–6 行摘要）
2. 主表（Table）
3. `Handle Mapping`
4. `Entry Pointers`

## RAG_HEAD 模板
```
RAG_HEAD:
- 覆盖范围…
- 关键对象…
- 读取优先级…
- 当前变化（可选）…
```

## 主表字段（建议统一）
- `@handle`
- `name`
- `one_line_summary`
- `status`（可选）

## Handle Mapping
```
## Handle Mapping
| handle | aliases |
| --- | --- |
| @xxx | ["别名1","别名2"] |
```

## Entry Pointers
```
## Entry Pointers
- @xxx → path/to/entry.md
```

