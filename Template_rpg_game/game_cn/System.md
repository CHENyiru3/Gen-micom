# System.md — 世界实例路由器（入口点，无内核细节）

> **用途**：本世界实例的"入口/路由"文件：告诉内核在哪里读取内容包和状态。
> **稳定内核协议**：见 `KERNEL_PROMPT.md`（回合管线、HUD、RAG、ARCHIVE_DELTA）。

---

## 0) 热启动（推荐入口点）

按 `HOT_START.md` 执行。

最小读取集合：
- `HOT_PACK.md`
- `PLAYER_PROFILE.md`
- `OBJECT_INDEX.md`
- `sessions/CURRENT_SESSION.md` → 对应的 `sessions/session_*.md` 末尾 Decision
- `STATE_PANEL.md`
- `index.md`（只读"下一步目标/指针"）

初始化入口：`INIT_PROTOCOL.md`

---

## 1) 世界实例：内容包入口（可变）

### 1.1 状态
- `STATE_PANEL.md`（玩家可见的持久面板）
- `index.md`（导航索引/简短摘要）
- `lore/WORLD_STATE.md`（后端世界状态：指标、时钟、完整线索索引）
- `GOVERNANCE_PANEL.md`（治理面板：领土/追随者/资产；可选）

### 1.2 事件
- `sessions/SESSION_INDEX.md`
- `sessions/session_*.md`

### 1.3 设定库（正史/迷雾）
- `lore/INDEX.md`
- `lore/CANON/*`
- `lore/MIST/*`
- `lore/MECHANICS/*`

### 1.4 对象库（NPC/地点/任务）
- `characters/PCs/*`
- `characters/NPCs/*`
- `quests/QUEST_LOG.md`
- `locations/LOCATION_INDEX.md`

### 1.5 地图（内容包）
- `maps/MAP_INDEX.md`
- `maps/macro/*`、`maps/micro/*`、`maps/instances/*`

### 1.6 派生叙事（写作）
- `Writing/PIPELINE.md`
- `Writing/Fiction_index.md`
- `Writing/Fiction_par*.md`

> 默认：回合执行不读取 `Writing/`（除非玩家明确要求"写小说/对齐正文"）。

---

## 2) 输入协议入口

- 玩家输入协议：`CLI_SPEC.md`
- 规则检索门：`mechanics/RAG_RULES.md`
- 规则目录索引：`mechanics/INDEX.md`

---

## 3) 兼容性与历史

- 旧的"内核全包提示"已归档：`archive/System_legacy_2026-01-29.md`
- 存档按 `ARCHIVE_DELTA` 是权威的；历史 session 可能包含非标准的"存档增量"段落，**不作为协议**。
