# NPC_GUIDELINES.md — NPC 一致性约束（稳定）

> **用途**：约束 NPC 的“底色一致性”，用于回合运行与小说同步；具体内容以每个 NPC 档案为准。

---

## 1) 不可破坏的底线

- 不把 NPC 写成与其“公开身份/目标/暗线目标”相反的角色（除非有新的会话事件触发并记录）
- 不凭空新增 NPC 的关键事实（新事实必须落到 `sessions/` 的 Decision，然后再 patch NPC 档案）
- 不替 NPC 做“超自然全知”推断（除非其档案明确标注为 `entity` 或等价）

---

## 2) 真源与更新流程

- NPC 的真源：`characters/NPCs/npc_*.md`
- NPC 的索引/别名入口：`characters/NPCs/npc_roster.md`
- 任何变更：先在 `sessions/` append Decision，再 patch NPC 档案（通过 `ARCHIVE_DELTA`）

