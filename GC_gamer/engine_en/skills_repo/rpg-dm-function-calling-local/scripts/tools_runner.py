#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _deny_template_write(path: Path) -> None:
    if "Blank_Cartidge_template" in path.parts:
        raise RuntimeError("refusing to write inside Blank_Cartidge_template")


def _apply_patch(path: Path, mode: str, content: str, pattern: str | None = None) -> None:
    if mode == "append":
        path.write_text(path.read_text(encoding="utf-8") + content, encoding="utf-8")
        return
    if mode == "prepend":
        path.write_text(content + path.read_text(encoding="utf-8"), encoding="utf-8")
        return
    if mode == "replace":
        if not pattern:
            raise RuntimeError("replace requires pattern")
        text = path.read_text(encoding="utf-8")
        new_text, n = re.subn(pattern, content, text, count=1, flags=re.MULTILINE)
        if n == 0:
            raise RuntimeError("replace pattern not found")
        path.write_text(new_text, encoding="utf-8")
        return
    raise RuntimeError(f"unsupported patch mode: {mode}")


def tool_read_file(args: dict) -> dict:
    path = Path(args["path"]).resolve()
    max_lines = int(args.get("max_lines", 200))
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    return {"path": str(path), "lines": lines[:max_lines]}


def tool_read_index(args: dict) -> dict:
    path = Path(args["path"]).resolve()
    text = path.read_text(encoding="utf-8")
    if args.get("head_only"):
        out = []
        in_head = False
        for line in text.splitlines():
            if line.strip() == "RAG_HEAD:":
                in_head = True
                out.append(line)
                continue
            if in_head:
                if line.startswith("-"):
                    out.append(line)
                else:
                    break
        return {"path": str(path), "rag_head": out}
    return {"path": str(path), "lines": text.splitlines()}


def tool_write_patch(args: dict) -> dict:
    path = Path(args["path"]).resolve()
    _deny_template_write(path)
    _apply_patch(path, args["mode"], args["content"], args.get("pattern"))
    return {"path": str(path), "status": "ok"}


def tool_route_lookup(args: dict) -> dict:
    path = Path(args["routes_path"]).resolve()
    text = path.read_text(encoding="utf-8")
    head = args["command_head"].strip()
    routes = []
    for line in text.splitlines():
        if "->" in line:
            left, right = line.split("->", 1)
            if left.strip() == head:
                routes = [p.strip() for p in right.split(",") if p.strip()]
                break
    return {"routes": routes}


def tool_fetch_facts(args: dict) -> dict:
    paths = [Path(p).resolve() for p in args["paths"]]
    limit = int(args["limit"])
    facts = []
    for p in paths:
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("-"):
                facts.append(line.strip("- "))
            if len(facts) >= limit:
                break
        if len(facts) >= limit:
            break
    return {"facts": facts[:limit]}


def tool_append_session(args: dict) -> dict:
    path = Path(args["session_path"]).resolve()
    _deny_template_write(path)
    path.write_text(path.read_text(encoding="utf-8") + args["content"], encoding="utf-8")
    return {"path": str(path), "status": "ok"}


def _update_panel(campaign_path: str, filename: str, args: dict) -> dict:
    base = Path(campaign_path).resolve()
    target = base / filename
    _deny_template_write(target)
    _apply_patch(target, args["mode"], args["content"], args.get("pattern"))
    return {"path": str(target), "status": "ok"}


def tool_update_hot_pack(args: dict) -> dict:
    return _update_panel(args["campaign_path"], "HOT_PACK.json", args)


def tool_update_mainline_panel(args: dict) -> dict:
    return _update_panel(args["campaign_path"], "MAINLINE_PANEL.json", args)


def tool_update_state_panel(args: dict) -> dict:
    return _update_panel(args["campaign_path"], "STATE_PANEL.json", args)


def tool_update_object_index(args: dict) -> dict:
    return _update_panel(args["campaign_path"], "OBJECT_INDEX.json", args)


def tool_copy_template(args: dict) -> dict:
    src = Path(args["src"]).resolve()
    dst = Path(args["dst"]).resolve()
    _deny_template_write(dst)
    if dst.exists():
        raise RuntimeError("destination exists")
    shutil.copytree(src, dst)
    return {"dst": str(dst), "status": "ok"}


def tool_bind_campaign(args: dict) -> dict:
    path = Path(args["campaign_path"]).resolve() / "CAMPAIGN.md"
    _deny_template_write(path)
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^cartridge_id:.*$", f"cartridge_id: {args['cartridge_id']}", text, flags=re.MULTILINE)
    text = re.sub(r"^cartridge_version_lock:.*$", f"cartridge_version_lock: {args['version_lock']}", text, flags=re.MULTILINE)
    path.write_text(text, encoding="utf-8")
    return {"path": str(path), "status": "ok"}


def tool_init_campaign(args: dict) -> dict:
    root = repo_root()
    from subprocess import run, PIPE
    payload = json.dumps(args["answers"], ensure_ascii=False)
    proc = run([sys.executable, str(root / "scripts" / "campaign_manager.py"), "init", "--from", "-"], input=payload.encode("utf-8"), stdout=PIPE, stderr=PIPE)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8"))
    return {"status": "ok"}


def tool_set_active(args: dict) -> dict:
    path = Path(args["campaign_path"]).resolve()
    _deny_template_write(path)
    root = repo_root()
    (root / "ACTIVE.md").write_text(f"active_campaign: {args['campaign_path']}\n", encoding="utf-8")
    return {"status": "ok"}


def tool_snapshot_update(args: dict) -> dict:
    base = Path(args["campaign_path"]).resolve()
    sessions = base / "sessions"
    _deny_template_write(sessions)
    current_ptr = (sessions / "CURRENT_SESSION.md").read_text(encoding="utf-8").strip()
    current_path = (base / current_ptr).resolve() if current_ptr else None
    if not current_path or not current_path.exists():
        raise RuntimeError("current session not found")
    snap_path = current_path.with_name(current_path.stem + "_快照.md")
    snap_path.write_text(current_path.read_text(encoding="utf-8"), encoding="utf-8")
    idx = sessions / "SESSION_INDEX.md"
    if idx.exists():
        idx.write_text(f"- {snap_path.name}\n", encoding="utf-8")
    return {"snapshot": str(snap_path)}


def tool_compress_history(args: dict) -> dict:
    base = Path(args["campaign_path"]).resolve()
    sessions = base / "sessions"
    _deny_template_write(sessions)
    current_ptr = (sessions / "CURRENT_SESSION.md").read_text(encoding="utf-8").strip()
    current_path = (base / current_ptr).resolve() if current_ptr else None
    comp_path = sessions / "history_压缩.md"
    parts = []
    for p in sorted(sessions.glob("session_*.md")):
        if current_path and p.resolve() == current_path.resolve():
            continue
        parts.append(p.read_text(encoding="utf-8"))
    comp_path.write_text("\n\n".join(parts), encoding="utf-8")
    return {"compressed": str(comp_path)}


def tool_load_snapshot(args: dict) -> dict:
    base = Path(args["campaign_path"]).resolve()
    sessions = base / "sessions"
    snaps = sorted(sessions.glob("*_快照.md"))
    if snaps:
        snap = snaps[-1]
        return {"snapshot": str(snap), "content": snap.read_text(encoding="utf-8")}
    current_ptr = (sessions / "CURRENT_SESSION.md").read_text(encoding="utf-8").strip()
    cur = (base / current_ptr).resolve()
    return {"snapshot": str(cur), "content": cur.read_text(encoding="utf-8")}


def tool_validate_no_new_facts(args: dict) -> dict:
    snap = Path(args["snapshot_path"]).read_text(encoding="utf-8")
    hot = Path(args["hot_pack_path"]).read_text(encoding="utf-8")
    out = args["load_output"]
    hay = snap + "\n" + hot
    ok = all(line.strip() in hay for line in out.splitlines() if line.strip())
    return {"status": "ok" if ok else "violation"}


def tool_register_handle(args: dict) -> dict:
    cart = Path(args["cartridge_path"]).resolve()
    idx = Path(args["index_path"]).resolve()
    _deny_template_write(cart)
    _deny_template_write(idx)
    handle = args["handle"]
    aliases = args["aliases"]
    cart_text = cart.read_text(encoding="utf-8")
    alias_line = f"{handle}: {aliases}\n"
    if handle not in cart_text:
        cart_text += "\n## aliases\n" + alias_line
        cart.write_text(cart_text, encoding="utf-8")
    idx_text = idx.read_text(encoding="utf-8")
    if "Handle Mapping" in idx_text and handle not in idx_text:
        idx_text += f"\n| {handle} | {aliases} |\n"
        idx.write_text(idx_text, encoding="utf-8")
    return {"status": "ok"}


def tool_validate_index_spec(args: dict) -> dict:
    path = Path(args["path"]).resolve()
    text = path.read_text(encoding="utf-8")
    required = ["RAG_HEAD:", "Handle Mapping", "Entry Pointers"]
    missing = [r for r in required if r not in text]
    return {"status": "ok" if not missing else "missing", "missing": missing}


def _load_manifest(role: str | None) -> set[str] | None:
    if not role:
        return None
    manifest = Path(__file__).resolve().parent.parent / "references" / "manifest.json"
    data = json.loads(manifest.read_text(encoding="utf-8"))
    role_def = data.get("roles", {}).get(role)
    if not role_def:
        raise RuntimeError(f"unknown role: {role}")
    return set(role_def.get("allowed_tools", []))


def run_calls(payload: dict, role: str | None = None) -> dict:
    allowed = _load_manifest(role)
    results = []
    for call in payload.get("tool_calls", []):
        name = call["name"]
        if allowed is not None and name not in allowed:
            raise RuntimeError(f"tool not allowed for role {role}: {name}")
        args = call.get("arguments", {})
        fn = TOOLMAP.get(name)
        if not fn:
            raise RuntimeError(f"unknown tool: {name}")
        results.append({"name": name, "result": fn(args)})
    return {"tool_results": results}


TOOLMAP = {
    "read_file": tool_read_file,
    "read_index": tool_read_index,
    "write_patch": tool_write_patch,
    "route_lookup": tool_route_lookup,
    "fetch_facts": tool_fetch_facts,
    "append_session": tool_append_session,
    "update_hot_pack": tool_update_hot_pack,
    "update_mainline_panel": tool_update_mainline_panel,
    "update_state_panel": tool_update_state_panel,
    "update_object_index": tool_update_object_index,
    "copy_template": tool_copy_template,
    "bind_campaign": tool_bind_campaign,
    "init_campaign": tool_init_campaign,
    "set_active": tool_set_active,
    "snapshot_update": tool_snapshot_update,
    "compress_history": tool_compress_history,
    "load_snapshot": tool_load_snapshot,
    "validate_no_new_facts": tool_validate_no_new_facts,
    "register_handle": tool_register_handle,
    "validate_index_spec": tool_validate_index_spec,
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", dest="json_file", help="tool_calls JSON file ('-' for stdin')")
    parser.add_argument("--role", dest="role", help="role name for tool whitelist")
    args = parser.parse_args()
    raw = sys.stdin.read() if args.json_file in (None, "-") else Path(args.json_file).read_text(encoding="utf-8")
    payload = json.loads(raw)
    out = run_calls(payload, role=args.role)
    sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
