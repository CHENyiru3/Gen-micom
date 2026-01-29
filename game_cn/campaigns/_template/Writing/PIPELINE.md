# PIPELINE.md — 小说写作流水线

> **用途**: 会话→小说的转换规则与流程
> **tags**: [writing, pipeline, fiction, novel, workflow]

---

## PIPELINE::001 核心原则

### 派生性质
- Writing 是 Event 的**派生层**，不是 Canon
- 小说**永远不产出设定**，只能引用 Event/State
- 小说**必须与 session 记录对齐**，不得新增 Canon 事实

### 真源优先级
```
State > Event > Canon > Writing
```

当小说描述与 State/Event 冲突时，以 State/Event 为准，小说需要被修正。

---

## PIPELINE::002 写作触发条件

### 自动触发
每次会话结束后，标记为 `→ 需写入小说` 的 Decision 自动进入写作队列。

### 手动触发
- 玩家说"写小说""续写小说"
- 作者说"检查小说一致性"

---

## PIPELINE::003 写作前检查清单

1. 阅读 `Fiction_index.md`（小说进度索引）
2. 阅读最近相关 `sessions/session_*.md`（Decision 记录）
3. 阅读 `index.md`（当前状态）
4. 阅读相关 NPC/地点条目（如需要）

**禁止**: 读取整本 System/随机表

---

## PIPELINE::004 写作标准

### 视角
- 以克莱蒙德为主视角（第三人称有限视角）
- 可穿插其他角色视角（非主要）

### 风格
- 出版级别的西方幻想/严肃历史通俗文学
- 画面感强、对话自然、氛围营造
- 内心声音自然触发

### 同步要求
- 与 `index.md` 状态保持同步
- 与 session 决策保持一致
- 重大转折点在 `Fiction_index.md` 用 `★` 标记

---

## PIPELINE::005 写作流程

### 步骤1: 收集素材
- 从 session 记录提取标记 `→ 需写入小说` 的 Decision
- 按时间顺序排列
- 识别关键场景和转折点

### 步骤2: 规划结构
- 确定章节划分
- 分配素材到各章节
- 标记需要扩展的场景

### 步骤3: 撰写正文
- 按章节撰写
- 使用内心对话系统
- 保持叙事一致性

### 步骤4: 质量检查
- [ ] 主角视角是否统一？
- [ ] 情节是否与 session 记录一致？
- [ ] 内心声音是否自然触发？
- [ ] 世界观细节是否准确？
- [ ] 与 index.md 状态是否同步？

### 步骤5: 更新索引
- 更新 `Fiction_index.md` 进度
- 标记已完成章节
- 添加待写内容

---

## PIPELINE::006 文件命名规范

```
/Writing/
├── Fiction_index.md          # 小说总索引（必读）
├── Fiction_par1.md           # 第一卷（当前进行中）
├── Fiction_par2.md           # 第二卷
├── Fiction_par3.md           # 第三卷
└── CONTINUITY_ISSUES.md      # 一致性问题记录（可选）
```

---

## PIPELINE::007 冲突处理

### 发现冲突时
1. 在 `CONTINUITY_ISSUES.md` 中记录冲突
2. 标记冲突类型：
   - State冲突（状态不一致）
   - Event冲突（与session记录不符）
   - Canon冲突（与世界观矛盾）

### 解决冲突
- 以 State/Event 为准修正小说
- 记录解决方案
- 标记为已解决

### 示例
```markdown
# CONTINUITY_ISSUES.md

## 待解决

| 日期 | 冲突 | 类型 | 状态 |
|------|------|------|------|
| 2026-01-29 | 第四章结局马库斯出现与session记录不符 | Event | 待修正 |

## 已解决
（无）
```

---

## PIPELINE::008 索引同步规则

### Fiction_index.md 必须包含
- 小说概览（卷数、状态、字数）
- 核心设定速查
- 已完成章节列表
- 待写入内容清单
- 关键转折点标记

### 更新时机
- 每写入新内容立即更新索引
- 每轮会话前必须引用 Fiction_index

---

## PIPELINE::009 禁止事项

1. **禁止**在小说中新增 Canon 事实
2. **禁止**改变 NPC 性格底色（见 `mechanics/NPC_GUIDELINES.md` 与 NPC 档案）
3. **禁止**修改指标数值或规则
4. **禁止**引入未在 session 中出现的设定
5. **禁止**让 Writing 作为规则来源

---

## PIPELINE::010 示例流程

### 输入（Session 记录）
```markdown
## Decision: 探索采石场
- Player input: `{检查地上的手套}`
- Resolution: 发现菲姆法庭手套，天平符号
→ 需写入小说
```

### 输出（小说段落）
```markdown
克莱蒙德蹲下身，捡起那只丢弃的手套。皮革已经磨损，但袖口的天平符号依然清晰可辨——那是菲姆法庭的标志。

他的手指微微发抖。不是因为恐惧，而是因为愤怒。
```

### 更新（Fiction_index.md）
```markdown
| 第五章 | 采石场的阴影 | 发现菲姆法庭踪迹 | 🔄 进行中 |
```
