# MAP_INDEX.md — Map Index (Ground Truth: maps/)

> **Purpose**: Register all map "three-piece sets" (render/data/logic), as map system entry and RAG retrieval anchor.
> **Rules**: Each map must have `.md` + `.data.yaml` + `.logic.md`, updates must bump version and record reason.

---

## MAPS::REGISTRY

| map_id | name | type | scale | version | status | files | updated | links |
|--------|------|------|-------|---------|--------|-------|---------|-------|
| micro_0001_nebelheim_city | Nebelheim City Map | micro | node | 0.1.0 | planned | `maps/micro/micro_0001_nebelheim_city.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `lore/MIST/LAESURAE.md`, `locations/LOCATION_INDEX.md` |
| macro_0001_nebelmark_region | Nebelmark Region Map | macro | hex | 0.1.0 | planned | `maps/macro/macro_0001_nebelmark_region.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `lore/CANON/WORLD.md`, `lore/CANON/FACTIONS.md` |

**status** value suggestions: `planned | active | frozen | deprecated`

