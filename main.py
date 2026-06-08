import pygame
from board import is_valid, place_block, get_full_rows, remove_rows
from score import add_points, get_score, get_level, reset
from renderer import width, height, draw_block, draw_board, draw_game_over, draw_preview, draw_score
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
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    pygame.display.set_caption("Blockparty")
    # Variables
    current_block = get_random_shape()
    next_block = get_random_shape()
    current_fall_speed = fall_times.get(get_level(), 16)
    last_fall_time = pygame.time.get_ticks()
    x = 4
    y = 0
    # Event loop
    while True:
        for event in pygame.event.get():
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
                        

                 
        if pygame.time.get_ticks() - last_fall_time > current_fall_speed:
                last_fall_time = pygame.time.get_ticks()
                if is_valid(current_block, x, y + 1):
                    y += 1
                else:
                        place_block(current_block, x, y)
                        current_block = next_block
                        next_block = get_random_shape()
                        x = 4
                        y = 0
                        cleared_rows = get_full_rows()
                        remove_rows(cleared_rows)
                        add_points (len(cleared_rows))
                        current_fall_speed = fall_times.get(get_level(), 16)

                        if not is_valid(current_block,x ,y):
                                draw_game_over(screen, get_score())
                                reset()


        if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()
if __name__ == "__main__":
    main()
