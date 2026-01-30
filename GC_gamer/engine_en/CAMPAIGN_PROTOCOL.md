# CAMPAIGN_PROTOCOL.md — Create/Switch Campaign (Prompt Engineering Workflow)

> **Goal**: Make "start new campaign / switch campaign" a repeatable, low-error process, fully compatible with hot start and incremental archiving.

---

## 0) Directory and Source of Truth

- Engine (shared): `engine/` (protocols/mechanics/scripts)
- Cartridge (world content): `cartridges/<cartridge_id>/`
- Template Cartridge: `Game_Cartridge/Blank_Cartidge_template/game_cn/cartridges/_template/` (template only; never write here)
- Campaign (save): `Game_Cartridge/<cartridge_root>/game_cn/campaigns/<campaign_id>/`
- Current campaign pointer: `ACTIVE.md`

**Hard rule**:
- New cartridges must live in a **separate root**: `Game_Cartridge/<cartridge_root>/game_cn/`
- Never create `card_*` or new content inside `Blank_Cartidge_template`

---

## 1) JSON tool_calls (Recommended)

```json
{
  "tool_calls": [
    {"name": "copy_template", "arguments": {"src": "Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/_template", "dst": "Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>"}},
    {"name": "bind_campaign", "arguments": {"campaign_path": "Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>", "cartridge_id": "<new_card_id>", "version_lock": "1.0.x"}},
    {"name": "set_active", "arguments": {"campaign_path": "Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>"}}
  ]
}
```

### Users Don't Need to Run Scripts (Conversation Control)

If you're talking to an AI, simply send:
- `<新战役 campaign_0002>` / `<new campaign campaign_0002>`
- `<切换战役 campaigns/campaign_0001>` / `<switch campaign campaigns/campaign_0001>`

The AI will execute the script in the background and update `ACTIVE.md`.

---

## 2) Pure Prompt Manual Method (No Script Scenario)

When the user says "start new campaign", DM must output JSON tool_calls in order:

1. `copy_template`
2. `bind_campaign`
3. `set_active`
4. `init_campaign` (per `INIT_PROTOCOL.md`)

On failure: Better to stop at "not successfully switched" than to write incorrect `ACTIVE.md`.
