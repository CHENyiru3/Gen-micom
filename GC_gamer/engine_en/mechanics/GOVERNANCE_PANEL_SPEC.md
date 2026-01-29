# GOVERNANCE_PANEL_SPEC.md — Governance Panel Field Specification (Kernel Interface)

> **Purpose**: Allow `campaigns/<id>/GOVERNANCE_PANEL.md` to be long-term maintainable, patchable, searchable; avoid duplication with `campaigns/<id>/WORLD_STATE.md`/`campaigns/<id>/STATE_PANEL.md`.

---

## 1) Panel Positioning

- `GOVERNANCE_PANEL.md` only records "player faction/assets/followers/income/settlement/governance clocks" and other governance information.
- If governance gameplay not entered: Keep empty/placeholder.

---

## 2) Chapter Order (Fixed)

1. `## Summary`
2. `## Faction Grade`
3. `## Resources`
4. `## Followers`
5. `## Military`
6. `## Land`
7. `## Commerce`
8. `## Buildings`
9. `## Governance Clocks`
10. `## Current Settlement`

---

## 3) Minimum Fields (Recommended)

- Faction grade: Reference `engine/mechanics/GOVERNANCE.md` tier name + key thresholds
- Resources: Food/silver/gold/credit/supply inventory
- Followers: Number, loyalty, core figures
- Current settlement: Income/expenditure/net profit (keep latest 1-3 periods)
