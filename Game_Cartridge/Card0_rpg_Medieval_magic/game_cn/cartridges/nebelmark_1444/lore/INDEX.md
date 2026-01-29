# lore/INDEX.md — 迷雾边境设定库索引

> **版本**: v1.1 | **用途**: RAG 检索入口 | **最后更新**: 2026-01-29

## RAG_HEAD（4-6行摘要）

- Canon：WORLD/FACTIONS/TIMELINE 为白昼史真源。
- Mist：LAESURAE/PHENOMENA 为可探索迷雾设定。
- Mechanics：INDICATORS 为四指标规则入口。
- 关键词检索优先从本索引表定位。

## 索引字段规范（兼容模板卡带）

| 字段 | 说明 |
|------|------|
| handle | 推荐 @句柄（稳定引用） |
| file | 目标文件 |
| tags | 关键标签 |
| summary | 一句话用途说明 |

## 句柄映射（不改变原内容）

| handle | file | summary |
|--------|------|---------|
| @lore_world | CANON/WORLD.md | 世界框架 |
| @lore_factions | CANON/FACTIONS.md | 势力详情 |
| @lore_timeline | CANON/TIMELINE.md | 时间线 |
| @lore_city | MIST/LAESURAE.md | 城市风貌 |
| @lore_phenomena | MIST/PHENOMENA.md | 迷雾现象 |
| @lore_indicators | MECHANICS/INDICATORS.md | 指标规则 |

---

## 0. 快速导航

| 玩家问题 | 检索锚点 | 片段限制 |
|----------|----------|----------|
| "这个时代教会怎样？" | `CANON/WORLD.md` + `tags: [church]` | ≤3 段 |
| "菲姆法庭是什么？" | `CANON/FACTIONS.md` + `tags: [vehm]` | ≤2 段 |
| "内伯尔海姆结构？" | `MIST/LAESURAE.md` + `tags: [city, urban]` | ≤2 段 |
| "查理七世是谁？" | `CANON/FACTIONS.md` + `tags: [npc, france]` | ≤1 段 |
| "恩典怎么用？" | `MECHANICS/INDICATORS.md` | ≤1 段 |
| "有什么怪异现象？" | `MIST/PHENOMENA.md` | ≤3 段 |

---

## 1. 目录结构

```
lore/
├── INDEX.md              ← 你在这里
├── CANON/                ← 白昼史（不可改）
│   ├── WORLD.md          ← 世界框架（地图/时代/势力）
│   ├── FACTIONS.md       ← 六大势力详情
│   └── TIMELINE.md       ← 1444-1446 大事记
├── MIST/                 ← 迷雾史（可探索）
│   ├── LAESURAE.md       ← 城市风貌与市井环境
│   └── PHENOMENA.md      ← 异想生物与怪异现象
└── MECHANICS/            ← 机制设定
    ├── INDICATORS.md     ← 四指标规则（Grace/Debt/Rumor/Heat）
    └── RANDOM_TABLES.md  ← 随机遭遇表
```

---

## 2. CANON 层（白昼史）

### 2.1 WORLD.md — 世界框架

| 标签 | 内容 |
|------|------|
| `tags` | [canon, world, geography, era] |
| `related` | [FACTIONS.md, TIMELINE.md] |

**速查锚点**：
- 迷雾边境：Nebelmark，位于莱茵上游左岸
- 主城：内伯尔海姆 (Nebelheim)
- 时代：1444年（裂纹期）
- 设计支柱：白昼史不被推翻、奇幻以渗出出现、神罚与赎罪并存

### 2.2 FACTIONS.md — 六大势力

| 标签 | 内容 |
|------|------|
| `tags` | [canon, faction, france, empire, burgundy, church, vehm] |
| `related` | [WORLD.md, TIMELINE.md] |

**势力速查**：
- 法兰西王国：瓦卢瓦王朝，查理七世，雇佣兵输出
- 神圣罗马帝国：空心皇冠，中央无力
- 勃艮第公国：好人菲利普，渗透策略
- 教会：巴塞尔会议，权威脆弱
- 菲姆法庭：秘密审判系统，迷雾史势力
- 剥皮者：雇佣兵联合体

### 2.3 TIMELINE.md — 大事记

| 标签 | 内容 |
|------|------|
| `tags` | [canon, timeline, history] |
| `related` | [FACTIONS.md, WORLD.md] |

**关键节点**：
- 1429：克莱门特八世退位
- 1444：裂纹期开始，个案怪事增多
- 1445/46：阈值跨越（瞬变发生），迷雾稳定

### 2.4 Char.md — 1444 莱茵危机人物网络（扩展 canon）

| 标签 | 内容 |
|------|------|
| `tags` | [canon, character-network, rhine_crisis, era:1444] |
| `related` | [CANON/WORLD.md, CANON/FACTIONS.md, CANON/TIMELINE.md] |

**用途**：
- 当玩家/DM需要“1444 莱茵危机的人物关系网、阵营投影、可用冒险钩子”时，检索本文件的小片段（≤2 段）。

---

## 3. MIST 层（迷雾史）

### 3.1 LAESURAE.md — 城市风貌与市井环境

| 标签 | 内容 |
|------|------|
| `tags` | [mist, location, city, urban, vice] |
| `related` | [PHENOMENA.md, WORLD.md] |

**分区**：
- 外层棚户与难民带：饥饿的围城
- 行会街与工坊带：噪音、手艺与算计
- 市集与酒馆：流言的发动机
- 犹太巷与账房：文字的刀
- 大教堂区与修会：光与腐朽同居
- 刽子手桥与城外边缘：被诅咒的必要之恶

### 3.2 PHENOMENA.md — 异想生物与怪异现象

| 标签 | 内容 |
|------|------|
| `tags` | [mist, creature, phenomenon, religion, heresy] |
| `related` | [LAESURAE.md, INDICATORS.md] |

**异想生物**：
- 赎罪鸟、告解蛞蝓、圣痕乞丐
- 七灯烛童、盐灰修士、雾庭辩者

**裂纹期现象**：
- 梦疫、雾印、漏圣所、错位账本
- 树上的匕首、狂猎残影

---

## 4. MECHANICS 层（机制）

### 4.1 INDICATORS.md — 四指标系统

| 标签 | 内容 |
|------|------|
| `tags` | [mechanic, indicator, grace, debt, rumor, heat] |
| `related` | [PHENOMENA.md] |

**指标**：
| 指标 | 范围 | 含义 |
|------|------|------|
| Grace | 0-10 | 神圣秩序可用性 |
| Debt | 0-10 | 人类赎罪压力 |
| Rumor | 0-3 | 公众议论程度 |
| Heat | 0-3 | 势力关注度 |

**核心法则**：
- 公开施法/怪物目击 → Rumor+1
- Rumor≥2 → 调查力量必介入
- 暴力/滥用魔法 → Debt+1
- 救人/拒绝诱惑 → Debt-1 或 Grace+1

### 4.2 RANDOM_TABLES.md — 随机遭遇表

| 标签 | 内容 |
|------|------|
| `tags` | [random, encounter, table, urban, travel, dream] |
| `related` | [MIST/LAESURAE.md] |

**遭遇类型**：
- 街头遭遇 d10（风险、线索、环境）
- 夜晚遭遇 d8（神秘、怪异、警觉）
- 梦境片段 d6（创伤、裂隙、预兆）

---

## 5. RAG 检索规则

| 触发条件 | 行为 |
|----------|------|
| 玩家问世界观问题 | 检索 CANON/ 文件，输出 ≤3 片段 |
| 玩家问机制问题 | 检索 MECHANICS/ 文件，输出 ≤1 片段 |
| 玩家问怪异现象 | 检索 MIST/PHENOMENA.md，输出 ≤3 片段 |
| 玩家问城市环境 | 检索 MIST/LAESURAE.md，输出 ≤2 片段 |
| 玩家问NPC背景 | 检索 CANON/FACTIONS.md 或 NPCs/，输出 ≤2 片段 |

**禁止**：整表/整章塞入上下文

---

## 6. 文件模板

新建设定文件请使用以下模板：

```md
---
tags: [canon|mist|mechanic, 主标签, 副标签]
related: [相关文件.md]
---

# 文件标题

## 0. 速查锚点
- 关键概念1
- 关键概念2

## 1. 核心设定
（正文，可被 RAG 片段检索）

## 2. 游戏关联
- 相关地点：loc_xxx
- 相关任务：quest_xxx
- 相关NPC：npc_xxx
```

---

*INDEX.md v1.1 - 迷雾边境编年史*
