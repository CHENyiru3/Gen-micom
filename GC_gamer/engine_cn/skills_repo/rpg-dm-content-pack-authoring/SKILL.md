---
name: rpg-dm-content-pack-authoring
description: Author and update RPG content packs (cartridges lore/NPC/quests/locations) while keeping kernel protocols stable and avoiding plot-driven drift.
---

# RPG Content Pack Authoring (Kernel/Content Separation)

Use this skill when the user asks to add/modify world content (NPCs, quests, locations, lore, random tables, session logs) and you must keep the kernel stable.

## Classification (stable)

- **Kernel (stable API)**: input protocol, turn pipeline, HUD schema, save protocol, RAG rules, conflict policy.
- **Content packs (mutable data)**: NPCs, quests, locations, world state, random tables, session history, fiction.

## Authoring rules

- Put **facts** in content (`cartridges/<id>/lore/`, `cartridges/<id>/characters/`, `cartridges/<id>/locations/`, `cartridges/<id>/quests/`), not in kernel prompts.
- Keep files **small and indexed**: add tags/anchors so RAG can fetch tiny snippets.
- Maintain **alias → stable ID** through roster/index files (so players can type natural language).
- Update dynamic state only via **append/patch** (ARCHIVE_DELTA style).

## Minimal workflows

- **New NPC**: add to `cartridges/<id>/characters/NPCs/npc_roster.md` + create `cartridges/<id>/characters/NPCs/npc_*.md`.
- **New location**: add to `cartridges/<id>/locations/LOCATION_INDEX.md` + create `cartridges/<id>/locations/loc_*.md` (if using per-location files).
- **New quest**: add to `cartridges/<id>/quests/QUEST_LOG.md`; keep status + hooks short.
- **New lore**: add under `cartridges/<id>/lore/CANON/` (static) or `cartridges/<id>/lore/MIST/` (discoverable); update `cartridges/<id>/lore/INDEX.md`.
- **Session logging**: append decisions to latest `campaigns/<id>/sessions/session_*.md` and keep `campaigns/<id>/sessions/SESSION_INDEX.md` updated.
- **New cartridge**: copy `cartridges/template_card/` → `cartridges/<new_id>/` and edit `CARTRIDGE.md`/aliases/invariants before spinning up a matching campaign.
