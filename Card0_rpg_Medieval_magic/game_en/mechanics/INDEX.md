# mechanics/INDEX.md — Mechanics File Index

> **Purpose**: Point to all rules and mechanics files
> **tags**: [index, mechanics, rules, reference]

---

## INDEX::001 Core Rules

| File | Purpose | When to Read |
|------|---------|--------------|
| `KERNEL_PROMPT.md` | Kernel (Stable Protocol) | Before each session |
| `System.md` | World Instance + Router (Entry and Index) | Before each session |
| `HOUSE_RULES.md` | House Rules and Dice Rules | When rules needed |
| `TRACKERS.md` | Tracker Templates (Not Ground Truth) | When manual recording/printing needed |
| `GOVERNANCE_PANEL_SPEC.md` | Governance Panel Field Spec (Stable) | When enabling governance panel |

---

## INDEX::002 Combat and Survival

| File | Purpose | When to Read |
|------|---------|--------------|
| `COMBAT.md` | Combat Rules (Attack/Defense/Status) | When entering combat |
| `SURVIVAL.md` | Survival Rules (Consumption/Rest/Status) | When survival check needed |
| `SOCIAL_INVESTIGATION.md` | Social and Investigation Rules | When social interaction |

---

## INDEX::003 Advanced Systems

| File | Purpose | When to Read |
|------|---------|--------------|
| `GOVERNANCE.md` | Governance Panel (Territory/Military/Commerce) | When gaining territory |
| `RANDOM_TABLES.md` | Random Encounter Tables | When random events needed |
| `../Map-Gen.md` | Map Generation and Save Spec (Extended) | When map system needed |

---

## INDEX::004 System Tools

| File | Purpose | When to Read |
|------|---------|--------------|
| `RAG_RULES.md` | RAG Retrieval Rules | When retrieval needed |
| `CONTEXT_PACK.md` | Context Pack Spec (Stable) | When context recovery/paste package needed |
| `CONTEXT_PACK_EXAMPLES.md` | Context Pack Examples (Variable) | When reference needed |
| `STATE_PANEL_SPEC.md` | STATE_PANEL Field Spec (Stable) | When maintaining panel format |

---

## INDEX::005 Quick Reference Table

### Indicator System (Definition in `lore/MECHANICS/INDICATORS.md`)

| Indicator | Range | Rule |
|-----------|-------|------|
| Grace | 0-10 | Divine order availability |
| Debt | 0-10 | Human redemption pressure |
| Rumor | 0-3 | Public discussion level |
| Heat | 0-3 | Faction attention level |

### Indicator Rules Quick Reference
- Public spell casting/monster sighting → Rumor+1
- Rumor≥2 → Investigation forces must intervene
- Violence/magic abuse → Debt+1
- Saving people/refusing temptation → Debt-1 or Grace+1

---

## INDEX::006 Combat Quick Reference

### Damage Table

| Melee Weapon | Damage | Ranged Weapon | Damage |
|--------------|--------|---------------|--------|
| Fist | d3 | Rock throw | d2 |
| Dagger | d4 | Throwing knife | d3 |
| Hand axe/Short sword | d6 | Shortbow | d6 |
| Longsword/Mace | d8 | Crossbow | d8 |

### AC Table

| Armor | AC |
|-------|----|
| Unarmored | 10+DEX |
| Leather | 11+DEX |
| Chain mail | 13+DEX-1 |
| Plate | 16+DEX-2 |

---

## INDEX::007 Social Quick Reference

### Social Check DC

| Type | DC Range |
|------|----------|
| Persuasion | 10-20 |
| Deception | 12-18 |
| Intimidation | 12-20 |
| Performance | 10-25 |

### Insight Results

| Gap | Result |
|-----|--------|
| ≥10 | Completely see through |
| 5-9 | Suspicious |
| 0-4 | No obvious suspicion |
| <0 | Believe player |

---

## INDEX::008 Survival Quick Reference

### Daily Consumption

| Item | Price |
|------|-------|
| Rations (1 day) | 2 silver |
| Beer | 1 silver |
| Lodging (hay) | 1 silver |
| Lodging (inn) | 5-10 silver |

### Status Penalties

| Status | Penalty |
|--------|---------|
| Hungry | -1 all checks |
| Dehydrated | -2 all checks |
| Fatigued | -1 all checks |

### Rest Recovery

| Rest | Recovery |
|------|----------|
| Short rest (1 hour) | 1d6 HP |
| Long rest (8 hours) | Full HP |
| Complete rest (24 hours) | All statuses |

---

## INDEX::009 Tag Index

Retrieve mechanics files by tag:

| Tag | Related Files |
|-----|---------------|
| [combat] | COMBAT.md, HOUSE_RULES.md |
| [survival] | SURVIVAL.md, HOUSE_RULES.md |
| [social] | SOCIAL_INVESTIGATION.md |
| [governance] | GOVERNANCE.md |
| [random] | RANDOM_TABLES.md |
| [system] | System.md, HOUSE_RULES.md, TRACKERS.md |
| [rag] | RAG_RULES.md, CONTEXT_PACK.md |

---

## INDEX::010 File Dependency Relationships

```
KERNEL_PROMPT.md (Kernel)
└── System.md (World Instance + Router)
├── HOUSE_RULES.md (House Rules)
├── TRACKERS.md (Trackers)
├── COMBAT.md (Combat)
├── SURVIVAL.md (Survival)
├── SOCIAL_INVESTIGATION.md (Social Investigation)
├── GOVERNANCE.md (Governance)
├── RANDOM_TABLES.md (Random Tables)
├── RAG_RULES.md (RAG Rules)
└── CONTEXT_PACK.md (Context Pack)
```
