---
name: rpg-dm-campaign-manager
description: Create and switch RPG campaigns by copying `campaigns/_template`, updating `ACTIVE.md`.
---

# Campaign Manager (Core/Save Separation)

Use this skill when the user asks to “新开战役/切换战役/分离core与存档/多周目管理”.

## Recommended automation

Run the repo script:

- New campaign: `python3 scripts/campaign_manager.py new --id campaign_0002`
- Switch campaign: `python3 scripts/campaign_manager.py switch --path campaigns/campaign_0001`

## Manual fallback (prompt workflow)

If scripts are unavailable:
1. Copy `campaigns/_template` → `campaigns/<new_id>`
2. Update `ACTIVE.md`
3. Update ACTIVE.md to point at the new campaign
4. Run `<初始化>` per `INIT_PROTOCOL.md`

## References

- Protocol: `CAMPAIGN_PROTOCOL.md`
- Hot start: `HOT_START.md`
