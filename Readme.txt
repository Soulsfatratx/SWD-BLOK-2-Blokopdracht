================================================================
BLOCKPARTY | Tetris project
Groep: Jona, Manuel, Bogac, Rids
================================================================

VEREISTEN
---------
- Python 3.10 of hoger (aanbevolen: 3.12)
- pygame (zie installatie hieronder)


EERSTE OPSTART
--------------

Stap 1 Controleer of Python geinstalleerd is
  Open een terminal (Windows: Command Prompt of PowerShell, Mac: Terminal)
  en typ:

    python --version

  Je moet iets zien zoals "Python 3.12.x".
  Zie je dat niet, download Python dan via https://www.python.org/downloads/

Stap 2 Installeer de benodigde packages
  Navigeer in de terminal naar de map waar de projectbestanden staan:

    Windows:  cd C:\pad\naar\je\map
    Mac:      cd /pad/naar/je/map

  Installeer daarna de packages met:

    pip install -r requirements.txt

  Dit installeert pygame automatisch.

  Lukt dat niet? Installeer pygame dan handmatig:

    pip install pygame

Stap 3 Start het spel
  Zorg dat je in de juiste map staat en typ:

    python main.py

  Het spel opent een venster met het hoofdmenu.


DAARNA OPSTARTEN
----------------
Na de eerste opstart hoef je pygame niet opnieuw te installeren.
Start het spel gewoon opnieuw met:

  python main.py


HOE SPEEL JE HET SPEL
----------------------
Navigeren in menu's:
  Pijltje omhoog / omlaag   Optie selecteren
  Enter                      Bevestigen

Blok besturen (tijdens het spelen):
  Pijltje links / rechts    Blok verplaatsen
  Pijltje omhoog            Blok roteren
  Pijltje omlaag            Blok sneller laten vallen
  Spatiebalk                Blok direct naar beneden droppen

Na game over (single player):
  R                          Opnieuw spelen
  Escape                     Terug naar het hoofdmenu


PROJECTBESTANDEN
----------------
main.py          Game-loop en spellogica            (Jona)
score.py         Scorebeheer en levelsysteem        (Jona)
board.py         Speelveld en botsingsdetectie      (Bogac)
leaderboard.py   Scorelijst bijhouden               (Bogac)
tetromino.py     Vormen en rotatie                  (Manuel)
renderer.py      Visuele weergave en menu's         (Rids)
Theme_style.py   Kleuren en stijl
requirements.txt Benodigde packages

================================================================