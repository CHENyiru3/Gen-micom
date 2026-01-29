# 迷雾边境编年史：瞬变（工程化跑团 Repo）

本仓库把“长期记忆/状态/设定”外置为文件，LLM 只做回合执行器，从而保证：
- 可重启（上下文归零也能恢复）
- 可追溯（所有关键事件都在 `sessions/`）
- 可压缩（热缓存只读少量文件）

---

## 1) 快速开始（新战役）

1. 发送：`<初始化>`
2. 按 `INIT_PROTOCOL.md` 完成两类配置：
   - 玩家偏好：写入 `PLAYER_PROFILE.md`
   - 玩家角色：写入 `characters/PCs/pc_current.md`
3. 初始化会创建新的 session，并更新：
   - `sessions/CURRENT_SESSION.md`
   - `STATE_PANEL.md`
   - `HOT_PACK.md`
   - `OBJECT_INDEX.md`

> 当前仓库已重置为“空白战役”。旧战役已归档：`archive/campaign_clermond_2026-01-29/`

---

## 0) 战役目录（core vs 存档分离）

本仓库把“可复用 core”与“每个战役的存档/状态”分离：

- **Core（共享）**：`KERNEL_PROMPT.md`、`mechanics/`、`lore/`、`maps/`、`Char.md`、`Map-Gen.md` 等
- **Campaign（每个战役一份）**：`campaigns/<campaign_id>/...`

当前激活战役：`CURRENT_CAMPAIGN.md`

为兼容旧路径，根目录的以下路径是**符号链接**（指向当前战役）：
- `sessions/`、`quests/`、`characters/`、`Writing/`
- `STATE_PANEL.md`、`HOT_PACK.md`、`OBJECT_INDEX.md`、`PLAYER_PROFILE.md`、`GOVERNANCE_PANEL.md`、`.DM_SECRETS.md`

切换战役的最小做法：
1) 更新 `CURRENT_CAMPAIGN.md` 指向新目录  
2) 重新建立上述符号链接（保持“根路径不变”）

### 自动化（推荐）

```bash
python3 scripts/campaign_manager.py new --id campaign_0002
python3 scripts/campaign_manager.py switch --path campaigns/campaign_0001
```

说明见：`CAMPAIGN_PROTOCOL.md`

### 用户友好方式（不需要你运行 Python）

你只需要在对话里输入控制指令，AI 会代为执行脚本与文件变更：
- `<新战役 campaign_0002>`：创建并切换到新战役
- `<切换战役 campaigns/campaign_0001>`：切换到已有战役
- `<初始化>`：在当前战役里运行初始化向导（角色 + 偏好）

---

## 2) 热缓存（HOT）是什么、怎么用

热缓存的目标：每回合/每次重启只读最少文件就能继续玩。

你只需要知道两个文件：
- `HOT_PACK.md`：**下一回合上下文包**（只含 1 个 `CONTEXT_PACK_NEXT` 注释块）
- `OBJECT_INDEX.md`：**活跃对象索引**（NPC/任务/地点/地图的“指针 + 1 行摘要”）

通常玩家不需要手动编辑它们；它们应由每回合输出的 `ARCHIVE_DELTA` 自动 patch。

规范见：
- `mechanics/CONTEXT_PACK.md`
- `ARCHIVE_DELTA.md`

---

## 3) 热启动（恢复/继续）

当你换设备/新窗口/上下文丢失时，按 `HOT_START.md` 执行（推荐直接发送 `<热启动>` 或 `<继续>`）。

热启动读取顺序（概念上）：
1. `HOT_PACK.md`
2. `PLAYER_PROFILE.md`（只读“偏好摘要”）
3. `OBJECT_INDEX.md`
4. `sessions/CURRENT_SESSION.md` → 当前 session 文件末尾 1–3 个 Decision
5. `STATE_PANEL.md`
6. `index.md`（只读导航）

如果仓库尚未初始化，会提示你重新 `<初始化>`。

---

## 4) 如何与 AI 高效交互（强烈推荐）

### 4.1 用标签输入，减少歧义

优先使用 `CLI_SPEC.md` 的标签：
- `[行动]{...}` / `[对话]"..."` / `[调查]{...}` / `[战斗]{...}` / `[管理]{...}` / `[内心]{...}` / `<OOC>...`

### 4.2 复制 HUD 短码，减少匹配失败

每回合 AI 会给 HUD（`L# / N# / I# / Q#`）。你可以直接引用：
- `[行动]{与 N1 交谈}`
- `[行动]{调查 L2}`

### 4.3 OOC 规则/协议问题

用 `<OOC>` 提问，并让 AI 指向具体文件作为权威来源（避免口径漂移）。

---

## 5) 故事偏好优化（个性化 DM）

偏好文件：`PLAYER_PROFILE.md`

使用方式：
- 初始化时填写（推荐）
- 你也可以随时 OOC 修改偏好（例如“更恐怖/更快节奏/战斗更少”），AI 会 patch `PLAYER_PROFILE.md`

上下文压缩策略：
- 每回合只需要把偏好摘要中的 1 行（如 `STYLE=...`）压进 `HOT_PACK.md flags=`，其余不常读。

---

## 6) 稳定真源（不要混用）

- 内核协议（怎么跑）：`KERNEL_PROMPT.md`
- 世界入口（指针/路由）：`System.md`
- 事件真源（历史）：`sessions/`
- 玩家侧状态面板：`STATE_PANEL.md`
- 后台世界状态索引：`lore/WORLD_STATE.md`
- 增量存档规范：`ARCHIVE_DELTA.md`
- 会话结束漂移检查：`CONTINUITY_CHECK.md`

---

## 7) 隐藏 DM 文件（提升体验：悬念/规划/幕后动机）

这些文件属于 DM/AI 的幕后工具，**严禁直接在玩家可见输出里引用或剧透**：

- `.DM_SECRETS.md`：未公开真相/幕后设定（触发后迁移到 `sessions/` 与内容包）
- `.DM_PLANNER.md`：故事规划与悬念引擎（主线/Fronts/线索库存/反转/下一会话 beats）

它们随战役一起存放在：`campaigns/<id>/root/`，根目录为兼容保留符号链接。
