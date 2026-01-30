# ARCHIVE_DELTA.md — 增量存档规范（稳定）

> **目标**：让“记忆/状态”外置并可追溯；每回合只做最小变更（append/patch），不重写整文件。  
> **适用范围**：回合结束持久化、地图更新、对象档案更新、初始化落盘。  
> **写入方式**：必须通过 JSON tool_calls（`write_patch` / `append_session`），不可在对话中直接输出。

---

## 1) 硬规则（必须）

- 只允许 `append` 或最小 `patch`；禁止整文件重写。
- `campaigns/<id>/sessions/` 是事件真源：每回合必须对当前 session 文件 **append** 一个 Decision。
- 可变状态文件（如 `campaigns/<id>/STATE_PANEL.json`、`campaigns/<id>/HOT_PACK.json`、`campaigns/<id>/PLAYER_PROFILE.md`、`campaigns/<id>/GOVERNANCE_PANEL.md`）只做章节级 patch。
- 若发现冲突：以 `campaigns/<id>/sessions/` 为准，写入“纠偏说明”（在本回合 Decision 中）。

---

## 2) 格式（HTML 注释块）

在回复末尾输出（玩家不可见）：


---

## 3) 推荐的“最小持久化集合”（每回合至少）

- `campaigns/<id>/sessions/<current>.md`：append Decision
- `campaigns/<id>/HOT_PACK.json`：patch 最新 `CONTEXT_PACK_NEXT`
- `campaigns/<id>/STATE_PANEL.json`：patch（只改变化章节）
- `campaigns/<id>/OBJECT_INDEX.json`：patch（只改 active 指针与 1 行摘要）

初始化回合还需：
- `campaigns/<id>/sessions/CURRENT_SESSION.md`：patch 指向新 session 文件
- `campaigns/<id>/PLAYER_PROFILE.md`：patch 偏好
- `campaigns/<id>/characters/PCs/pc_current.md`：patch 角色信息

---

## 4) patch 写法建议（降低歧义）

- patch 只贴出“目标章节/表格”的新内容（不要夹带整页复制）。
- 表格字段必须保持稳定（见 `engine/mechanics/skills_repo/rpg-dm-function-calling-local/references/panels.json`、`engine/mechanics/GOVERNANCE_PANEL_SPEC.md`）。
