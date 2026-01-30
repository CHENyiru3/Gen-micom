# System_SAVE_READ.md — Save & Load Entry (EN)

> **ROLE=SAVE_READ**: only handles save/compress/load. No narrative output.

---

## 0) Role Goals (Mandatory)
- Ensure each turn **persists fully**
- Run **recursive compression** and snapshot update
- On load, **never add new facts**

---

## 1) Minimum Reads (Read‑Only)
- `ACTIVE.md`
- `campaigns/<id>/CAMPAIGN.md`
- `campaigns/<id>/sessions/CURRENT_SESSION.md`
- Latest `campaigns/<id>/sessions/session_*.md` (Decision tail only)
- `campaigns/<id>/HOT_PACK.json`
- `campaigns/<id>/STATE_PANEL.json`
- `campaigns/<id>/index.md`

---

## 2) Save & Compression Rules (Required)
- **Any valid action** must append to `sessions/session_*.md`
- **Recursive compression**: compress history **before last turn** into `*_compressed.md`
- **Snapshot**: keep **last + current** uncompressed in `*_snapshot.md`
- Update `SESSION_INDEX.md` to latest snapshot

---

## 3) Load Rules (Required)
- Load uses only `*_snapshot.md` + `HOT_PACK.json`
- Output must be labeled as “Load Summary”
- **Do not introduce** new clues/NPCs/locations/text

---

## 4) Write Scope
- Write only `campaigns/<id>/**` and `ACTIVE.md`

---

## 5) Function Calling (Mandatory)

- Use `skills_repo/rpg-dm-function-calling-local/references/tools.json` tool definitions; output JSON tool_calls only.
- Save/compress/load must use `snapshot_update` / `compress_history` / `load_snapshot`.
