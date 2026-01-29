# GOVERNANCE_PANEL_SPEC.md — 统治面板字段规范（内核接口）

> **用途**：让 `campaigns/<id>/GOVERNANCE_PANEL.md` 可长期维护、可 patch、可检索；避免与 `campaigns/<id>/WORLD_STATE.md`/`campaigns/<id>/STATE_PANEL.md` 重复。

---

## 1) 面板定位

- `GOVERNANCE_PANEL.md` 只记录“玩家势力/资产/追随者/收支/治理时钟”等治理信息。
- 若没有进入治理玩法：保持为空/占位即可。

---

## 2) 章节顺序（固定）

1. `## 摘要`
2. `## 势力等级`
3. `## 资源`
4. `## 追随者`
5. `## 军事`
6. `## 土地`
7. `## 商业`
8. `## 建筑`
9. `## 治理时钟`
10. `## 本期结算`

---

## 3) 最小字段（建议）

- 势力等级：引用 `engine/mechanics/GOVERNANCE.md` 的 tier 名称 + 关键门槛
- 资源：食物/银币/金币/信用/物资库存
- 追随者：人数、忠诚度、核心人物
- 本期结算：收入/支出/净收益（保持最近 1–3 期即可）
