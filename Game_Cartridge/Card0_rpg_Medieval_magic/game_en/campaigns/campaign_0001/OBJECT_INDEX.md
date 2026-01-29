# OBJECT_INDEX.md — Active Object Index (Hot Cache, Avoid Multi-File Scanning)

> **Purpose**: Compress "objects truly needed for current turn/session" into one-page index, for hot start and per-turn minimum reading.
> **Rule**: Only store "pointer + 1-line summary"; details still in object files (NPC/Quest/Location/Map).

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

- This file is updated each turn with `ARCHIVE_DELTA` patch (don't rewrite entire page).

