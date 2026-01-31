#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import shutil
import sys
from pathlib import Path


ROOT_FILES_TO_LINK = {
    "sessions": "sessions",
    "quests": "quests",
    "characters": "characters",
    "Writing": "Writing",
    "STATE_PANEL.json": "STATE_PANEL.json",
    "HOT_PACK.json": "HOT_PACK.json",
    "OBJECT_INDEX.json": "OBJECT_INDEX.json",
    "PLAYER_PROFILE.md": "PLAYER_PROFILE.md",
    "GOVERNANCE_PANEL.md": "GOVERNANCE_PANEL.md",
    ".DM_SECRETS.md": ".DM_SECRETS.md",
    ".DM_PLANNER.md": ".DM_PLANNER.md",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _assert_not_template_root(root: Path) -> None:
    if "Blank_Cartidge_template" in root.parts:
        raise RuntimeError(
            "refusing to write inside Blank_Cartidge_template; "
            "run this script under Game_Cartridge/<cartridge_root>/game_cn/"
        )


def _assert_path_not_in_template(path: Path) -> None:
    if "Blank_Cartidge_template" in path.parts:
        raise RuntimeError(
            "refusing to target Blank_Cartidge_template; "
            "new campaigns must live in Game_Cartridge/<cartridge_root>/game_cn/"
        )


def ensure_symlink(path: Path) -> None:
    if not path.exists() and not path.is_symlink():
        raise RuntimeError(f"expected {path} to exist or be a symlink")
    if not path.is_symlink():
        raise RuntimeError(
            f"refusing to proceed: {path} is not a symlink (won't delete real directories/files)"
        )


def replace_symlink(link_path: Path, target: Path) -> None:
    if link_path.exists() or link_path.is_symlink():
        ensure_symlink(link_path)
        link_path.unlink()
    link_path.symlink_to(target)


def read_current_campaign(root: Path) -> str | None:
    ptr = root / "ACTIVE.md"
    if not ptr.exists():
        return None
    raw = ptr.read_text(encoding="utf-8").strip()
    if not raw:
        return None
    if raw.startswith("active_campaign:"):
        return raw.split(":", 1)[1].strip()
    return raw


def write_current_campaign(root: Path, rel_path: str) -> None:
    (root / "ACTIVE.md").write_text(f"active_campaign: {rel_path.strip()}\n", encoding="utf-8")


def validate_campaign_layout(campaign_dir: Path) -> None:
    required = [
        campaign_dir / "sessions",
        campaign_dir / "quests",
        campaign_dir / "characters",
        campaign_dir / "Writing",
        campaign_dir / "STATE_PANEL.json",
        campaign_dir / "sessions" / "CURRENT_SESSION.md",
    ]
    missing = [str(p) for p in required if not p.exists()]
    if missing:
        raise RuntimeError(
            "campaign layout invalid; missing:\n" + "\n".join(f"- {m}" for m in missing)
        )


def _slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "init"


def _require_file(path: Path) -> None:
    if not path.exists():
        raise RuntimeError(f"missing expected file: {path}")


def _replace_summary_line(text: str, key: str, value: str) -> str:
    pattern = re.compile(rf"^-\s*{re.escape(key)}=.*$", re.MULTILINE)
    if not pattern.search(text):
        raise RuntimeError(f"could not find summary key in PLAYER_PROFILE.md: {key}")
    return pattern.sub(f"- {key}={value}", text)


def _replace_pc_table_value(text: str, field: str, value: str) -> str:
    pattern = re.compile(rf"^[|]\s*{re.escape(field)}\s*[|]\s*.*?\s*[|]$", re.MULTILINE)
    if not pattern.search(text):
        raise RuntimeError(f"could not find PC field in pc_current.md: {field}")
    return pattern.sub(f"| {field} | {value} |", text)


def _replace_state_date_row(text: str, date_value: str) -> str:
    pattern = re.compile(r"^[|]\s*-\s*[|]\s*-\s*[|]\s*-\s*[|]$", re.MULTILINE)
    if not pattern.search(text):
        return text
    return pattern.sub(f"| {date_value} | - | - |", text, count=1)


def _replace_state_location(text: str, loc: str) -> str:
    pattern = re.compile(r"^[*][*]当前[*][*]:\s*.*$", re.MULTILINE)
    if not pattern.search(text):
        raise RuntimeError("could not find current location line in STATE_PANEL.json")
    return pattern.sub(f"**当前**: {loc}", text, count=1)


def _replace_hot_pack(text: str, *, t: str, loc: str, pc: str, flags: str) -> str:
    block = re.search(r"<!--\s*CONTEXT_PACK_NEXT(?P<body>[\s\S]*?)-->", text)
    if not block:
        raise RuntimeError("could not find CONTEXT_PACK_NEXT block in HOT_PACK.json")
    body = block.group("body")
    for k, v in [("t", t), ("loc", loc), ("pc", pc), ("flags", flags)]:
        body = re.compile(rf"^\s*{re.escape(k)}=.*$", re.MULTILINE).sub(
            f"{k}={v}", body, count=1
        )
    new_block = f"<!-- CONTEXT_PACK_NEXT{body}-->"
    return text[: block.start()] + new_block + text[block.end() :]


def _is_tty() -> bool:
    return sys.stdin.isatty() and sys.stdout.isatty()


def _prompt(label: str, default: str | None = None) -> str:
    if default:
        prompt = f"{label} [{default}]: "
    else:
        prompt = f"{label}: "
    value = input(prompt).strip()
    return value or (default or "")


def _load_init_answers(from_file: str) -> dict[str, str]:
    if from_file == "-":
        raw = sys.stdin.read()
        source = "<stdin>"
    else:
        p = Path(from_file)
        raw = p.read_text(encoding="utf-8")
        source = from_file

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"invalid init answers JSON in {source}: {e}") from e

    if not isinstance(data, dict):
        raise RuntimeError(f"init answers JSON must be an object; got {type(data).__name__}")

    cleaned: dict[str, str] = {}
    for k, v in data.items():
        if not isinstance(k, str):
            continue
        if v is None:
            continue
        if isinstance(v, (str, int, float, bool)):
            cleaned[k] = str(v).strip()
            continue
        raise RuntimeError(f"init answers JSON value must be string-ish; key={k} type={type(v).__name__}")

    return cleaned


def _coalesce(primary: str | None, fallback: str | None) -> str:
    primary = (primary or "").strip()
    if primary:
        return primary
    return (fallback or "").strip()


def cmd_init(args: argparse.Namespace) -> None:
    root = repo_root()
    _assert_not_template_root(root)
    current_rel = read_current_campaign(root)
    if not current_rel:
        raise RuntimeError("ACTIVE.md is empty; run campaign_manager.py switch/new first")

    campaign_dir = (root / current_rel).resolve()
    validate_campaign_layout(campaign_dir)

    answers: dict[str, str] = {}
    if getattr(args, "from_file", None):
        answers = _load_init_answers(args.from_file)

    today = _coalesce(args.date, answers.get("date")) or _dt.date.today().isoformat()
    try:
        _dt.date.fromisoformat(today)
    except ValueError:
        raise RuntimeError(f"invalid --date (expected YYYY-MM-DD): {today}")

    presets: dict[str, dict[str, str]] = {
        "轻松叙事": {
            "STYLE": "温柔治愈-轻松",
            "DIFFICULTY": "轻松",
            "RULES": "叙事优先",
            "PACING": "快",
            "COMBAT_FREQ": "低",
            "MYSTERY_VS_ACTION": "行动",
            "LINES_VEILS": "-",
        },
        "标准冒险": {
            "STYLE": "史诗-明快",
            "DIFFICULTY": "标准",
            "RULES": "折中",
            "PACING": "中",
            "COMBAT_FREQ": "中",
            "MYSTERY_VS_ACTION": "平衡",
            "LINES_VEILS": "-",
        },
        "硬核写实": {
            "STYLE": "写实-高压",
            "DIFFICULTY": "硬核",
            "RULES": "规则优先",
            "PACING": "慢",
            "COMBAT_FREQ": "低但致命",
            "MYSTERY_VS_ACTION": "行动-后果强",
            "LINES_VEILS": "-",
        },
        "悬疑调查": {
            "STYLE": "写实-悬疑",
            "DIFFICULTY": "标准",
            "RULES": "折中",
            "PACING": "中",
            "COMBAT_FREQ": "低",
            "MYSTERY_VS_ACTION": "调查优先",
            "LINES_VEILS": "-",
        },
        "宗教恐怖": {
            "STYLE": "恐怖-宗教-异象",
            "DIFFICULTY": "标准到硬核",
            "RULES": "折中",
            "PACING": "慢",
            "COMBAT_FREQ": "低",
            "MYSTERY_VS_ACTION": "恐怖/调查优先",
            "LINES_VEILS": "-",
        },
    }

    preset = _coalesce(args.preset, answers.get("preset"))
    if preset and preset not in presets:
        raise RuntimeError(f"unknown --preset: {preset} (expected one of: {', '.join(presets)})")

    pref = presets.get(preset, {}).copy()
    for k in ["STYLE", "DIFFICULTY", "RULES", "PACING", "COMBAT_FREQ", "MYSTERY_VS_ACTION", "LINES_VEILS"]:
        override = _coalesce(getattr(args, k.lower(), None), answers.get(k.lower()))
        if override:
            pref[k] = override.strip()

    if _is_tty():
        if not preset:
            chosen = _prompt(
                "PRESET(可选：轻松叙事/标准冒险/硬核写实/悬疑调查/宗教恐怖；留空=自填)",
                default="",
            )
            if chosen in presets:
                preset = chosen
                pref = presets[preset].copy()
        for k in ["STYLE", "DIFFICULTY", "RULES", "PACING", "COMBAT_FREQ", "MYSTERY_VS_ACTION", "LINES_VEILS"]:
            pref[k] = _prompt(k, default=pref.get(k, "-") or "-") or "-"

    if not pref:
        raise RuntimeError("no preferences provided; pass --preset or explicit preference flags (or run in a TTY)")

    pc_name = _coalesce(args.pc_name, answers.get("pc_name"))
    pc_archetype = _coalesce(args.pc_archetype, answers.get("pc_archetype"))
    pc_drive = _coalesce(args.pc_drive, answers.get("pc_drive"))
    pc_strengths = _coalesce(args.pc_strengths, answers.get("pc_strengths"))
    pc_weakness = _coalesce(args.pc_weakness, answers.get("pc_weakness"))
    pc_bg_hook = _coalesce(args.pc_bg_hook, answers.get("pc_bg_hook"))

    if _is_tty():
        pc_name = pc_name or _prompt("PC 名字", default="-")
        pc_archetype = pc_archetype or _prompt("身份原型（一句话）", default="-")
        pc_drive = pc_drive or _prompt("驱动力（1-2条）", default="-")
        pc_strengths = pc_strengths or _prompt("强项（2条）", default="-")
        pc_weakness = pc_weakness or _prompt("弱点（1条）", default="-")
        pc_bg_hook = pc_bg_hook or _prompt("背景钩子（1条）", default="-")

    if not pc_name:
        raise RuntimeError("missing PC fields; pass --pc-name (or run in a TTY)")

    start_loc = _coalesce(args.start_loc, answers.get("start_loc"))
    start_hook = _coalesce(args.start_hook, answers.get("start_hook"))
    if _is_tty():
        start_loc = start_loc or _prompt("开局地点（loc）", default="-")
        start_hook = start_hook or _prompt("开局钩子（简述）", default="初始化开局")
    if not start_loc:
        start_loc = "-"
    if not start_hook:
        start_hook = "初始化开局"

    slug = _coalesce(args.slug, answers.get("slug")) or _slugify(f"{pc_name}-{start_loc}")
    session_rel = f"sessions/session_{today}_{slug}.md"
    session_path = campaign_dir / session_rel
    if session_path.exists():
        raise RuntimeError(f"session already exists: {session_rel}")

    profile_path = campaign_dir / "PLAYER_PROFILE.md"
    _require_file(profile_path)
    profile_text = profile_path.read_text(encoding="utf-8")
    for key, value in pref.items():
        profile_text = _replace_summary_line(profile_text, key, value)
    profile_path.write_text(profile_text, encoding="utf-8")

    pc_path = campaign_dir / "characters" / "PCs" / "pc_current.md"
    _require_file(pc_path)
    pc_text = pc_path.read_text(encoding="utf-8")
    pc_text = _replace_pc_table_value(pc_text, "名字", pc_name or "-")
    pc_text = _replace_pc_table_value(pc_text, "身份原型（一句话）", pc_archetype or "-")
    pc_text = _replace_pc_table_value(pc_text, "为何在此（驱动力）", pc_drive or "-")
    pc_text = _replace_pc_table_value(pc_text, "强项（2条）", pc_strengths or "-")
    pc_text = _replace_pc_table_value(pc_text, "弱点（1条）", pc_weakness or "-")
    pc_text = _replace_pc_table_value(pc_text, "背景钩子（1条）", pc_bg_hook or "-")
    pc_text = re.sub(
        r"^- \\[ \\] 用 `<初始化>` 完成角色创建并写入本文件\\s*$",
        "- [x] 用 `<初始化>` 完成角色创建并写入本文件",
        pc_text,
        flags=re.MULTILINE,
    )
    pc_path.write_text(pc_text, encoding="utf-8")

    decision = "\n".join(
        [
            "## Decision: 初始化",
            f"- Real time: {today}",
            "- In-world time: -",
            "- Player input: <初始化>",
            f"- PC: {pc_name} | {pc_archetype}",
            f"- Start: {start_hook}",
            "",
        ]
    )
    session_body = "\n".join(
        [
            "# Session 0: 初始化",
            f"日期：{today}",
            "时间锚点：-",
            "",
            decision,
        ]
    )
    session_path.write_text(session_body + "\n", encoding="utf-8")

    current_session_ptr = campaign_dir / "sessions" / "CURRENT_SESSION.md"
    _require_file(current_session_ptr)
    current_session_ptr.write_text(session_rel + "\n", encoding="utf-8")

    state_path = campaign_dir / "STATE_PANEL.json"
    _require_file(state_path)
    state_obj = json.loads(state_path.read_text(encoding="utf-8"))
    state_obj["time"] = today
    state_obj["location"] = start_loc
    state_path.write_text(json.dumps(state_obj, ensure_ascii=False, indent=2), encoding="utf-8")

    hot_path = campaign_dir / "HOT_PACK.json"
    _require_file(hot_path)
    hot_obj = json.loads(hot_path.read_text(encoding="utf-8"))
    hot_obj.setdefault("context", {})
    hot_obj["context"]["t"] = today
    hot_obj["context"]["loc"] = start_loc
    hot_obj["context"]["pc"] = pc_name
    hot_obj["context"]["flags"] = f"STYLE={pref.get('STYLE','-')}"
    hot_obj["context"]["voice"] = pref.get("STYLE", "-")
    hot_path.write_text(json.dumps(hot_obj, ensure_ascii=False, indent=2), encoding="utf-8")

    print("OK: init complete")
    print(f"- campaign: {current_rel}")
    print(f"- session: {session_rel}")


def cmd_switch(args: argparse.Namespace) -> None:
    root = repo_root()
    _assert_not_template_root(root)
    rel = args.path.strip().rstrip("/")
    campaign_dir = (root / rel).resolve()
    _assert_path_not_in_template(campaign_dir)
    if not campaign_dir.exists():
        raise RuntimeError(f"campaign not found: {rel}")
    validate_campaign_layout(campaign_dir)

    write_current_campaign(root, rel)
    print(f"OK: switched current campaign -> {rel}")


def cmd_new(args: argparse.Namespace) -> None:
    root = repo_root()
    _assert_not_template_root(root)
    template_rel = args.template.strip().rstrip("/")
    template_dir = (root / template_rel).resolve()
    _assert_path_not_in_template(template_dir)
    if not template_dir.exists():
        raise RuntimeError(f"template not found: {template_rel}")

    new_rel = args.id.strip().rstrip("/")
    if not new_rel.startswith("campaigns/"):
        new_rel = f"campaigns/{new_rel}"
    new_dir = root / new_rel
    _assert_path_not_in_template(new_dir.resolve())

    if new_dir.exists():
        raise RuntimeError(f"destination already exists: {new_rel}")

    shutil.copytree(template_dir, new_dir)
    validate_campaign_layout(new_dir.resolve())

    # Switch to it.
    cmd_switch(argparse.Namespace(path=new_rel))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="campaign_manager.py",
        description="Create/switch/init campaigns by copying a template and updating ACTIVE.md",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_new = sub.add_parser("new", help="Create a new campaign from template and switch to it")
    p_new.add_argument("--id", required=True, help="campaign id or path (e.g. campaign_0002 or campaigns/campaign_0002)")
    p_new.add_argument(
        "--template",
        default="campaigns/_template",
        help="template folder to copy (default: campaigns/_template)",
    )
    p_new.set_defaults(func=cmd_new)

    p_switch = sub.add_parser("switch", help="Switch to an existing campaign path")
    p_switch.add_argument("--path", required=True, help="campaign path (e.g. campaigns/campaign_0001)")
    p_switch.set_defaults(func=cmd_switch)

    p_init = sub.add_parser("init", help="Initialize the current campaign per INIT_PROTOCOL.md")
    p_init.add_argument(
        "--from",
        dest="from_file",
        help="read init answers from JSON file ('-' = stdin); CLI flags override JSON keys",
    )
    p_init.add_argument("--date", help="real-world date (YYYY-MM-DD); default: today")
    p_init.add_argument("--slug", help="session slug; default: derived from PC+loc (ASCII only)")
    p_init.add_argument("--preset", help="one of: 轻松叙事 / 标准冒险 / 硬核写实 / 悬疑调查 / 宗教恐怖")
    p_init.add_argument("--style", help="STYLE summary value")
    p_init.add_argument("--difficulty", help="DIFFICULTY summary value")
    p_init.add_argument("--rules", help="RULES summary value")
    p_init.add_argument("--pacing", help="PACING summary value")
    p_init.add_argument("--combat_freq", help="COMBAT_FREQ summary value")
    p_init.add_argument("--mystery_vs_action", help="MYSTERY_VS_ACTION summary value")
    p_init.add_argument("--lines_veils", help="LINES_VEILS summary value")
    p_init.add_argument("--pc-name", dest="pc_name", help="PC name")
    p_init.add_argument("--pc-archetype", dest="pc_archetype", help="PC archetype (1 sentence)")
    p_init.add_argument("--pc-drive", dest="pc_drive", help="PC drive (1-2)")
    p_init.add_argument("--pc-strengths", dest="pc_strengths", help="PC strengths (2)")
    p_init.add_argument("--pc-weakness", dest="pc_weakness", help="PC weakness (1)")
    p_init.add_argument("--pc-bg-hook", dest="pc_bg_hook", help="PC background hook (1)")
    p_init.add_argument("--start-loc", dest="start_loc", help="start location")
    p_init.add_argument("--start-hook", dest="start_hook", help="start hook summary")
    p_init.set_defaults(func=cmd_init)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    try:
        args.func(args)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
