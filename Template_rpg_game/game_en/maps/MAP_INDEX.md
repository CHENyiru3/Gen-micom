# MAP_INDEX.md — Map Index (Ground Truth: maps/)

> **Purpose**: Register all map "three-piece sets" (render/data/logic), as map system entry and RAG retrieval anchor.
> **Rules**: Each map must have `.md` + `.data.yaml` + `.logic.md`, updates must bump version and record reason.

---

## MAPS::REGISTRY

| map_id | name | type | scale | version | status | files | updated | links |
|--------|------|------|-------|---------|--------|-------|---------|-------|
| macro_0001_template | Template Region Map | macro | hex | 0.1.0 | planned | `maps/macro/macro_0001_template.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `lore/CANON/WORLD.md` |
| micro_0001_template | Template Location Map | micro | node | 0.1.0 | planned | `maps/micro/micro_0001_template.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `locations/LOCATION_INDEX.md` |

**status** value suggestions: `planned | active | frozen | deprecated`

---

## Map Type Definitions

### Macro Maps (Regional)
- Scale: Hex-based
- Purpose: Regional exploration
- Format: Regional features, travel times, settlements

### Micro Maps (Local)
- Scale: Node-based
- Purpose: Local exploration
- Format: Rooms, points of interest, connections

---

## Adding New Maps

To add a new map:

1. Create render file: `maps/[type]/[map_id].md`
2. Create data file: `maps/[type]/[map_id].data.yaml`
3. Create logic file: `maps/[type]/[map_id].logic.md`
4. Update this index with the new map entry
