# UI Short Codes (HUD)

Short codes are UI-only labels that expire each turn. Internally, bind them to stable IDs.

## Recommended prefixes

- `L#` location target (point of interaction in the current scene)
- `N#` NPC
- `I#` item / clue
- `Q#` quest
- `F#` faction (optional)

## Rules

- Re-number freely each turn; always reprint HUD.
- Never store short codes as truth; store stable IDs in files.
- When a player types a name/alias, resolve to stable ID; if ambiguous, present 2–4 candidates and map to short codes for selection.
