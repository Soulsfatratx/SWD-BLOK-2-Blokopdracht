# Theme_style.py
# Verantwoordelijke: Rids
#
# Contains:
# - Color palettes (UI colors, neon accents, level backgrounds)
# - hex_to_rgb helper
# - draw_panel: sharp square panel (fill + border, no radius, no glow)

import pygame


# ============ COLORS ============

# Basic UI colors for panels and text
UI_COLORS = {
    "foreground":       "#fafaf9",   # main text
    "card":             "#1b1817",   # panel background
    "muted-foreground": "#a69f9b",   # secondary / hint text
}

# Neon accent colors
NEON = {
    "purple":   "#28da00",   # menus, preview, falling block fallback
    "cyan":     "#007e02",   # board border, level panel, name entry
    "pink":     "#ff2d2d",   # game over
    "yellow":   "#ffaa00",   # leaderboard
    "green":    "#bb00ff",   # score, selected menu option
}

# Background color per level (1-9); above 9 falls back to level 1
LEVEL_COLORS = {
    1: "#0B1849",
    2: "#124D1C",
    3: "#E4B028",
    4: "#EBEDE3",
    5: "#FE7F2D",
    6: "#233D4D",
    7: "#000000",
    8: "#C13383",
    9: "#792CA2",
}


# ============ HELPERS ============

def hex_to_rgb(hex_color):
    """
    Turn a hex color like "#8d51ff" into (red, green, blue) numbers,
    because pygame wants colors as three numbers from 0 to 255.
    """
    hex_color = hex_color.lstrip("#")        # remove the "#" at the front
    red   = int(hex_color[0:2], 16)          # first two letters
    green = int(hex_color[2:4], 16)          # middle two letters
    blue  = int(hex_color[4:6], 16)          # last two letters
    return (red, green, blue)


def draw_panel(screen, rect, fill_color=None, border_color=None, border_width=2):
    """
    Draw a sharp square panel.
    fill_color   — hex string like "#1b1817", or None for no fill
    border_color — hex string, or None for no border
    """
    if fill_color is not None:
        pygame.draw.rect(screen, hex_to_rgb(fill_color), rect)
    if border_color is not None:
        pygame.draw.rect(screen, hex_to_rgb(border_color), rect, border_width)
