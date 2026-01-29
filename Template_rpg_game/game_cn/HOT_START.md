# HOT_START.md — 热启动/重启协议（稳定）

> **目标**：允许单个 agent 在"上下文=0"的情况下 30-60 秒内恢复到可运行状态，并确保记忆外置可追溯。

---

## 0) 单一真源：文件职责（避免重复）

- `sessions/`：**事件真源**（Decision appends；永远不要重写历史）
- `STATE_PANEL.md`：**玩家侧持久面板**（简短，可 patch，易于查看）
- `HOT_PACK.md`：**下一回合热启动包**（≤25 行，机器可读；优先读取）
- `index.md`：**导航索引**（只有指针和非常短的摘要，没有冗长的世界观构建）
- `lore/WORLD_STATE.md`：**世界状态/后端指标和完整线索索引**（需要时读取）
- `lore/INDEX.md`：**设定库入口**（回答世界观问题时使用）
- `GOVERNANCE_PANEL.md`：**治理面板（可选）**（进入领土/追随者游戏时读取）
- `mechanics/`：规则包（触发时读取，遵循 `mechanics/RAG_RULES.md`）
- `maps/`：地图内容包（需要地图时读取，先读 `maps/MAP_INDEX.md`）
- `Writing/`：派生叙事（不产出设定；默认不读取）

---

## 1) 热启动读取顺序（强制）

1. `HOT_PACK.md`：读取 `<!-- CONTEXT_PACK_NEXT ... -->`（如果存在）
2. `PLAYER_PROFILE.md`：只读"偏好摘要"（≤8 行）
3. `OBJECT_INDEX.md`：只读活跃指针（NPC/任务/地点/地图 的 1 行摘要）
4. `sessions/CURRENT_SESSION.md`：定位当前活跃 session 文件路径
5. 对应的 `sessions/session_*.md`：只读最近 1-3 个 Decision（不是整个文档）
6. `STATE_PANEL.md`：读取时间/指标/任务/NPC/时钟/地点（需要时）
7. `index.md`：只读"下一会话目标/指针"（不要长文）

如果"信息不足"：然后按需读取 `quests/QUEST_LOG.md` 或 `locations/LOCATION_INDEX.md`，最后读取 `lore/WOR---

## 2LD_STATE.md`。

) 启动自检（防止漂移）

启动后立即检查：
- `STATE_PANEL.md` 中的指标/地点与最近的 Decision 是否一致
- `sessions/CURRENT_SESSION.md` 指向现有文件且是最新会话
- 如果冲突：使用 `sessions/` 作为权威，在下一个 `ARCHIVE_DELTA` 中写"纠偏说明"

### 未初始化检测（新战役）

如果满足任一条件，视为"战役尚未初始化"：
- `sessions/CURRENT_SESSION.md` 指向 `sessions/session_0000_bootstrap.md`
- `PLAYER_PROFILE.md` 中的"偏好摘要"仍是 `-`

处理：提示用户发送 `<初始化>`，按 `INIT_PROTOCOL.md` 完成持久化。

---

## 3) 每回合必须写入（确保持久化）

每回合结束通过 `ARCHIVE_DELTA` 至少更新：
- `sessions/<current>.md`：append Decision
- `STATE_PANEL.md`：patch（仅变化的段落）
- `HOT_PACK.md`：patch（写入最新的 `CONTEXT_PACK_NEXT`）
