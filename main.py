import pygame
from board import is_valid, place_block, get_full_rows, remove_rows
from score import add_points, get_score, get_level, reset
from renderer import TOTAL_WIDTH, TOTAL_HEIGHT, draw_block, draw_board_area, draw_game_over, draw_preview, draw_score, draw_level, draw_background
from tetromino import get_random_shape, rotate
from pygame.locals import QUIT

# screen size (pixels)
# define sensible defaults for width and height

# main.py
# Verantwoordelijke: Jona
fall_times = {
    0: 800,
    1: 717,
    2: 633,
    3: 550,
    4: 467,
    5: 383,
    6: 300,
    7: 217,
    8: 133,
    9: 100,
}
# start pygame op
def main():
    pygame.init()
    # pygame.init(), scherm aanmaken
    screen = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT))
    pygame.display.set_caption("Blockparty")
    # Variables
    current_block, current_color = get_random_shape()
    next_block, next_color = get_random_shape()

    current_fall_speed = fall_times.get(get_level(), 16)
    last_fall_time = pygame.time.get_ticks()
    x = 4
    y = 0
    # Event loop
    while True:
        for event in pygame.event.get():
            # Handle user input for moving and rotating the block
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys; sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x = x - 1
                    if is_valid(current_block, new_x, y):
                        x = new_x

                elif event.key == pygame.K_RIGHT:
                    new_x = x + 1
                    if is_valid(current_block, new_x, y):
                        x = new_x 

                elif event.key == pygame.K_UP:
                    rotated_block = rotate(current_block)
                    if is_valid(rotated_block, x, y ):
                         current_block = rotated_block

                elif event.key == pygame.K_DOWN:
                    new_y = y + 1
                    if is_valid(current_block, x, new_y):
                        y = new_y

                elif event.key == pygame.K_SPACE:
                    while is_valid(current_block, x, y + 1):
                        y += 1
                        

                 # Auto-fall based on current fall speed
        if pygame.time.get_ticks() - last_fall_time > current_fall_speed:
                last_fall_time = pygame.time.get_ticks()
                if is_valid(current_block, x, y + 1):
                    y += 1
                else:
                        place_block(current_block, x, y)
                        current_block, current_color = next_block, next_color
                        next_block, next_color = get_random_shape()
                        x = 4
                        y = 0
                        cleared_rows = get_full_rows()
                        remove_rows(cleared_rows)
                        add_points (len(cleared_rows))
                        current_fall_speed = fall_times.get(get_level(), 16)

                        if not is_valid(current_block,x ,y):
                                draw_game_over(screen, get_score(), TOTAL_WIDTH, TOTAL_HEIGHT)
                                reset()
        # Rendering
        draw_background(screen, get_level())
        draw_board_area(screen)
        draw_block(screen, current_block, x, y, current_color)
        draw_preview(screen, next_block, next_color)
        draw_score(screen, get_score())
        draw_level(screen, get_level())
        pygame.display.flip()

if __name__ == "__main__":
    main()                                


       