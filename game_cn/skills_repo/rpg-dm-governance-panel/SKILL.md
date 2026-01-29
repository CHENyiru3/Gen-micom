---
name: rpg-dm-governance-panel
description: Maintain a stable governance panel (assets/followers/army/income/clocks) as a patch-friendly state file, triggered by manage/governance gameplay.
---

# Governance Panel (Optional State)

Use this skill when the game enters territory/followers/economy/army management, or the user asks to enable/operate the governance subsystem.

## Files

- State: `GOVERNANCE_PANEL.md`
- Schema: `mechanics/GOVERNANCE_PANEL_SPEC.md`
- Rules: `mechanics/GOVERNANCE.md`

## Rules

- Keep `GOVERNANCE_PANEL.md` structured and patchable; do not mix it into `STATE_PANEL.md`.
- Log governance decisions in `sessions/` and apply changes via `ARCHIVE_DELTA`.
- If the subsystem is not active, keep the panel in “未启用” state (no fake numbers).

