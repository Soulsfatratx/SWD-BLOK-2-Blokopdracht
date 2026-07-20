# Theme_style.py
# Verantwoordelijke: Rids

import pygame

# ============ COLORS ============

UI_COLORS = {
    "foreground":       "#fafaf9",   # main text
    "card":             "#1b1817",   # panel background
    "muted-foreground": "#a69f9b",   # secondary / hint text
}

ACCENT_COLORS = {
    "board":         "#007e02",   # border around the game board
    "blocks":        "#28da00",   # falling block when it has no color of its own
    "preview":       "#28da00",   # next block panel
    "score":         "#bb00ff",   # score panel
    "level":         "#007e02",   # level panel
    "leaderboard":   "#ffaa00",   # leaderboard panel
    "menu":          "#28da00",   # menu popups
    "menu_selected": "#bb00ff",   # menu options
    "game_over":     "#ff2d2d",   # game over popup
    "name_entry":    "#007e02",   # enter-your-name popup
}

LEVEL_COLORS = {
    1: "#0B1849",
    2: "#124D1C",
    3: "#E4B028",
    4: "#EBEDE3",
    5: "#883C0A",
    6: "#233D4D",
    7: "#000000",
    9: "#792CA2",
}


# ============ HELPERS ============

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    red   = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue  = int(hex_color[4:6], 16)
    return (red, green, blue)


def draw_panel(screen, rect, fill_color=None, border_color=None, border_width=2):
    if fill_color is not None:
        pygame.draw.rect(screen, hex_to_rgb(fill_color), rect)
    if border_color is not None:
        pygame.draw.rect(screen, hex_to_rgb(border_color), rect, border_width)
