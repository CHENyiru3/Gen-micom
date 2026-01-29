# OBJECT_INDEX.md — Active Object Index (Hot Cache, Avoid Multi-File Scanning)

> **Purpose**: Compress "objects truly needed this turn/current session" into one index page, for hot start and minimum per-turn reads.
> **Rules**: Only store "pointer + 1-line summary"; details remain in object files (NPC/Quest/Location/Map).

---

## Active Session

- current: `sessions/CURRENT_SESSION.md`

---

## Active PC

- pc: `characters/PCs/pc_current.md` — (not initialized)
- pet: `characters/PCs/pet_current.md` — (optional)

---

## Active Location Targets

- (none)

---

## Active Quests

- (none)

---

## Active NPCs

- (none)

---

## Active Maps (optional)

- index: `maps/MAP_INDEX.md`
- (none)

---

## Notes

- This file updated via `ARCHIVE_DELTA` patch each turn (do not rewrite entire page).
