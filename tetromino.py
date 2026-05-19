'''
Tetromino module - Manuel
'''

import random

# 2D arrays of all possible shapes
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]]
}

# Colors matching with their shapes
COLORS = {
    'I': 'cyan',
    'O': 'yellow',
    'T': 'purple',
    'S': 'green',
    'Z': 'red',
    'J': 'blue',
    'L': 'orange'
}


def get_shape(name):
    '''Get a 2D array representing a shape'''

    return SHAPES[name]


def rotate(shape):
    '''Rotate a shape 90 degrees to the right'''

    height = len(shape)
    width = len(shape[0])

    match (height, width):
        case (1, 4) | (4, 1):
            return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]))]
        case (2, 2):
            return [[shape[x][y] for y in range(len(shape))] for x in range(len(shape[0]))]
        case (2, 3):
            return [[shape[1 - y][x] for y in range(len(shape))] for x in range(len(shape[0]))]
        case (3, 2):
            return [[shape[2 - y][x] for y in range(len(shape))] for x in range(len(shape[0]))]


def get_random_shape():
    '''Get a random shape'''

    return random.choice(list(SHAPES.values()))
