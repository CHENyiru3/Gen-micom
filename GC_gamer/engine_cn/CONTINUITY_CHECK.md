# CONTINUITY_CHECK.md — 会话结束一致性检查（稳定）

> **用途**：每次会话结束或长窗口运行后，做一次 2 分钟的“漂移检查”，保证可重启、可追溯、可压缩。  
> **原则**：`campaigns/<id>/sessions/` 为事件真源；其余文件均应与其对齐。

---

## 1) 必查 6 项（每次会话结束）

1. `campaigns/<id>/sessions/CURRENT_SESSION.md` 是否指向本次写入的 session 文件
2. 当前 session 文件末尾是否存在最新 `Decision`（append）
3. `campaigns/<id>/HOT_PACK.json` 的 `CONTEXT_PACK_NEXT` 是否与最新 Decision 一致（时间/地点/指标/钩子）
4. `campaigns/<id>/STATE_PANEL.json` 是否已 patch（时间/指标/位置/任务/NPC/时钟至少一项有对应变化或保持不变）
5. `campaigns/<id>/OBJECT_INDEX.json` 是否已 patch（active 对象指针与 1 行摘要）
6. 若涉及世界宏观变化：`campaigns/<id>/WORLD_STATE.md` 是否已 patch（只做索引级更新）

### 可选：体验增强（建议）

- `.DM_PLANNER.md` 是否已根据本次会话更新（Fronts/线索库存/下一会话 beats）

---

## 2) 冲突处理（固定）

若发现冲突：
- 以 `campaigns/<id>/sessions/` 为准
- 在下一回合 `ARCHIVE_DELTA` 中：
  - append 一条 “Decision: 纠偏” 或在最近 Decision 中补充“纠偏说明”
  - patch 相关 state 文件使其对齐

---

## 3) 初始化专用检查（新战役）

初始化完成后额外确认：
- `campaigns/<id>/PLAYER_PROFILE.md` 的偏好摘要不为 `-`
- `campaigns/<id>/characters/PCs/pc_current.md` 已填入基础信息
- `campaigns/<id>/sessions/session_0000_bootstrap.md` 不再是 current（已切换为新 session）
