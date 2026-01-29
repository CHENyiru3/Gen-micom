# COMBAT.md — Combat Rules

> **Purpose**: Combat system for this game template

---

## 0) Combat Basics

### Starting Combat
1. Combat begins when hostile action is taken
2. Determine if either side is surprised
3. Roll initiative for all combatants
4. Establish combat positions

### Surprise
- Surprised creatures cannot act in first round
- Perception check to notice ambush (DC based on stealth)
- If neither side notices the other, no surprise

---

## 1) Initiative

### Initiative Roll
```
1d20 + Dexterity Modifier
```

### Initiative Order
1. Highest initiative goes first
2. Ties: highest Dexterity modifier
3. If still tied: flip coin or simultaneous actions

### Ready Actions
- Can ready an action before your turn
- Trigger: "If [condition], then [action]"
- Action resolves immediately when trigger occurs

---

## 2) Actions in Combat

### Actions (Choose One)
| Action | Description |
|--------|-------------|
| **Attack** | Make one melee or ranged attack |
| **Dash** | Double movement speed |
| **Disengage** | Move without provoking opportunity attacks |
| **Dodge** | Take the Defend action |
| **Help** | Give ally advantage on one check |
| **Hide** | Attempt to hide (Stealth check) |
| **Use Item** | Use or administer an item |
| **Cast Spell** | Cast a spell (if spellcaster) |
| **Grapple** | Attempt to grab a creature |
| **Shove** | Push a creature 5 feet |
| **Escape** | Escape a grapple |
| **Ready** | Prepare an action for later |
| **Search** | Make a Perception check |
| **Stabilize** | Stabilize unconscious creature |

---

## 3) Attack Rolls

### Attack Roll Formula
```
1d20 + Ability Modifier + Proficiency Bonus (if proficient)
```

### Armor Class (AC)
| Armor Type | AC |
|------------|-----|
| Unarmored | 10 + Dexterity Modifier |
| Light Armor | 11 + Dexterity Modifier |
| Medium Armor | 13 + Dexterity Modifier (max +2 from DEX) |
| Heavy Armor | 16 + Dexterity Modifier (max +0 from DEX) |
| Shield | +2 |

### Attack Modifiers (Customize for Your Game)
| Weapon | Damage | Properties |
|--------|--------|------------|
| Unarmed | d3 | Light, finesse |
| Dagger | d4 | Light, finesse, thrown (20/60) |
| Shortsword | d6 | Light |
| Longsword | d8 | Versatile (d10) |
| Greatsword | 2d6 | Heavy, two-handed |
| Shortbow | d6 | Ammunition (80/320), two-handed |
| Longbow | d8 | Ammunition (150/600), heavy, two-handed |
| Crossbow, Light | d8 | Ammunition (80/320), loading |
| Crossbow, Heavy | 2d8 | Ammunition (120/400), heavy, loading |

---

## 4) Damage and Healing

### Damage Types
- **Slashing**: Swords, axes
- **Piercing**: Daggers, spears
- **Blunt**: Maces, hammers
- **Fire**: Fire, lava
- **Cold**: Ice, winter
- **Lightning**: Thunder, electricity
- **Poison**: Venom, toxins
- **Psychic**: Mind effects

### Damage Roll
```
Weapon Die + Strength Modifier (melee) or Dexterity Modifier (ranged)
```

### Critical Hits
- Natural 20 on attack roll
- Roll damage dice twice
- Apply only to weapon damage

### Healing
| Type | Amount |
|------|--------|
| Short Rest | 1d6 per Hit Die spent |
| Long Rest | Full HP |
| Stabilize | 0 HP (no healing) |
| Healing Potion | As per item |

### Temporary HP
- Gained from spells or abilities
- Lost before regular HP
- Not restored by rest

---

## 5) Conditions

| Condition | Effects |
|-----------|---------|
| **Blinded** | Cannot see, automatically fail sight-based checks, attacks against have advantage |
| **Charmed** | Cannot harm charmer, charmer has advantage on social checks |
| **Frightened** | Cannot move closer to source, advantage on checks while in range |
| **Grappled** | Speed becomes 0, cannot benefit from bonus to speed |
| **Incapacitated** | Cannot take actions or reactions |
| **Invisible** | Cannot be seen, attacks against have disadvantage, own attacks have advantage |
| **Paralyzed** | Cannot move, speak, or take actions, attacks against have advantage |
| **Petrified** | Transformed to stone, weight x10, cannot take actions |
| **Poisoned** | Disadvantage on attacks and checks |
| **Prone** | Crawling speed, attacks within 5ft have advantage, attacks from range have disadvantage |
| **Restrained** | Speed 0, attacks against have advantage, own attacks have disadvantage |
| **Stunned** | Cannot take actions, speak, or take reactions |
| **Unconscious** | Cannot take actions, drop items, fall prone, cannot perceive |
| **Exhaustion** | See exhaustion levels below |

### Exhaustion Levels
| Level | Effect |
|-------|--------|
| 1 | Disadvantage on ability checks |
| 2 | Speed halved |
| 3 | Disadvantage on attack rolls and saving throws |
| 4 | HP maximum halved |
| 5 | Speed reduced to 0 |
| 6 | Death |

---

## 6) Opportunity Attacks

### Trigger
- Creature moves out of your reach
- Creature stands up from prone (if within 5ft)

### Resolution
- One melee attack
- Reaction used

### Avoiding Opportunity Attacks
- Disengage action
- Move through friendly creatures
- Teleportation

---

## 7) Cover

| Cover Type | AC Bonus | Examples |
|------------|----------|----------|
| Half Cover | +2 | Low wall, tree trunk |
| Three-Quarters Cover | +5 | Corner of wall, arrow slit |
| Total Cover | Cannot be targeted | Behind solid wall |

---

## 8) Death and Dying

### Hit Points at 0
- Unconscious
- Must make Death Saving Throws

### Death Saving Throws
- Roll 1d20
- 10+: Success
- Below 10: Failure
- Three successes: stabilized
- Three failures: death
- Natural 20: regain 1 HP

### Damage at 0 HP
- If damage ≥ HP maximum: instant death
- If damage < HP maximum: one failed death save per 1 damage dealt

---

## 9) Combat Summary

| Phase | Action |
|-------|--------|
| 1 | Roll initiative |
| 2 | Highest goes first |
| 3 | Each turn: Move, Action, Bonus Action, Reaction |
| 4 | End of turn: Effects expire |
| 5 | Combat ends when one side surrenders, flees, or is defeated |
