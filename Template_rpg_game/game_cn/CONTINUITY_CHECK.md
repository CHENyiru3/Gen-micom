# CONTINUITY_CHECK.md — 会话结束漂移验证检查清单

> **用途**：在会话结束前验证状态文件一致；防止 `sessions/`（权威）与 `STATE_PANEL.md`/`OBJECT_INDEX.md` 之间的漂移。

---

## 飞行前检查清单（结束会话前）

### 1) 事件真源验证
- [ ] `sessions/<current>.md` 已追加最新的 Decision
- [ ] Decision 包含：现实时间、游戏中时间、玩家输入、裁决、后果、指标、时钟

### 2) 状态面板验证
- [ ] `STATE_PANEL.md` 时间与最新的 Decision 一致
- [ ] `STATE_PANEL.md` 指标（恩泽/债务/传闻/热度）反映了所有变化
- [ ] `STATE_PANEL.md` 任务状态反映了所有已完成/更新的任务
- [ ] `STATE_PANEL.md` NPC 关系更新了新的信任/状态值
- [ ] `STATE_PANEL.md` 时钟推进到正确的进度
- [ ] `STATE_PANEL.md` 背包反映了所有获得/丢失的物品
- [ ] `STATE_PANEL.md` 关键线索列表是最新的
- [ ] `STATE_PANEL.md` 地点是当前的

### 3) 对象索引验证
- [ ] `OBJECT_INDEX.md` 活跃地点目标是准确的
- [ ] `OBJECT_INDEX.md` 活跃任务是当前的
- [ ] `OBJECT_INDEX.md` 活跃 NPC 反映了遇到的人
- [ ] `OBJECT_INDEX.md` 当前 PC 指向正确的文件

### 4) 热启动包验证
- [ ] `HOT_PACK.md` 包含有效的 `CONTEXT_PACK_NEXT`
- [ ] `CONTEXT_PACK_NEXT` 反映当前状态

### 5) 漂移纠正（如发现）

如果发现任何不一致：
1. 使用 `sessions/` 作为权威来源
2. 在会话的最后一个 Decision 中写"纠偏说明"
3. Patch `STATE_PANEL.md` / `OBJECT_INDEX.md` 使其匹配

---

## 会话结束输出模板

```markdown
<!-- SESSION_END_CHECK
verified:
  - sessions_last_decision: true/false
  - state_panel_time: true/false
  - state_panel_indicators: true/false
  - state_panel_quests: true/false
  - state_panel_npcs: true/false
  - state_panel_clocks: true/false
  - state_panel_inventory: true/false
  - state_panel_clues: true/false
  - state_panel_location: true/false
  - object_index: true/false
  - hot_pack: true/false
drift_corrections:
  - (列出任何做出的纠正)
-->
```
