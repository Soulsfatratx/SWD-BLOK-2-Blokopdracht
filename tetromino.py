'''
Tetromino module - Manuel
'''

import random

# 2D arrays of all possible shapes
SHAPES = {
    "I": [[1, 1, 1, 1]],
    "O": [[1, 1], [1, 1]],
    "T": [[0, 1, 0], [1, 1, 1]],
    "S": [[0, 1, 1], [1, 1, 0]],
    "Z": [[1, 1, 0], [0, 1, 1]],
    "J": [[1, 0, 0], [1, 1, 1]],
    "L": [[0, 0, 1], [1, 1, 1]]
}

# Colors matching with their shapes
COLORS = {
    "I": "#37DCDC",  # cyan
    "O": "#FFFF00",  # yellow
    "T": "#800080",  # purple
    "S": "#008000",  # green
    "Z": "#FF0000",  # red
    "J": "#0000FF",  # blue
    "L": "#FFA500",  # orange
}


def populate_bag(bag: list):
    for key, shape in SHAPES.items():
        bag.append((shape, COLORS[key]))

    return bag


bag = populate_bag([])


def get_shape(name):
    """Get a 2D array representing a shape"""

    return SHAPES[name]


def rotate(shape):
    """Rotate a shape 90 degrees to the right"""

    height = len(shape)
    width = len(shape[0])

    match (height, width):
        case (1, 4) | (4, 1):
            return [[shape[y][x] for y in range(height)] for x in range(width)]
        case (2, 2):
            return [[shape[x][y] for y in range(height)] for x in range(width)]
        case (2, 3):
            return [[shape[1 - y][x] for y in range(height)] for x in range(width)]
        case (3, 2):
            return [[shape[2 - y][x] for y in range(height)] for x in range(width)]


def get_random_shape():
    """Get a random shape and its color"""

    if not bag:
        populate_bag(bag)

    i = random.randint(0, len(bag) - 1)

    return bag.pop(i)
