---
name: rpg-dm-governance-panel
description: Maintain a stable governance panel (assets/followers/army/income/clocks) as a patch-friendly state file, triggered by manage/governance gameplay.
---

# Governance Panel (Optional State)

Use this skill when the game enters territory/followers/economy/army management, or the user asks to enable/operate the governance subsystem.

## Files

- State: `GOVERNANCE_PANEL.md`
- Schema: `engine/mechanics/GOVERNANCE_PANEL_SPEC.md`
- Rules: `engine/mechanics/GOVERNANCE.md`

## Rules

- Keep `campaigns/<id>/GOVERNANCE_PANEL.md` structured and patchable; do not mix it into `campaigns/<id>/STATE_PANEL.json`.
- Log governance decisions in `campaigns/<id>/sessions/` and apply changes via `ARCHIVE_DELTA`.
- If the subsystem is not active, keep the panel in "Not Enabled" state (no fake numbers).
