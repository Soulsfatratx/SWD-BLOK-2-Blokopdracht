# renderer.py
# Verantwoordelijke: Rids
#
# Draws everything on the screen. main.py calls these functions.
# This file only draws — it never changes the game itself.

import pygame
from Theme_style import UI_COLORS, NEON, LEVEL_COLORS, hex_to_rgb, draw_panel


# ============ LAYOUT ============
# All positions and sizes in one place.

CELL_SIZE = 60
COLUMNS   = 10
ROWS      = 20

BOARD_WIDTH  = CELL_SIZE * COLUMNS
BOARD_HEIGHT = CELL_SIZE * ROWS

BLOCK_GAP = 3   # empty pixels around every block, so blocks don't touch

# All side panels sit in one column right of the board: same x, same width
PANEL_MARGIN = 20
PANEL_X      = BOARD_WIDTH + PANEL_MARGIN
PANEL_WIDTH  = CELL_SIZE * 4 + PANEL_MARGIN

TOTAL_WIDTH  = PANEL_X + PANEL_WIDTH + PANEL_MARGIN
TOTAL_HEIGHT = BOARD_HEIGHT + PANEL_MARGIN * 2

# The panels stack top to bottom: each one starts under the one above it
PREVIEW_Y      = 20
PREVIEW_HEIGHT = CELL_SIZE * 4 + 40
SCORE_Y        = PREVIEW_Y + PREVIEW_HEIGHT + PANEL_MARGIN
SCORE_HEIGHT   = 70
LEVEL_Y        = SCORE_Y + SCORE_HEIGHT + PANEL_MARGIN
LEVEL_HEIGHT   = 60
LEADER_Y       = LEVEL_Y + LEVEL_HEIGHT + PANEL_MARGIN
LEADER_HEIGHT  = TOTAL_HEIGHT - LEADER_Y - PANEL_MARGIN

# Grid lines between the cells: 0 = invisible, 255 = completely black
GRID_LINE_DARKNESS = 90


# ============ FONTS ============
fonts = {}

def get_font(size):
    if size not in fonts:
        fonts[size] = pygame.font.Font(None, size)
    return fonts[size]


# ============ SHARED HELPERS ============

def draw_text(screen, text, size, color, x, y):
    """Draw text with its top-left corner at (x, y)."""
    text_image = get_font(size).render(str(text), True, hex_to_rgb(color))
    screen.blit(text_image, (x, y))


def draw_text_centered(screen, text, size, color, center_x, y):
    """Draw text so that the middle of the text is at center_x."""
    text_image = get_font(size).render(str(text), True, hex_to_rgb(color))
    screen.blit(text_image, (center_x - text_image.get_width() // 2, y))


def draw_popup(screen, screen_width, screen_height, panel_width, panel_height, border_color):
    """
    The start of every popup: a dark see-through layer over the whole
    screen, with a panel in the middle. Gives back the y of the panel's
    top edge, so the caller can place text down from there.
    """
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))

    panel_x = screen_width  // 2 - panel_width  // 2
    panel_y = screen_height // 2 - panel_height // 2
    draw_panel(screen, (panel_x, panel_y, panel_width, panel_height),
                fill_color=UI_COLORS["card"], border_color=border_color)
    return panel_y


# ============ BOARD ============

def draw_background(screen, level):
    """Fill the whole screen with the background color of the current level."""
    color = LEVEL_COLORS.get(level, LEVEL_COLORS[1])
    screen.fill(hex_to_rgb(color))


def draw_grid_lines(screen):
    """
    Thin dark lines between the cells, so you can see the grid.
    The lines follow CELL_SIZE, so they always match the block size.
    """
    lines_layer = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT), pygame.SRCALPHA)
    line_color = (0, 0, 0, GRID_LINE_DARKNESS)

    # Standing lines: one between every column
    for column in range(1, COLUMNS):
        line_x = column * CELL_SIZE
        pygame.draw.line(lines_layer, line_color, (line_x, 0), (line_x, BOARD_HEIGHT))

    # Lying lines: one between every row
    for row in range(1, ROWS):
        line_y = row * CELL_SIZE
        pygame.draw.line(lines_layer, line_color, (0, line_y), (BOARD_WIDTH, line_y))

    screen.blit(lines_layer, (0, 0))


def draw_cell(screen, column, row, color):
    """Draw one square block at board position (column, row)."""
    pixel_x = column * CELL_SIZE + BLOCK_GAP
    pixel_y = row * CELL_SIZE + BLOCK_GAP
    size = CELL_SIZE - BLOCK_GAP * 2
    draw_panel(screen, (pixel_x, pixel_y, size, size), fill_color=color)


def draw_board_area(screen, grid=None):
    """
    Draw the game board: grid lines, a sharp cyan border around the edge,
    and all locked blocks that are saved in the grid.
    """
    draw_grid_lines(screen)
    draw_panel(screen, (0, 0, BOARD_WIDTH, BOARD_HEIGHT),
                border_color=NEON["cyan"], border_width=1)

    if grid is not None:
        for row in range(ROWS):
            for column in range(COLUMNS):
                if grid[row][column] != 0:
                    draw_cell(screen, column, row, grid[row][column])


def draw_block(screen, shape, x, y, color=None):
    """Draw the currently falling block, one cell at a time."""
    if color is None:
        color = NEON["purple"]

    for row in range(len(shape)):
        for column in range(len(shape[0])):
            if shape[row][column] == 1:
                draw_cell(screen, x + column, y + row, color)


# ============ SIDE PANELS ============

def draw_preview(screen, shape, color=None):
    """Panel that shows the next block."""
    if color is None:
        color = NEON["purple"]

    draw_panel(screen, (PANEL_X, PREVIEW_Y, PANEL_WIDTH, PREVIEW_HEIGHT),
                fill_color=UI_COLORS["card"], border_color=NEON["purple"])
    draw_text(screen, "NEXT", 24, NEON["purple"], PANEL_X + 12, PREVIEW_Y + 10)

    # The preview blocks are a bit smaller than the board blocks
    preview_cell = CELL_SIZE - 10

    # Put the shape in the middle of the panel
    shape_columns = len(shape[0])
    shape_rows = len(shape)
    start_x = PANEL_X + (PANEL_WIDTH - shape_columns * preview_cell) // 2
    start_y = PREVIEW_Y + 30 + (PREVIEW_HEIGHT - 30 - shape_rows * preview_cell) // 2

    for row in range(shape_rows):
        for column in range(shape_columns):
            if shape[row][column] == 1:
                block_x = start_x + column * preview_cell
                block_y = start_y + row * preview_cell
                block_size = preview_cell - BLOCK_GAP * 2
                draw_panel(screen, (block_x, block_y, block_size, block_size),
                            fill_color=color)


def draw_info_panel(screen, y, height, title, value, color, value_size):
    """
    Small panel with a title on top and a value under it.
    Used for the SCORE and LEVEL panels, because they look the same.
    """
    draw_panel(screen, (PANEL_X, y, PANEL_WIDTH, height),
                fill_color=UI_COLORS["card"], border_color=color)
    draw_text(screen, title, 22, color, PANEL_X + 12, y + 10)
    draw_text(screen, value, value_size, UI_COLORS["foreground"], PANEL_X + 12, y + 30)


def draw_score(screen, score):
    """Score panel, green."""
    draw_info_panel(screen, SCORE_Y, SCORE_HEIGHT, "SCORE", score, NEON["green"], 38)


def draw_level(screen, level):
    """Level panel, cyan."""
    draw_info_panel(screen, LEVEL_Y, LEVEL_HEIGHT, "LEVEL", level, NEON["cyan"], 34)


def draw_leaderboard(screen, scores):
    """
    Leaderboard panel, yellow.
    scores = list of [name, points, level]
    """
    draw_panel(screen, (PANEL_X, LEADER_Y, PANEL_WIDTH, LEADER_HEIGHT),
                fill_color=UI_COLORS["card"], border_color=NEON["yellow"])
    draw_text(screen, "LEADERBOARD", 26, NEON["yellow"], PANEL_X + 14, LEADER_Y + 14)

    # One score per line: "1. NAME  1200  L4"
    place = 1
    for score in scores:
        text = str(place) + ". " + score[0] + "   " + str(score[1]) + "   L" + str(score[2])
        draw_text(screen, text, 26, UI_COLORS["foreground"],
                  PANEL_X + 14, LEADER_Y + 50 + (place - 1) * 34)
        place = place + 1


# ============ POPUPS (game over, menus, name entry) ============

def draw_game_over(screen, score, screen_width, screen_height):
    """Game over popup, pink."""
    panel_y = draw_popup(screen, screen_width, screen_height, 420, 220, NEON["pink"])
    center_x = screen_width // 2

    draw_text_centered(screen, "GAME OVER", 56, NEON["pink"], center_x, panel_y + 40)
    draw_text_centered(screen, "Score: " + str(score), 36, UI_COLORS["foreground"], center_x, panel_y + 110)
    draw_text_centered(screen, "Press R to restart", 24, UI_COLORS["muted-foreground"], center_x, panel_y + 160)


def draw_menu(screen, title, options, selected, width, height):
    """
    Menu popup, purple.
    options  = list of texts
    selected = index of the chosen option (gets highlighted)
    """
    panel_height = 130 + len(options) * 60
    panel_y = draw_popup(screen, width, height, 460, panel_height, NEON["purple"])
    center_x = width // 2

    draw_text_centered(screen, title, 52, NEON["purple"], center_x, panel_y + 30)

    # Draw each option. The selected one gets a different color and arrows.
    for i in range(len(options)):
        if i == selected:
            color = NEON["green"]
            text = "> " + options[i] + " <"
        else:
            color = UI_COLORS["muted-foreground"]
            text = options[i]
        draw_text_centered(screen, text, 38, color, center_x, panel_y + 110 + i * 60)


def draw_name_entry(screen, player_number, name, width, height):
    """Popup where a player types their name (multiplayer), cyan."""
    panel_y = draw_popup(screen, width, height, 460, 200, NEON["cyan"])
    center_x = width // 2

    draw_text_centered(screen, "Player " + str(player_number) + " - enter name", 40, NEON["cyan"], center_x, panel_y + 30)
    # The typed name with an underscore behind it, so it looks like a cursor
    draw_text_centered(screen, name + "_", 46, UI_COLORS["foreground"], center_x, panel_y + 90)
    draw_text_centered(screen, "Press Enter to confirm", 24, UI_COLORS["muted-foreground"], center_x, panel_y + 150)
