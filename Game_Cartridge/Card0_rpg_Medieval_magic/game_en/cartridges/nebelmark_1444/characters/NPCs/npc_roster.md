# NPC Roster npc_roster.md (Blank Campaign Starting Point)
Version: v0.1
Last Updated: 2026-01-29

---

## RAG_HEAD (4-6 line summary)

- NPC index is blank template, key figures not yet registered.
- Recommended to use @npc_ prefix handles.
- Character details need individual files in npc_*.md.
- New NPCs: update this table first, then add files.

## Index field specification (compatible with template cartridge)

| Field | Description |
|-------|-------------|
| handle | Recommended @handle (stable reference) |
| id | Legacy ID (retained for compatibility) |
| name | Name |
| faction | Faction |
| role | Role |
| status | Status |

## Handle mapping (don't change original content)

| handle | id | name |
|--------|----|------|
| @npc_template | - | - |

## Important NPC List

| ID | Name | Faction | Role | Status | Secrets |
|----|------|---------|------|--------|---------|
| - | - | - | - | - | - |

---

## NPC Template

```md
## NPC_ID:
- **Name**:
- **Faction**:
- **Public Identity**:
- **Action Style**:
- **Resources/Assets**:
- **Public Goal**:
- **Hidden Goal**:
- **Easily Discovered Secrets** (2):
  1.
  2.
- **Hard to Discover Secrets** (1):
- **Key Relationships**:
  -
- **Mist Status**: none|touched|agent|entity
- **First Appearance**: session_YYYY-MM-DD_slug.md
```
