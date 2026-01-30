# HOT_START.md — 热启动/重启协议（稳定）

> **目标**：让单 agent 在“上下文=0”的情况下，30–60 秒恢复可运行状态，并保证记忆外置可追溯。

---

## 0) 单一真源：各文件职责（避免重复）

- `campaigns/<id>/sessions/`：**事件真源**（Decision 追加；不重写历史）
- `campaigns/<id>/STATE_PANEL.json`：**玩家侧常驻面板**（短、可 patch、便于查看）
- `campaigns/<id>/HOT_PACK.json`：**下一回合热启动包**（≤25 行，机器可读；优先读取）
- `campaigns/<id>/index.md`：**导航索引**（只放指针与极短摘要，不放长篇世界观）
- `campaigns/<id>/WORLD_STATE.md`：**世界状态/后台指标与完整线索索引**（需要时再读）
- `cartridges/<id>/lore/INDEX.md`：**设定库入口**（回答世界观问题时用）
- `campaigns/<id>/GOVERNANCE_PANEL.md`：**统治面板（可选）**（进入领地/追随者玩法才读取）
- `engine/mechanics/`：规则包（触发才读，遵守 `engine/mechanics/RAG_RULES.md`）
- `cartridges/<id>/maps/`：地图内容包（需要地图时才读，先读 `cartridges/<id>/maps/MAP_INDEX.md`）
- `campaigns/<id>/Writing/`：派生叙事（不产出设定；默认不读）

---

## 1) 热启动读取顺序（强制）

1. `campaigns/<id>/HOT_PACK.json`：读取 `<!-- CONTEXT_PACK_NEXT ... -->`（如果存在）
2. `campaigns/<id>/PLAYER_PROFILE.md`：只读“偏好摘要”（≤8 行）
3. `campaigns/<id>/OBJECT_INDEX.json`：只读 active 指针（NPC/Quest/Location/Map 的 1 行摘要）
4. `campaigns/<id>/sessions/CURRENT_SESSION.md`：定位当前活跃 session 文件路径
5. 对应的 `campaigns/<id>/sessions/session_*.md`：只读末尾最近 1–3 个 Decision（不读整篇）
6. `campaigns/<id>/STATE_PANEL.json`：只读时间/指标/任务/NPC/时钟/位置（按需）
7. `campaigns/<id>/index.md`：只读“下一步会话目标/指针”（不读长篇）

若出现“信息不足”：再按需读取 `campaigns/<id>/quests/QUEST_LOG.md` 或 `cartridges/<id>/locations/LOCATION_INDEX.md`，最后才读 `campaigns/<id>/WORLD_STATE.md`。

---

## 2) 启动自检（防漂移）

启动后立刻检查：
- `campaigns/<id>/STATE_PANEL.json` 的指标/位置与最近 Decision 是否一致
- `campaigns/<id>/sessions/CURRENT_SESSION.md` 指向的文件是否存在且为最新会话
- 若冲突：以 `campaigns/<id>/sessions/` 为准，并在下一次 `ARCHIVE_DELTA` 写“纠偏说明”

### 未初始化检测（新战役）

若满足任一条件，视为“战役尚未初始化”：
- `campaigns/<id>/sessions/CURRENT_SESSION.md` 指向 `campaigns/<id>/sessions/session_0000_bootstrap.md`
- `campaigns/<id>/PLAYER_PROFILE.md` 的“偏好摘要”仍为 `-`

处理：提示用户发送 `<初始化>`，并按 `INIT_PROTOCOL.md` 完成落盘。

---

## 3) 每回合必须写入（确保持久性）

每回合结束通过 `ARCHIVE_DELTA` 至少更新：
- `campaigns/<id>/sessions/<current>.md`：append Decision
- `campaigns/<id>/STATE_PANEL.json`：patch（只改变化章节）
- `campaigns/<id>/HOT_PACK.json`：patch（写入最新 `CONTEXT_PACK_NEXT`）
