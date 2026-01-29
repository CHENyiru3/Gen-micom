# CONTEXT_PACK_EXAMPLES.md — Context Pack 示例（内容/样例，允许变化）

> **用途**：示例与历史兼容；规范以 `mechanics/CONTEXT_PACK.md` 为准。  
> **注意**：本文件可以包含具体世界内容（地点名、NPC名、任务名等），因此视作“内容包/样例”。

---

## EX::001 会话恢复包（示例）

```md
<!-- CONTEXT_PACK_NEXT
t=1444-裂纹期
loc=内伯尔海姆大教堂忏悔室地下室入口
pc=克莱蒙德(伪神学生)
grace=6 debt=4 rumor=2 heat=3
flags=Rumor>=2调查介入|Heat=3被盯上
quests=quest_002:探索采石场(进行中)|quest_004:调查他们(进行中)
npcs=马库斯:愧疚|以利亚:失联|莱因霍尔德:死亡
inventory=油灯,采石场地图,地下室钥匙
timers=调查介入(已触发)|菲姆法庭追踪(进行中)
hooks=进入地下室|确认“七个人”线索|处理追踪
-->
```

---

## EX::010 规则速记包（示例：战斗/社交/生存）

这些示例属于“可选卡带块”，当且仅当本回合触发对应域时才加载：
- 战斗：`mechanics/COMBAT.md`
- 社交/调查：`mechanics/SOCIAL_INVESTIGATION.md`
- 生存：`mechanics/SURVIVAL.md`

