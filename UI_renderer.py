# UI_renderer.py
# Verantwoordelijke: Rids
#
# Standalone test runner for the UI renderer.
# Only handles the game loop and input.
# All drawing logic is in renderer.py
# All colors and style helpers are in Theme_style.py
#
# Controls:
#   Arrow keys     — move block
#   Enter          — spawn new block
#   Shift          — swap to next block
#   Ctrl           — change block color
#   Q              — quit

import pygame
from pygame.locals import QUIT
import random

from renderer import (
    COLUMNS,
    ROWS,
    CELL_SIZE,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    PANEL_X,
    PANEL_WIDTH,
    draw_background,
    draw_board_area,
    draw_block,
    draw_preview,
    draw_score,
    draw_level,
    draw_game_over,
)
from Theme_style import TETROMINO_COLORS, NEON


# ============ SHAPES ============
# Placeholder shapes until tetromino.py is connected

SHAPES = {
    "I": [[1, 1, 1, 1]],
    "O": [[1, 1],
          [1, 1]],
    "T": [[0, 1, 0],
          [1, 1, 1]],
    "S": [[0, 1, 1],
          [1, 1, 0]],
    "Z": [[1, 1, 0],
          [0, 1, 1]],
    "J": [[1, 0, 0],
          [1, 1, 1]],
    "L": [[0, 0, 1],
          [1, 1, 1]],
}

SHAPE_KEYS    = list(SHAPES.keys())
COLOR_POOL    = list(TETROMINO_COLORS.values()) + list(NEON.values())

SCREEN_WIDTH  = PANEL_X + PANEL_WIDTH + 20
SCREEN_HEIGHT = BOARD_HEIGHT


# ============ GAME STATE ============

def new_shape():
    key = random.choice(SHAPE_KEYS)
    return SHAPES[key], TETROMINO_COLORS.get(key, NEON["purple"])


def initial_state():
    shape, color       = new_shape()
    next_shape, next_c = new_shape()
    return {
        "current_shape": shape,
        "current_color": color,
        "current_x":     COLUMNS // 2 - 2,
        "current_y":     0,
        "next_shape":    next_shape,
        "next_color":    next_c,
        "score":         0,
        "level":         1,
        "game_over":     False,
    }


# ============ GAME LOOP ============

def run():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SWD-BLOK-2 — UI Preview")
    clock = pygame.time.Clock()

    state = initial_state()

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if state["game_over"]:
                    if event.key == pygame.K_r:
                        state = initial_state()
                    continue

                # Move block
                if event.key == pygame.K_LEFT:
                    state["current_x"] = max(0, state["current_x"] - 1)

                if event.key == pygame.K_RIGHT:
                    max_x = COLUMNS - len(state["current_shape"][0])
                    state["current_x"] = min(max_x, state["current_x"] + 1)

                if event.key == pygame.K_DOWN:
                    max_y = ROWS - len(state["current_shape"])
                    state["current_y"] = min(max_y, state["current_y"] + 1)

                # Spawn new block and add score
                if event.key == pygame.K_RETURN:
                    state["score"] += 10
                    if state["score"] >= state["level"] * 50:
                        state["level"] = min(9, state["level"] + 1)
                    shape, color = new_shape()
                    state["current_shape"] = shape
                    state["current_color"] = color
                    state["current_x"]     = COLUMNS // 2 - 2
                    state["current_y"]     = 0

                # Swap to next block
                if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                    state["current_shape"] = state["next_shape"]
                    state["current_color"] = state["next_color"]
                    state["current_x"]     = COLUMNS // 2 - 2
                    state["current_y"]     = 0
                    state["next_shape"], state["next_color"] = new_shape()

                # Change block color
                if event.key in (pygame.K_LCTRL, pygame.K_RCTRL):
                    state["current_color"] = random.choice(COLOR_POOL)

                # Trigger game over for testing
                if event.key == pygame.K_g:
                    state["game_over"] = True

                # Quit
                if event.key == pygame.K_q:
                    running = False

        # ---- DRAW ----

        draw_background(screen, state["level"])
        draw_board_area(screen, grid=None)
        draw_block(
            screen,
            state["current_shape"],
            state["current_x"],
            state["current_y"],
            state["current_color"]
        )
        draw_preview(screen, state["next_shape"], state["next_color"])
        draw_score(screen, state["score"])
        draw_level(screen, state["level"])

        if state["game_over"]:
            draw_game_over(screen, state["score"], SCREEN_WIDTH, SCREEN_HEIGHT)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()