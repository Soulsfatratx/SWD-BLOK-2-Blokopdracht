import pygame
from renderer import width, height
from pygame.locals import QUIT

# screen size (pixels)
# define sensible defaults for width and height

# main.py
# Verantwoordelijke: Jona

# importeert alle bestanden
# from board import ...
# from tetromino import ...
# from score import ...
# from renderer import ...

# start pygame op
def main():
    pygame.init()
    # pygame.init(), scherm aanmaken
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    pygame.display.set_caption("Blockparty")
    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()
if __name__ == "__main__":
    main()


# houdt bij: huidige positie x, y
# waar het blok nu is

# houdt bij: huidig blok + volgend blok


# GAME-LOOP (ELKE FRAME):

# Stap 1: toetsen uitlezen

# Stap 2: is_valid() checken bij beweging

# Stap 3: blok laten vallen op tijd

# Stap 4: place_block() bij landing

# Stap 5: get_full_rows() + remove_rows()

# Stap 6: add_points() met aantal rijen

# Stap 7: alles tekenen via renderer
