# ARCHIVE_DELTA.md — 增量存档规范（稳定）

> **目标**：外置"记忆/状态"并使其可追溯；每回合只做最小更改（append/patch），不要重写整个文件。
> **范围**：回合结束持久化、地图更新、对象文件更新、初始化持久化。

---

## 1) 硬规则（必须）

- 只允许 `append` 或最小 `patch`；禁止整个文件重写。
- `sessions/` 是事件真源：必须每回合向当前 session 文件 **append** 一个 Decision。
- 变量状态文件（如 `STATE_PANEL.md`、`HOT_PACK.md`、`PLAYER_PROFILE.md`、`GOVERNANCE_PANEL.md`）只做段落级 patch。
- 如果发现冲突：使用 `sessions/` 作为权威，在本回合 Decision 中写"纠偏说明"。

---

## 2) 格式（HTML 注释块）

在回复末尾输出（对玩家不可见）：

```md
<!-- ARCHIVE_DELTA
files:
  - path: sessions/session_YYYY-MM-DD_slug.md
    append: |
      ## Decision: ...
      - Real time: ...
      - In-world time: ...
      - Player input: ...
      - Resolution: ...
      - Consequences: ...
      - Indicators: ...
      - Clocks: ...
  - path: HOT_PACK.md
    patch: |
      <!-- CONTEXT_PACK_NEXT
      ...
      -->
-->
```

---

## 3) 推荐的"最小持久化集合"（每回合至少）

- `sessions/<current>.md`：append Decision
- `HOT_PACK.md`：patch 最新的 `CONTEXT_PACK_NEXT`
- `STATE_PANEL.md`：patch（仅变化的段落）
- `OBJECT_INDEX.md`：patch（仅活跃指针和 1 行摘要）

初始化回合还需要：
- `sessions/CURRENT_SESSION.md`：patch 指向新 session 文件
- `PLAYER_PROFILE.md`：patch 偏好
- `characters/PCs/pc_current.md`：patch 角色信息

---

## 4) Patch 编写建议（减少歧义）

- Patch 只粘贴"目标段落/表格"新内容（不要夹杂整个页面复制）。
- 表格字段必须保持稳定（见 `mechanics/STATE_PANEL_SPEC.md`、`mechanics/GOVERNANCE_PANEL_SPEC.md`）。
