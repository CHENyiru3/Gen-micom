# CONTINUITY_CHECK.md — Session End Consistency Check (Stable)

> **Purpose**: At each session end or after a long runtime window, do a 2-minute "drift check" to ensure restartability, traceability, and compressibility.
> **Principle**: `campaigns/<id>/sessions/` is the event source of truth; all other files should align with it.

---

## 1) Required 6 Checks (Each Session End)

1. Does `campaigns/<id>/sessions/CURRENT_SESSION.md` point to the session file written this time?
2. Does the current session file end have the latest `Decision` (append)?
3. Is `campaigns/<id>/HOT_PACK.json`'s `CONTEXT_PACK_NEXT` consistent with the latest Decision (time/location/indicators/hooks)?
4. Has `campaigns/<id>/STATE_PANEL.json` been patched (time/indicators/location/quest/NPC/clock should have at least corresponding changes or remain unchanged)?
5. Has `campaigns/<id>/OBJECT_INDEX.json` been patched (active object pointer and 1-line summary)?
6. If macro world changes are involved: Has `campaigns/<id>/WORLD_STATE.md` been patched (only index-level updates)?

### Optional: Experience Enhancement (Recommended)

- Has `.DM_PLANNER.md` been updated based on this session (Fronts/clue inventory/next session beats)?

---

## 2) Conflict Handling (Fixed)

If conflicts are found:
- Use `campaigns/<id>/sessions/` as the standard
- In the next turn's `ARCHIVE_DELTA`:
  - Append a "Decision: Correction" or supplement "correction note" in the most recent Decision
  - Patch relevant state files to align

---

## 3) Initialization-Specific Check (New Campaign)

After initialization completes, additionally confirm:
- `campaigns/<id>/PLAYER_PROFILE.md`'s preference summary is not `-`
- `campaigns/<id>/characters/PCs/pc_current.md` has basic info filled in
- `campaigns/<id>/sessions/session_0000_bootstrap.md` is no longer current (has switched to new session)
