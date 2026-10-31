#style.py  (colors + pull text, no game logic)
import os
import random

os.system('')   # enables ANSI on older Windows consoles

RESET = '\033[0m'
BOLD  = '\033[1m'
DIM   = '\033[2m'

def fg(n):
    """256-color foreground."""
    return f'\033[38;5;{n}m'

# one entry per tier in banners.py, same keys
RARITY = {
    '1s': {'color': fg(245), 'stars': '★',      'label': 'Common'},
    '2s': {'color': fg(114), 'stars': '★★',     'label': 'Uncommon'},
    '3s': {'color': fg(75),  'stars': '★★★',    'label': 'Rare'},
    '5s': {'color': fg(141), 'stars': '★★★★★',  'label': 'Epic'},
    '7s': {'color': fg(208), 'stars': '★★★★★★★', 'label': 'Legendary'},
    '9s': {'color': fg(220), 'stars': '✦✦✦✦✦✦✦✦✦', 'label': 'Mythic'},
}

# several lines per tier so pulls don't feel repetitive; {name} gets filled in
PULL_TEXT = {
    '1s': [
        'A faint breeze passes by...',
        'Nothing special happens. Someone shows up anyway.',
        'A familiar face wanders in.',
    ],
    '2s': [
        'A soft glow flickers across the terminal...',
        'Something stirs in the summoning circle.',
        'A dependable ally steps forward.',
    ],
    '3s': [
        'The air hums with energy...',
        'A bright spark cuts through the dark.',
        'Someone capable answers your call.',
    ],
    '5s': [
        'The ground trembles as a strong presence arrives...',
        'Light spirals upward in a violet storm.',
        'A figure steps out of the glow, unbothered.',
    ],
    '7s': [
        'One of the strongest beings in the worlds blesses you...',
        'The sky splits open. Someone legendary descends.',
        'Even the terminal goes quiet as they arrive.',
    ],
    '9s': [
        'A brilliant white light flashes across the world... Somebody is arriving from that streak of light...',
        'Reality itself bends. The summoning was never meant to reach this far.',
        'A mysterious aura fills up the terminal... This is no ordinary arrival.',
    ],
}

def tag(tier):
    """Colored rarity tag, e.g. ★★★★★ Epic"""
    r = RARITY[tier]
    return f"{r['color']}{BOLD}{r['stars']} {r['label']}{RESET}"

def pull_banner(tier, name):
    """Full multi-line pull message. Returns a string, you decide when to print it."""
    r = RARITY[tier]
    line = random.choice(PULL_TEXT[tier])
    width = 44
    bar = '─' * width
    return (
        f"\n{r['color']}{bar}{RESET}\n"
        f"{DIM}{line}{RESET}\n\n"
        f"  {tag(tier)}\n"
        f"  {r['color']}{BOLD}{name}{RESET}\n"
        f"{r['color']}{bar}{RESET}\n"
    )

def inv_row(tier, name, count):
    """One aligned inventory row. Pad the PLAIN text first, then add color."""
    r = RARITY[tier]
    return f"{r['color']}{name:<18}{RESET}{r['stars']:<10} x{count}"

if __name__ == '__main__':
    for t in RARITY:
        print(pull_banner(t, 'Test Character'))
        print(inv_row(t, 'Test Character', 3))
