# Blank Cartridge Template (EN)

This template is designed for **AI‑driven dialogue workflows** to create a new cartridge + campaign.

## Dialogue Workflow (Recommended)

1) **Create a new cartridge**
   - Copy: `cartridges/_template/` → `cartridges/<new_card_id>/`
   - Update `CARTRIDGE.md` (routes / aliases / invariants / feature_flags)

2) **Create a new campaign**
   - Send: `<new campaign campaigns/<new_campaign>>`
   - AI copies the campaign template and binds `cartridge_id`

3) **Initialize**
   - Send: `<initialize>`
   - AI writes runtime files per `engine/INIT_PROTOCOL.md`

## Template Layout

```
game_en/
├── cartridges/_template/        # Cartridge template (minimal indices)
└── campaigns/_template/        # Campaign skeleton (HOT_PACK/STATE_PANEL/sessions/…)
    └── .DM_BLUEPRINT.md        # Mainline blueprint (DM only)
    ├── MAINLINE_PANEL.md       # Mainline panel (ultra‑short)
    └── clues/CLUE_LOG.md       # Clue log (separate from quests)
```
