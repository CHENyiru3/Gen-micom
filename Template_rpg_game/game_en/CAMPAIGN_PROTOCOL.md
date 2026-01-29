# CAMPAIGN_PROTOCOL.md — Campaign Management Protocol

> **Purpose**: How to create, switch, and manage campaigns
> **Core Principle**: Campaigns are isolated from each other; core (mechanics, lore, maps) is shared

---

## 0) Campaign Directory Structure

```
campaigns/
├── _template/              # Template for new campaigns
│   ├── root/               # Campaign root files (symlinked to root)
│   ├── characters/         # Character files
│   ├── quests/             # Quest files
│   ├── sessions/           # Session files
│   └── Writing/            # Writing files
├── campaign_0001/          # First campaign
│   ├── root/               # Campaign-specific root files
│   ├── characters/
│   ├── quests/
│   ├── sessions/
│   └── Writing/
└── campaign_0002/          # Second campaign
    └── ...
```

---

## 1) Creating a New Campaign

### Method A: Using Control Commands (Recommended)

Send: `<New campaign campaign_XXXX>`

AI will:
1. Create directory structure from `_template`
2. Initialize blank state files
3. Update `CURRENT_CAMPAIGN.md` pointing to new campaign
4. Rebuild symbolic links

### Method B: Using Python Script

```bash
python3 scripts/campaign_manager.py new --id campaign_XXXX
```

---

## 2) Switching Campaigns

### Method A: Using Control Commands (Recommended)

Send: `<Switch campaign campaigns/campaign_XXXX>`

AI will:
1. Update `CURRENT_CAMPAIGN.md` pointing to target campaign
2. Rebuild symbolic links to target campaign

### Method B: Using Python Script

```bash
python3 scripts/campaign_manager.py switch --path campaigns/campaign_XXXX
```

---

## 3) Symbolic Link Management

The following paths are symbolic links pointing to `campaigns/<current>/`:

| Path | Points To |
|------|-----------|
| `sessions/` | `campaigns/<current>/sessions/` |
| `quests/` | `campaigns/<current>/quests/` |
| `characters/` | `campaigns/<current>/characters/` |
| `Writing/` | `campaigns/<current>/Writing/` |
| `STATE_PANEL.md` | `campaigns/<current>/root/STATE_PANEL.md` |
| `HOT_PACK.md` | `campaigns/<current>/root/HOT_PACK.md` |
| `OBJECT_INDEX.md` | `campaigns/<current>/root/OBJECT_INDEX.md` |
| `PLAYER_PROFILE.md` | `campaigns/<current>/root/PLAYER_PROFILE.md` |
| `GOVERNANCE_PANEL.md` | `campaigns/<current>/root/GOVERNANCE_PANEL.md` |
| `.DM_SECRETS.md` | `campaigns/<current>/root/.DM_SECRETS.md` |
| `.DM_PLANNER.md` | `campaigns/<current>/root/.DM_PLANNER.md` |

---

## 4) Current Campaign Tracking

Current active campaign is tracked in `CURRENT_CAMPAIGN.md`:

```markdown
# CURRENT_CAMPAIGN.md

campaign_id: campaign_0001
campaign_path: campaigns/campaign_0001
created: 2026-01-29
last_switched: 2026-01-29
```
