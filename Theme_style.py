# Theme_style.py
# Verantwoordelijke: Rids
#
# Contains:
# - Shadcn dark and light color palettes (correctly converted)
# - Cyberpunk neon glow drawing helpers
# - Rounded rect helper
# - Border opacity helpers

import math
import pygame

# ============ SHADCN DARK MODE PALETTE ============
# All values correctly converted from Shadcn1.css oklch values

SHADCN_DARK = {
    "background":               "#0b0a09",
    "foreground":               "#fafaf9",
    "card":                     "#1b1817",
    "card-foreground":          "#fafaf9",
    "primary":                  "#5d0ec0",
    "primary-foreground":       "#f4f2fe",
    "secondary":                "#26262a",
    "secondary-foreground":     "#f9f9f9",
    "muted":                    "#292423",
    "muted-foreground":         "#a69f9b",
    "accent":                   "#292423",
    "accent-foreground":        "#fafaf9",
    "destructive":              "#ff6366",
    "border":                   "#2a2826",
    "input":                    "#302d2b",
    "ring":                     "#78706b",
    "sidebar":                  "#1b1817",
    "sidebar-foreground":       "#fafaf9",
    "sidebar-primary":          "#8d51ff",
    "sidebar-primary-foreground": "#f4f2fe",
    "sidebar-accent":           "#292423",
    "sidebar-accent-foreground": "#fafaf9",
    "sidebar-border":           "#2a2826",
    "sidebar-ring":             "#78706b",
}


# ============ SHADCN LIGHT MODE PALETTE ============

SHADCN_LIGHT = {
    "background":                   "#fefefe",
    "foreground":                   "#0b0a09",
    "card":                         "#fefefe",
    "card-foreground":              "#0b0a09",
    "primary":                      "#7008e7",
    "primary-foreground":           "#f4f2fe",
    "secondary":                    "#f3f3f4",
    "secondary-foreground":         "#17171a",
    "muted":                        "#f5f5f4",
    "muted-foreground":             "#78706b",
    "accent":                       "#f5f5f4",
    "accent-foreground":            "#1b1817",
    "destructive":                  "#e7000a",
    "border":                       "#e7e4e3",
    "input":                        "#e7e4e3",
    "ring":                         "#a69f9b",
    "sidebar":                      "#fafaf9",
    "sidebar-foreground":           "#0b0a09",
    "sidebar-primary":              "#7f22fd",
    "sidebar-primary-foreground":   "#f4f2fe",
    "sidebar-accent":               "#f5f5f4",
    "sidebar-accent-foreground":    "#1b1817",
    "sidebar-border":               "#e7e4e3",
    "sidebar-ring":                 "#a69f9b",
}


# ============ CYBERPUNK NEON COLORS ============
# Extra neon colors for glow effects on top of Shadows palette

NEON = {
    "purple":   "#8d51ff",   # Shadcn sidebar-primary — main glow color
    "cyan":     "#00f5ff",   # board border glow
    "pink":     "#ff2d78",   # destructive / danger glow
    "yellow":   "#ffe600",   # accent highlight
    "green":    "#00ff9f",   # success / score glow
}


# ============ LEVEL BACKGROUND COLORS ============
# Background gets slightly lighter as levels increase

LEVEL_COLORS = {
    1: "#091833",
    2: "#224E9F",
    3: "#0abdc6",
    4: "#0ac68e",
    5: "#ea00d9",
    6: "#711c91",
    7: "#ff0000",
    8: "#ffa200",
    9: "#ffe100",
}


# ============ TETROMINO COLORS ============

TETROMINO_COLORS = {
    "I": "#00f5ff",   # cyan neon
    "O": "#ffe600",   # yellow neon
    "T": "#8d51ff",   # purple neon
    "S": "#00ff9f",   # green neon
    "Z": "#ff2d78",   # pink neon
    "J": "#5d0ec0",   # deep purple
    "L": "#ff8c00",   # orange neon
}


# ============ HELPER: HEX TO RGB TUPLE ============

def hex_to_rgb(hex_color):
    """Convert hex string to (r, g, b) tuple for pygame"""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


# ============ HELPER: ROUNDED RECT ============

def draw_rounded_rect(screen, color, rect, radius=10):
    """Draw a filled rounded rectangle"""
    x, y, w, h = rect
    color = hex_to_rgb(color) if isinstance(color, str) else color
    if radius * 2 > min(w, h):
        radius = min(w, h) // 2
    pygame.draw.rect(screen, color, (x + radius, y, w - 2 * radius, h))
    pygame.draw.rect(screen, color, (x, y + radius, w, h - 2 * radius))
    pygame.draw.circle(screen, color, (x + radius,     y + radius),     radius)
    pygame.draw.circle(screen, color, (x + w - radius, y + radius),     radius)
    pygame.draw.circle(screen, color, (x + radius,     y + h - radius), radius)
    pygame.draw.circle(screen, color, (x + w - radius, y + h - radius), radius)


# ============ HELPER: ROUNDED RECT BORDER ONLY ============

def drawrounded_rect_border(screen, color, rect, radius=10, width=2):
    """Draw only the border of a rounded rectangle"""
    x, y, w, h = rect
    color = hex_to_rgb(color) if isinstance(color, str) else color
    if radius * 2 > min(w, h):
        radius = min(w, h) // 2
    pygame.draw.rect(screen, color, (x + radius, y, w - 2 * radius, width))
    pygame.draw.rect(screen, color, (x + radius, y + h - width, w - 2 * radius, width))
    pygame.draw.rect(screen, color, (x, y + radius, width, h - 2 * radius))
    pygame.draw.rect(screen, color, (x + w - width, y + radius, width, h - 2 * radius))
    pygame.draw.arc(screen, color, (x, y, radius * 2, radius * 2),
                    math.pi / 2, math.pi, width)
    pygame.draw.arc(screen, color, (x + w - radius * 2, y, radius * 2, radius * 2),
                    0, math.pi / 2, width)
    pygame.draw.arc(screen, color, (x, y + h - radius * 2, radius * 2, radius * 2),
                    math.pi, 3 * math.pi / 2, width)
    pygame.draw.arc(screen, color, (x + w - radius * 2, y + h - radius * 2, radius * 2, radius * 2),
                    3 * math.pi / 2, 2 * math.pi, width)


# ============ HELPER: NEON GLOW EFFECT ============

def draw_neon_glow(screen, color, rect, radius=10, glow_size=12, glow_layers=4):
    """
    Draw cyberpunk neon glow around a rounded rect.
    Fakes bloom by drawing increasingly larger transparent rects underneath.

    color     — neon hex color string e.g. '#8d51ff'
    rect      — (x, y, w, h)
    glow_size — how many pixels the glow extends outward
    glow_layers — how many layers of glow (more = softer bloom)
    """
    x, y, w, h = rect
    r, g, b = hex_to_rgb(color)

    glow_surface = pygame.Surface((w + glow_size * 2, h + glow_size * 2), pygame.SRCALPHA)

    for i in range(glow_layers, 0, -1):
        alpha = int(60 * (i / glow_layers))
        expand = int(glow_size * (i / glow_layers))
        glow_rect = (
            glow_size - expand,
            glow_size - expand,
            w + expand * 2,
            h + expand * 2
        )
        glow_radius = radius + expand
        draw_rounded_rect(
            glow_surface,
            (r, g, b, alpha),
            glow_rect,
            glow_radius
        )

    screen.blit(glow_surface, (x - glow_size, y - glow_size))


# ============ HELPER: NEON PANEL (full card with glow + fill + border) ============

def draw_neon_panel(screen, rect, fill_color, glow_color, border_color=None,
                    radius=10, glow_size=12, border_width=2):

    if border_color is None:
        border_color = glow_color

    draw_neon_glow(screen, glow_color, rect, radius=radius, glow_size=glow_size)
    draw_rounded_rect(screen, fill_color, rect, radius=radius)
    draw_rounded_rect_border(screen, border_color, rect, radius=radius, width=border_width)