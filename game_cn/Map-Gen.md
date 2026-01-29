---
tags: [map, guide, protocol]
related: [maps/MAP_INDEX.md, HOT_START.md, KERNEL_PROMPT.md]
---

# MAPS_GUIDE.md — 命令行式地图生成与存档规范（宏观/微观 + 逻辑保存）
版本：v1.0  
用途：指导 DM/AI 以“命令行输出”的方式生成 ASCII 地图（宏观与微观），并**持久保存地图与其生成逻辑**，保证后续续写一致性与可检索（RAG）。

---

## 0) 目标与原则
### 0.1 目标
1) 以**纯文本/命令行风格**输出地图（ASCII），可直接贴进终端或文档。  
2) 同步保存：
- 地图本体（渲染图）
- 地图数据（可解析的结构化信息）
- 地图逻辑（为什么这样画：约束、推导、来源、假设、未确定点）
3) 支持：
- **宏观地图**：区域/路线/势力边界/风险层
- **微观地图**：城市街区/建筑/地下城/战斗格网

### 0.2 约束
- 地图必须与白昼史/迷雾史设定、经济/外交、城市肌理一致。  
- 地图允许“未探索/未知”，并必须用 Fog-of-War 表示。  
- 地图每次更新必须可追溯（diff / changelog）。

---

## 1) 地图目录与文件结构（必须遵守）
建议在你的设定仓库中新增：
```

/maps/
MAP_INDEX.md
macro/
macro_0001_nebelmark_region.md
macro_0001_nebelmark_region.data.yaml
macro_0001_nebelmark_region.logic.md
micro/
micro_0001_nebelheim_city.md
micro_0001_nebelheim_city.data.yaml
micro_0001_nebelheim_city.logic.md
instances/
inst_YYYY-MM-DD_slug.md          # 单次会话临时/揭示版（Fog变化）
inst_YYYY-MM-DD_slug.logic.md

````

### 1.1 MAP_INDEX.md（索引必须维护）
每新增地图必须登记：
- map_id
- 名称
- 类型（macro/micro）
- 尺度
- 覆盖范围
- 当前版本
- 最近更新时间
- 关联 session / quest / location / faction tags

---

## 2) 地图类型与尺度规范
### 2.1 宏观地图（macro）
用于：区域地理、道路、河流、关卡、势力影响、风险溢价、天气/迷雾窗口。  
推荐两种尺度（二选一或同时维护）：
- **Hex 模式**：1 hex = 6 miles（约 10km）或 12 miles（约 20km）  
- **Node 模式**：城市/要塞/集市/渡口为节点，路网为边（适合政治经济与通行控制）

宏观地图必须包含：
- 交通节点（城、堡、修道院、关卡、桥、集市）
- 路网类型（官道/土路/商道/秘密小径）
- 通行风险（RP 0–3）
- 物价影响（PI 1–5，可标注在节点）
- 迷雾活跃区（Mist Zone：低/中/高）

### 2.2 微观地图（micro）
用于：城市街区、关键建筑、室内场景、地下城、战斗地形。  
推荐尺度：
- **城市/街区图**：不强制格网，采用块状/街道拓扑 + 路口节点  
- **地下城/战斗图**：方格（1格=5尺）或以房间节点表示（room graph）

微观地图必须包含：
- 入口/出口/瓶颈点
- 可交互对象（门、楼梯、井口、密道、岗哨）
- 可见性与照明（明亮/昏暗/黑暗）
- 噪音/气味/人流（可选但强烈建议：市井地图尤其重要）
- Fog-of-War（未知区域不可凭空全显示）

---

## 3) ASCII 渲染规范（命令行风格）
### 3.1 通用符号表（建议）
- 地形：
  - `~` 水域 / 河流
  - `^` 山地 / 高坡
  - `"` 农田 / 葡萄园
  - `,` 草地 / 荒地
  - `#` 城墙 / 厚结构
  - `=` 官道 / 主路
  - `-` 小路
  - `:` 小径/湿地栈道
  - `*` 迷雾活跃点 / 异常点
- 建筑/节点：
  - `C` 城市（City）
  - `T` 塔楼/岗哨（Tower）
  - `B` 桥（Bridge）
  - `G` 城门（Gate）
  - `M` 市集（Market/Fair）
  - `K` 要塞/城堡（Keep）
  - `A` 修道院/教堂（Abbey）
  - `D` 地下入口/地窖（Dungeon access）
- Fog-of-War：
  - `?` 未探索
  - `·` 已探索但细节未知（朦胧）
- 标注：
  - 坐标轴：行列编号或 A1、B2…
  - 关键点用 `[@1]`、`[@2]` 标签（与 data.yaml 对应）

> 允许按地图类型扩展符号，但必须在地图文件顶部写 `Legend`。

### 3.2 输出模板（必须）
每次输出地图必须按以下顺序：
1) 标题 + 元数据（front matter）
2) Legend（符号说明）
3) 渲染图（ASCII block）
4) POI 列表（Points of Interest：编号→含义→状态）
5) 逻辑摘要（本次更新原因/新增信息来源/未确定点）

---

## 4) 地图数据模型（必须保存为 .data.yaml）
每张地图都必须有一个结构化数据文件，便于 RAG 与一致性校验。

### 4.1 统一 YAML 字段
```yaml
map_id: "macro_0001"
name: "Nebelmark 区域图"
type: "macro"                 # macro | micro
scale:
  mode: "hex"                 # hex | node | grid
  hex_miles: 6                # 若 hex
  grid_ft: null               # 若 grid
coverage:
  center: "Nebelheim"
  bbox: "W-E: 60mi, N-S: 48mi"
version: "1.0.3"
updated: "YYYY-MM-DD"
tags: ["region:nebelmark", "era:1444", "mist:crack_phase"]
layers:
  terrain: true
  routes: true
  factions: true
  risk: true
  mist: true
fog:
  policy: "reveal_on_discovery"
  unexplored_symbol: "?"
nodes:
  - id: "@1"
    name: "Nebelheim"
    kind: "city"
    coord: "H7"              # hex坐标或网格坐标
    attributes:
      PI: 3
      Rumor: 1
      Heat: 0
      MistZone: "medium"
edges:
  - from: "@1"
    to: "@2"
    kind: "road"             # road | river | trail | secret
    travel_time: "6h"
    risk_RP: 2
pois:
  - id: "@7"
    name: "椴树刑场"
    status: "known"          # known | rumored | hidden | destroyed
    hooks: ["vehm_mark", "ssgg_dagger"]
constraints:
  - "Nebelheim 必须位于莱茵支流附近"
  - "法军冬营距离城市 1-2 天行军"
provenance:
  sources:
    - "session_1444_01_opening"
  assumptions:
    - "河面冬季可部分结冰"
  uncertainties:
    - "黑松林边界尚未测绘"
````

---

## 5) “地图逻辑”文件（必须保存为 .logic.md）

每张地图必须有一个逻辑说明文件，回答三类问题：

1. **为什么这样画**（历史/经济/军情/地形约束）
2. **哪些是确定的**、哪些是传闻/推测
3. **这张图如何随剧情更新**

### 5.1 逻辑文件模板

```md
# Logic — <map_id> <name>

## 1) 设计约束（硬约束）
- ...

## 2) 推导链（关键因果）
- 因为 A（法军冬营需要补给线）→ 必须有 B（道路与村庄节点）→ 因此放置在 ...

## 3) 不确定与 Fog 策略
- 未探索区：保持 ?；只在玩家获得“测绘/传闻/目击”后揭示
- 传闻标注：用 status=rumored，且不画细节，只标一个点

## 4) 更新规则（Diff 原则）
- 只增量修改：新增 POI、揭示 Fog、调整 RP/PI
- 不重画已确认地形（除非有灾变事件）

## 5) 与系统指标联动
- Rumor≥2：城内新增“巡逻/告密点”
- Debt 上升：迷雾活跃点 * 数量增加或移动
```

---

## 6) 命令行式“地图生成命令”规范（给 AI 的操作接口）

> 这不是你真的要执行的 shell，而是你对用户/日志输出的“CLI 风格协议”。
> 每次玩家或 DM 发出命令，你输出：`COMMAND` → `RESULT` → `ARCHIVE_DELTA`。

### 6.1 命令集合（建议最小集）

* `map new <type> <name> --scale <hex|node|grid> --id <...>`
* `map render <map_id> --layer terrain,routes,fog,...`
* `map reveal <map_id> <coord|poi_id> --reason "<session clue>"`
* `map add-poi <map_id> "<poi name>" --coord <...> --status known|rumored|hidden`
* `map link <map_id> <from> <to> --kind road|trail|secret --risk <0-3> --time "<...>"`
* `map annotate <map_id> <poi_id> --note "<text>" --tags "..."`
* `map update-risk <map_id> <edge_or_region> --RP <0-3> --PI <1-5>`
* `map diff <map_id> --from <v> --to <v>`（输出变更摘要）
* `map export <map_id> --format ascii|yaml|both`

### 6.2 输出格式（严格）

命令回显：

```txt
$ map reveal micro_0001 A12 --reason "玩家从刽子手处买到下水道路线"
OK: Revealed cells: A12..A14
OK: Updated fog status: unexplored -> explored
```

随后给出地图渲染（或局部渲染），最后给出 ARCHIVE_DELTA（见第 7 节）。

---

## 7) 保存与更新：必须写入存档（ARCHIVE_DELTA）

每次地图发生变化（new/reveal/add-poi/link/update-risk），必须在回复末尾追加：

```md
<!-- ARCHIVE_DELTA
files:
  - path: maps/MAP_INDEX.md
    patch: |
      - added: micro_0002_sewer.md (v1.0.0)
  - path: maps/micro/micro_0002_sewer.md
    append: |
      ## v1.0.0 Render
      ...
  - path: maps/micro/micro_0002_sewer.data.yaml
    patch: |
      - pois: ...
  - path: maps/micro/micro_0002_sewer.logic.md
    append: |
      ## Update Reason
      ...
-->
```

**强制要求**：

* `.md`（渲染）、`.data.yaml`（结构）、`.logic.md`（逻辑）三件套缺一不可。
* 每次更新要 bump `version`，并在 `.logic.md` 记录“更新原因与来源”（session clue / NPC 证词 / 实测路径）。

---

## 8) 一致性与校验规则（防止“画着画着忘了”）

每次更新地图前，AI 必须执行自检（在内部完成，结果以摘要呈现）：

1. **拓扑一致**：道路连通是否断裂？节点是否孤立？
2. **尺度一致**：旅行时间与距离是否匹配？
3. **指标一致**：RP/PI/Heat/Rumor 与剧情现状是否冲突？
4. **Fog 一致**：未探索区域不得出现细节 POI；rumored POI 不给精确结构。
5. **跨图一致**：宏观节点 `Nebelheim` 与微观城市图入口/城门坐标对应。

如发现冲突，必须：

* 在 `.logic.md` 增加 `uncertainties` 或修正推导；
* 或生成“临时实例地图”（/maps/instances/）供本次会话使用，待后续确认再合并进主图。

---

## 9) 生成工作流（推荐）

### 9.1 宏观地图工作流（Region）

1. `map new macro "Nebelmark 区域图" --scale hex --id macro_0001`
2. 画地形骨架（河、山、林、主要道路）
3. 放置三角博弈节点（法/帝/勃关键触点）
4. 标注 RP/PI 初始值与迷雾活跃区
5. Fog：仅揭示玩家已知范围，其余 `?`

### 9.2 微观地图工作流（City）

1. `map new micro "Nebelheim 城市图" --scale node --id micro_0001`
2. 画三重城防 + 难民带 + 行会街 + 犹太巷 + 教堂区 + 刽子手桥
3. 放置关键 POI（市政厅、酒窖、城门、市场、修会、下水口）
4. 为每个 POI 绑定：派系、风险、可获得资源、典型遭遇
5. 只在玩家探索后 reveal 具体巷道/内部结构

### 9.3 地下城/战斗格网工作流（Dungeon/Grid）

1. `map new micro "下水道段落" --scale grid --id micro_0002`
2. 初始只画入口与第一间房，其余 `?`
3. 每次玩家前进一段：`map reveal` + 更新怪异点 `*`
4. 房间必须有：入口/出口/遮蔽/光照/可互动对象

---

## 10) 最小示例（微观：街区拓扑图）

```txt
MAP: Nebelheim (micro_0001)  TYPE: micro(node)  VER: 1.0.0
Legend: #城墙  =主街  -巷道  G城门  M市集  A教堂  R市政厅  J犹太巷  X刽子手桥  ?未探索  *异常

            ###########G###########
            #         =           #
            #   [A]===M===R       #
            #     -  ==  -        #
            #   J-?-==?- -        #
            #     -  ==  -    X   #
            #   [棚户区与外壕]  -  #
            ###########G###########

POI:
[@1] A 主座堂区（known）
[@2] M 市集（known）
[@3] R 市政厅与酒窖（known）
[@4] J 犹太巷（rumored: 夜间上锁；账房密集）
[@5] X 刽子手桥（known: 名誉代价高）
[*1] 异常点（hidden: 裂纹期低概率出现）
```

---

## 11) RAG 标签建议（便于检索）

在每张地图 front matter 的 `tags` 中至少包含：

* `region:<...>` / `city:<...>` / `dungeon:<...>`
* `era:1444` / `mist:crack_phase` / `mist:threshold_crossing`
* `faction:france|empire|burgundy|church|guild|vehm|outcasts`
* `economy:PI3` `risk:RP2`（可选）

— End of MAPS_GUIDE.md —

> 注：本 repo 已创建 `maps/` 目录与 `maps/MAP_INDEX.md`，后续地图更新按本文件第 7 节通过 `ARCHIVE_DELTA` 增量写入。
