# RAG_ENGINE.md — Routing Retrieval and Fragment Facts

## Purpose
- Use command headers to route retrieval scope, limit context size.
- Only extract fragment facts (8-12 items, each ≤16 characters).

## Input
- Player input (must contain command header)
- cartridges/<id>/CARTRIDGE.md routes
- campaigns/<id>/HOT_PACK.json
- campaigns/<id>/index.md (only top snapshot)

## Output
- ROUTE_FACTS (8-12 items)
- List of files participating in retrieval

## Rules
1) Based on command header, select routes list.
2) Only read index/summary/entry headers, not swallow full text.
3) Maximum 4 file fragments per time, each ≤80 characters.
4) Priority read: *_INDEX.md / *_roster.md / QUEST_LOG.md headers and first paragraphs.
5) Consistent with engine/mechanics/RAG_RULES.md, if conflict, that file takes precedence.

## Failure Handling
- Unknown command header: Return error prompt + available command header list + 1 example.
- Target file missing: Record to ARCHIVE_DELTA risk_flag.

## Length Limits
- ROUTE_FACTS: 8-12 items, each ≤16 characters.
- HOT_PACK: ≤100 lines.
