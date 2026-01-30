# ROLE_SYSTEMS.md — Role Split & Read Scope (EN)

> **Purpose**: separate “content creation / campaign setup / runtime DM” into distinct roles with strict read scopes to reduce drift and forgetting.

---

## 1) Roles (Must Distinguish)

### A) Content Author
**Goal**: create/extend cartridge content (world lore, indices, object libraries).
**May read**:
- `cartridges/<id>/CARTRIDGE.md`
- `cartridges/<id>/lore/**`
- `cartridges/<id>/locations/**`
- `cartridges/<id>/characters/**`
- `cartridges/<id>/quests/**`
- `cartridges/<id>/maps/**`
**Must not read**: all `campaigns/**` (avoid runtime contamination)

### B) Campaign Builder
**Goal**: copy template, bind cartridge, initialize a campaign.
**May read**:
- `engine/INIT_PROTOCOL.md`
- `engine/CAMPAIGN_PROTOCOL.md`
- `campaigns/_template/**`
- `cartridges/<id>/CARTRIDGE.md` (binding/routing only)
**Must not read**: storyline content (`sessions/**`) and player private data

### C) Runtime DM
**Goal**: advance play each turn and persist state.
**Minimum read set** (only what's needed):
- `ACTIVE.md`
- `campaigns/<id>/CAMPAIGN.md`
- `cartridges/<id>/CARTRIDGE.md`
- `campaigns/<id>/HOT_PACK.json`
- `campaigns/<id>/STATE_PANEL.json`
- `campaigns/<id>/sessions/CURRENT_SESSION.md` → `session_*.md` tail Decision
- `campaigns/<id>/index.md` (only “main thread / next goal” block)
- **Optional**: `campaigns/<id>/.DM_BLUEPRINT.md` (read **SPINE summary only**, not full)

**Must not read**: full lore unless routing explicitly hits it.

---

## 2) Role Switch Rules (Mandatory)

- Start every run by declaring role: `ROLE=AUTHOR | BUILDER | DM`
- Roles must not read/write outside scope
- DM uses routing only; no full‑repo scans

---

## 3) Mainline Consistency (Anti‑Drift)

- The **mainline spine** is defined in `.DM_BLUEPRINT.md` (generated at init)
- DM must keep the mainline intact; side quests can branch but must keep a return path

