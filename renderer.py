# renderer.py
# Verantwoordelijke: Rids
#
# ONTVANGT VAN ANDERE BESTANDEN:
# grid        van board.py   — 2D array of color strings
# shape, x, y van main.py   — positie van het vallende blok
# score       van score.py  — getal om op scherm te zetten
# next_shape  van main.py   — voor de preview
#
# Imports all colors and style helpers from Theme_style.py
# Does NOT run any game loop — only rendering functions

import pygame
from Theme_style import (
    SHADCN_DARK,
    NEON,
    LEVEL_COLORS,
    TETROMINO_COLORS,
    hex_to_rgb,
    draw_rounded_rect,
    draw_rounded_rect_border,
    draw_neon_glow,
    draw_neon_panel,
)


# ============ LAYOUT CONFIG ============

CELL_SIZE    = 60
COLUMNS      = 10
ROWS         = 20
BOARD_BORDER = 1
RADIUS       = 10   # matches Shadcn --radius: 0.625rem ≈ 10px

BOARD_WIDTH  = CELL_SIZE * COLUMNS
BOARD_HEIGHT = CELL_SIZE * ROWS

# Panel positions — right side of board
PANEL_MARGIN      = 20
PANEL_X           = BOARD_WIDTH + PANEL_MARGIN
PANEL_WIDTH       = CELL_SIZE * 4 + PANEL_MARGIN

TOTAL_WIDTH       = PANEL_X + PANEL_WIDTH + PANEL_MARGIN
TOTAL_HEIGHT      = BOARD_HEIGHT + PANEL_MARGIN * 2
# Preview box
PREVIEW_X         = PANEL_X
PREVIEW_Y         = 20
PREVIEW_W         = PANEL_WIDTH
PREVIEW_H         = CELL_SIZE * 4 + 40

# Scoreboard
SCORE_X           = PANEL_X
SCORE_Y           = PREVIEW_Y + PREVIEW_H + PANEL_MARGIN
SCORE_W           = PANEL_WIDTH
SCORE_H           = 70

# Level indicator
LEVEL_X           = PANEL_X
LEVEL_Y           = SCORE_Y + SCORE_H + PANEL_MARGIN
LEVEL_W           = PANEL_WIDTH
LEVEL_H           = 60

# Game over overlay — center of full screen
GAMEOVER_W        = 420
GAMEOVER_H        = 220

# ============ BOARD ============

def draw_background(screen, level):
    """Fill screen background based on current level"""
    color = LEVEL_COLORS.get(level, LEVEL_COLORS[1])
    screen.fill(hex_to_rgb(color))


def draw_board_area(screen, grid=None):
    """
    Draw the game board.
    - Neon cyan border glow around board edge
    - Draws all locked blocks from grid if provided
    """
    board_rect = (0, 0, BOARD_WIDTH, BOARD_HEIGHT)

    # Neon cyan glow on board border
    draw_neon_glow(screen, NEON["cyan"], board_rect, radius=0, glow_size=5, glow_layers=3)

    # Sharp board border line
    draw_rounded_rect_border(screen, NEON["cyan"], board_rect, radius=0, width=BOARD_BORDER)

    # Draw locked blocks from grid
    if grid is not None:
        for row in range(ROWS):
            for col in range(COLUMNS):
                cell_color = grid[row][col]
                if cell_color:
                    cx = col * CELL_SIZE + BOARD_BORDER + 2
                    cy = row * CELL_SIZE + BOARD_BORDER + 2
                    cw = CELL_SIZE - BOARD_BORDER * 2 - 4
                    ch = CELL_SIZE - BOARD_BORDER * 2 - 4
                    color_rgb = hex_to_rgb(cell_color) if isinstance(cell_color, str) else cell_color
                    draw_neon_panel(
                        screen,
                        (cx, cy, cw, ch),
                        fill_color=cell_color,
                        glow_color=cell_color,
                        radius=4,
                        glow_size=4,
                        border_width=1
                    )


def draw_block(screen, shape, x, y, color=None):
    """
    Draw the currently falling block.
    Each cell gets a neon panel with glow matching block color.
    """
    if color is None:
        color = NEON["purple"]

    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                cx = (x + col) * CELL_SIZE + BOARD_BORDER + 2
                cy = (y + row) * CELL_SIZE + BOARD_BORDER + 2
                cw = CELL_SIZE - BOARD_BORDER * 2 - 4
                ch = CELL_SIZE - BOARD_BORDER * 2 - 4
                draw_neon_panel(
                    screen,
                    (cx, cy, cw, ch),
                    fill_color=color,
                    glow_color=color,
                    radius=4,
                    glow_size=6,
                    border_width=1
                )


# ============ SIDE PANELS ============

def draw_preview(screen, shape, color=None):
    """
    Draw next piece preview panel with purple neon glow.
    """
    if color is None:
        color = NEON["purple"]

    draw_neon_panel(
        screen,
        (PREVIEW_X, PREVIEW_Y, PREVIEW_W, PREVIEW_H),
        fill_color=SHADCN_DARK["card"],
        glow_color=NEON["purple"],
        radius=RADIUS,
        glow_size=5
    )

    font = pygame.font.Font(None, 24)
    label = font.render("NEXT", True, hex_to_rgb(NEON["purple"]))
    screen.blit(label, (PREVIEW_X + 12, PREVIEW_Y + 10))

    # Center shape in preview box
    shape_cols = len(shape[0])
    shape_rows = len(shape)
    offset_x = PREVIEW_X + (PREVIEW_W - shape_cols * (CELL_SIZE - 10)) // 2
    offset_y = PREVIEW_Y + 30 + (PREVIEW_H - 30 - shape_rows * (CELL_SIZE - 10)) // 2

    for row in range(shape_rows):
        for col in range(shape_cols):
            if shape[row][col] == 1:
                cx = offset_x + col * (CELL_SIZE - 10)
                cy = offset_y + row * (CELL_SIZE - 10)
                cw = CELL_SIZE - 14
                ch = CELL_SIZE - 14
                draw_neon_panel(
                    screen,
                    (cx, cy, cw, ch),
                    fill_color=color,
                    glow_color=color,
                    radius=4,
                    glow_size=5,
                    border_width=1
                )


def draw_score(screen, score):
    """
    Draw score panel with green neon glow.
    """
    draw_neon_panel(
        screen,
        (SCORE_X, SCORE_Y, SCORE_W, SCORE_H),
        fill_color=SHADCN_DARK["card"],
        glow_color=NEON["green"],
        radius=RADIUS,
        glow_size=5
    )

    font_label = pygame.font.Font(None, 22)
    font_score = pygame.font.Font(None, 38)

    label = font_label.render("SCORE", True, hex_to_rgb(NEON["green"]))
    score_text = font_score.render(str(score), True, hex_to_rgb(SHADCN_DARK["foreground"]))

    screen.blit(label, (SCORE_X + 12, SCORE_Y + 10))
    screen.blit(score_text, (SCORE_X + 12, SCORE_Y + 30))


def draw_level(screen, level):
    """
    Draw level indicator panel with cyan neon glow.
    """
    draw_neon_panel(
        screen,
        (LEVEL_X, LEVEL_Y, LEVEL_W, LEVEL_H),
        fill_color=SHADCN_DARK["card"],
        glow_color=NEON["cyan"],
        radius=RADIUS,
        glow_size=5
    )

    font_label = pygame.font.Font(None, 22)
    font_level = pygame.font.Font(None, 34)

    label = font_label.render("LEVEL", True, hex_to_rgb(NEON["cyan"]))
    level_text = font_level.render(str(level), True, hex_to_rgb(SHADCN_DARK["foreground"]))

    screen.blit(label, (LEVEL_X + 12, LEVEL_Y + 8))
    screen.blit(level_text, (LEVEL_X + 12, LEVEL_Y + 28))


# ============ GAME OVER OVERLAY ============

def draw_game_over(screen, score, screen_width, screen_height):
    """
    Draw game over overlay in center of screen with pink neon glow.
    """
    gx = screen_width  // 2 - GAMEOVER_W // 2
    gy = screen_height // 2 - GAMEOVER_H // 2

    # Dark overlay behind panel
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    screen.blit(overlay, (0, 0))

    draw_neon_panel(
        screen,
        (gx, gy, GAMEOVER_W, GAMEOVER_H),
        fill_color=SHADCN_DARK["card"],
        glow_color=NEON["pink"],
        radius=RADIUS,
        glow_size=16
    )

    font_title  = pygame.font.Font(None, 56)
    font_score  = pygame.font.Font(None, 36)
    font_prompt = pygame.font.Font(None, 24)

    title  = font_title.render("GAME OVER",      True, hex_to_rgb(NEON["pink"]))
    s_text = font_score.render(f"Score: {score}", True, hex_to_rgb(SHADCN_DARK["foreground"]))
    prompt = font_prompt.render("Press R to restart", True, hex_to_rgb(SHADCN_DARK["muted-foreground"]))

    screen.blit(title,  (gx + GAMEOVER_W // 2 - title.get_width()  // 2, gy + 40))
    screen.blit(s_text, (gx + GAMEOVER_W // 2 - s_text.get_width() // 2, gy + 110))
    screen.blit(prompt, (gx + GAMEOVER_W // 2 - prompt.get_width() // 2, gy + 160))