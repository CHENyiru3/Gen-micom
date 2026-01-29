# Gen-micom

![Engine](https://img.shields.io/badge/Engine-Shared-2E86AB?style=flat-square)
![Cartridge](https://img.shields.io/badge/Cartridge-Hot--Swappable-3B8B3B?style=flat-square)
![Campaign](https://img.shields.io/badge/Campaign-Persistent-5C6BC0?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-4x80%20%7C%208%E2%80%9312-8E44AD?style=flat-square)

Research‑oriented Engine–Cartridge–Campaign framework for low‑context, long‑running RPG execution.

**Primary Entry (CN)**  
- Engine: `GC_gamer/engine_cn/`  
- Cartridge & Campaign: `Game_Cartridge/Card0_rpg_Medieval_magic/game_cn/`

**Documentation**  
- 中文：`Game_Cartridge/Card0_rpg_Medieval_magic/game_cn/README_CN.md`  
- English: `Game_Cartridge/Card0_rpg_Medieval_magic/game_en/README_EN.md`

---

## Architecture Summary

| Layer | Responsibility | Location |
|------|----------------|----------|
| Engine | Protocols, CLI, RAG, save rules | `GC_gamer/engine_cn/` |
| Cartridge | World content (read‑only) | `.../cartridges/<id>/` |
| Campaign | Runtime state (read‑write) | `.../campaigns/<id>/` |

Pointer: `ACTIVE.md`
