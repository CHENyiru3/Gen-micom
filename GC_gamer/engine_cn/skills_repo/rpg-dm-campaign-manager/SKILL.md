---
name: rpg-dm-campaign-manager
description: Create and switch RPG campaigns by copying `campaigns/_template`, updating `ACTIVE.md`.
---

# Campaign Manager (Core/Save Separation)

Use this skill when the user asks to “新开战役/切换战役/分离core与存档/多周目管理”.

## Recommended automation (JSON tool_calls)

Use function calling via skill tools:
- `copy_template` + `bind_campaign` + `set_active`
- `init_campaign` for initialization

## Manual fallback (prompt workflow)

If scripts are unavailable:
1. Copy `campaigns/_template` → `campaigns/<new_id>`
2. Update `ACTIVE.md`
3. Run `<初始化>` per `INIT_PROTOCOL.md` (JSON tool_calls)

## References

- Protocol: `CAMPAIGN_PROTOCOL.md` (JSON tool_calls)
- Hot start: `HOT_START.md`
