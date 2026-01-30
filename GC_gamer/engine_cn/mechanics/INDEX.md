# mechanics/INDEX.md — 机制文件索引

> **用途**: 指向所有规则与机制文件
> **tags**: [index, mechanics, rules, reference]

---

## INDEX::001 核心规则

| 文件 | 用途 | 何时读 |
|------|------|--------|
| `KERNEL_PROMPT.md` | Kernel（稳定协议） | 每次会话前 |
| `System.md` | World Instance + Router（入口与索引） | 每次会话前 |
| `HOUSE_RULES.md` | 房规与掷骰规则 | 需要规则时 |
| `TRACKERS.md` | 追踪器模板（非真源） | 需要手动记录/打印时 |
| `GOVERNANCE_PANEL_SPEC.md` | 统治面板字段规范（稳定） | 启用统治面板时 |

---

## INDEX::002 战斗与生存

| 文件 | 用途 | 何时读 |
|------|------|--------|
| `COMBAT.md` | 战斗规则（攻击/防御/状态） | 进入战斗时 |
| `SURVIVAL.md` | 生存规则（消耗/休息/状态） | 生存检定时 |
| `SOCIAL_INVESTIGATION.md` | 社交与调查规则 | 社交互动时 |

---

## INDEX::003 高级系统

| 文件 | 用途 | 何时读 |
|------|------|--------|
| `GOVERNANCE.md` | 统治面板（领土/军队/商业） | 获得领土时 |
| `RANDOM_TABLES.md` | 随机遭遇表 | 需要随机事件时 |
| `../Map-Gen.md` | 地图生成与存档规范（扩展） | 需要地图系统时 |

---

## INDEX::004 系统工具

| 文件 | 用途 | 何时读 |
|------|------|--------|
| `RAG_RULES.md` | RAG检索规则 | 需要检索时 |
| `CONTEXT_PACK.md` | Context Pack规范（稳定） | 上下文恢复/粘贴包时 |
| `CONTEXT_PACK_EXAMPLES.md` | Context Pack示例（可变） | 需要参考时 |
| `skills_repo/rpg-dm-function-calling-local/references/panels.json` | STATE_PANEL字段规范（稳定） | 维护面板格式时 |

---

## INDEX::005 快速参考表

### 指标系统（定义见 `cartridges/<id>/lore/MECHANICS/INDICATORS.md`）

| 指标 | 范围 | 规则 |
|------|------|------|
| Grace | 0-10 | 神圣秩序可用性 |
| Debt | 0-10 | 人类赎罪压力 |
| Rumor | 0-3 | 公众议论程度 |
| Heat | 0-3 | 势力关注度 |

### 指标规则速查
- 公开施法/怪物目击 → Rumor+1
- Rumor≥2 → 调查力量必介入
- 暴力/滥用魔法 → Debt+1
- 救人/拒绝诱惑 → Debt-1 或 Grace+1

---

## INDEX::006 战斗速查

### 伤害表

| 近战武器 | 伤害 | 远程武器 | 伤害 |
|----------|------|----------|------|
| 拳头 | d3 | 投石 | d2 |
| 匕首 | d4 | 飞刀 | d3 |
| 手斧/短剑 | d6 | 短弓 | d6 |
| 长剑/钉头锤 | d8 | 弩 | d8 |

### AC表

| 护甲 | AC |
|------|-----|
| 无甲 | 10+DEX |
| 皮革 | 11+DEX |
| 锁子 | 13+DEX-1 |
| 板甲 | 16+DEX-2 |

---

## INDEX::007 社交速查

### 社交检定DC

| 类型 | DC范围 |
|------|--------|
| 说服 | 10-20 |
| 欺骗 | 12-18 |
| 恐吓 | 12-20 |
| 表演 | 10-25 |

### 洞察结果

| 差距 | 结果 |
|------|------|
| ≥10 | 完全识破 |
| 5-9 | 怀疑 |
| 0-4 | 无明显怀疑 |
| <0 | 相信玩家 |

---

## INDEX::008 生存速查

### 日常消耗

| 物品 | 价格 |
|------|------|
| 口粮（一天） | 2银 |
| 啤酒 | 1银 |
| 住宿（干草） | 1银 |
| 住宿（旅馆） | 5-10银 |

### 状态惩罚

| 状态 | 惩罚 |
|------|------|
| 饥饿 | -1全检定 |
| 脱水 | -2全检定 |
| 疲劳 | -1全检定 |

### 休息恢复

| 休息 | 恢复 |
|------|------|
| 短休（1小时） | 1d6生命 |
| 长休（8小时） | 全部生命 |
| 完全休息（24小时） | 所有状态 |

---

## INDEX::009 标签索引

按标签检索机制文件：

| 标签 | 相关文件 |
|------|----------|
| [combat] | COMBAT.md, HOUSE_RULES.md |
| [survival] | SURVIVAL.md, HOUSE_RULES.md |
| [social] | SOCIAL_INVESTIGATION.md |
| [governance] | GOVERNANCE.md |
| [random] | RANDOM_TABLES.md |
| [system] | System.md, HOUSE_RULES.md, TRACKERS.md |
| [rag] | RAG_RULES.md, CONTEXT_PACK.md |

---

## INDEX::010 文件依赖关系

```
KERNEL_PROMPT.md (Kernel)
└── System.md (World Instance + Router)
├── HOUSE_RULES.md (房规)
├── TRACKERS.md (追踪器)
├── COMBAT.md (战斗)
├── SURVIVAL.md (生存)
├── SOCIAL_INVESTIGATION.md (社交调查)
├── GOVERNANCE.md (统治)
├── RANDOM_TABLES.md (随机表)
├── RAG_RULES.md (RAG规则)
└── CONTEXT_PACK.md (Context Pack)
```
