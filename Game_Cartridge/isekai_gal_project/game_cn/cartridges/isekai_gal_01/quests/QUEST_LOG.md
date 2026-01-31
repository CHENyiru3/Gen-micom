# quests/QUEST_LOG.md — 任务索引（框架）

RAG_HEAD:
- 覆盖范围：任务/目标的索引面板（仅定义目标与状态，不写推进结果）。
- 关键对象：适应小马谷、建立身份与许可、离开小马谷门槛（RouteClear>=1）。
- 读取优先级：需要行动目标时先读 Active；需要规则时读 lore/MECHANICS/INDICATORS.md。
- 备注：任务条目可后续拆分为 quests/q_*.md 并在 Entry Pointers 登记。

## Table
| @handle | title | one_line_summary | status |
| --- | --- | --- | --- |
| @q_arrival_adapt | 适应小马谷生活 | 学会作为“雄性小马”在镇上正常生活与交流 | active |
| @q_identity_cover | 建立可持续身份 | 让“外来者/异常”不构成长期风险（Heat 控制） | active |
| @q_first_route | 完全攻略一位女主 | 达成 RouteClear>=1 以解锁离开小马谷的自由行动 | active |
| @q_travel_unlock | 获得离境自由行动 | LeavePonyvilleGate 解锁后的旅行与多城叙事框架 | locked |

## Handle Mapping
| handle | aliases |
| --- | --- |
| @q_arrival_adapt | ["新来者适应"] |
| @q_identity_cover | ["身份遮掩","身份建立"] |
| @q_first_route | ["首条攻略","首位女主"] |
| @q_travel_unlock | ["离开小马谷","旅行解锁"] |

## Entry Pointers
- @q_travel_unlock → lore/MECHANICS/INDICATORS.md
