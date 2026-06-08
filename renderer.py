# renderer.py
# Verantwoordelijke: Rids

# ONTVANGT VAN ANDERE BESTANDEN:
# grid      van board.py    — weet welke vakjes gevuld zijn (2D array of color strings)
# shape, x, y van main.py  — positie van het vallende blok
# score     van score.py   — getal om op scherm te zetten
# next_shape van main.py   — voor de preview

import pygame

# ============ STYLE CONFIG ============

# Cell size (pixels) — adjustable for scaling
CELL_SIZE = 60

# Grid dimensions
columns = 10
rows = 20

# Screen size
width = CELL_SIZE * columns
height = CELL_SIZE * rows

# Border size per block
BOARD_BORDER = 1

# ============ BACKGROUND COLORS PER LEVEL ============

LEVEL_COLORS = {
    1: "#1a1a2e",  # deep navy
    2: "#2d2d3e",  # mid navy
    3: "#3e3e4f",  # light navy
    4: "#4f4f60",  # gray navy
    5: "#606071",  # mid gray
    6: "#717182",  # light gray
}

# ============ COLORS FROM tetromino.py ============

COLORS = {
    "I": "#37DCDC",  # cyan
    "O": "#FFFF00",  # yellow
    "T": "#800080",  # purple
    "S": "#008000",  # green
    "Z": "#FF0000",  # red
    "J": "#0000FF",  # blue
    "L": "#FFA500",  # orange
}

# ============ UI LAYOUT ============

# Preview box position (right side above board)
preview_box_x = width + 100
preview_box_y = 50
preview_box_width = CELL_SIZE * 4
preview_box_height = CELL_SIZE * 4

# Scoreboard position (bottom-middle)
scoreboard_x = width // 2 - 100
scoreboard_y = height - 80
scoreboard_width = 200
scoreboard_height = 60

# Game over overlay position (middle of screen)
game_over_x = width // 2 - 200
game_over_y = height // 2 - 100
game_over_width = 400
game_over_height = 200

# ============ RENDERING FUNCTIONS ============

def draw_board(screen, grid):
    """Draw the game board area — solid color rectangle in middle of screen"""
    board_x = 0
    board_y = 0
    board_width = width
    board_height = height

    # Draw board border
    pygame.draw.rect(screen, "#ffffff", (board_x, board_y, board_width, board_height), BOARD_BORDER)

    # If grid is provided, draw the blocks
    if grid is not None:
        for row in range(rows):
            for col in range(columns):
                cell_color = grid[row][col]
                if cell_color is not None and cell_color != "":
                    cell_x = col * CELL_SIZE + BOARD_BORDER
                    cell_y = row * CELL_SIZE + BOARD_BORDER
                    cell_width = CELL_SIZE - BOARD_BORDER * 2
                    cell_height = CELL_SIZE - BOARD_BORDER * 2
                    pygame.draw.rect(screen, cell_color, (cell_x, cell_y, cell_width, cell_height))


def draw_block(screen, shape, x, y, color=None):
    """Draw the piece that is currently falling"""
    # Determine color from shape name or use provided color
    if color is None:
        # Assume shape name is passed or use default
        color = "#ffffff"

    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                cell_x = (x + col) * CELL_SIZE + BOARD_BORDER
                cell_y = (y + row) * CELL_SIZE + BOARD_BORDER
                cell_width = CELL_SIZE - BOARD_BORDER * 2
                cell_height = CELL_SIZE - BOARD_BORDER * 2
                pygame.draw.rect(screen, color, (cell_x, cell_y, cell_width, cell_height))


def draw_score(screen, score):
    """Draw the score number on screen at bottom-middle"""
    # Scoreboard background
    pygame.draw.rect(screen, "#333333", (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height))

    # Score text
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, "#ffffff")
    screen.blit(score_text, (scoreboard_x + 10, scoreboard_y + 15))


def draw_preview(screen, shape, color=None):
    """Draw the next piece (small preview box) on right side above board"""
    # Preview box background
    pygame.draw.rect(screen, "#222222", (preview_box_x, preview_box_y, preview_box_width, preview_box_height))
    pygame.draw.rect(screen, "#ffffff", (preview_box_x, preview_box_y, preview_box_width, preview_box_height), BOARD_BORDER)

    # Preview text
    font_small = pygame.font.Font(None, 24)
    preview_text = font_small.render("Next:", True, "#cccccc")
    screen.blit(preview_text, (preview_box_x + 10, preview_box_y + 5))

    # Determine color from shape name or use provided color
    if color is None:
        color = "#ffffff"

    # Draw the shape in preview
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                cell_x = preview_box_x + 10 + col * CELL_SIZE + BOARD_BORDER
                cell_y = preview_box_y + 30 + row * CELL_SIZE + BOARD_BORDER
                cell_width = CELL_SIZE - BOARD_BORDER * 2
                cell_height = CELL_SIZE - BOARD_BORDER * 2
                pygame.draw.rect(screen, color, (cell_x, cell_y, cell_width, cell_height))


def draw_game_over(screen, score):
    """Draw the Game Over screen — overlay banner solid color rectangle in middle with score + 'Game Over', rest blurred in background"""
    # Overlay background
    pygame.draw.rect(screen, "#000000", (game_over_x, game_over_y, game_over_width, game_over_height))

    # Game Over text
    font_large = pygame.font.Font(None, 48)
    game_over_text = font_large.render("Game Over", True, "#ffffff")
    screen.blit(game_over_text, (game_over_x + 50, game_over_y + 40))

    # Final score text
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Final Score: {score}", True, "#cccccc")
    screen.blit(score_text, (game_over_x + 60, game_over_y + 100))

    # Restart prompt
    font_small = pygame.font.Font(None, 24)
    restart_text = font_small.render("Press R to restart", True, "#aaaaaa")
    screen.blit(restart_text, (game_over_x + 80, game_over_y + 140))
