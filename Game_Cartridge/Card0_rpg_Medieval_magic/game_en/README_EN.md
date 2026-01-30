# Chronicles of the Misty Border: The Transient (Research‑Oriented RPG)

![Engine](https://img.shields.io/badge/Engine-Shared-2E86AB?style=flat-square)
![Cartridge](https://img.shields.io/badge/Cartridge-Hot--Swappable-3B8B3B?style=flat-square)
![Campaign](https://img.shields.io/badge/Campaign-Persistent-5C6BC0?style=flat-square)
![RAG](https://img.shields.io/badge/RAG-4x80%20%7C%208%E2%80%9312-8E44AD?style=flat-square)
![Language](https://img.shields.io/badge/Language-English-555?style=flat-square)

**Keywords**: Engine / Cartridge / Campaign  
**Goal**: stable long‑running play under minimal context budgets.

---

## 0) Structure & Entry

| Layer | Responsibility | Location |
|------|----------------|----------|
| Engine | Protocols / rules / RAG / save specs | `engine/` (symlink → `GC_gamer/engine_cn/`) |
| Cartridge | World content | `cartridges/<id>/` |
| Campaign | Runtime state | `campaigns/<id>/` |

Pointer: `ACTIVE.md`

---

## 1) Quick Start (Initialize)

Command: `<initialize>`  
Entry: `engine/System.md` → `engine/INIT_PROTOCOL.md`  
Writes:
- `campaigns/<id>/PLAYER_PROFILE.md`
- `campaigns/<id>/characters/PCs/pc_current.md`
- `campaigns/<id>/sessions/`
- `campaigns/<id>/STATE_PANEL.md`
- `campaigns/<id>/HOT_PACK.md`

---

## 2) New Cartridge / New Campaign

**New Cartridge**  
Copy: `../../Blank_Cartidge_template/game_cn/cartridges/template/` → `cartridges/<new_card_id>/`  
Edit: `CARTRIDGE.md` (routes/aliases/invariants/feature_flags)

**New Campaign (dialogue automation)**  
Send: `<new campaign campaigns/<new_campaign>>`  
AI: creates campaign + binds `cartridge_id`

---

## 3) Hot Start & Recovery

Command: `<hot start>` or `<continue>`  
Entry: `engine/System.md` → `engine/HOT_START.md`  
Load order: `ACTIVE.md` → `CAMPAIGN.md` → `CARTRIDGE.md` → `HOT_PACK.md`

---

## 4) Hot‑Swap & Resume

- New cartridge: see Section 2  
- Resume old progress: `<switch campaign campaigns/<old_campaign>>` → `<continue>`

---

## 5) Save & Fiction Sync

**Save**: per‑turn `ARCHIVE_DELTA` (append/patch)  
**Fiction**: `Writing/PIPELINE.md` synced from session decisions

---

## 6) Method Constraints

- Command‑head routing: ACT / LOOK / ASK / FIGHT / CAST / MANAGE / OOC  
- RAG throttling: ≤4 snippets, ≤80 chars/snippet, ROUTE_FACTS 8–12  
- Index summaries: `RAG_HEAD` at top of indices  
- Hot cache: `HOT_PACK` ≤100 lines  
- Shared Engine: `engine_cn` reused
