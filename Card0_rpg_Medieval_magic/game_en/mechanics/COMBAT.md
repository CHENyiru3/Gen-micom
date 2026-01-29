# COMBAT.md — Combat Rules

> **Purpose**: Combat adjudication, attack damage, defense, status effects
> **When to Retrieve**: When entering combat or combat check needed
> **tags**: [combat, combat, initiative, damage, ac, status]

---

## COMBAT::Initiative Order

1. At start of each round, roll `1d20 + DEX modifier`
2. Sort from high to low
3. Same DEX, each party in tie rolls once

### Turn Structure
1. Player declares action
2. DM describes result/requests check
3. Roll adjudication
4. DM describes result

---

## COMBAT::Attack and Damage

### Melee Attack

| Weapon | Damage | Speed | Notes |
|--------|--------|-------|-------|
| Fist | d3 | Fast | No damage bonus |
| Dagger | d4 | Fast | Can be concealed |
| Hand axe | d6 | Medium | Can be thrown |
| Shortsword | d6 | Medium | Common weapon |
| Longsword | d8 | Slow | Proficient +1 |
| Club | d4 | Medium | Easy to obtain |
| Mace | d8 | Slow | +1 vs armor |

### Ranged Attack

| Weapon | Damage | Range | Notes |
|--------|--------|-------|-------|
| Rock throw | d2 | Short | Available anywhere |
| Throwing knife | d3 | Medium | Can be concealed |
| Shortbow | d6 | Medium | Needs bow |
| Crossbow | d8 | Long | Slow reload |

### Damage Formula
```
Damage = Weapon die + STR modifier (melee) / DEX modifier (ranged)
```

---

## COMBAT::Defense

### Dodge (AC)

| Status | AC |
|--------|-----|
| Unarmored | 10 + DEX modifier |
| Leather | 11 + DEX modifier |
| Chain mail | 13 + DEX modifier (DEX-1) |
| Plate | 16 + DEX modifier (DEX-2) |

### Parry
- Need to use shield or off-hand weapon
- Successful parry: invalidates one attack
- Failure: take damage normally

---

## COMBAT::Status Effects

| Status | Effect | Duration |
|--------|--------|----------|
| **Injured** | -1 attack/defense | Until healed |
| **Seriously Wounded** | -2 attack/defense, bleeding 1/round | Until healed |
| **Unconscious** | Cannot act | 1d6 minutes or healed |
| **Poisoned** | STR/DEX-2 | 1d4 hours or antidote |
| **Stunned** | Cannot act | 1 round |
| **Frightened** | Must Will check or flee | 1 round or pass |
| **Invisible** | Enemy cannot preemptive attack before attack | Until attack or discovered |

---

## COMBAT::Environment Factors

| Factor | Effect |
|--------|--------|
| **Narrow Space** | Cannot flank, dodge+1 |
| **Darkness/Fog** | Ranged attack disadvantage, perception-2 |
| **Mud/Uneven** | Movement-1/2 |
| **Flammables** | Fire damage+2 |
| **High Ground** | Thrown weapons+1, melee-1 |
| **Crowd Watching** | May trigger riot/wanted |

---

## COMBAT::Non-Lethal Conflict

### Grapple
- Strength vs strength
- Loser pinned, cannot use both hands

### Shove
- Strength vs strength
- Loser falls (needs 1 round to stand)

### Intimidate
- Use weapon to threaten
- Target needs Will check (vs threat level)

