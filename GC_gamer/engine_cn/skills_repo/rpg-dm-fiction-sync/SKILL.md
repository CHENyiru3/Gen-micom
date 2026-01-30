---
name: rpg-dm-fiction-sync
description: Convert session/event logs into fiction chapters without creating new canon; enforce State/Event truth and track continuity issues.
---

# Fiction Sync (Session → Novel)

Use this skill when the user asks to “写小说/续写小说/同步正文/检查一致性”.

## Truth model (stable)

- Writing is **derived**: it never creates canon facts.
- Priority: `State > Event > Canon > Writing`.

## Workflow

1. Read `campaigns/<id>/Writing/Fiction_index.md` for progress/queue.
2. Read the relevant `campaigns/<id>/sessions/session_*.md` decisions (only the needed parts).
3. Cross-check against `campaigns/<id>/index.md` + `campaigns/<id>/STATE_PANEL.json`.
4. Write fiction in the repo’s chosen style, keeping POV consistent.
5. Update `campaigns/<id>/Writing/Fiction_index.md` and optionally record issues in `campaigns/<id>/Writing/CONTINUITY_ISSUES.md`.

## Reference

- Repo pipeline spec: `campaigns/<id>/Writing/PIPELINE.md`
