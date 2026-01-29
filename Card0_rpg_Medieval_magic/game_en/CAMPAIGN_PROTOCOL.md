# CAMPAIGN_PROTOCOL.md — New/Switch Campaign (Prompt Engineering Workflow)

> **Goal**: Make "start new campaign/switch campaign" into repeatable, low-error workflow, fully compatible with hot start/incremental save.

---

## 0) Directory and Ground Truth

- Core (Shared): Repository root (`KERNEL_PROMPT.md`, `mechanics/`, `lore/`, `maps/`...)
- Campaign (One per campaign): `campaigns/<campaign_id>/`
- Current campaign pointer: `CURRENT_CAMPAIGN.md`

Root's `sessions/ quests/ characters/ Writing/` and various state files are **symbolic links**, pointing to current campaign.

---

## 1) Automation Method (Recommended)

Use scripts:

```bash
python3 scripts/campaign_manager.py new --id campaign_0002
python3 scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

### Users Don't Need to Run Scripts (Conversational Control)

If talking with AI, recommend directly sending:
- `<New campaign campaign_0002>`
- `<Switch campaign campaigns/campaign_0001>`

AI executes scripts in background and completes `CURRENT_CAMPAIGN.md` and root symbolic link updates.

---

## 2) Pure Prompt Manual Method (No Script Scenario)

When user says "new campaign", DM must execute in order (internal/tool layer completion):

1. Copy template `campaigns/_template` → `campaigns/<new_id>`
2. Update `CURRENT_CAMPAIGN.md` to new path
3. Rebuild root symbolic links (sessions/quests/characters/Writing and state files)
4. Run `<Initialize>` (complete persistence per `INIT_PROTOCOL.md`)

On failure: Better stop at "switch unsuccessful" than write wrong `CURRENT_CAMPAIGN.md`.
