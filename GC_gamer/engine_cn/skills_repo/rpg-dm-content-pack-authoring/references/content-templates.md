# Content Pack Templates (Portable)

Keep kernel protocols stable. Put “world truth” in content files.

## NPC file template (minimal)

```md
## npc_XXX:
- **名字**:
- **派系**:
- **公开身份**:
- **公开目标**:
- **暗线目标**:
- **易发现秘密**:
  1.
  2.
- **难发现秘密**:
  1.
- **关键关系**:
- **迷雾状态**: none|touched|agent|entity
- **首次出现**: session_YYYY-MM-DD*.md
```

## Lore file template (RAG-friendly)

```md
---
tags: [canon|mist|mechanic, ...]
related: [...]
---

# Title

## 0. 速查锚点
- ...

## 1. 核心设定

## 2. 游戏关联
- 相关地点：loc_...
- 相关任务：quest_...
- 相关NPC：npc_...
```


## JSON Panels (Runtime)

Use JSON for runtime panels (not MD):
- STATE_PANEL.json
- HOT_PACK.json
- MAINLINE_PANEL.json
- OBJECT_INDEX.json
- clues/CLUE_LOG.json

Schema: skills_repo/rpg-dm-function-calling-local/references/panels.json
