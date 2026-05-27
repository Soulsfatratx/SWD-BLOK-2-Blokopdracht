# renderer.py
# Verantwoordelijke: Rids

# ONTVANGT VAN ANDERE BESTANDEN:
# grid      van board.py    — weet welke vakjes gevuld zijn
# shape, x, y van main.py  — positie van het vallende blok
# score     van score.py   — getal om op scherm te zetten
# next_shape van main.py   — voor de preview
columns = 10
rows = 20
CELL_SIZE = 60 #change this to change the size of the blocks
width = CELL_SIZE * columns
height = CELL_SIZE * rows

def draw_board(screen, grid):
    # All locked blocks already on the grid
    pass


def draw_block(screen, shape, x, y):
    # The piece that is currently falling
    pass


def draw_score(screen, score):
    # The score number on screen
    pass


def draw_preview(screen, shape):
    # The next piece (small preview box)
    pass


def draw_game_over(screen, score):
    # The Game Over screen
    pass
