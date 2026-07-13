import sys
import pygame
import board
import leaderboard
from board import is_valid, place_block, get_full_rows, remove_rows
from score import add_points, get_score, get_level, reset
from renderer import TOTAL_WIDTH, TOTAL_HEIGHT, draw_block, draw_board_area, draw_game_over, draw_preview, draw_score, draw_level, draw_background, draw_leaderboard, draw_menu, draw_name_entry
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


def nieuw_spel():
    # Zet het bord en de score terug en maak twee nieuwe blokken.
    # Geeft de blokken terug zodat main() ze kan gebruiken.
    board.reset()
    reset()   # reset van score.py (score en level terug naar begin)
    current_block, current_color = get_random_shape()
    next_block, next_color = get_random_shape()
    return current_block, current_color, next_block, next_color


# start pygame op
def main():
    pygame.init()
    # pygame.init(), scherm aanmaken
    screen = pygame.display.set_mode((TOTAL_WIDTH, TOTAL_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)

    pygame.display.set_caption("Blockparty")
    # Spel variabelen
    current_block, current_color = None, None
    next_block, next_color = None, None
    current_fall_speed = fall_times.get(get_level(), 16)
    last_fall_time = pygame.time.get_ticks()
    x = 4
    y = 0

    # game_state zegt welk scherm we laten zien
    # "menu", "player_count", "playing", "game_over", "name_entry", "end_menu"
    game_state = "menu"
    # modus zegt of we single of multiplayer spelen
    modus = "single"

    # Keuzes in de menus (welke optie is geselecteerd)
    menu_keuze = 0     # 0 = Single Player, 1 = Multiplayer
    aantal_keuze = 0   # 0 = 2 spelers, 1 = 3 spelers
    eind_keuze = 0     # 0 = Restart Multiplayer, 1 = Single Player

    # Multiplayer variabelen
    aantal_spelers = 2
    huidige_speler = 1
    getypte_naam = ""
    huidige_naam = ""   # de naam van de speler die nu speelt

    # Event loop
    while True:
        space_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                # ----- MENU: kies Single of Multiplayer -----
                if game_state == "menu":
                    if event.key == pygame.K_UP:
                        menu_keuze = 0
                    elif event.key == pygame.K_DOWN:
                        menu_keuze = 1
                    elif event.key == pygame.K_RETURN:
                        if menu_keuze == 0:
                            # Single player starten
                            modus = "single"
                            leaderboard.reset()
                            leaderboard.zet_max(5)
                            current_block, current_color, next_block, next_color = nieuw_spel()
                            x = 4
                            y = 0
                            last_fall_time = pygame.time.get_ticks()
                            current_fall_speed = fall_times.get(get_level(), 16)
                            game_state = "playing"
                        else:
                            # Eerst aantal spelers kiezen
                            game_state = "player_count"

                # ----- PLAYER COUNT: kies 2 of 3 spelers -----
                elif game_state == "player_count":
                    if event.key == pygame.K_UP:
                        aantal_keuze = 0
                    elif event.key == pygame.K_DOWN:
                        aantal_keuze = 1
                    elif event.key == pygame.K_RETURN:
                        if aantal_keuze == 0:
                            aantal_spelers = 2
                        else:
                            aantal_spelers = 3
                        # Multiplayer starten
                        modus = "multi"
                        leaderboard.reset()
                        leaderboard.zet_max(None)
                        huidige_speler = 1
                        # Eerst het spel klaarzetten, daarna de naam vragen
                        current_block, current_color, next_block, next_color = nieuw_spel()
                        x = 4
                        y = 0
                        last_fall_time = pygame.time.get_ticks()
                        current_fall_speed = fall_times.get(get_level(), 16)
                        getypte_naam = ""
                        game_state = "name_entry"

                # ----- PLAYING: het blok besturen -----
                elif game_state == "playing":
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
                        if is_valid(rotated_block, x, y):
                            current_block = rotated_block

                    elif event.key == pygame.K_DOWN:
                        new_y = y + 1
                        if is_valid(current_block, x, new_y):
                            y = new_y

                    elif event.key == pygame.K_SPACE:
                        space_pressed = True

                        while is_valid(current_block, x, y + 1):
                            y += 1

                # ----- GAME OVER (single): R = opnieuw, Esc = menu -----
                elif game_state == "game_over":
                    if event.key == pygame.K_r:
                        current_block, current_color, next_block, next_color = nieuw_spel()
                        x = 4
                        y = 0
                        last_fall_time = pygame.time.get_ticks()
                        current_fall_speed = fall_times.get(get_level(), 16)
                        game_state = "playing"
                    elif event.key == pygame.K_ESCAPE:
                        leaderboard.reset()
                        game_state = "menu"

                # ----- NAME ENTRY (multiplayer): typ je naam -----
                elif game_state == "name_entry":
                    if event.key == pygame.K_RETURN:
                        # Lege naam? Dan geven we een standaard naam
                        if getypte_naam == "":
                            getypte_naam = "P" + str(huidige_speler)
                        # Onthoud de naam van deze speler en begin te spelen
                        huidige_naam = getypte_naam
                        getypte_naam = ""
                        game_state = "playing"
                    elif event.key == pygame.K_BACKSPACE:
                        # Laatste letter weghalen
                        getypte_naam = getypte_naam[:-1]
                    else:
                        # Een letter of cijfer toevoegen (maximaal 8 tekens)
                        if len(getypte_naam) < 8:
                            letter = event.unicode
                            if letter.isalnum():
                                getypte_naam = getypte_naam + letter.upper()

                # ----- END MENU (multiplayer klaar) -----
                elif game_state == "end_menu":
                    if event.key == pygame.K_UP:
                        eind_keuze = 0
                    elif event.key == pygame.K_DOWN:
                        eind_keuze = 1
                    elif event.key == pygame.K_RETURN:
                        if eind_keuze == 0:
                            # Restart Multiplayer: opnieuw aantal spelers kiezen
                            game_state = "player_count"
                        else:
                            # Single Player starten
                            modus = "single"
                            leaderboard.reset()
                            leaderboard.zet_max(5)
                            current_block, current_color, next_block, next_color = nieuw_spel()
                            x = 4
                            y = 0
                            last_fall_time = pygame.time.get_ticks()
                            current_fall_speed = fall_times.get(get_level(), 16)
                            game_state = "playing"

        # Blok valt automatisch (alleen tijdens het spelen)
        if game_state == "playing" and (pygame.time.get_ticks() - last_fall_time > current_fall_speed or space_pressed):
            last_fall_time = pygame.time.get_ticks()
            if is_valid(current_block, x, y + 1):
                y += 1
            else:
                place_block(current_block, x, y, current_color)
                current_block, current_color = next_block, next_color
                next_block, next_color = get_random_shape()
                x = 4
                y = 0
                cleared_rows = get_full_rows()
                remove_rows(cleared_rows)
                add_points(len(cleared_rows))
                current_fall_speed = fall_times.get(get_level(), 16)

                # Game over: past het nieuwe blok nog wel bovenaan?
                if not is_valid(current_block, x, y):
                    if modus == "single":
                        # Score in de lijst zetten en game over scherm tonen
                        leaderboard.voeg_single_toe(get_score(), get_level())
                        game_state = "game_over"
                    else:
                        # Multiplayer: score van deze speler opslaan met zijn naam
                        leaderboard.voeg_multi_toe(huidige_naam, get_score(), get_level())
                        if huidige_speler < aantal_spelers:
                            # De volgende speler: eerst het spel klaarzetten en naam vragen
                            huidige_speler = huidige_speler + 1
                            current_block, current_color, next_block, next_color = nieuw_spel()
                            x = 4
                            y = 0
                            last_fall_time = pygame.time.get_ticks()
                            current_fall_speed = fall_times.get(get_level(), 16)
                            getypte_naam = ""
                            game_state = "name_entry"
                        else:
                            # Alle spelers zijn geweest
                            game_state = "end_menu"

        # ----- Tekenen -----
        draw_background(screen, get_level())
        draw_board_area(screen, board.grid)

        # De panelen laten we zien zodra er gespeeld is (niet in de startmenus)
        if game_state != "menu" and game_state != "player_count":
            if game_state == "playing":
                draw_block(screen, current_block, x, y, current_color)
            draw_preview(screen, next_block, next_color)
            draw_score(screen, get_score())
            draw_level(screen, get_level())
            draw_leaderboard(screen, leaderboard.get_scores())

        # Menus en popups komen bovenop
        if game_state == "menu":
            draw_menu(screen, "BLOCKPARTY", ["Single Player", "Multiplayer"], menu_keuze, TOTAL_WIDTH, TOTAL_HEIGHT)
        elif game_state == "player_count":
            draw_menu(screen, "PLAYERS", ["2 Players", "3 Players"], aantal_keuze, TOTAL_WIDTH, TOTAL_HEIGHT)
        elif game_state == "game_over":
            draw_game_over(screen, get_score(), TOTAL_WIDTH, TOTAL_HEIGHT)
        elif game_state == "name_entry":
            draw_name_entry(screen, huidige_speler, getypte_naam, TOTAL_WIDTH, TOTAL_HEIGHT)
        elif game_state == "end_menu":
            draw_menu(screen, "GAME OVER", ["Restart Multiplayer", "Single Player"], eind_keuze, TOTAL_WIDTH, TOTAL_HEIGHT)

        pygame.display.flip()

if __name__ == "__main__":
    main()
