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

## 1) Automated Method (Recommended)

Use the script:

```bash
python3 engine/scripts/campaign_manager.py new --id campaign_0002
python3 engine/scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

> Note: run the script inside the cartridge root (`Game_Cartridge/<cartridge_root>/game_cn/`).  
> Never create new campaigns under `Blank_Cartidge_template`.

### Users Don't Need to Run Scripts (Conversation Control)

If you're talking to an AI, simply send:
- `<新战役 campaign_0002>` / `<new campaign campaign_0002>`
- `<切换战役 campaigns/campaign_0001>` / `<switch campaign campaigns/campaign_0001>`

The AI will execute the script in the background and update `ACTIVE.md`.

---

## 2) Pure Prompt Manual Method (No Script Scenario)

When the user says "start new campaign", the DM must execute in order (internal/tool layer completes):

1. Copy template under **independent cartridge root**  
   `Game_Cartridge/Blank_Cartidge_template/game_cn/campaigns/_template`  
   → `Game_Cartridge/<cartridge_root>/game_cn/campaigns/<new_id>`
2. Update `ACTIVE.md` to the new path
3. Update the new campaign's `CAMPAIGN.md` (cartridge_id/version lock)
4. Run `<初始化>` / `<initialize>` (per `INIT_PROTOCOL.md`)

On failure: Better to stop at "not successfully switched" than to write incorrect `ACTIVE.md`.
