---
name: rpg-dm-campaign-manager
description: Create, switch, and initialize campaigns using the campaign protocol, including symbolic link management.
---

# RPG DM Campaign Manager

Use this skill when managing campaigns (creating new ones, switching between them, or initializing them).

## Campaign Operations

### Create New Campaign

**Command**: `<New campaign campaign_XXXX>`

**Process**:
1. Create directory structure from `_template`
2. Initialize blank state files
3. Update `CURRENT_CAMPAIGN.md`
4. Rebuild symbolic links
5. Return summary of new campaign

### Switch Campaign

**Command**: `<Switch campaign campaigns/campaign_XXXX>`

**Process**:
1. Verify target campaign exists
2. Update `CURRENT_CAMPAIGN.md`
3. Rebuild symbolic links
4. Load new campaign's state
5. Return current status

### Initialize Campaign

**Command**: `<Initialize>`

**Process**:
1. Run initialization protocol from `INIT_PROTOCOL.md`
2. Collect player preferences
3. Create player character
4. Set starting location and hook
5. Create first session file
6. Return ready status

## Directory Structure

```
campaigns/
├── _template/              # Template for new campaigns
│   ├── root/               # Campaign root files
│   ├── characters/         # Character files
│   ├── quests/             # Quest files
│   ├── sessions/           # Session files
│   └── Writing/            # Writing files
├── campaign_0001/          # Existing campaign
└── campaign_0002/          # Existing campaign
```

## Symbolic Links

The following paths are symbolic links (managed by this skill):

| Path | Target |
|------|--------|
| `sessions/` | `campaigns/<current>/sessions/` |
| `quests/` | `campaigns/<current>/quests/` |
| `characters/` | `campaigns/<current>/characters/` |
| `Writing/` | `campaigns/<current>/Writing/` |
| `STATE_PANEL.md` | `campaigns/<current>/root/STATE_PANEL.md` |
| `HOT_PACK.md` | `campaigns/<current>/root/HOT_PACK.md` |
| `OBJECT_INDEX.md` | `campaigns/<current>/root/OBJECT_INDEX.md` |
| `PLAYER_PROFILE.md` | `campaigns/<current>/root/PLAYER_PROFILE.md` |

## Campaign Metadata

Stored in `CURRENT_CAMPAIGN.md`:

```yaml
campaign_id: campaign_0001
campaign_path: campaigns/campaign_0001
created: YYYY-MM-DD
last_switched: YYYY-MM-DD
notes: [Optional notes]
```

## Quality Checklist

- [ ] Directory structure created correctly
- [ ] Symbolic links established
- [ ] CURRENT_CAMPAIGN.md updated
- [ ] State files initialized
- [ ] Return summary is accurate
