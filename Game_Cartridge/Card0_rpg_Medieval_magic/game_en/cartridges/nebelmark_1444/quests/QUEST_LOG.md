# QUEST_LOG.md (Blank Campaign Starting Point)
Version: v0.1
Last Updated: 2026-01-29

---

## RAG_HEAD (4-6 line summary)

- Quest log is placeholder template, no active quests currently.
- Clue table and completion table empty, placeholder waiting to fill.
- Recommend using @q_ prefix as quest handle.
- New quests only need update "Active Quest Table" and "Quest Template."

## Index Field Specification (compatible with template cartridge)

| Field | Description |
|-------|-------------|
| handle | Recommended @handle (stable reference) |
| id | Legacy ID (retained for compatibility) |
| title | Quest name |
| source | Source |
| goal | Goal |
| status | Status |
| reward | Reward |
| risk | Risk |

## Handle Mapping (don't change original content)

| handle | id | title |
|--------|----|-------|
| @q_template | - | - |

## Active Quests

| ID | Quest Name | Source | Goal | Status | Reward | Risk |
|----|------------|--------|------|--------|--------|------|
| - | - | - | - | - | - | - |

---

## Pending Clues

| ID | Clue Description | Source | Related Quest | Time Limit |
|----|------------------|--------|---------------|------------|
| - | - | - | - | - |

---

## Completed Quests

| ID | Quest Name | Completion Date | Result | Consequence |
|----|------------|-----------------|--------|-------------|
| - | - | - | - | - |

---

## Quest Template

```md
## quest_XXX:
- **Title**:
- **Source**:
- **Goal**:
- **Reward**:
- **Risk**:
- **Time Limit**:
- **Status**:
- **Related Clues**:
- **Plot Hook**:
```
