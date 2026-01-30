# Gen-micom

This repository implements a "Game Console (Engine) + Cartridge + Campaign" three-layer architecture, emphasizing small context, hot-swappable, persistent text-based tabletop RPG system.

**Current Entry Points:**
- **Shared Engine (Engine)**: `GC_gamer/engine_en/`
- **Cartridge & Campaign**: `Game_Cartridge/Blank_Cartidge_template/game_en/`

---

## 1) Architecture (Engine / Cartridge / Storage)

- **Engine (Game Console)**: Stable protocols and mechanisms, no world content
  - Location: `GC_gamer/engine_cn/` (Chinese baseline)
  - Location: `GC_gamer/engine_en/` (English translated)
- **Cartridge**: World settings and content library (lore / locations / quests / characters / maps)
  - Location: `Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/<id>/`
- **Campaign**: Current game runtime state (HOT_PACK / STATE_PANEL / sessions / PCs)
  - Location: `Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/<id>/`

Entry Pointer: `Game_Cartridge/Blank_Cartidge_template/game_cn/ACTIVE.md`

---

## 2) Creating Games (New Cartridge / New Campaign)

### 2.1 New Cartridge (Starting from Template)

1. Copy `Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/_template/`
   → `Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/<new_card_id>/`
2. Edit `CARTRIDGE.md`: Fill in routes / aliases / invariants / feature_flags
3. Fill minimum content index (lore/locations/quests/characters/maps)

### 2.2 New Campaign (Save)

> **Recommended Method (Conversation Automation)**: AI/Agent executes scripts and file modifications, you just need conversation commands.

Send in conversation:
```
<new campaign campaigns/<new_campaign>>
```

AI will automatically:
- Execute `campaign_manager.py new`
- Modify `campaigns/<new_campaign>/CAMPAIGN.md` (set `cartridge_id=<new_card_id>` and lock version)

---

## 3) Starting Game (Initialization)

After entering cartridge, execute initialization (conversation automation):
- Send `<initialize>` (entry first reads `GC_gamer/engine_cn/System.md`, then executes `INIT_PROTOCOL.md`)
- Initialization will write:
  - `campaigns/<id>/PLAYER_PROFILE.md`
  - `campaigns/<id>/characters/PCs/pc_current.md`
  - `campaigns/<id>/sessions/` (creates first session)
  - `campaigns/<id>/STATE_PANEL.md`
  - `campaigns/<id>/HOT_PACK.md`

---

## 3.1 Conversation Command Entry Convention (Unified Entry)

All commands first read `GC_gamer/engine_cn/System.md` as entry router, then read corresponding protocol files:
- `<initialize>` → `GC_gamer/engine_cn/INIT_PROTOCOL.md`
- `<new campaign ...>` / `<switch campaign ...>` → `GC_gamer/engine_cn/CAMPAIGN_PROTOCOL.md`
- `<hot start>` / `<continue>` → `GC_gamer/engine_cn/HOT_START.md`

---

## 4) Save and Recovery (Hot Start)

### Save (Automatic)
- Each turn outputs `ARCHIVE_DELTA`, auto append/patch:
  - `sessions/<current>.md`
  - `HOT_PACK.md`
  - `STATE_PANEL.md`
  - `OBJECT_INDEX.md`

### Recovery (Hot Start)
- Read order see `GC_gamer/engine_cn/HOT_START.md`
- Send `<hot start>` or `<continue>` in conversation
- **Entry Consistency**: First read `GC_gamer/engine_cn/System.md`, then load per `HOT_START.md` order (including `ACTIVE.md` → `CAMPAIGN.md` → `CARTRIDGE.md` → `HOT_PACK.md`).

---

## 5) Hot-Swap New Cartridge (Switch Cartridge / Restore Progress)

### Switch Cartridge
1. Copy or create new cartridge
2. Send `<new campaign campaigns/<new_campaign>>` (AI automatically creates and binds cartridge)
3. `ACTIVE.md` will be auto-updated by AI

### Restore Old Progress
Switch back to old campaign:
```
<switch campaigns/<old_campaign>>
```
Then `<continue>` to restore.

---

## 6) Fiction Sync (Novel Update)

Fiction pipeline location:
`campaigns/<id>/Writing/PIPELINE.md`

Principles:
- Main text not dependency for turn execution
- Only sync key decisions from `sessions/` and `STATE_PANEL.md`
- Triggered by DM/script when needed

---

## 7) Prompt Optimization Engineering and Design

Completed key optimizations:
- **Command Header Routing**: `[ACT]/[LOOK]/[ASK]/[FIGHT]/[CAST]/[MANAGE]/[OOC]`
- **HOT_PACK Minimization**: ≤100 lines, strict context control
- **RAG Throttling**: ≤4 fragments, each ≤80 chars, ROUTE_FACTS 8-12 items
- **RAG_HEAD**: 4-6 line summary at index file top
- **Handle System**: @handle + aliases, reduce player memory burden
- **External Engine**: `GC_gamer/engine_cn` / `engine_en` shared reuse

Design Goals:
- Stable progress under minimal token budget
- World settings and runtime state separation
- Sustainable hot-swappable cartridges and save recovery
