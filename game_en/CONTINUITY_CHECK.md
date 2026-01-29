# CONTINUITY_CHECK.md — Session End Consistency Check (Stable)

> **Purpose**: After each session end or long window run, perform a 2-minute "drift check" to ensure restartable, traceable, compressible.
> **Principle**: `sessions/` is event ground truth; all other files should align with it.

---

## 1) Must Check 6 Items (Each Session End)

1. Does `sessions/CURRENT_SESSION.md` point to this session's written file?
2. Does current session file end have latest `Decision` (append)?
3. Does `HOT_PACK.md` `CONTEXT_PACK_NEXT` match latest Decision (time/location/indicators/hook)?
4. Has `STATE_PANEL.md` been patched (time/indicators/location/tasks/NPC/clocks at least one has corresponding change or remains unchanged)?
5. Has `OBJECT_INDEX.md` been patched (active object pointers and 1-line summaries)?
6. If macro world changes involved: Has `lore/WORLD_STATE.md` been patched (only index-level updates)?

### Optional: Experience Enhancement (Recommended)

- Has `.DM_PLANNER.md` been updated based on this session (Fronts/clue inventory/next session beats)?

---

## 2) Conflict Resolution (Fixed)

If conflict discovered:
- Use `sessions/` as authority
- In next turn `ARCHIVE_DELTA`:
  - Append a "Decision: Correction" or supplement "correction explanation" in recent Decision
  - Patch related state files to align

---

## 3) Initialization-Specific Check (New Campaign)

After initialization completes, additionally confirm:
- `PLAYER_PROFILE.md` preference summary is not `-`
- `characters/PCs/pc_current.md` has basic info filled
- `sessions/session_0000_bootstrap.md` is no longer current (switched to new session)
