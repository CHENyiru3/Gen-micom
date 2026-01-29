---
name: rpg-dm-maps
description: Generate and maintain ASCII maps as a content pack (render+data+logic triad) with fog-of-war, version bumps, and ARCHIVE_DELTA persistence.
---

# RPG Maps (Content Pack)

Use this skill when the user asks to create/update/query maps, reveal fog-of-war, or ensure spatial consistency across sessions.

## Files (authoritative)

- Index: `maps/MAP_INDEX.md`
- Macro maps: `maps/macro/*`
- Micro maps: `maps/micro/*`
- Session instances (temporary reveals): `maps/instances/*`

Each map is a triad:
- `*.md` (render)
- `*.data.yaml` (structured data)
- `*.logic.md` (constraints, derivations, update reasons)

## Workflow (stable)

1. Resolve which `map_id` is relevant (or create one) and register it in `maps/MAP_INDEX.md`.
2. Update the triad minimally; bump `version` on any change.
3. Enforce fog-of-war: unknown stays `?`; rumored POI is a point, not a full layout.
4. Persist via `ARCHIVE_DELTA` (append/patch only). Never rewrite whole map files.

## References

- Full map protocol: `Map-Gen.md`
- Reboot protocol: `HOT_START.md` (maps are WARM; don't load unless needed)

