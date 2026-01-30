# 迷雾边境编年史：瞬变（工程化跑团 Repo）

本仓库把“长期记忆/状态/设定”外置为文件，LLM 只做回合执行器，从而保证：
- 可重启（上下文归零也能恢复）
- 可追溯（所有关键事件都在 `campaigns/<id>/sessions/`）
- 可压缩（热缓存只读少量文件）

---

## 1) 快速开始（新战役）

1. 发送：`<初始化>`（入口先读 `engine/System.md`）
2. 按 `engine/INIT_PROTOCOL.md` 完成两类配置：
   - 玩家偏好：写入 `campaigns/<id>/PLAYER_PROFILE.md`
   - 玩家角色：写入 `campaigns/<id>/characters/PCs/pc_current.md`
3. 初始化会创建新的 session，并更新：
   - `campaigns/<id>/sessions/CURRENT_SESSION.md`
   - `campaigns/<id>/STATE_PANEL.md`
   - `campaigns/<id>/HOT_PACK.md`
   - `campaigns/<id>/OBJECT_INDEX.md`

> 当前仓库已重置为“空白战役”。旧战役已归档：`archive/campaign_clermond_2026-01-29/`

---

## 0) 战役目录（core vs 存档分离）

本仓库把“可复用 core”与“每个战役的存档/状态”分离：

- **Engine（共享）**：`engine/`（此处为软链接，真实位置在 `GC_gamer/engine_cn/`）
- **Cartridge（世界内容）**：`cartridges/<cartridge_id>/...`
- **Template 卡带**：`../../Blank_Cartidge_template/game_cn/cartridges/template/`（所有新卡带的起点）
- **Campaign（每个战役一份）**：`campaigns/<campaign_id>/...`

当前激活战役：`ACTIVE.md`

切换战役的最小做法：
1) 更新 `ACTIVE.md` 指向新目录  
2) 更新目标战役 `CAMPAIGN.md` 的 cartridge 绑定（如需）

### 自动化（推荐）

```bash
python3 engine/scripts/campaign_manager.py new --id campaign_0002
python3 engine/scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

说明见：`engine/CAMPAIGN_PROTOCOL.md`

### 用户友好方式（不需要你运行 Python）

你只需要在对话里输入控制指令，AI 会代为执行脚本与文件变更：
- `<新战役 campaign_0002>`：创建并切换到新战役（入口先读 `engine/System.md`）
- `<切换战役 campaigns/campaign_0001>`：切换到已有战役（入口先读 `engine/System.md`）
- `<初始化>`：在当前战役里运行初始化向导（入口先读 `engine/System.md`）

---

## 3.1 对话命令入口约定（统一入口）

以下命令均先读取 `engine/System.md` 作为入口路由，然后再读取对应协议文件：
- `<初始化>` → `engine/INIT_PROTOCOL.md`
- `<新战役 ...>` / `<切换战役 ...>` → `engine/CAMPAIGN_PROTOCOL.md`
- `<热启动>` / `<继续>` → `engine/HOT_START.md`

---

## 2) 热缓存（HOT）是什么、怎么用

热缓存的目标：每回合/每次重启只读最少文件就能继续玩。

你只需要知道两个文件：
- `campaigns/<id>/HOT_PACK.md`：**下一回合上下文包**（只含 1 个 `CONTEXT_PACK_NEXT` 注释块）
- `campaigns/<id>/OBJECT_INDEX.md`：**活跃对象索引**（NPC/任务/地点/地图的“指针 + 1 行摘要”）

通常玩家不需要手动编辑它们；它们应由每回合输出的 `ARCHIVE_DELTA` 自动 patch。

规范见：
- `engine/mechanics/CONTEXT_PACK.md`
- `engine/ARCHIVE_DELTA.md`

---

## 3) 热启动（恢复/继续）

当你换设备/新窗口/上下文丢失时，按 `engine/HOT_START.md` 执行（推荐直接发送 `<热启动>` 或 `<继续>`）。
入口统一：先读 `engine/System.md`，再按 `HOT_START.md` 顺序加载。

热启动读取顺序（概念上）：
1. `campaigns/<id>/HOT_PACK.md`
2. `campaigns/<id>/PLAYER_PROFILE.md`（只读“偏好摘要”）
3. `campaigns/<id>/OBJECT_INDEX.md`
4. `campaigns/<id>/sessions/CURRENT_SESSION.md` → 当前 session 文件末尾 1–3 个 Decision
5. `campaigns/<id>/STATE_PANEL.md`
6. `campaigns/<id>/index.md`（只读导航）

如果仓库尚未初始化，会提示你重新 `<初始化>`。

---

## 4) 如何与 AI 高效交互（强烈推荐）

### 4.1 用标签输入，减少歧义

优先使用 `engine/CLI_SPEC.md` 的命令头：
- `[ACT]` / `[LOOK]` / `[ASK]` / `[FIGHT]` / `[CAST]` / `[MANAGE]` / `[OOC]`

### 4.2 复制 HUD 短码，减少匹配失败

每回合 AI 会给 HUD（`L# / N# / I# / Q#`）。你可以直接引用：
- `[行动]{与 N1 交谈}`
- `[行动]{调查 L2}`

### 4.3 OOC 规则/协议问题

用 `[OOC]` 提问，并让 AI 指向具体文件作为权威来源（避免口径漂移）。

---

## 5) 故事偏好优化（个性化 DM）

偏好文件：`campaigns/<id>/PLAYER_PROFILE.md`

使用方式：
- 初始化时填写（推荐）
- 你也可以随时 OOC 修改偏好（例如“更恐怖/更快节奏/战斗更少”），AI 会 patch `campaigns/<id>/PLAYER_PROFILE.md`

上下文压缩策略：
- 每回合只需要把偏好摘要中的 1 行（如 `STYLE=...`）压进 `campaigns/<id>/HOT_PACK.md flags=`，其余不常读。

---

## 6) 稳定真源（不要混用）

- 内核协议（怎么跑）：`engine/KERNEL_PROMPT.md`
- 世界入口（指针/路由）：`engine/System.md`
- 事件真源（历史）：`campaigns/<id>/sessions/`
- 玩家侧状态面板：`campaigns/<id>/STATE_PANEL.md`
- 后台世界状态索引：`campaigns/<id>/WORLD_STATE.md`
- 增量存档规范：`engine/ARCHIVE_DELTA.md`
- 会话结束漂移检查：`engine/CONTINUITY_CHECK.md`

---

## 7) 隐藏 DM 文件（提升体验：悬念/规划/幕后动机）

这些文件属于 DM/AI 的幕后工具，**严禁直接在玩家可见输出里引用或剧透**：

- `.DM_SECRETS.md`：未公开真相/幕后设定（触发后迁移到 `campaigns/<id>/sessions/` 与内容包）
- `.DM_PLANNER.md`：故事规划与悬念引擎（主线/Fronts/线索库存/反转/下一会话 beats）

它们随战役一起存放在：`campaigns/<id>/`（不再使用 root 子目录）。

---

## 8) 现在开始创建新的卡带故事

1. 复制 `../../Blank_Cartidge_template/game_cn/cartridges/template/` → `cartridges/<new_card_id>/`（保持 lore/locations/quests/characters/maps 等结构）。
2. 编辑 `cartridges/<new_card_id>/CARTRIDGE.md`：补全 `routes`、`aliases`、`invariants` 以及是否启用的 `feature_flags`（如地图/小说/治理）。
3. 使用 `python3 engine/scripts/campaign_manager.py new --id campaigns/<new_campaign>` 创建新战役。
4. 将新战役的 `CAMPAIGN.md` 里的 `cartridge_id` 修改为刚刚创建的 `<new_card_id>` 并锁定 `cartridge_version_lock`。
5. 切换到该战役 (`<切换战役 campaigns/<new_campaign>`)，所有 Engine 模块继续共用，世界则由新的卡带提供。
