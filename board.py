# board.py — Bogac
# Het speelbord: 20 rijen × 10 kolommen

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
    # geeft lijst van volle rij-nummers terug
    return [i for i, rij in enumerate(grid) if all(cel != 0 for cel in rij)]


def remove_rows(rijen):
    # verwijdert rijen, schuift rest omlaag
    global grid
    grid = [rij for i, rij in enumerate(grid) if i not in rijen]
    for _ in rijen:
        grid.insert(0, [0] * 10)


def reset():
    global grid
    grid = [[0] * 10 for _ in range(20)]