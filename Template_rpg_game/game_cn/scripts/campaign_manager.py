#!/usr/bin/env python3
"""
campaign_manager.py — Campaign Management Script

Usage:
    python3 scripts/campaign_manager.py new --id campaign_XXXX
    python3 scripts/campaign_manager.py switch --path campaigns/campaign_XXXX
    python3 scripts/campaign_manager.py init --from answers.json
"""

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from datetime import datetime

# Base directory (where this script is located)
BASE_DIR = Path(__file__).parent.parent
GAME_EN_DIR = BASE_DIR / "game_en"
GAME_CN_DIR = BASE_DIR / "game_cn"


def get_campaign_path(campaign_id: str, lang: str = "en") -> Path:
    """Get the full path to a campaign directory."""
    game_dir = GAME_EN_DIR if lang == "en" else GAME_CN_DIR
    return game_dir / "campaigns" / campaign_id


def create_campaign(campaign_id: str, lang: str = "en") -> bool:
    """Create a new campaign from the template."""
    game_dir = GAME_EN_DIR if lang == "en" else GAME_CN_DIR
    template_dir = game_dir / "campaigns" / "_template"
    campaign_dir = get_campaign_path(campaign_id, lang)

    # Check if campaign already exists
    if campaign_dir.exists():
        print(f"Error: Campaign '{campaign_id}' already exists.")
        return False

    # Check if template exists
    if not template_dir.exists():
        print(f"Error: Template directory not found at {template_dir}")
        return False

    # Copy template to new campaign
    print(f"Creating campaign '{campaign_id}' from template...")
    shutil.copytree(template_dir, campaign_dir)

    # Update CURRENT_CAMPAIGN.md
    current_campaign_file = game_dir / "CURRENT_CAMPAIGN.md"
    current_content = f"""# CURRENT_CAMPAIGN.md

campaign_id: {campaign_id}
campaign_path: {campaign_dir}
created: {datetime.now().strftime('%Y-%m-%d')}
last_switched: {datetime.now().strftime('%Y-%m-%d')}
"""
    with open(current_campaign_file, 'w') as f:
        f.write(current_content)

    print(f"Campaign '{campaign_id}' created successfully at {campaign_dir}")
    print(f"Current campaign updated to: {campaign_id}")

    return True


def switch_campaign(campaign_path: str, lang: str = "en") -> bool:
    """Switch to an existing campaign."""
    game_dir = GAME_EN_DIR if lang == "en" else GAME_CN_DIR
    campaign_dir = Path(campaign_path)

    # Validate campaign directory
    if not campaign_dir.exists():
        print(f"Error: Campaign directory not found at {campaign_path}")
        return False

    # Get campaign ID from path
    campaign_id = campaign_dir.name

    # Update CURRENT_CAMPAIGN.md
    current_campaign_file = game_dir / "CURRENT_CAMPAIGN.md"
    current_content = f"""# CURRENT_CAMPAIGN.md

campaign_id: {campaign_id}
campaign_path: {campaign_dir}
created: {datetime.now().strftime('%Y-%m-%d')}
last_switched: {datetime.now().strftime('%Y-%m-%d')}
"""
    with open(current_campaign_file, 'w') as f:
        f.write(current_content)

    print(f"Switched to campaign '{campaign_id}'")
    return True


def initialize_campaign(answers_file: str = None, lang: str = "en") -> bool:
    """Initialize a campaign with player preferences and character."""
    game_dir = GAME_EN_DIR if lang == "en" else GAME_CN_DIR
    current_campaign_file = game_dir / "CURRENT_CAMPAIGN.md"

    # Read current campaign
    if not current_campaign_file.exists():
        print("Error: No campaign selected. Create or switch to a campaign first.")
        return False

    # Parse answers
    answers = {}
    if answers_file:
        with open(answers_file, 'r') as f:
            answers = json.load(f)

    # Create session file if needed
    sessions_dir = game_dir / "sessions"
    sessions_dir.mkdir(exist_ok=True)

    # Create initial session
    pc_name = answers.get('pc_name', 'Unknown')
    slug = answers.get('slug', f"{pc_name.lower().replace(' ', '_')}_start")
    date = answers.get('date', datetime.now().strftime('%Y-%m-%d'))
    session_file = sessions_dir / f"session_{date}_{slug}.md"

    session_content = f"""# Session: {pc_name}'s Adventure

> **Date**: {date}

## Decision: Initialization Complete

- Real time: {datetime.now().strftime('%Y-%m-%d')}
- In-world time: {answers.get('start_date', date)}
- Player input: Character creation complete
- Resolution: Campaign ready to begin
- Character: {pc_name}
- Starting location: {answers.get('start_loc', 'Unknown')}
- Opening hook: {answers.get('start_hook', 'None')}
"""

    with open(session_file, 'w') as f:
        f.write(session_content)

    # Update CURRENT_SESSION.md
    current_session_file = game_dir / "sessions" / "CURRENT_SESSION.md"
    with open(current_session_file, 'w') as f:
        f.write(f"sessions/{session_file.name}\n")

    # Update STATE_PANEL.md if answers provided
    state_panel = game_dir / "STATE_PANEL.md"
    if state_panel.exists():
        # Could patch STATE_PANEL.md with answers here
        pass

    print(f"Campaign initialized. Session file: {session_file}")
    print("Run '<Hot Start>' or '<Continue>' to begin playing.")

    return True


def list_campaigns(lang: str = "en") -> None:
    """List all campaigns."""
    game_dir = GAME_EN_DIR if lang == "en" else GAME_CN_DIR
    campaigns_dir = game_dir / "campaigns"

    if not campaigns_dir.exists():
        print("No campaigns directory found.")
        return

    print(f"\nCampaigns in {lang.upper()} version:")
    print("-" * 40)

    for campaign in sorted(campaigns_dir.iterdir()):
        if campaign.is_dir() and campaign.name != "_template":
            print(f"  - {campaign.name}")

    print()


def main():
    parser = argparse.ArgumentParser(
        description="Campaign Management Script"
    )
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # new command
    new_parser = subparsers.add_parser("new", help="Create new campaign")
    new_parser.add_argument("--id", required=True, help="Campaign ID (e.g., campaign_0001)")
    new_parser.add_argument("--lang", default="en", choices=["en", "cn"], help="Language version")

    # switch command
    switch_parser = subparsers.add_parser("switch", help="Switch to existing campaign")
    switch_parser.add_argument("--path", required=True, help="Path to campaign directory")
    switch_parser.add_argument("--lang", default="en", choices=["en", "cn"], help="Language version")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize campaign")
    init_parser.add_argument("--from", dest="from_file", help="JSON file with answers")
    init_parser.add_argument("--lang", default="en", choices=["en", "cn"], help="Language version")

    # list command
    list_parser = subparsers.add_parser("list", help="List all campaigns")
    list_parser.add_argument("--lang", default="en", choices=["en", "cn"], help="Language version")

    args = parser.parse_args()

    if args.command == "new":
        success = create_campaign(args.id, args.lang)
        sys.exit(0 if success else 1)

    elif args.command == "switch":
        success = switch_campaign(args.path, args.lang)
        sys.exit(0 if success else 1)

    elif args.command == "init":
        answers_file = getattr(args, "from_file", None)
        success = initialize_campaign(answers_file, args.lang)
        sys.exit(0 if success else 1)

    elif args.command == "list":
        list_campaigns(args.lang)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
