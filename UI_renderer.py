# UI_renderer.py
# Verantwoordelijke: Rids

# This file loads the style and visual elements for SWD-BLOK-2-Blokopdracht.
# Run this to see the styling work in progress.
# Does not implement full game logic — only visual styling components.

import pygame
from pygame.locals import QUIT

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

# ============ RANDOM COLORS ============

# Available color pool for random block coloring
RANDOM_COLOR_POOL = [
    "#37DCDC",  # cyan
    "#FFFF00",  # yellow
    "#800080",  # purple
    "#008000",  # green
    "#FF0000",  # red
    "#0000FF",  # blue
    "#FFA500",  # orange
    "#FF69B4",  # hot pink
    "#00FFFF",  # turquoise
    "#8B00FF",  # dark violet
    "#FFD700",  # gold
    "#ADFF2F",  # green yellow
]

import random

# ============ MISSING DEPENDENCIES (PLACEHOLDER FOR OTHER CLASSMATES CODE) ============
# These calls reference files from other classmates. Use hardcoded values for testing until their code is ready.

# [1] SHAPES from tetromino.py — 2D arrays of all possible shapes
SHAPES = {
    "I": [[1, 1, 1, 1]],
    "O": [[1, 1], [1, 1]],
    "T": [[0, 1, 0], [1, 1, 1]],
    "S": [[0, 1, 1], [1, 1, 0]],
    "Z": [[1, 1, 0], [0, 1, 1]],
    "J": [[1, 0, 0], [1, 1, 1]],
    "L": [[0, 0, 1], [1, 1, 1]]
}

# [2] board.py — grid (2D array of color strings) — placeholder: use None for empty board
# board_grid = board.py sends grid → currently hardcoded as None

# [3] score.py — score value → placeholder: use manual score variable

# [4] main.py — shape, x, y (current falling position), next_shape (preview) → placeholder: use game state variables

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

def draw_background(screen, level):
    """Draw the background color based on current game level"""
    bg_color = LEVEL_COLORS.get(level, LEVEL_COLORS[1])
    screen.fill(bg_color)


def draw_board_area(screen, grid=None):
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


def draw_block(screen, shape, x, y, color):
    """Draw a single falling block at position (x, y)"""
    for row in range(len(shape)):
        for col in range(len(shape[0])):
            if shape[row][col] == 1:
                cell_x = (x + col) * CELL_SIZE + BOARD_BORDER
                cell_y = (y + row) * CELL_SIZE + BOARD_BORDER
                cell_width = CELL_SIZE - BOARD_BORDER * 2
                cell_height = CELL_SIZE - BOARD_BORDER * 2
                pygame.draw.rect(screen, color, (cell_x, cell_y, cell_width, cell_height))


def draw_score(screen, score):
    """Draw the scoreboard at bottom-middle"""
    # Scoreboard background
    pygame.draw.rect(screen, "#333333", (scoreboard_x, scoreboard_y, scoreboard_width, scoreboard_height))

    # Score text
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, "#ffffff")
    screen.blit(score_text, (scoreboard_x + 10, scoreboard_y + 15))


def draw_preview(screen, shape, color):
    """Draw the next piece preview box on right side above board"""
    # Preview box background
    pygame.draw.rect(screen, "#222222", (preview_box_x, preview_box_y, preview_box_width, preview_box_height))
    pygame.draw.rect(screen, "#ffffff", (preview_box_x, preview_box_y, preview_box_width, preview_box_height), BOARD_BORDER)

    # Preview text
    font_small = pygame.font.Font(None, 24)
    preview_text = font_small.render("Next:", True, "#cccccc")
    screen.blit(preview_text, (preview_box_x + 10, preview_box_y + 5))

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
    """Draw the game over overlay banner in middle of screen"""
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


# ============ GAME STATE ============

# All game state wrapped in mutable container to avoid UnboundLocalError
game_state = {
    "current_shape": [[1, 1, 1, 1]],  # I-shape default
    "current_x": 4,  # starting column
    "current_y": 0,  # starting row
    "current_color": random.choice(RANDOM_COLOR_POOL),
    "next_shape": [[1, 1], [1, 1]],  # O-shape default
    "next_color": random.choice(RANDOM_COLOR_POOL),
    "score": 0,
    "current_level": 1
}

# ============ STANDALONE TEST ============

def test_ui_renderer():
    """Run this to see the styling work in progress with block spawning and movement"""
    pygame.init()
    screen = pygame.display.set_mode((width + preview_box_width + 100, height))
    pygame.display.set_caption("UI Renderer — Style Preview")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            # Keyboard controls
            if event.type == pygame.KEYDOWN:
                # Arrow keys to move the object
                if event.key == pygame.K_LEFT:
                    game_state["current_x"] = max(0, game_state["current_x"] - 1)
                if event.key == pygame.K_RIGHT:
                    game_state["current_x"] = min(columns - 1, game_state["current_x"] + 1)
                if event.key == pygame.K_DOWN:
                    game_state["current_y"] = min(rows - 1, game_state["current_y"] + 1)

                # Enter to place new object (spawn new block)
                if event.key == pygame.K_RETURN:
                    game_state["score"] += 10
                    game_state["current_shape"] = random.choice(list(SHAPES.values()))
                    game_state["current_x"] = 4
                    game_state["current_y"] = 0
                    game_state["current_color"] = random.choice(RANDOM_COLOR_POOL)

                # Shift to change to next object
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    game_state["current_shape"] = game_state["next_shape"]
                    game_state["current_color"] = game_state["next_color"]
                    game_state["next_shape"] = random.choice(list(SHAPES.values()))
                    game_state["next_color"] = random.choice(RANDOM_COLOR_POOL)

                # Control to change color of object
                if event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    game_state["current_color"] = random.choice(RANDOM_COLOR_POOL)

        # Change background based on level
        draw_background(screen, game_state["current_level"])

        # Draw empty board area
        draw_board_area(screen, grid=None)

        # Draw scoreboard (example score)
        draw_score(screen, score=game_state["score"])

        # Draw preview
        draw_preview(screen, shape=game_state["next_shape"], color=game_state["next_color"])

        # Draw falling block
        draw_block(screen, game_state["current_shape"], game_state["current_x"], game_state["current_y"], game_state["current_color"])

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    test_ui_renderer()
