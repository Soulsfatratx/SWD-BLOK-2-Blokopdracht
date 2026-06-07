# score.py
# Verantwoordelijke: Jona

# VARIABELEN
score = 0
lines_to_next_level = 10
level = 1
lines_cleared = 0
BASE_SINGLE = 100
BASE_DOUBLE = 300
BASE_TRIPLE = 500
BASE_TETRIS = 800
# huidige puntentelling


# FUNCTIES
# rekent punten uit en telt op
def add_points(aantal_rijen):
    global score 
    global lines_cleared
    if aantal_rijen == 1:
        score = score + BASE_SINGLE * level

    elif aantal_rijen == 2:
        score = score + BASE_DOUBLE * level

    elif aantal_rijen == 3:
        score = score + BASE_TRIPLE * level
        
    elif aantal_rijen == 4:
        score = score + BASE_TETRIS * level

    lines_cleared += aantal_rijen #Keeps track of the current amount of lines cleared
    check_level_up()

def check_level_up():
    global lines_cleared, level, lines_to_next_level
    
    while lines_cleared >= lines_to_next_level:
        level += 1
        lines_cleared -= lines_to_next_level # Carry over excess lines
        lines_to_next_level = 10 # Reset threshold for next level

def get_score():
    return score

def get_level(): 
    return level


def reset():
    global score, level, lines_cleared, lines_to_next_level
    score = 0
    level = 1
    lines_cleared = 0
    lines_to_next_level = 10