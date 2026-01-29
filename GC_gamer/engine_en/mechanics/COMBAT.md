# COMBAT.md — Combat Rules

> **Purpose**: Combat adjudication, attack damage, defense, status effects
> **When to Retrieve**: Enter combat or when combat check needed
> **tags**: [combat, combat, initiative, damage, ac, status]

---

## COMBAT::initiative Initiative Order

1. At start of each round, roll `1d20 + Dexterity modifier`
2. Sort from high to low
3. Same dexterity: both parties in tie roll once

### Turn Structure
1. Player declares action
2. DM describes result/requests check
3. Roll check
4. DM describes result

---

## COMBAT::attack Attack and Damage

### Melee Attack

| Weapon | Damage | Speed | Notes |
|--------|--------|-------|-------|
| Fist | d3 | Fast | No damage bonus |
| Dagger | d4 | Fast | Can be concealed |
| Handaxe | d6 | Medium | Can be thrown |
| Shortsword | d6 | Medium | Common weapon |
| Longsword | d8 | Slow | Skilled +1 |
| Club | d4 | Medium | Easy to obtain |
| Mace | d8 | Slow | +1 vs armor |

### Ranged Attack

| Weapon | Damage | Range | Notes |
|--------|--------|-------|-------|
| Rock | d2 | Short | Available anywhere |
| Dart | d3 | Medium | Can be concealed |
| Shortbow | d6 | Medium | Requires bow |
| Crossbow | d8 | Far | Slow reload |

### Damage Formula
```
Damage = Weapon die + Strength modifier (melee) / Dexterity modifier (ranged)
```

---

## COMBAT::defense Defense

### Dodge (AC)

| Status | AC |
|--------|-----|
| Unarmored | 10 + Dexterity modifier |
| Leather | 11 + Dexterity modifier |
| Chainmail | 13 + Dexterity modifier (Dexterity -1) |
| Plate | 16 + Dexterity modifier (Dexterity -2) |

### Parry
- Requires using shield or off-hand weapon
- Successful parry: nullify one attack
- Failure: take damage normally

---

## COMBAT::status Status Effects

| Status | Effect | Duration |
|--------|--------|----------|
| **Injured** | -1 attack/defense | Until healed |
| **Severely Wounded** | -2 attack/defense, bleeding 1/round | Until healed |
| **Unconscious** | Cannot act | 1d6 minutes or healed |
| **Poisoned** | Strength/Dexterity -2 | 1d4 hours or antidote |
| **Stunned** | Cannot act | 1 round |
| **Frightened** | Will check required or flee | 1 round or pass |
| **Invisible** | Enemy cannot act first before attack | Until attack or discovered |

---

## COMBAT::environment Environmental Factors

| Factor | Effect |
|--------|--------|
| **Narrow Space** | Cannot flank, dodge +1 |
| **Dark/Fog** | Ranged attack disadvantage, perception -2 |
| **Muddy/uneven** | Movement -1/2 |
| **Flammables** | Fire damage +2 |
| **High Ground** | Thrown weapons +1, melee -1 |
| **Crowd Watching** | May cause unrest/wanted poster |

---

## COMBAT::non_lethal Non-Lethal Conflict

### Grappling
- Strength vs Strength
- Loser restrained, cannot use both hands

### Shoving
- Strength vs Strength
- Loser falls (1 round to stand)

### Coercion
- Using weapon to threaten
- Target needs Will check (vs threat level)
