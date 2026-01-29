# RAG_RULES.md — RAG Retrieval Rules

> **Purpose**: Rules for retrieving content from files during gameplay

---

## 0) RAG Basics

### What is RAG?
Retrieval-Augmented Generation — loading relevant file content to inform DM decisions and responses.

### RAG Principles
1. Only retrieve what's needed for current context
2. Retrieve minimal fragments (≤12 lines each)
3. Prefer HOT summaries over WARM/COLD files
4. Never dump entire files into context

---

## 1) File Temperature Classification

### HOT (Always Read)
| File | When to Read | What to Get |
|------|--------------|-------------|
| `HOT_PACK.md` | Every turn | Full `CONTEXT_PACK_NEXT` |
| `PLAYER_PROFILE.md` | Every turn | Preference summary only |
| `OBJECT_INDEX.md` | Every turn | Active pointers |

### WARM (Triggered Read)
| File | Trigger | What to Get |
|------|---------|-------------|
| `mechanics/*.md` | Combat/Survival/Social triggers | Relevant section only |
| `lore/CANON/*` | World-building questions | ≤3 paragraphs |
| `lore/MIST/*` | Supernatural questions | ≤3 paragraphs |
| `lore/WORLD_STATE.md` | Backend state needed | Relevant section |
| `characters/NPCs/*` | NPC appears | Full file |
| `locations/*` | New location | Full file |
| `quests/*` | Quest referenced | Full file |
| `maps/*` | Map needed | Full file |

### COLD (Rarely Read)
| File | When to Read | What to Get |
|------|--------------|-------------|
| `Writing/Fiction_*.md` | Player requests | Relevant section |
| `.DM_SECRETS.md` | DM planning | Relevant section |
| `.DM_PLANNER.md` | DM planning | Relevant section |

---

## 2) Retrieval Limits

### Per-Turn Limits
- Maximum 3 file fragments
- Each fragment ≤12 lines
- Total retrieved content ≤36 lines

### Per-Session Limits
- No hard limit, but be efficient
- Use summaries and pointers when possible
- Don't re-read what hasn't changed

---

## 3) Retrieval Tags

Use tags to help with RAG:

| Tag | Trigger Retrieval |
|-----|-------------------|
| [combat] | COMBAT.md, HOUSE_RULES.md combat section |
| [survival] | SURVIVAL.md, HOUSE_RULES.md survival section |
| [social] | SOCIAL_INVESTIGATION.md |
| [lore] | lore/INDEX.md, relevant lore files |
| [npc] | relevant NPC file |
| [location] | relevant location file |
| [quest] | relevant quest file |
| [map] | maps/MAP_INDEX.md, relevant map file |
| [system] | System.md, mechanics/INDEX.md |

---

## 4) Retrieval Process

### Step 1: Identify Need
What information does the current turn need?
- Rule clarification
- World information
- NPC behavior
- Location details
- Quest status

### Step 2: Select Files
Based on need, select files:
- HOT files: always
- WARM files: if triggered
- COLD files: only if necessary

### Step 3: Extract Fragments
Retrieve only relevant sections:
- Use file structure (headings, tables)
- Limit to ≤12 lines
- Skip unrelated sections

### Step 4: Integrate
Use retrieved information:
- Inform DM adjudication
- Answer player questions
- Guide NPC responses
- Describe environment

---

## 5) Caching Strategy

### Per-Turn Cache
- Read `HOT_PACK.md` first
- Cache `CONTEXT_PACK_NEXT`
- Use cache for quick reference

### Session Cache
- Cache player preferences
- Cache active quest status
- Cache current location

### Never Cache
- NPC secret motivations (refresh each encounter)
- Time-sensitive information
- Dynamic world state

---

## 6) RAG Mistakes to Avoid

### Mistake 1: Dumping Entire Files
Bad: Reading entire `lore/CANON/WORLD.md` for a simple question
Good: Retrieve only relevant paragraph about the specific topic

### Mistake 2: Not Using Tags
Bad: Manually searching through files
Good: Use file tags and INDEX files

### Mistake 3: Over-Retrieving
Bad: Retrieving 10 files for a simple action
Good: Retrieve maximum 3 files, only what's essential

### Mistake 4: Not Using HOT
Bad: Reading deep lore for every action
Good: Use HOT summaries, retrieve WARM only when needed

### Mistake 5: Forgetting OBJECT_INDEX
Bad: Searching through all NPC files
Good: Check `OBJECT_INDEX.md` first for active objects

---

## 7) Quick RAG Reference

| Player Action | Retrieve |
|---------------|----------|
| Combat action | COMBAT.md, relevant NPC stat block |
| Social interaction | NPC file, SOCIAL_INVESTIGATION.md |
| Investigation | Clue files, relevant lore |
| Travel | SURVIVAL.md, map files |
| Rest | SURVIVAL.md (rest section) |
| World question | Relevant lore file (≤3 paragraphs) |
| Rule question | Relevant mechanics file |
| New location | Location file, map |
| New quest | Quest file, relevant NPCs |
| Status check | STATE_PANEL.md, PLAYER_PROFILE.md |
