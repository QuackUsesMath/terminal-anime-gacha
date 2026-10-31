#style.py  (colors + pull text, claude baba took care of this)
import os
import random
from itertools import zip_longest
import textwrap
from collections import Counter


ART_PLACEHOLDER = [
    '┌──────────┐',
    '│          │',
    '│  ASCII   │',
    '│   ART    │',
    '│          │',
    '└──────────┘',
]

# Spare art, one per tier. NOT used anywhere yet: wiring it in and the alignment are up to you.
# e.g. detail_view(..., art=ART_BY_TIER[tier])
ART_BY_TIER = {
    '1s': [
        '    .    ',
        '   .:.   ',
        '  .:★:.  ',
        '   `:´   ',
        '    ´    ',
    ],
    '2s': [
        '  ╭─────╮  ',
        '  │ ★ ★ │  ',
        '  │  ◡  │  ',
        '  ╰─────╯  ',
    ],
    '3s': [
        '   /\\   ',
        '  /  \\  ',
        ' / ★★★\\ ',
        '/______\\',
    ],
    '4s': [
        '  ╔═══════╗  ',
        '  ║ ◆ ◆ ◆ ║  ',
        '  ║  ★★★★ ║  ',
        '  ╚═══════╝  ',
    ],
    '5s': [
        '    ▲    ',
        '   ▲▲▲   ',
        '  ▲▲★▲▲  ',
        ' ▲▲▲▲▲▲▲ ',
        '    █    ',
    ],
    '7s': [
        '  \\ | /  ',
        '-- ★★★ --',
        '  / | \\  ',
        ' ═══╬═══ ',
        '    ║    ',
    ],
    '9s': [
        '  ✦ . ✦ . ✦  ',
        ' . ╔═════╗ . ',
        '✦  ║  ✦  ║  ✦',
        ' . ╚═════╝ . ',
        '  ✦ . ✦ . ✦  ',
    ],
}

os.system('')   # enables ANSI on older Windows consoles

RESET  = '\033[0m'
BOLD   = '\033[1m'
DIM    = '\033[2m'
ITALIC = '\033[3m'

def multi_summary(results):
    order = list(RARITY)                       # '1s' ... '9s', lowest to highest
    counts = Counter(results)                  # {('1s', 'Piccolo'): 4, ...}
    rows = sorted(counts.items(), key=lambda kv: order.index(kv[0][0]), reverse=True)

    lines = [f'{len(results)} pulls', '']
    for (tier, name), n in rows:
        r = RARITY[tier]
        lines.append(f"{r['color']}{r['stars']:<10}{name:<22}{RESET}x{n}")
    return '\n'.join(lines)

def wrap(text, width):
    return textwrap.wrap(text, width)


def fg(n):
    """256-color foreground."""
    return f'\033[38;5;{n}m'

# one entry per tier in banners.py, same keys. KEEP THIS ORDERED lowest -> highest,
# multi_summary uses the order to sort by rarity.
RARITY = {
    '1s': {'color': fg(245), 'stars': '★',         'label': 'Common'},
    '2s': {'color': fg(114), 'stars': '★★',        'label': 'Uncommon'},
    '3s': {'color': fg(75),  'stars': '★★★',       'label': 'Rare'},
    '4s': {'color': fg(43),  'stars': '★★★★',      'label': 'Super Rare'},
    '5s': {'color': fg(141), 'stars': '★★★★★',     'label': 'Epic'},
    '7s': {'color': fg(208), 'stars': '★★★★★★★',   'label': 'Legendary'},
    '9s': {'color': fg(220), 'stars': '✦✦✦✦✦✦✦✦✦', 'label': 'Mythic'},
}

# the pattern each tier's border repeats; higher tiers get heavier borders
BAR_UNIT = {
    '1s': '─',
    '2s': '─',
    '3s': '━',
    '4s': '━',
    '5s': '═',
    '7s': '═',
    '9s': '✦ ',
}

# several lines per tier so pulls don't feel repetitive
PULL_TEXT = {
    '1s': [
        'A faint breeze passes by...',
        'Nothing special happens. Someone shows up anyway.',
        'A familiar face wanders in.',
        'Dust settles. A figure shrugs and waves.',
    ],
    '2s': [
        'A soft glow flickers across the terminal...',
        'Something stirs in the summoning circle.',
        'A dependable ally steps forward.',
        'A small spark catches. Someone useful appears.',
    ],
    '3s': [
        'The air hums with energy...',
        'A bright spark cuts through the dark.',
        'Someone capable answers your call.',
        'The circle flares blue. A skilled fighter arrives.',
    ],
    '4s': [
        'A cold teal light pours out of the circle...',
        'The terminal flickers. Someone impressive steps through.',
        'Static crackles in the air. A strong presence takes shape.',
        'The summoning rings twice. Somebody notable heard it.',
    ],
    '5s': [
        'The ground trembles as a strong presence arrives...',
        'Light spirals upward in a violet storm.',
        'A figure steps out of the glow, unbothered.',
        'The air bends. Whoever this is, they are not here by accident.',
    ],
    '7s': [
        'One of the strongest beings in the worlds blesses you...',
        'The sky splits open. Someone legendary descends.',
        'Even the terminal goes quiet as they arrive.',
        'Flames of gold race across the screen. A legend answers.',
    ],
    '9s': [
        'A brilliant white light flashes across the world... Somebody is arriving from that streak of light...',
        'Reality itself bends. The summoning was never meant to reach this far.',
        'A mysterious aura fills up the terminal... This is no ordinary arrival.',
        'Every star in the sky goes dark for a single heartbeat. Then, someone steps out.',
    ],
}

def tag(tier):
    """Colored rarity tag, e.g. ★★★★★ Epic"""
    r = RARITY[tier]
    return f"{r['color']}{BOLD}{r['stars']} {r['label']}{RESET}"

def pull_banner(tier, name):
    """Full multi-line pull message. Returns a string, you decide when to print it."""
    r = RARITY[tier]
    c = r['color']
    line = random.choice(PULL_TEXT[tier])
    width = 44
    bar = (BAR_UNIT[tier] * width)[:width]
    return (
        f"\n{c}{bar}{RESET}\n"
        f"{DIM}{ITALIC}{line}{RESET}\n\n"
        f"  {tag(tier)}\n"
        f"  {c}{BOLD}» {name} «{RESET}\n"
        f"{c}{bar}{RESET}\n"
    )

def inv_row(tier, name, count):
    """One aligned inventory row. Pad the PLAIN text first, then add color."""
    r = RARITY[tier]
    return f"{r['color']}{name:<22}{RESET}{r['stars']:<10} x{count}"


def detail_view(tier, name, count, desc, art=None):
    art = art or ART_PLACEHOLDER
    r = RARITY[tier]
    art_width = max(len(line) for line in art)

    text = [
        f"{r['color']}{BOLD}{name}{RESET}",
        tag(tier),
        f"Owned: x{count}",
        '',
        *wrap(desc, 38),
    ]

    rows = []
    for a, t in zip_longest(art, text, fillvalue=''):
        rows.append(f"{r['color']}{a:<{art_width}}{RESET}   {t}")
    return '\n'.join(rows)



if __name__ == '__main__':
    for t in RARITY:
        print(pull_banner(t, 'Test Character'))
        print(inv_row(t, 'Test Character', 3))
