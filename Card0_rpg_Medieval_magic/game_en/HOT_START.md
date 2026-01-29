# HOT_START.md — Hot Start/Restart Protocol (Stable)

> **Goal**: Allow single agent to recover to runnable state in 30-60 seconds with "context=0", and ensure memory externalization is traceable.

---

## 0) Single Ground Truth: File Responsibilities (Avoid Duplication)

- `sessions/`: **Event ground truth** (Decision appends; never rewrite history)
- `STATE_PANEL.md`: **Player-side persistent panel** (short, patchable, easy to view)
- `HOT_PACK.md`: **Next turn hot start package** (≤25 lines, machine-readable; priority read)
- `index.md`: **Navigation index** (only pointers and very short summary, no long world-building)
- `lore/WORLD_STATE.md`: **World state/backend indicators and complete clue index** (read when needed)
- `lore/INDEX.md`: **Setting library entry** (use when answering world-building questions)
- `GOVERNANCE_PANEL.md`: **Governance panel (optional)** (read when entering territory/follower gameplay)
- `mechanics/`: Rule packages (read when triggered, follow `mechanics/RAG_RULES.md`)
- `maps/`: Map content packages (read when maps needed, read `maps/MAP_INDEX.md` first)
- `Writing/`: Derived narrative (doesn't produce settings; not read by default)

---

## 1) Hot Start Read Order (Mandatory)

1. `HOT_PACK.md`: Read `<!-- CONTEXT_PACK_NEXT ... -->` (if exists)
2. `PLAYER_PROFILE.md`: Read only "preference summary" (≤8 lines)
3. `OBJECT_INDEX.md`: Read only active pointers (1-line summary of NPC/Quest/Location/Map)
4. `sessions/CURRENT_SESSION.md`: Locate current active session file path
5. Corresponding `sessions/session_*.md`: Read only last 1-3 Decisions (not entire document)
6. `STATE_PANEL.md`: Read time/indicators/tasks/NPC/clocks/location (as needed)
7. `index.md`: Read only "next session objective/pointer" (not long)

If "insufficient information": Then read `quests/QUEST_LOG.md` or `locations/LOCATION_INDEX.md` as needed, finally read `lore/WORLD_STATE.md`.

---

## 2) Startup Self-Check (Prevent Drift)

After startup, immediately check:
- Consistency of indicators/location in `STATE_PANEL.md` with recent Decisions
- That `sessions/CURRENT_SESSION.md` points to existing file and is latest session
- If conflict: Use `sessions/` as authority, write "correction explanation" in next `ARCHIVE_DELTA`

### Uninitialized Detection (New Campaign)

If any condition met, consider "campaign not yet initialized":
- `sessions/CURRENT_SESSION.md` points to `sessions/session_0000_bootstrap.md`
- "Preference summary" in `PLAYER_PROFILE.md` still is `-`

Handling: Prompt user to send `<Initialize>`, complete persistence per `INIT_PROTOCOL.md`.

---

## 3) Must Write Each Turn (Ensure Persistence)

Each turn end via `ARCHIVE_DELTA` at least update:
- `sessions/<current>.md`: append Decision
- `STATE_PANEL.md`: patch (only changed sections)
- `HOT_PACK.md`: patch (write latest `CONTEXT_PACK_NEXT`)
