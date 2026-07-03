# leaderboard.py
# Verantwoordelijke: Bogac
# Houdt de scores bij tijdens deze sessie.
# We slaan niks op in een bestand, dus als je het spel sluit is alles weg.

# Elke score is een klein lijstje: [naam, punten, level]
scores = []

# Teller voor single player. Zo krijgen we "RUN 1", "RUN 2", enzovoort.
run_teller = 0

# Hoeveel scores we maximaal bewaren.
# None = geen limiet (multiplayer). 5 = alleen de top 5 (single player).
max_scores = None


def reset():
    # Maakt de lijst helemaal leeg (bij nieuwe modus of terug naar het menu)
    global scores, run_teller
    scores = []
    run_teller = 0


def zet_max(n):
    # Stelt in hoeveel scores we bewaren (5 bij single, None bij multiplayer)
    global max_scores
    max_scores = n


def sorteer_sleutel(score):
    # We sorteren eerst op punten, en bij gelijke punten op level
    return (score[1], score[2])


def sorteer():
    # Zet de hoogste scores bovenaan
    scores.sort(key=sorteer_sleutel, reverse=True)


def knip_lijst():
    # Als er een limiet is, houden we alleen de bovenste scores over
    global scores
    if max_scores is not None:
        scores = scores[:max_scores]


def voeg_multi_toe(naam, punten, level):
    # Voegt een score met naam toe (multiplayer)
    scores.append([naam, punten, level])
    sorteer()
    knip_lijst()


def voeg_single_toe(punten, level):
    # Voegt een score zonder naam toe (single player), met een RUN nummer
    global run_teller
    run_teller = run_teller + 1
    naam = "RUN " + str(run_teller)
    scores.append([naam, punten, level])
    sorteer()
    knip_lijst()


def get_scores():
    # Geeft de lijst met scores terug
    return scores
