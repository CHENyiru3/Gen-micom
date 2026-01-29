# RAG_RULES.md — 检索增强生成规则

> **用途**: RAG 检索策略、门禁、片段提取规范
> **何时检索**: 当需要具体规则/数据时
> **tags**: [rag, retrieval, policy, context]

---

## RAG::001 调用门禁策略

### 默认策略
- **禁止**: 自动检索 `Writing/` 目录
- **禁止**: 整表/整段塞入上下文
- **按需检索**: 每次 ≤6 片段，每段 ≤120 字

### 允许触发检索的情况

| 触发条件 | 检索目标 | 片段上限 |
|----------|----------|----------|
| 需要战斗判定 | `mechanics/COMBAT.md` | 2段 |
| 需要社交/调查 | `mechanics/SOCIAL_INVESTIGATION.md` | 2段 |
| 需要生存检定 | `mechanics/SURVIVAL.md` | 1段 |
| 需要统治结算 | `mechanics/GOVERNANCE.md` | 3段 |
| 需要随机遭遇 | `mechanics/RANDOM_TABLES.md` | 1段 |
| 需要地图信息/绘制/一致性 | `maps/MAP_INDEX.md` + 对应 `maps/**` | 3段 |
| 需要人物网络/莱茵危机背景 | `Char.md` | 2段 |
| 需要世界观知识 | `Background*.md` | 2段 |
| 需要小说进度 | `Writing/Fiction_index.md` | 1段 |

---

## RAG::002 片段提取规则

### 命中目标表/列表
```markdown
## COMBAT::initiative    ← 提取"先攻顺序"段落
## SURVIVAL::rest        ← 提取"休息规则"段落
```

### 禁止行为
- 提取完整表格（只取相关行）
- 提取完整章节（只取相关段首句+关键行）
- 提取背景百科整段

### 片段格式模板
```markdown
> [文件路径: 锚点]
> 摘要: 1句总结
> 内容: 核心规则（≤120字）
```

---

## RAG::003 冲突解决

当多个文件提供冲突信息时：

```
优先级: Event > State > Canon > Writing
```

1. 检查 `sessions/session_*.md`（Event）
2. 检查 `index.md` / `lore/WORLD_STATE.md` / `STATE_PANEL.md`（State）
3. 检查 `Background*.md`（Canon）
4. Writing 只用于"一致性检查"，不作为设定来源

---

## RAG::004 检索禁用词

以下情况**禁止**触发 RAG：
- 沉浸式叙事描写中
- NPC 对话生成中
- 内心对话触发中
- 玩家自由行动裁决中（除非涉及明确机制）

---

## RAG::005 缓存策略

### 长期可缓存（静态）
- `Background*.md` 世界观设定
- `mechanics/*.md` 规则文件
- `mechanics/RANDOM_TABLES.md` 随机表

### 每次会话必刷新（可变）
- `index.md` 状态快照
- `sessions/session_*.md` 会话记录
- `Fiction_index.md` 小说进度

---

## RAG::006 RAG 片段示例

**场景**: 玩家在街头遭遇可疑人物，需要判断是否触发随机遭遇

```markdown
> [mechanics/RANDOM_TABLES.md:21.1]
> 摘要: 街头遭遇 d10 随机表
> 内容: "骰10检定街头遭遇。1=创伤触发, 2=城卫搜查, 3=神秘纸条..."

> [mechanics/SOCIAL_INVESTIGATION.md:INSIGHT]
> 摘要: 洞察检定规则
> 内容: "洞察 DC=8+目标洞察技能。差距≥10完全识破，5-9怀疑，<0相信。"
```
