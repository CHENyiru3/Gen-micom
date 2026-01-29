# MAP_INDEX.md — 地图索引（真源：maps/）

> **用途**：登记所有地图“三件套”（render/data/logic），作为地图系统入口与 RAG 检索锚点。  
> **规则**：每张地图必须有 `.md` + `.data.yaml` + `.logic.md`，更新必须 bump 版本并记录原因。

---

## MAPS::REGISTRY

| map_id | name | type | scale | version | status | files | updated | links |
|--------|------|------|-------|---------|--------|-------|---------|-------|
| micro_0001_nebelheim_city | Nebelheim 城市图 | micro | node | 0.1.0 | planned | `maps/micro/micro_0001_nebelheim_city.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `lore/MIST/LAESURAE.md`, `locations/LOCATION_INDEX.md` |
| macro_0001_nebelmark_region | Nebelmark 区域图 | macro | hex | 0.1.0 | planned | `maps/macro/macro_0001_nebelmark_region.md` / `.data.yaml` / `.logic.md` | 2026-01-29 | `lore/CANON/WORLD.md`, `lore/CANON/FACTIONS.md` |

**status** 取值建议：`planned | active | frozen | deprecated`

