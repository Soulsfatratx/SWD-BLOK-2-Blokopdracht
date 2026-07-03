# board.py
# Verantwoordelijke: Bogac
# Het speelbord: 20 rijen x 10 kolommen

grid = [[0] * 10 for _ in range(20)]


def is_valid(shape, x, y):
    # True als positie geldig is (geen botsing)
    for rij_i, rij in enumerate(shape):
        for col_i, cel in enumerate(rij):
            if cel:
                nieuw_x = x + col_i
                nieuw_y = y + rij_i
                if nieuw_x < 0 or nieuw_x >= 10 or nieuw_y >= 20:
                    return False
                if nieuw_y >= 0 and grid[nieuw_y][nieuw_x] != 0:
                    return False
    return True


def place_block(shape, x, y, color):
    # schrijft blok vast in grid
    for rij_i, rij in enumerate(shape):
        for col_i, cel in enumerate(rij):
            if cel:
                grid[y + rij_i][x + col_i] = color


def get_full_rows():
    # geeft een lijst met de nummers van de volle rijen terug
    volle_rijen = []
    for i, rij in enumerate(grid):
        vol = True
        for cel in rij:
            if cel == 0:
                vol = False
        if vol:
            volle_rijen.append(i)
    return volle_rijen


def remove_rows(rijen):
    # haalt de volle rijen weg en schuift de rest naar beneden
    global grid
    nieuw_grid = []
    for i, rij in enumerate(grid):
        if i not in rijen:
            nieuw_grid.append(rij)
    # voor elke weggehaalde rij bovenaan een lege rij toevoegen
    for keer in range(len(rijen)):
        nieuw_grid.insert(0, [0] * 10)
    grid = nieuw_grid


def reset():
    global grid
    grid = [[0] * 10 for _ in range(20)]