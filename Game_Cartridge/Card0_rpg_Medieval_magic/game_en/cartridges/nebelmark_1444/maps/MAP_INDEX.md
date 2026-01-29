# MAP_INDEX.md — Map Index (True Source: maps/)

> **Purpose**: Register all map "three-piece sets" (render/data/logic) as map system entry and RAG retrieval anchor.
> **Rule**: Each map must have `.md` + `.data.yaml` + `.logic.md`, updates must bump version and record reason.

---

## RAG_HEAD (4-6 line summary)

- Two maps registered: city micro and region macro.
- Current status is all planned.
- All maps follow render/data/logic three-piece set.
- Handle recommendation uses @map_ prefix.

## Index Field Specification (compatible with template cartridge)

| Field | Description |
|-------|-------------|
| handle | Recommended @handle (stable reference) |
| map_id | Map ID |
| name | Map name |
| type | macro/micro |
| status | planned/active/frozen |

## Handle Mapping (don't change original content)

| handle | map_id | name |
|--------|--------|------|
| @map_micro_nebelheim | micro_0001_nebelheim_city | Nebelheim City Map |
| @map_macro_nebelmark | macro_0001_nebelmark_region | Nebelmark Region Map |

## MAPS::REGISTRY

| map_id | name | type | scale | version | status | files | updated | links |
|--------|------|------|-------|---------|--------|-------|---------|-------0001_nebel|
| micro_heim_city | Nebelheim City Map | micro | node | 0.1.0 | planned | `maps/micro/micro_0001_nebelheim_city.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `lore/MIST/LAESURAE.md`, `locations/LOCATION_INDEX.md` |
| macro_0001_nebelmark_region | Nebelmark Region Map | macro | hex | 0.1.0 | planned | `maps/macro/macro_0001_nebelmark_region.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `lore/CANON/WORLD.md`, `lore/CANON/FACTIONS.md` |

**status** suggested values: `planned | active | frozen | deprecated`
