# Gen-micom


Gen-micom (Generative AI Famicom) is a prompt-engineered Engine–Cartridge–Campaign framework for low‑context, long‑running RPG execution.  
It separates **protocols (Engine)**, **content (Cartridge)**, and **runtime state (Campaign)** to enable hot‑swaps and durable play, and the whole structure is based on markdown files, which means you can run this with any AI model. 

---

## 1) Project Overview

Primary entry (CN):
- Engine: `GC_gamer/engine_cn/`
- Cartridge & Campaign: `Game_Cartridge/Card0_rpg_Medieval_magic/game_cn/`

Docs:
- 中文：`Game_Cartridge/Card0_rpg_Medieval_magic/game_cn/README_CN.md`
- English: `Game_Cartridge/Card0_rpg_Medieval_magic/game_en/README_EN.md`

---

## 2) Usage (Quick Start)

1. Open the cartridge repo docs (CN or EN).
2. Create or switch a campaign via dialogue commands.
3. Initialize with `<初始化>` / `<initialize>`.
4. Continue with `<继续>` / `<continue>`.

---

## 3) Create a Cartridge 

1. Copy template:
   `Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/template/`
   → `.../cartridges/<new_card_id>/`
2. For campaigns, use:
   `Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/_template/`
2. Edit `CARTRIDGE.md` (routes / aliases / invariants / feature_flags).
3. Fill minimal index files:
   - `lore/INDEX.md`
   - `locations/LOCATION_INDEX.md`
   - `quests/QUEST_LOG.md`
   - `characters/NPCs/npc_roster.md`
   - `maps/MAP_INDEX.md`
4. Bind it to a new campaign via `<新战役 campaigns/<new_campaign>>`.
