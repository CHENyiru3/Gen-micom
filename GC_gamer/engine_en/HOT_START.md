# HOT_START.md — Hot Start/Restart Protocol (Stable)

> **Goal**: Allow a single agent to recover to operational state in 30-60 seconds with "context=0", and ensure memory is externalized and traceable.

---

## 0) Single Source of Truth: File Responsibilities (Avoid Duplication)

- `campaigns/<id>/sessions/`: **Event source of truth** (Decision append; never rewrite history)
- `campaigns/<id>/STATE_PANEL.md`: **Player-side persistent panel** (short, patchable, easy to view)
- `campaigns/<id>/HOT_PACK.md`: **Next turn hot start package** (≤25 lines, machine-readable; priority read)
- `campaigns/<id>/index.md`: **Navigation index** (only pointers and very short summary, no long lore)
- `campaigns/<id>/WORLD_STATE.md`: **World state/backend indicators and complete clue index** (read when needed)
- `cartridges/<id>/lore/INDEX.md`: **Lore library entry** (use when answering lore questions)
- `campaigns/<id>/GOVERNANCE_PANEL.md`: **Governance panel (optional)** (only read when entering territory/follower gameplay)
- `engine/mechanics/`: Rule packs (read when triggered, obey `engine/mechanics/RAG_RULES.md`)
- `cartridges/<id>/maps/`: Map content packs (only read maps when needed, first read `cartridges/<id>/maps/MAP_INDEX.md`)
- `campaigns/<id>/Writing/`: Derived fiction (doesn't generate lore; not read by default)

---

## 1) Hot Start Reading Order (Mandatory)

1. `campaigns/<id>/HOT_PACK.md`: Read `<!-- CONTEXT_PACK_NEXT ... -->` (if exists)
2. `campaigns/<id>/PLAYER_PROFILE.md`: Only read "preference summary" (≤8 lines)
3. `campaigns/<id>/OBJECT_INDEX.md`: Only read active pointer (1-line summary for NPC/Quest/Location/Map)
4. `campaigns/<id>/sessions/CURRENT_SESSION.md`: Locate current active session file path
5. Corresponding `campaigns/<id>/sessions/session_*.md`: Only read the last 1-3 Decisions (not the whole thing)
6. `campaigns/<id>/STATE_PANEL.md`: Only read time/indicators/quest/NPC/clocks/location (as needed)
7. `campaigns/<id>/index.md`: Only read "next session goal/pointers" (not long text)

If "insufficient information": then as needed read `campaigns/<id>/quests/QUEST_LOG.md` or `cartridges/<id>/locations/LOCATION_INDEX.md`, finally read `campaigns/<id>/WORLD_STATE.md`.

---

## 2) Startup Self-Check (Prevent Drift)

After startup, immediately check:
- Are the indicators/location in `campaigns/<id>/STATE_PANEL.md` consistent with recent Decisions?
- Does `campaigns/<id>/sessions/CURRENT_SESSION.md` point to a file that exists and is the latest session?
- If conflict: Use `campaigns/<id>/sessions/` as standard, and in the next `ARCHIVE_DELTA` write "correction note"

### Uninitialized Detection (New Campaign)

If any condition is met, consider "campaign not yet initialized":
- `campaigns/<id>/sessions/CURRENT_SESSION.md` points to `campaigns/<id>/sessions/session_0000_bootstrap.md`
- `campaigns/<id>/PLAYER_PROFILE.md`'s "preference summary" is still `-`

Handling: Prompt user to send `<initialize>`, and complete disk persistence per `INIT_PROTOCOL.md`.

---

## 3) Must Write Each Turn (Ensure Persistence)

At the end of each turn, via `ARCHIVE_DELTA`, update at least:
- `campaigns/<id>/sessions/<current>.md`: append Decision
- `campaigns/<id>/STATE_PANEL.md`: patch (only changed chapters)
- `campaigns/<id>/HOT_PACK.md`: patch (write latest `CONTEXT_PACK_NEXT`)
