# OBJECT_INDEX.schema.md — 对象索引最小字段规范

## 通用字段
- id: 内部唯一ID（可选）
- handle: @句柄（必须）
- name: 人类可读名（必须）
- type: NPC | LOC | QUEST | ITEM | FACTION
- status: active | inactive | resolved | hidden
- tags: [关键词]
- summary: 一句摘要

## NPC
- role: 角色定位
- affiliation: 阵营/组织
- location: 常驻地点

## LOC
- region: 大区域
- access: 可达性/限制
- hazards: 风险

## QUEST
- giver: 任务发布者
- stage: 当前阶段
- stakes: 失败后果

## ITEM
- rarity: 稀有度
- effect: 核心效果

## 句柄规范
- 全小写，使用下划线
- 示例: @marcus, @nebelheim_gate, @q_002_quarry
