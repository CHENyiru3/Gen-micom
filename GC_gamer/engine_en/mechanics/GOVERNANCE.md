# GOVERNANCE.md — Governance Panel

> **Purpose**: Territory management, followers, military, commercial assets
> **When to Retrieve**: When player gains land/followers or performs governance settlement
> **tags**: [governance, territory, followers, military, commerce]

---

## GOV::resources Resource Classification System

### Human Resources

| Type | Quantity | Loyalty | Description |
|------|----------|---------|-------------|
| **Serfs/Peasants** | X people | 0-10 | Cultivate land, produce food |
| **Citizens/Freemen** | X people | 0-10 | Engage in handicraft/commerce |
| **Soldiers** | X people | 0-10 | Combat units |
| **Specialists** | X people | 0-10 | Blacksmiths, physicians, scholars, etc. |
| **Followers** | X people | 0-10 | Adventure companions, advisors |

### Loyalty Impact

| Loyalty | Effect |
|---------|--------|
| ≥8 | Voluntary obedience, may serve for free |
| 5-7 | Normal obedience, reasonable payment |
| 2-4 | Requires monitoring, may flee |
| ≤1 | May rebel, sabotage |

---

## GOV::military Military Forces

| Type | Quantity | Equipment | Training | Monthly Cost |
|------|----------|-----------|----------|--------------|
| **Militia** | X people | Crude | Low | Food |
| **Standing Army** | X people | Standard | Medium | Silver X |
| **Knights** | X people | Excellent | High | Gold X |
| **Archers** | X people | Compound bow | Medium | Silver X |
| **Cavalry** | X people | War horse | High | Gold X |

### Training Level Grades

| Level | Description |
|-------|-------------|
| 1 (Lowest) | Just picked up weapons peasants |
| 2-3 (Low) | Has basic combat experience |
| 4-5 (Medium) | Regular army level |
| 6-7 (High) | Elite forces |
| 8-10 (Highest) | Elite among elites |

---

## GOV::land Land Assets

| Type | Scale | Output | Special Resources |
|------|-------|--------|-------------------|
| **Farmland** | X mu | Food X units/year | - |
| **Pasture** | X mu | Meat X units/year | War horses |
| **Forest** | X mu | Wood X units/year | Game |
| **Mine** | X spots | Ore X units/year | Precious metals |
| **Fishing Ground** | X spots | Fish X units/year | - |
| **Settlement** | X spots | Tax X/year | Population |

### Land Grades

| Grade | Output |
|-------|--------|
| Barren | -50% |
| Normal | Standard |
| Fertile | +50% |
| Abundant | +100% |

---

## GOV::commerce Commercial Assets

| Type | Quantity | Capital | Profit/Period |
|------|----------|---------|---------------|
| **Caravan** | X trains | Gold X | X% |
| **Merchant Ship** | X ships | Gold X | X% |
| **Shop** | X rooms | Silver X | X/month |
| **Warehouse** | X buildings | - | Store X units |
| **Trade Route** | X routes | - | Exclusive/Competition |

---

## GOV::tier Faction Grades

| Grade | Name | Requirements | Privileges |
|-------|------|--------------|------------|
| 0 | Exile | No land | - |
| 1 | Minor Noble | 1 land + 10 followers | Receive title |
| 2 | Baron | 2 lands + 50 followers | Tax right |
| 3 | Viscount | 3 lands + 100 followers + 30 soldiers | Build fortress |
| 4 | Earl | 5 lands + 200 followers + 100 soldiers | Minting right |
| 5 | Marquis | 8 lands + 500 followers + 300 soldiers | Army limit +1 |
| 6 | Duke | 12 lands + 1000 followers + 500 soldiers | Declare war |
| 7 | Kingdom Founder | 20 lands + 2000 followers + 1000 soldiers | Establish kingdom |

---

## GOV::settlement Turn Settlement

### Income Calculation
```
Total Income = Agricultural Output + Commercial Profit + Tax - Maintenance Cost
```

### Expenditure Items

| Item | Cost |
|------|------|
| Army monthly salary | Calculated by people × training |
| Official salary | By position |
| Building maintenance | By building count |
| Emergencies | Disease, disaster, war compensation |

### Net Profit
```
Net Profit = Total Income - Total Expenditure
Positive: Accumulate wealth, can use for investment/savings
Negative: Consume reserves, loyalty decline risk
```

---

## GOV::followers Follower System

### Acquisition Methods

| Method | Success Rate | Risk |
|--------|--------------|------|
| Recruit wanderers | High | Low loyalty |
| Hire professionals | Medium | High cost |
| Conquer prisoners | Low | Requires conversion |
| Attract refugees | High | Management difficulty |
| Save village | Medium | Protection promise needed |

### Daily Management

- Monthly food consumption = follower count × 2 units
- Insufficient food → Loyalty -1/month, escape probability +10%
- Regular rewards → Loyalty +1

### Loyalty Events

| Event | Loyalty Change |
|-------|----------------|
| Battle victory | +1~2 |
| Battle defeat | -1~3 |
| Issue bonus | +1~2 |
| Withhold supplies | -2~5 |
| Lord dies in battle | Followers scatter |

---

## GOV::military_units Military Unit Management

### Unit Creation
```
Recruitment Cost = Basic Equipment + Training Fee + Settlement Fee
Training Time = Basic Training × (10 - Training Level) / 10
```

### Unit Upgrades

| Upgrade | Condition | Effect |
|---------|-----------|--------|
| Militia→Regular | 30 days training + 1 battle | Combat effectiveness +2 |
| Regular→Elite | 60 days training + gold X | Combat effectiveness +3 |
| Elite→Guard | Special task + lord recognition | Exclusive loyalty |

### Standard Configuration (100 people)
- 20% Archers (ranged)
- 30% Pikemen (defense)
- 30% Swordsmen (assault)
- 20% Cavalry (mobile)

### Special Units

| Unit | Features |
|------|----------|
| Heavy Armored Knight | Training cost 3×, maintenance cost 2× |
| Ranger Scout | Reconnaissance +2, combat -1 |
| Combat Engineer | Siege efficiency +3, combat -2 |

---

## GOV::buildings Building Management

### Building Types

| Building | Function | Build Time | Build Cost |
|----------|----------|------------|------------|
| Cottage | Accommodate 10 people | 10 days | 50 silver |
| Warehouse | Store 100 units | 15 days | 100 silver |
| Mill | Food processing | 20 days | 150 silver |
| Blacksmith | Weapon repair | 25 days | 200 silver |
| Barracks | Soldier training | 30 days | 300 silver |
| Fortress | Defense +5 | 60 days | 50 gold |
| City Wall | Defense +10 | 90 days | 100 gold |
| Port | Ship docking | 45 days | 80 gold |

### Recommended Development Order
1. Cottage (accommodate population)
2. Warehouse (store resources)
3. Mill (increase output)
4. Barracks (train army)
5. Blacksmith (equipment maintenance)
6. Fortress/City Wall (defense)
7. Port (trade expansion)

---

## GOV::events Event Impact Table

| Event | Trigger Condition | Impact |
|-------|-------------------|--------|
| Harvest | Agriculture level ≥3 + good weather | Food +50%, Loyalty +1 |
| Poor harvest | Agriculture level ≤2 + bad weather | Food -30%, Loyalty -2 |
| Plague | Poor sanitation + crowded population | Population -10% |
| Rebellion | Persistent low loyalty + high tax | Lose land/followers |
| Invasion | Border empty + hostile faction | Battle or cede land |
| Prosperity | Commerce level ≥4 + many trade routes | Income +30% |
| Harvest celebration | Any quarter | Loyalty +1, gold -5% |
| Monastery donation | Church reputation ≥ friendly | Grace +1, gold -10% |

---

## GOV::interface Governance Panel Interface Template

```
╔════════════════════════════════════════════════════════════╗
║              Governance Panel - [Faction Name]              ║
╠════════════════════════════════════════════════════════════╣
║ Faction Grade: [X] [Grade Name]      Ruling Days: XXX      ║
╠════════════════════════════════════════════════════════════╣
║ 🌾 Resources                                                ║
║   Gold: XXX     Food: XXX units    Wood: XXX    Ore: XXX   ║
║   Population: XXX   Army: XXX people   Land: XXX mu        ║
╠════════════════════════════════════════════════════════════╣
║ ⚔️ Military                                                ║
║   Militia: XX   Standing Army: XX   Knights: XX   Special: XX  ║
║   Average Training: X.X   Defense Level: XX   Monthly Cost: XXX║
╠════════════════════════════════════════════════════════════╣
║ 🏰 Land                                                    ║
║   [Land1] [Grade] [Output] [Garrison]  [Status: Normal/Damaged]║
║   [Land2] [Grade] [Output] [Garrison]  [Status: Normal/Damaged]║
╠════════════════════════════════════════════════════════════╣
║ ⚓ Commerce                                                ║
║   Caravan: XX   Merchant Ship: XX   Shop: XX   Trade Routes: XX║
║   Monthly Profit: XXX   Transport Capacity: XXX   Port Grade: X║
╠════════════════════════════════════════════════════════════╣
║ 👥 Followers                                               ║
║   Core Followers: [list]                                   ║
║   Common Population: XXX   Loyalty: XX   Monthly Consumption: XXX║
╠════════════════════════════════════════════════════════════╣
║ 📊 Last Quarter Settlement                                 ║
║   Total Income: XXX   Total Expenditure: XXX   Net Profit: XXX [+/ -]║
║   Status: [Surplus/Balance/Deficit]                        ║
╚════════════════════════════════════════════════════════════╝
```
